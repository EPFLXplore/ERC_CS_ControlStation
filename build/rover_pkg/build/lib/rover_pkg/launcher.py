from subprocess import Popen, PIPE
import time

class Launcher:

    #def __init__(self):
        #self.process = Popen()
    
    bashrc = ". ~/.bashrc"
    sourcei = "source install/setup.sh"

    #nav_ws = "cd /home/xplore/Desktop/NAV_workspace_2023_master/nav_ws"
    nav_ws = "cd ~/Desktop/NAV_workspace_2023/nav_ws"
    global setup_nav_ws
    #setup_nav_ws = "{bashrc} & {nav_ws} & {sourcei}"
    setup_nav_ws = bashrc + " & " + nav_ws + " & " + sourcei

    hd_ws = "cd /home/xplore/Desktop/main_HD_workspace/hd_ws"
    setup_hd_ws = "{bashrc} & {hd_ws} & {sourcei}"

    # TODO potential ambiguity with the ethercat_device_config package because manual_hd uses that too
    def start_science(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run ethercat_device_configurator motor_control '/home/xplore/Desktop/ROVER/rover_ws/src/drill_workspace/src/ethercat_device_configurator/config_mot/setup.yaml'; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run sc_fsm_drill science_fsm; bash"], stdout=PIPE, stderr=PIPE)

    def start_manual(self):
        # self.__start_cameras()
        self.__start_manual_nav()
        self.__start_manual_hd()

    def start_auto_nav(self):
        ouster = setup_nav_ws + " & ros2 launch ros2_ouster ouster.launch.py; bash"
        #Popen(["gnome-terminal", "-x", "sh", "-c", "{setup_nav_ws} & ros2 launch ros2_ouster ouster.launch.py; bash"], stdout=PIPE, stderr=PIPE)
        Popen([". /home/rocknd79/Desktop/CS_workspace/cs_ws/src/rover_pkg/rover_pkg/auto_nav.sh"], stdin=PIPE, shell=True)
        time.sleep(20)
        #Popen(["gnome-terminal", "-x", "sh", "-c", "{setup_nav_ws} & ros2 launch nav.launch.xml; bash"], stdout=PIPE, stderr=PIPE)
        #Popen(["gnome-terminal", "-x", "sh", "-c", "{setup_nav_ws} & ros2 launch nav2_bringup navigation_launch.py; bash"], stdout=PIPE, stderr=PIPE)

    def __start_cameras(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & cd ~ros2 run rover_pkg cameras_publisher; bash"], stdout=PIPE, stderr=PIPE)

    def __start_manual_nav(args):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch wheels_cmds wheels_control.launch.xml; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch game_pad game_pad.launch.xml; bash"], stdout=PIPE, stderr=PIPE)

    def __start_manual_hd(args):
        #Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run ethercat_device_configurator motor_control '/home/xplore/Desktop/ROVER/rover_ws/src/motor_controls.ws/src/ethercat_device_configurator/config_mot/setup.yaml'; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", "echo 'xplore' | sudo -i & . ~/.bashrc & cd /home/xplore/Desktop/ROVER/rover_ws/ & ros2 run ethercat_device_configurator motor_control '/home/xplore/Desktop/ROVER/rover_ws/src/motor_controls.ws/src/ethercat_device_configurator/config_mot/setup.yaml'; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run hd_fsm fsm; bash"], stdout=PIPE, stderr=PIPE)
