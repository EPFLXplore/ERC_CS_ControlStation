#!/usr/bin/env python
#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           Roman Danylovych
#           roman.danylovych@epfl.ch
#
# @brief: This file contains the Application class of the backend. It will
#         create the ROS node for the Control Station and take care of creating
#         and subscribing to the needed ROS topic. It will also define and run 
#         the listening thread that will receive the data from the rover and store
#         it into the database.
#-------------------------------------------------------------------------------

#================================================================================
# Libraries

import os
from turtle import st
import rospy
import django


from CS2022.models         import *
from std_msgs.msg          import Int8MultiArray    , Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16

# TODO
# from ros_package.src.custom_msg_python.msg     import move_base_action_goal 

from geometry_msgs.msg     import Twist, PoseStamped
from actionlib_msgs.msg    import GoalID
from nav_msgs.msg          import Odometry
from src.controller        import *
from sensor_msgs.msg       import JointState


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

#================================================================================


class CS:
    '''
        Control Station node in the ROS network of the rover
    '''
    
    def __init__(self):

        rospy.init_node("CS2022", anonymous=False)

        

        self.controller = Controller(self)
        self.rover      = Rover()
        # self.cameras    = Cameras()

        self.navID      = [0]

        # ---------------------------------------------------
        #  publishers
        self.Task_pub               = rospy.Publisher('Task',               Int8MultiArray, queue_size=1)
        self.CS_confirm_pub         = rospy.Publisher('CS_Confirm',        Bool,            queue_size=1)

        # Handling Device
        self.HD_mode_pub            = rospy.Publisher('CS_HD_mode',            Int8,           queue_size=1)
        self.HD_SemiAuto_Id_pub     = rospy.Publisher('CS_HD_SemiAuto_Id',     Int8,           queue_size=1)
        self.HD_Angles_pub          = rospy.Publisher('HD_Angles',          Int8MultiArray, queue_size=1)
        #TODO necessary? 
        #self.HD_ManualVelocity_pub  = rospy.Publisher('HD_ManualVelocity',  Float32,        queue_size=1)
        self.HD_InvManual_Coord_pub = rospy.Publisher('HD_InvManual_Coord', Int8MultiArray, queue_size=1)
        self.HD_homeGo_pub          = rospy.Publisher('HD_reset_arm_pos',   Bool,           queue_size=1)
        self.HD_homeSet_pub         = rospy.Publisher('HD_set_zero_arm_pos',Bool,           queue_size=1)
        self.HD_voltmeter_pub       = rospy.Publisher('HD_voltmeter',       Int8,           queue_size=1)

        # Navigation

        # TODO
        # self.Nav_Goal_pub           = rospy.Publisher('CS_NAV_goal',     move_base_action_goal, queue_size=1)
        self.Nav_Goal_pub           = rospy.Publisher('CS_NAV_goal',       PoseStamped,        queue_size=1)
        self.Nav_CancelGoal_pub     = rospy.Publisher('CS_NAV_cancel',     GoalID,             queue_size=1)
        self.Nav_Joystick_pub       = rospy.Publisher('/cmd_vel',          Twist,              queue_size=1)
        self.Nav_DebugWheels_pub    = rospy.Publisher('/debug/wheel_cmds', Int16MultiArray,    queue_size=1)

        # ---------------------------------------------------
        #  Subscribers

        rospy.Subscriber('ROVER_RoverConfirm',             String,          self.controller.rover_confirmation )
        rospy.Subscriber('ROVER_Exception',                String,          self.controller.exception_clbk     )
        rospy.Subscriber('ROVER_TaskProgress',             Int8,            self.controller.task_progress      )
        rospy.Subscriber('ROVER_SC_state',                 String,          self.controller.sc_state           )
        rospy.Subscriber('ROVER_SC_info',                  String,          self.controller.sc_text_info       )
        rospy.Subscriber('ROVER_SC_params',                Int16MultiArray, self.controller.sc_params          )
        rospy.Subscriber('ROVER_SC_measurements_humidity', Int16,           self.controller.sc_humidity        )
        #rospy.Subscriber('ROVER_SC_measurements_mass',     Int16,           self.controller.sc_mass            )
        rospy.Subscriber('ROVER_HD_telemetry',             JointState,      self.controller.hd_telemetry       )
        rospy.Subscriber('ROVER_HD_tof',                   Int32,           self.controller.hd_tof             )
        rospy.Subscriber('ROVER_HD_detected_element',      Int16MultiArray, self.controller.hd_detected_element)


        # TODO
        # rospy.Subscriber('detection/state', UInt8, detection_state)
        # rospy.Subscriber('detection/bounding_boxes', Image, ...)
        # rospy.Subscriber('detection/RGB_intel', Image, ...)
        # rospy.Subscriber('detection/RGB_webcam_1', Image, ...)
        # rospy.Subscriber('detection/RGB_webcam_2', Image, ...)
        

        rospy.Subscriber('/cmd_vel',           Twist,    self.controller.test_joystick)
        rospy.Subscriber('ROVER_NAV_odometry', Odometry, self.controller.nav_data     )
        #rospy.Subscriber('ROVER_NAV_odometry', Int8, self.controller.nav_data     )

        # Elpased time
        rospy.Subscriber('Time',                Int32MultiArray, self.controller.elapsed_time )
