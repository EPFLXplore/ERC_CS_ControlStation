#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#           
#           Roman Danylovych
#           roman.danylovych@epfl.ch
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

from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal

from geometry_msgs.msg import Pose, Point

from actionlib_msgs.msg import GoalID

from Gamepad.GamepadTest import Gamepad

#================================================================================


class Controller():
    def __init__(self):
        self.cs = CS()
        self.gpad = Gamepad(self.cs)


###############################
#             TASK            #
###############################

# send array: [task, instr]:
    #
    # TASK: 
    #       - Manual      = 1 
    #       - Navigation  = 2 
    #       - Maintenance = 3
    #       - Science     = 4
    #
    # INSTR:  
    #       - Launch = 1 
    #       - Abort  = 2 
    #       - Wait   = 3 
    #       - Resume = 4 
    #       - Retry  = 5

# TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
    def pub_Task(self, task, instr): 
        arr = [task, instr]
        self.cs.Task_pub.publish(Int8MultiArray(data = arr))
        
        if(arr[0] == 1 and arr[1] == 1 ) : self.launch_Manual() # arr[0] == 1 et arr[1] == 1 


    ###############################
    #       HANDLING DEVICE       #
    ###############################

    # Set HD mode:
    #  - 0 Autonomous
    #  - 1 SemiAutonomous
    #  - 2 Inverse Manual
    #  - 3 Direct Manual
    def pub_hd_mode(self, mode) :
        if(mode == 0 or mode == 1):
            self.cs.HD_mode_pub.publish(data = mode)
        else:
            #rospy.loginfo("Error: HD mode can either 0 or 1 not ")
            print("Error: HD mode can be either 0 or 1 not ", mode)

    # Send the id of the element the HD must reach 
    # when in Autonomous or SemiAutonomous mode
    def pub_hd_elemId(self, id) :
        self.cs.HD_SemiAuto_Id_pub.publish(data = Int8(id))


    ###############################
    #          NAVIGATION         #
    ###############################

    # give the coordinates the rover must reach
    def pub_nav_goal(self,x, y, z):
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

        g_id = GoalID(stamp = rospy.get_time(), id = 1) # TODO UNE FACON D'INCRÉMENTER L'ID À CHAQUE FOIS
        moveBaseGoal = MoveBaseGoal(target_pose = Pose(position = Point(x, y, z)))

        self.cs.Nav_Goal_pub.publish(MoveBaseActionGoal(goal_id = g_id, goal = moveBaseGoal))


    # cancel a specific Navigation goal by giving the goal's id
    def pub_cancel_nav_goal(self, given_id):
        self.cs.Nav_CancelGoal_pub.publish(GoalID(stamp = rospy.get_time(), id = given_id))


    # Debugging commands to individual wheels. Only use in "emergencies".
    
    #  Message : 
    #  [ [wheel_ID] [rotation_velocity] [steering_angle] ]

    #  Wheel_ID : 
    #  1 : FL | 2 : FR | 3 : HR | 4 : HL
    
    #  rotation_veloctiy (in RPM):
    #  range: -60 and +60
    
    #  steering_angle (in degrees) : 
    #  range: -180 and +180

    def pub_debug_wheels(self, wheel_id, rot_vel, range):
        self.cs.Nav_DebugWheels_pub(Int16MultiArray(data = [wheel_id, rot_vel, range]))


    ###############################
    #             MANUAL          #
    ###############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):
        rospy.loginfo("\nlaunching manual controls\n")
        self.gpad.run()

    def abort_Manual(self):
        rospy.loginfo("\naborting manual controls\n")
        self.gpad.join()


# ----------------- MAIN -----------------
''' 
if __name__ == '__main__' and len(sys.argv)>1:
	arg = sys.argv
	l = len(arg)
	name = arg[1]
	
	if l==4 and name=="pub_Task":
		globals()[name](int(arg[2]), int(arg[3]))
'''