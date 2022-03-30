#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           ...
#
# @brief: This file contains the Controller (following the Model View Controller
#         design pattern)
#         Here are created all the methods that define the I/O behavior with the
#         user.
#
#================================================================================
import rospy
import sys
from time import sleep
from CS_node import *
from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray


#================================================================================
'''
'''
# class Controller:

#     def __init__(self, CS_node):
#         #the controller is aware of the CS node it is linked to.
#         self.application = CS_node

#     ''' 
#         Here you should define methods that will be called from javascript. They will
#         use the publishers defined in CS_node.py to publish data
#     ''' 


#cstation = CS()


def pubTask(task, instr): 
	#sleep(1)
    arr = [task, instr]
    CStation.Task_pub.publish(Int8MultiArray(data = arr))


if __name__ == '__main__' and len(sys.argv)>1:
	arg = sys.argv
	l = len(arg)
	name = arg[1]
	
	if l==4 and name=="pubTask":
		globals()[name](int(arg[2]), int(arg[3]))
