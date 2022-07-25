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
import rospy
import django


from CS2022.models         import *
from std_msgs.msg          import Int8MultiArray    , Int8        , Float32, Bool, String, Int16MultiArray, Int16
from move_base_msgs.msg    import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg     import Twist 
from actionlib_msgs.msg    import GoalID
from nav_msgs.msg          import Odometry
from src.callbacks         import *
from src.controller        import *
from sensor_msgs.msg       import CompressedImage
from src.cameras               import *

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
        self.cameras    = Cameras()

        self.navID      = [0]

        # ---------------------------------------------------
        #  publishers

        # HD
        self.Task_pub               = rospy.Publisher('Task',               Int8MultiArray, queue_size=1)
        self.HD_mode_pub            = rospy.Publisher('HD_mode',            Int8,           queue_size=1)
        self.HD_SemiAuto_Id_pub     = rospy.Publisher('HD_SemiAuto_Id',     Int8,           queue_size=1)
        self.HD_Angles_pub          = rospy.Publisher('HD_Angles',          Int8MultiArray, queue_size=1)
        self.HD_ManualVelocity_pub  = rospy.Publisher('HD_ManualVelocity',  Float32,        queue_size=1)
        self.HD_InvManual_Coord_pub = rospy.Publisher('HD_InvManual_Coord', Int8MultiArray, queue_size=1)

        # NAV
        self.Nav_Goal_pub           = rospy.Publisher('/move_base/goal',    MoveBaseActionGoal, queue_size=1)
        self.Nav_CancelGoal_pub     = rospy.Publisher('/move_base/cancel',  GoalID,             queue_size=1)
        self.Nav_Joystick_pub       = rospy.Publisher('/cmd_vel',           Twist,              queue_size=1)
        self.Nav_DebugWheels_pub    = rospy.Publisher('/debug/wheel_cmds',  Int16MultiArray,    queue_size=1)

        # ---------------------------------------------------
        #  Subscribers

        rospy.Subscriber('RoverConfirm',            Bool,            rover_confirmation )
        rospy.Subscriber('Exception',               String,          exception_clbk     )
        rospy.Subscriber('TaskProgress',            Int8,            task_progress      )
        rospy.Subscriber('sc_state',                String,          sc_text_info       )
        rospy.Subscriber('sc_measurments_humidity', Int16MultiArray, sc_humidity        )
        rospy.Subscriber('sc_measurments_mass',     Int16,           sc_mass            )

        rospy.Subscriber('camera_1',                CompressedImage, display_cam_1      , self.cameras)
        rospy.Subscriber('camera_2',                CompressedImage, display_cam_2      , self.cameras)
        rospy.Subscriber('camera_3',                CompressedImage, display_cam_3      , self.cameras)
        rospy.Subscriber('camera_4',                CompressedImage, display_cam_4      , self.cameras)
        rospy.Subscriber('camera_5',                CompressedImage, display_cam_5      , self.cameras)
        rospy.Subscriber('camera_6',                CompressedImage, display_cam_6      , self.cameras)

        ''' 
        rospy.Subscriber('detection/state', UInt8, detection_state)

        rospy.Subscriber('detection/bounding_boxes', Image, ...)

        rospy.Subscriber('detection/RGB_intel', Image, ...)

        rospy.Subscriber('detection/RGB_webcam_1', Image, ...)

        rospy.Subscriber('detection/RGB_webcam_2', Image, ...)
        '''

        rospy.Subscriber('/cmd_vel',           Twist,    test_joystick)
        rospy.Subscriber('/odometry/filtered', Odometry, nav_data     )
