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

import asyncio
import os
import rclpy
import sys
import django

from .controller import Controller
from .models.rover import Rover


from csApp.models         import *
from std_msgs.msg         import Int8MultiArray    , Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from diagnostic_msgs.msg  import DiagnosticStatus
from std_srvs.srv import SetBool
import MVC_node.models.utils as utils


# TODO
# from ros_package.src.custom_msg_python.msg     import move_base_action_goal 

from geometry_msgs.msg     import Twist, PoseStamped
from actionlib_msgs.msg    import GoalID
from nav_msgs.msg          import Odometry
from sensor_msgs.msg       import JointState, Image, Joy

from threading import Thread

# from manage                import CONTROL_STATION


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

#================================================================================


class CS:
    '''
        Control Station node in the ROS network of the rover
    '''

    def run(self):
        '''
            Run the node
        '''
        rclpy.spin(self.node)
        print("Listening")
    
    def __init__(self, node):

        # if(not rclpy.ok()):
        #     rclpy.init(args=sys.argv)
            
        # self.node = rclpy.create_node("CONTROL_STATION")
        # from manage                import CONTROL_STATION

        self.node = node
        t2 = Thread(target=rclpy.spin, args=(node, None))
        t2.start()
        print("CS node spin started")
        # MVC pattern => model, view (front-end), controller


        self.controller = Controller(self) # controller
        self.rover      = Rover()          # model
        self.roverConnected = False

 
        #==================Service CLIENT==========================
        print("Waiting for ROVER_ONLINE service...")
        self.onlineConfirmClient = self.node.create_client(SetBool, "ROVER_ONLINE")
        print("Sending Request...")
        self.sendRequest()



        # self.cameras    = Cameras()
        # self.navID      = [0]

        # ---------------------------------------------------
        # ===== Publishers ===== 
        # CS --> ROVER 

        #Doit etre remplacé par un service 
        self.Task_pub               = self.node.create_publisher(Int8MultiArray,    'Task',                1)
        self.CS_confirm_pub         = self.node.create_publisher(Bool,              'CS_Confirm',          1)

        #CS --> ROVER (GAMEPAD)
        self.Gamepad_pub            = self.node.create_publisher(Joy,    'Gamepad',             1)

        # CS --> ROVER (HD)
        self.HD_mode_pub            = self.node.create_publisher(Int8,              'CS_HD_mode',          1)
        self.HD_SemiAuto_Id_pub     = self.node.create_publisher(Int8,              'CS_HD_SemiAuto_Id',   1)
        self.HD_Angles_pub          = self.node.create_publisher(Int8MultiArray,    'HD_Angles',           1)
        #TODO necessary? 
        #self.HD_ManualVelocity_pub  = self.node.create_publisher('HD_ManualVelocity',  Float32,        1)
        self.HD_InvManual_Coord_pub = self.node.create_publisher(Int8MultiArray,    'HD_InvManual_Coord',  1)
        self.HD_homeGo_pub          = self.node.create_publisher(Bool,              'HD_reset_arm_pos',    1)
        self.HD_homeSet_pub         = self.node.create_publisher(Bool,              'HD_set_zero_arm_pos', 1)
        self.HD_voltmeter_pub       = self.node.create_publisher(Int8,              'HD_voltmeter',        1)

        # CS --> ROVER (NAV)
        self.Nav_CancelGoal_pub     = self.node.create_publisher(GoalID,            'CS_NAV_cancel',       1)

        self.Nav_Goal_pub           = self.node.create_publisher(PoseStamped,       'CS_NAV_goal',         1)
        self.Nav_status_pub         = self.node.create_publisher(String,            'CS_NAV_status',       1)
        
        self.Nav_Joystick_pub       = self.node.create_publisher(Twist,             '/cmd_vel',            1)
        self.Nav_DebugWheels_pub    = self.node.create_publisher(Int16MultiArray,   '/debug/wheel_cmds',   1)

        # ---------------------------------------------------
        # ===== Subscribers =====
        self.node.create_subscription(String,           'ROVER_RoverConfirm',              self.controller.rover_confirmation , 10)
        self.node.create_subscription(String,           'ROVER_Exception',                 self.controller.exception_clbk     , 10)
       # self.node.create_subscription(Int8,             'ROVER_TaskProgress',              self.controller.task_progress      , 10)
        self.node.create_subscription(DiagnosticStatus, 'ROVER/CS_log',                    self.controller.log_clbk   , 10)
        
        # SC messages
        self.node.create_subscription(String,           'ROVER_SC_state',                  self.controller.sc_text_info       , 10)
        self.node.create_subscription(String,           'ROVER_SC_info',                   self.controller.sc_text_info       , 10)
        self.node.create_subscription(Int16MultiArray,  'ROVER_SC_params',                 self.controller.sc_params          , 10)
        self.node.create_subscription(Int16,            'ROVER_SC_measurements_humidity',  self.controller.sc_humidity        , 10)

        #TODO : changer le nom du subscriber
        self.node.create_subscription(Image,            'sc_camera',                       self.controller.sc_image           , 10)

        # HD messages
        self.node.create_subscription(JointState,       'ROVER_HD_telemetry',              self.controller.hd_telemetry       , 10)
        self.node.create_subscription(Int32,            'ROVER_HD_tof',                    self.controller.hd_tof             , 10)
        self.node.create_subscription(Float32MultiArray,'ROVER_HD_detected_element',       self.controller.hd_detected_element, 10)

        # NAV messages
        self.node.create_subscription(Twist,            '/cmd_vel',                        self.controller.test_joystick      , 10) 
        # TODO i forgot why we subcribed to this... + if its usefull change the name !
        self.node.create_subscription(Odometry,         'ROVER_NAV_odometry',              self.controller.nav_data           , 10)

        # TODO
        # c'est quoi ?
        # self.node.create_subscription('detection/state', UInt8, detection_state)
        # self.node.create_subscription('detection/bounding_boxes', Image, ...)
        # self.node.create_subscription('detection/RGB_intel', Image, ...)
        # self.node.create_subscription('detection/RGB_webcam_1', Image, ...)
        # self.node.create_subscription('detection/RGB_webcam_2', Image, ...)
        
        # Elpased time
        #self.node.create_subscription(Int32MultiArray,  'Time',                            self.controller.elapsed_time       , 10) #useless

    def sendRequest(self):
            self.node._logger.info("Sending request")
            while not self.onlineConfirmClient.wait_for_service(timeout_sec=1.0):
                    self.node.get_logger().info('service not available, waiting again...')

            self.node.get_logger().info('service is available')
            self.roverConnected = True
            req = SetBool.Request()
            req.data = True
            future = self.onlineConfirmClient.call_async(req)
            future.add_done_callback(self.roverAnswerReceived)
        

    def roverAnswerReceived(self,future):
        self.roverConnected = future.result().success
        self.node.get_logger().info('ROVER is online')

    # ===============================
    #            GAMEPAD
    # ===============================

    def send_gamepad_data(self, axes, buttons):
        '''
            send gamepad data to rover
        '''

        joy_msg = Joy()
        joy_msg.axes = axes
        joy_msg.buttons = buttons

        self.Gamepad_pub.publish(joy_msg)
