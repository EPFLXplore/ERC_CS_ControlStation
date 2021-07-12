#!/usr/bin/python
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class
from std_msgs.msg import Int32, Int32MultiArray
from threading import Thread, Event
from Globals import *

exitFlag = 0

rospy.init_node('rover_nav', anonymous=True)

#======================================================
'''
Abstract class for different Threads for the FSM

  extends: Thread, ABC

  Attributes:

'''
class Rover_Thread(Thread, ABC):

  def __init__(self, threadID, name, flag):
    Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.start_flag = flag
    self.wait_flag = Event()
    self.wait_flag.set()
    self.stop_flag = False

  def set_flags(self, instruction):
    if (instruction == instruction.WORK.value): # i.e. work
      self.start_flag == True

    elif (instruction == instruction.WAIT.value): # i.e. wait

      self.wait_flag.set()

    elif (instruction == instruction.RESUME.value): # i.e. resume

      self.wait_flag.clear()

    elif (instruction == instruction.STOP.value): # i.e. abort

      self.stop_flag == True

    self.confirmation_pub.publish(1)

  @abstractmethod
  def run(self):
    pass

#======================================================

'''
  Navigation task
'''
class Navigation_Thread(Rover_Thread):

   def __init__(self, threadID, name, flag):
     super().__init__(threadID, name, flag)
     self.count = 0

   def run(self):
      print("Starting " + self.name)
      while(True):
        if (self.flag):

          self.navigation_task()

          print("Completed " + self.name)
          break
        time.sleep(1)

      print("Exiting " + self.name)
      

    def navigation_task(self):
      while (not stop_flag):
        self.wait_flag.wait()
        # do stuff
        self.count += 1
        print(self.count)
        time.sleep(1)



'''
  Finite State Machine inputs reception
'''
class Reception_Thread(Rover_Thread):

  def __init__(self, threadID, name, flag):
      super().__init__(threadID, name, flag)
      rospy.Subscriber('state', Int32MultiArray, callback_state)
      self.confirmation_pub = rospy.Publisher('confirmation', Int32, queue_size=1)

  def run():
    super.run()
    rospy.spin() ##listens to the 'state' topic

def callback_state(state):

  if (state.data[0] == task.NAVIGATION.value): # i.e. the task for nav
    navigation.set_flags(state.data[0])
  # elif (state.data[0] == task.SCIENCE.value): # i.e. the task for nav
  #   callback_nav(state.data[0])
  # elif (state.data[0] == task.NAVIGATION.value): # i.e. the task for nav
  #   callback_nav(state.data[0])
  # elif (state.data[0] == task.NAVIGATION.value): # i.e. the task for nav
  #   callback_nav(state.data[0])


# def autonomous_navigation(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# Create new threads
navigation = Navigation_Thread(1, "Navigation task", False)
reception  = Reception_Thread(2, "Reception loop", True)

# Start new Threads
navigation.start()
reception.start()

print("Exiting Main Thread")


##==========================================================================


# rospy.init_node('rover_nav', anonymous=True)

# # task / instruction
# # for nav task = 3
# # instructions are work = 1, wait = 2, stop = 3 and resume = 4

# confirmation_pub = rospy.Publisher('confirmation', Int32, queue_size=1)

# class Nav_task(Thread):
#   def __init__(self):
#     self.flag = Event() # used to pause the nav task
#     self.flag.clear() # Set to False
#     self.running = Event()
#     self.running.set()
#     self.count = 0


#   def run(self):
#     while self.running.is_set():
#       self.flag.wait() # returns instantly if true, waits until true otherwise
#       

#   def pause(self):
#     self.flag.clear() # set flag to false
#     print("PAUSED")

#   def resume(self):
#     self.flag.set()
#     print("RESUMED")

#   def stop(self):
#     self.flag.set()
#     self.running.clear()
#     print("STOPPED")


# task = Nav_task()      
# def callback_state(state):
#   if (state.data[0] == 5): # i.e. the task for nav
#     print(state.data[1])
#     if (state.data[1] == 1): # i.e. work
#       print("debug confirmation rover")
#       task.flag.set()
#       i = Int32(data=1)
#       confirmation_pub.publish(i)
      
#     elif (state.data[1] == 2): # i.e. wait
#       task.pause()
#       confirmation_pub.publish(1)
#     elif (state.data[1] == 4): # i.e. resume
#       task.resume()
#       confirmation_pub.publish(1)
#     elif (state.data[1] == 3): # i.e. abort
#       task.stop()
#       confirmation_pub.publish(1)



# rospy.Subscriber('state', Int32MultiArray, callback_state)

# def main():
#   # rospy.spin()
#   # task.run()
#   print("jaj")


# main()
