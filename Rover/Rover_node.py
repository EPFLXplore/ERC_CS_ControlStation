#!/usr/bin/python
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class
from std_msgs.msg import Int32, UInt8MultiArray

from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID

from Globals import *

#======================================================

'''
    This class initializes all ROS publishers and subscribes to all the needed topics
'''
class Rover:

    def __init__(self):
        rospy.init_node('ROVER', anonymous=True)
        self.ROVER_STATE = Task.IDLE

        # --------------------- PUBLISHERS ---------------------

        # publish True if instruction receivd from CS (Rover node --> CS_node)
        self.RoverConfirm_pub = rospy.Publisher('RoverConfirm', Bool, queue_size=1)
        
        # publish info on exception if one was thrown (Rover node --> CS_node)
        self.Exception_pub = rospy.Publisher('Exception', String, queue_size=1)

        # publish instruction concerning the Maintenance task  (Rover node --> HD node)
        self.Maintenance_pub = rospy.Publisher('Maintenance', Int8, queue_size=1)

        # publish instruction concerning the Navigation task (Rover node --> Nav node)
        self.Nav_pub = rospy.Publisher('Navigation', Int8, queue_size=1)

        # publish instruction concerning the Science Bay (Rover node --> Science node)
        self.SC_pub = rospy.Publisher('Science', Int8, queue_size=1)


        # --------------------- SUBSCRIPTIONS ---------------------

        # receive an array = [task, instruction] (CS_node --> Rover node)
        rospy.Subscriber('Task', Int8MultiArray, self.task_instr)


    def task_instr(self, array):

        task = array.data[0]
        instr = array.data[1]

        if not(1 <= task <= 4):
            self.Exception_pub.publish("Task number denied, received:", task) 
            pass
        if not(1 <= instr <= 5):
            self.Exception_pub.publish("Instr number denied, received:", instr) 
            pass
        
        rospy.loginfo("Rover: [task, instr] received")
        self.RoverConfirm_pub.publish(Bool(True))

        if (task == 1):
            self.ROVER_STATE = Task.MANUAL

        elif (task == 2): #Navigation
            self.ROVER_STATE = Task.NAVIGATION
            self.Nav_pub.publish(instr)

        elif (task == 3): #Maintenance
            self.ROVER_STATE = Task.MAINTENANCE
            self.Maintenance_pub.publish(instr)

        else:  #task == 4, Science
            self.ROVER_STATE = Task.SCIENCE
            print("AHHHHH")
            self.SC_pub.publish(instr)


    def run(self):
        print("Listening")
        rospy.spin() ##listens to the 'state' topic
        # self.rate.sleep()
        ##rate = rospy.Rate(1) # 1 hz
        # while not rospy.is_shutdown():
        #     self.send()
        #     rate.sleep()

    def send(self):
        self.RoverConfirm_pub.publish(Bool(True))


#==========================================================================
#MAIN
if __name__ == '__main__':
    listener = Rover()
    #listener.send() #ne marche pas
    listener.run()
