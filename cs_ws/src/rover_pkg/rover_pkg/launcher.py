from subprocess import Popen, PIPE

class Launcher:

    #def __init__(self):
        #self.process = Popen()

    def start_science(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run sc_fsm_drill science_fsm; bash"], stdout=PIPE, stderr=PIPE)
        #Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch sc_fsm_drill drill.py; bash"], stdout=PIPE, stderr=PIPE)

    def start_manual(self):
        #self.__start_cameras()
        self.__start_manual_nav()
        self.__start_manual_hd()

    def __start_cameras(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run rover_pkg cameras_publisher; bash"], stdout=PIPE, stderr=PIPE)

    def __start_manual_nav(args):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch wheels_cmds wheels_control.launch.xml; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch game_pad game_pad.launch.xml; bash"], stdout=PIPE, stderr=PIPE)

    def __start_manual_hd(args):
        #Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run ethercat_device_configurator motor_control '/home/xplore/Desktop/ROVER/rover_ws/src/motor_controls.ws/src/ethercat_device_configurator/config_mot/setup.yaml'; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", "echo 'xplore' | sudo -i & . ~/.bashrc & cd /home/xplore/Desktop/ROVER/rover_ws/ & ros2 run ethercat_device_configurator motor_control '/home/xplore/Desktop/ROVER/rover_ws/src/motor_controls.ws/src/ethercat_device_configurator/config_mot/setup.yaml'; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run hd_fsm fsm; bash"], stdout=PIPE, stderr=PIPE)
