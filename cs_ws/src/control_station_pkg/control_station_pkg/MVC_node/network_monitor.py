#
# @date:    27/11/2021
#
# @authors: Ugo Balducci
#           ugo.balducci@epfl.ch
#
# @brief: This file contains the network monitor class
#           that is used to monitor the network strength
#
# -------------------------------------------------------------------------------


# ================================================================================
# Libraries
import subprocess
import re
from time import sleep
from threading import Thread
from std_msgs.msg import Int32
from socket import AddressFamily
import psutil

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models.utils import session

channel_layer = get_channel_layer()
HOST = "admin@169.254.55.1"
CMD = "/interface wireless registration-table print"

# ================================================================================
# Network monitor class
# This class is used to monitor the network strength in the background

class NetworkMonitor(Thread):
    def __init__(self, publisher):
        Thread.__init__(self)
        self.publisher = publisher
        self._stop_event = False
        self.mac_addr = self.get_mac_addr()

    def run(self):
        while not self._stop_event:
            self.get_network_strength()
            sleep(1)

    def stop(self):
        self._stop_event = True

    def get_network_strength(self):
        signal_strength = 1

        # Get the signal strength
        try:
            ssh = subprocess.Popen(["ssh", "%s" % HOST, CMD], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = ssh.stdout.readlines()
            ssh.kill()

            for line in result:
                if b"2C:C8:1B:18:9A:AF" in line and signal_strength == 1:
                    line = line.decode("utf-8")
                    signal_strength = int(re.search(r'-[0-9]*dBm', line)[0].split('dBm')[0])
                    break
                if self.mac_addr.encode('utf-8') in line:
                    line = line.decode("utf-8")
                    signal_strength = int(re.search(r'-[0-9]*dBm', line)[0].split('dBm')[0])
                    break
        except:
            pass

        # Publish the signal strength to the topic
        msg = Int32()
        msg.data = signal_strength
        self.publisher.publish(msg)

        # Update the signal strength in the web app
        session.signal_strength = signal_strength
        async_to_sync(channel_layer.group_send)("session", {"type": "broadcast",
                                                            'nb_users': session.nb_users,
                                                            'rover_state': session.rover_state,
                                                            'subsystems_state': session.subsystems_state,
                                                            'signal_strength': session.signal_strength
                                                            })
        
    @staticmethod
    def get_mac_addr():
        # Iterate over all the keys in the dictionary
        for interface in psutil.net_if_addrs():
            # Check if the interface has a valid MAC address
            if("wlp0s20f3" in interface):
                for i in psutil.net_if_addrs()[interface]:
                    if(i.family == AddressFamily.AF_PACKET):
                        return i.address.upper()