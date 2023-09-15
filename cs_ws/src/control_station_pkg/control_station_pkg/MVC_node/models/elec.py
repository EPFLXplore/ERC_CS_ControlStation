from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Electronic:
    def __init__(self):

        self.channel_layer = get_channel_layer()

        self.can0 = [False]*16
        self.can1 = [False]*16
        
    def UpdateElecDeviceSocket(self):

        async_to_sync(self.channel_layer.group_send)("elec", {"type": "elec_message",
                                                                'can0': str(x for x in self.can0),
                                                                'can1': str(x for x in self.can1)
                                                                })