import time
from . import gamepad

class Session:
    def __init__(self):
        self.sessions_list = {}
        self.nb_users = 0
        self.rover_state = 0
        self.subsystems_state = 0
        #comment representer les tab utilise par les users ?

class Cameras:
    def __init__(self):
        self.nb_cameras = 7
        self.cameras_list = [0] * self.nb_cameras
        
class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.is_running = False

    def start(self):
        self.is_running = True
        self.start_time = time.time()

    def time_left(self):
        if(self.is_running == False):
            self.start_time = time.time()
            return self.duration
        current = time.time() - self.start_time
        if(current < self.duration):
            return self.duration - current
        return 0

    def get_time(self):
        
        m = int(self.time_left() / 60)
        s = int(self.time_left() - m * 60)
        
        return m,s
        
class Log:
    def __init__(self):
        self.log = []
        self.last_log = ""

    def add(self, msg):
        self.log.append(msg)
        self.last_log = msg

session = Session()
timer = Timer(600)
gamepad = gamepad.Gamepad()
cameras = Cameras()
log = Log()
