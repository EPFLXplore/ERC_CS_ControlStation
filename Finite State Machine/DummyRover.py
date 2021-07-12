#!/usr/bin/python

import threading
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class
from std_msgs.msg import Int32, Int32MultiArray
from threading import Thread, Event

exitFlag = 0

rospy.init_node('rover_nav', anonymous=True)

#======================================================
'''
Abstract class for different Threads for the FSM

  extends: Thread, ABC

  Attributes:

'''
class Rover_Thread(threading.Thread, ABC):

  def __init__(self, threadID, name, flag):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.flag = flag

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

   def run(self):
      super().run()
      print("Starting " + self.name)
      
      print("Exiting " + self.name)

'''
  Finite State Machine inputs reception
'''
class Reception_Thread(Rover_Thread):

  def __init__(self, threadID, name, flag):
      super().__init__(threadID, name, flag)
      rospy.Subscriber('state', Int32MultiArray, callback_state)

  def run():
    super.run()
    rospy.spin() ##listens to the 'state' topic

def callback_state(state):
  if (state.data[0] == 5): # i.e. the task for nav
    print(state.data[1])
    if (state.data[1] == 1): # i.e. work
      print("debug confirmation rover")
      task.flag.set()
      i = Int32(data=1)
      confirmation_pub.publish(i)
      
    elif (state.data[1] == 2): # i.e. wait
      task.pause()
      confirmation_pub.publish(1)
    elif (state.data[1] == 4): # i.e. resume
      task.resume()
      confirmation_pub.publish(1)
    elif (state.data[1] == 3): # i.e. abort
      task.stop()
      confirmation_pub.publish(1)


def autonomous_navigation(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
navigation = Task_Thread(1, "Navigation task", False)
reception  = Task_Thread(2, "Reception loop", True)

# Start new Threads
thread1.start()
thread2.start()

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
#     self.flag.clear() # Set to True
#     self.running = Event()
#     self.running.set()
#     self.count = 0


#   def run(self):
#     while self.running.is_set():
#       self.flag.wait() # returns instantly if true, waits until true otherwise
#       self.count += 1
#       print(self.count)
#       time.sleep(1)

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
