import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.is_running = False

    def start(self, duration = None):
        if(self.is_running == True):
            return
        if(duration != None):
            self.duration = duration
        self.is_running = True
        self.start_time = time.time()

    def time_left(self):
        if(self.is_running == False):
            return self.duration
        current = time.time() - self.start_time
        if(current < self.duration):
            return self.duration - current
        return 0
    
    def pause(self):
        self.duration = self.time_left()
        self.is_running = False
        
    


class Log:
    def __init__(self):
        self.log = []
        self.last_log = ""

    def add(self, msg):
        self.log.append(msg)
        self.last_log = msg
