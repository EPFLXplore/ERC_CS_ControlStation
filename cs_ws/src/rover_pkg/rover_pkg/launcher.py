from subprocess import Popen, PIPE

class Launcher:

    #def __init__(self):
        #self.process = Popen()

    def start_science(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run sc_fsm_drill science_fsm; bash"], stdout=PIPE, stderr=PIPE)
        #Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch sc_fsm_drill drill.py; bash"], stdout=PIPE, stderr=PIPE)

    def start_manual(self):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 run rover_pkg cameras_publisher; bash"], stdout=PIPE, stderr=PIPE)
        self.start_manual_nav()
        self.start_manual_hd()

    def start_manual_nav(args):
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch wheels_cmds wheels_control.launch.xml; bash"], stdout=PIPE, stderr=PIPE)
        Popen(["gnome-terminal", "-x", "sh", "-c", ". ~/.bashrc & ros2 launch game_pad game_pad.launch.xml; bash"], stdout=PIPE, stderr=PIPE)

    def start_manual_hd(args):
        pass
