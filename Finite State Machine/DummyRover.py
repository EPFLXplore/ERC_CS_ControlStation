#!/usr/bin/python
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class
from std_msgs.msg import Int32, UInt8MultiArray
from threading import Thread
from Globals import *
import multiprocessing as mp
import targets


#======================================================

'''
  Finite State Machine inputs reception
'''
class Reception_Thread(Thread):

  def __init__(self, threadID, name):
      Thread.__init__(self)
      rospy.Subscriber('state', UInt8MultiArray, callback_state)
      self.threadID = threadID
      self.name     = name
      # self.rate = rospy.Rate(10)
      

  def run(self):
    print("Listening")
    rospy.spin() ##listens to the 'state' topic
    # self.rate.sleep()




def check_instruction(instr, process):
    global FLAG
    global PFLAG
    confirmation_pub = rospy.Publisher('confirmation', Int32, queue_size=1)
    if(instr == instruction.WORK.value):
      process.start()
      print("debug")
    elif(instr == instruction.STOP.value):

      print("debug STOP value")
      print(process)
      
      rospy.sleep(0.5)
      confirmation_pub.publish(1)
      process.kill()
      PFLAG = 0
      RUNNING_FLAG.value = 0
    elif(instr == instruction.WAIT.value):
      confirmation_pub.publish(1)
      FLAG.value = 1
    elif(instr == instruction.RESUME.value):
      print("resume reception")
      confirmation_pub.publish(1)
      FLAG.value = 0

def callback_state(state):
    global PFLAG
    global navigation
    if(PFLAG == 0):
      navigation = mp.Process(target=targets.nav, args=(RUNNING_FLAG, FLAG))
      PFLAG = 1
    if (state.data[0] == task.NAVIGATION.value): # i.e. the task for nav
      check_instruction(state.data[1], navigation)
    # elif (state.data[0] == task.SCIENCE.value): # i.e. the task for sc
    #   check_instruction(state.data[1], science)
    # elif (state.data[0] == task.PROBING.value): # i.e. the task for probing
    #   check_instruction(state.data[1], probing)
    # elif (state.data[0] == task.MAINTENANCE.value): # i.e. the task for maintenance
    #   check_instruction(state.data[1], hd)
    # elif (state.data[0] == task.MAINTENANCE.value): 
    #   pass
#==========================================================================
#MAIN
if __name__ == '__main__':
  exitFlag = 0

  mp.set_start_method('spawn')
  rospy.init_node('Rover', anonymous=True)
  #WAIT/RESUME Flag
  FLAG  = mp.Value("i", 0) 
  RUNNING_FLAG = mp.Value("i", 0)
  #Process Flag
  PFLAG = 0
  #===========================================================================


  #===========================================================================
  # Create The reception thread
  reception  = Reception_Thread(1, "Reception loop")
  # Start the reception thread
  reception.start()


  #Create the processes



  navigation = 0
  # navigation = mp.Process(target=targets.nav, args=(RUNNING_FLAG, FLAG))
  # science    = mp.Process(target=Science_task.target,    args=(confirmation_pub, FLAG))
  # hd         = mp.Process(target=HD_task.target,         args=(confirmation_pub, FLAG))
  # probing    = mp.Process(target=HD_task.target,         args=(confirmation_pub, FLAG))

  print("Exiting Main Thread")


  ##==========================================================================


