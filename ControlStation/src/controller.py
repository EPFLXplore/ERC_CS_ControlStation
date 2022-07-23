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
#-------------------------------------------------------------------------------


#================================================================================
# Libraries

import rospy
import sys

from time                import sleep
# from src.cs_node         import *
from std_msgs.msg        import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg  import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg   import Pose, Point
from actionlib_msgs.msg  import GoalID
# from Gamepad.GamepadTest import Gamepad
from src.model           import *


#================================================================================


class Controller():

    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):
        #self.cs = CS()
        self.cs = cs
        # self.gpad = Gamepad(self.cs)


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
        '''
            publishes task instructions to the self.cs.rover
        '''
        checkArgs(task, instr)

        arr = [task, instr]
        self.cs.Task_pub.publish(Int8MultiArray(data = arr))

        self.cs.rover.setState(task, instr)

        if(task == 1 and instr == 1) : self.launch_Manual() 
        if(task == 1 and instr == 2) : self.abort_Manual()


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
            rospy.loginfo("Set HD mode %d", mode)
            self.cs.HD_mode_pub.publish(data = mode)
            self.cs.rover.HD.setHDMode(mode)
        else:
            #rospy.loginfo("Error: HD mode can either 0 or 1 not ")
            rospy.loginfo("Error: HD mode can be either 0 or 1 not %s", mode)

    # Send the id of the element the HD must reach 
    # when in Autonomous or SemiAutonomous mode
    def pub_hd_elemId(self, id) :
        rospy.loginfo("HD: object id - %d", id)
        self.cs.HD_SemiAuto_Id_pub.publish(data = Int8(id))


    ###############################
    #          NAVIGATION         #
    ###############################

    # give the coordinates the self.cs.rover must reach
    def pub_nav_goal(self, x, y, z):
        rospy.loginfo("NAV: set goal (%d, %d, %d)", x, y, z)
        moveBaseGoal = MoveBaseGoal(target_pose = Pose(position = Point(x, y, z)))
        self.cs.Nav_Goal_pub.publish(MoveBaseActionGoal(goal_id = self.cs.rover.currId, goal = moveBaseGoal))
        self.cs.rover.Nav.addGoal([x,y,z])


    # cancel a specific Navigation goal by giving the goal's id
    def pub_cancel_nav_goal(self, given_id):
        rospy.loginfo("NAV: cancel goal %d", given_id)
        self.cs.Nav_CancelGoal_pub.publish(GoalID(stamp = rospy.get_time(), id = given_id))
        self.cs.rover.Nav.cancelGoal(given_id)


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
        rospy.loginfo("Debug wheels")
        self.cs.Nav_DebugWheels_pub(Int16MultiArray(data = [wheel_id, rot_vel, range]))


    ##############################
    #            MANUAL          #
    ##############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):
        rospy.loginfo("\nTrying manual controls\n")

        #TODO ma boi
        #self.gpad.findJoystick()

        # TODO need to make it so that the control attribute of GamePad activates when plugging in joystick (patron Observateur?)
        # to avoid raising an Exception (if gamepad was found then launch)
        if(self.gpad.control != None) : 
            rospy.loginfo("\nLaunching manual controls\n")
            self.gpad.start()

    def abort_Manual(self):
        rospy.loginfo("\nAborting manual controls\n")
        self.gpad.join()

