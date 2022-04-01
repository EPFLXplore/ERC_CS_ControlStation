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
from CS_node import CStation
from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray

from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal

from geometry_msgs.msg import Pose, Point


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

def print_GFG():
    for i in range(5):
        # suspend the current thread.
        sleep(1)
        print("GFG")

def pubTask(task, instr): 
	#rospy.sleep(1)
    arr = [task, instr]
    CStation.Task_pub.publish(Int8MultiArray(data = arr))
    lastId = CStation.navID[-1]
    CStation.navID.append(lastId+1)
    rospy.loginfo(CStation.navID[-1])
    print(CStation.navID)
    print("\n")


def set_hd_mode(mode) :
    if(mode == 0 or mode == 1):
        CStation.HD_mode_pub.publish(data = mode)
    else:
        #rospy.loginfo("Error: HD mode can either 0 or 1 not ")
        print("Error: HD mode can be either 0 or 1 not ", mode)


def set_nav_goal(x, y, z):
    '''
    actionlib_msgs/GoalID goal_id
        time stamp
        string id
    move_base_msgs/MoveBaseGoal goal
        geometry_msgs/PoseStamped target_pose
            geometry_msgs/Pose pose
                geometry_msgs/Point position
                    float64 x
                    float64 y
                    float64 z
    '''

    #g_id = GoalID(stamp = rospy.get_time(), id = )
    moveBaseGoal = MoveBaseGoal(target_pose = Pose(position = Point(x, y, z)))

    #CStation.Nav_Goal_pub.publish(MoveBaseActionGoal(goal_id = g_id, goal = moveBaseGoal))


#rospy.loginfo("redis wallah")


if __name__ == '__main__' and len(sys.argv)>1:
	arg = sys.argv
	l = len(arg)
	name = arg[1]
	
	if l==4 and name=="pubTask":
		globals()[name](int(arg[2]), int(arg[3]))
