from threading import Thread
from model     import Model

'''
Class : Stopwatch

@Description: setup for a stopwatch to keep track of time during the rover tasks

@Attributes
'''
class Stopwatch(Thread):

  def __init__(self):
    Thread.__init__(self)
    self.hours   = 0
    self.minutes = 0
    self.seconds = 0
  
  def run(self):
    Model.get_time()
    