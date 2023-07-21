import os
import rclpy
import sys
import django
import numpy as np

from .controller import Controller
from .models.rover import Rover


from csApp.models         import *
from std_msgs.msg         import Int8MultiArray    , Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from diagnostic_msgs.msg  import DiagnosticStatus
from std_srvs.srv import SetBool
import MVC_node.models.utils as utils

import cameras_reciever


# TODO
# from ros_package.src.custom_msg_python.msg     import move_base_action_goal 

from geometry_msgs.msg     import Twist, PoseStamped
from actionlib_msgs.msg    import GoalID
from nav_msgs.msg          import Odometry
from sensor_msgs.msg       import JointState, Image, Joy, CompressedImage


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

#================================================================================

import threading
import asyncio
#from ../views import views


class CS:
    '''
        Control Station node in the ROS network of the rover
    '''
    
    def __init__(self):

        if(not rclpy.ok()):
            rclpy.init(args=sys.argv)
            
        self.node = rclpy.create_node("CONTROl_STATION")  

        #self.loop = asyncio.get_event_loop()

        #self.loop = asyncio.get_event_loop().run_forever(rclpy.spin(self.node))
        #asyncio.create_task(rclpy.spin(self.node))

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
        self.Task_pub               = self.node.create_publisher(Int8MultiArray,    'CS/Task',                1)
        self.CS_confirm_pub         = self.node.create_publisher(Bool,              'CS/Confirm',          1)

        #CS --> ROVER (GAMEPAD)

        # CS --> ROVER (HD)
        self.HD_mode_pub            = self.node.create_publisher(Int8,              'CS/HD_mode',          1)
        self.HD_SemiAuto_Id_pub     = self.node.create_publisher(Int8,              'CS/HD_SemiAuto_Id',   1)
        self.HD_Angles_pub          = self.node.create_publisher(Int8MultiArray,    'CS/HD_Angles',        1)
        self.HD_id                  = self.node.create_publisher(Int8,              'CS/HD_element_id',    1)
        self.HD_toggle_camera_pub   = self.node.create_publisher(Bool,              'CS/HD_toggle_camera', 1)
        #self.Gamepad_pub            = self.node.create_publisher(Joy,    'Gamepad',             1)

        # CS --> ROVER (HD)
        self.HD_Gamepad_pub         = self.node.create_publisher(Joy,               'CS/HD_gamepad',       1)
        self.NAV_Gamepad_pub         = self.node.create_publisher(Joy,               'CS/NAV_gamepad',       1)

        #TODO necessary? 
        #self.HD_ManualVelocity_pub  = self.node.create_publisher('HD_ManualVelocity',  Float32,        1)
        self.HD_InvManual_Coord_pub = self.node.create_publisher(Int8MultiArray,    'CS/HD_InvManual_Coord',  1)
        self.HD_homeGo_pub          = self.node.create_publisher(Bool,              'CS/HD_reset_arm_pos',    1)
        self.HD_homeSet_pub         = self.node.create_publisher(Bool,              'CS/HD_set_zero_arm_pos', 1)
        self.HD_voltmeter_pub       = self.node.create_publisher(Int8,              'CS/HD_voltmeter',        1)

        # CS --> ROVER (NAV)

        self.Nav_Goal_pub           = self.node.create_publisher(PoseStamped,       'CS/NAV_goal',         1)
        self.Nav_Status_pub         = self.node.create_publisher(GoalID,            'CS/NAV_STATUS',       1)
        self.Nav_Joystick_pub       = self.node.create_publisher(Twist,             '/cmd_vel',            1)
        #self.Nav_DebugWheels_pub    = self.node.create_publisher(Int16MultiArray,   '/debug/wheel_cmds',   1)

        # Cam
        self.Cam_index_pub = self.node.create_publisher(Int8MultiArray, 'CS/CAM_index', 1)

        # ---------------------------------------------------
        # ===== Subscribers =====
        self.node.create_subscription(String,           'ROVER/RoverConfirm',              self.controller.rover_confirmation , 10)
       # self.node.create_subscription(Int8,             'ROVER/TaskProgress',              self.controller.task_progress      , 10)
        self.node.create_subscription(DiagnosticStatus, 'ROVER/CS_log',                    self.controller.log_clbk   , 10)
        
        # -- SC messages --
        self.node.create_subscription(Int8,               'ROVER/SC_fsm_state',         self.controller.science_state        , 10)
        self.node.create_subscription(Int8,               'ROVER/module_motors_pos',    self.controller.science_motors_pos   , 10)
        self.node.create_subscription(Int8,               'ROVER/motors_velocities',    self.controller.science_motors_vels  , 10)
        self.node.create_subscription(Int8,               'ROVER/motors_currents',      self.controller.science_motors_currents, 10)

        # -- EL(SC) messages --
        self.node.create_subscription(Int8,               'EL/mass',                    self.controller.science_mass         , 10)
        self.node.create_subscription(Int8,               'EL/spectrometer',            self.controller.science_spectrometer , 10)
        self.node.create_subscription(Int8,               'EL/npk',                     self.controller.science_npk          , 10)
        self.node.create_subscription(Int8,               'EL/four_in_one',             self.controller.science_4in1         , 10)

        # -- HD messages --
        self.node.create_subscription(JointState,       'HD/arm_control/joint_telemetry',  self.controller.hd_data       , 10)
        
        # -- NAV messages --
        #self.node.create_subscription(Twist,            '/cmd_vel',                        self.controller.test_joystick      , 10) 
        #self.node.create_subscription(Odometry,         'ROVER_NAV_odometry',              self.controller.nav_data           , 10)
        self.node.create_subscription(Odometry,         'NAV/odometry/filtered',            self.controller.nav_data           , 10)

        # -- Camera messages --
        self.node.create_subscription(CompressedImage,            '/camera_1',                 cameras_reciever.display_cam_1   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_2',                 cameras_reciever.display_cam_2   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_3',                 cameras_reciever.display_cam_2   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_4',                 cameras_reciever.display_cam_4   , 1)
        
        # Elpased time
        #self.node.create_subscription(Int32MultiArray,  'Time',                            self.controller.elapsed_time       , 10) #useless

        #rclpy.spin(self.node)

        #views.launch_nav(None)


        thr = threading.Thread(target=rclpy.spin, args=(self.node,)).start()
        print("start spinning")
        

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
        self.node.get_logger().info('Received message from rover')
        self.roverConnected = future.result().success
        self.node.get_logger().info('ROVER is online')

    # ===============================
    #            GAMEPAD
    # ===============================

    def send_gamepad_data(self, axes, buttons, id, target):
        print(buttons)
        '''
            send gamepad data to rover
        '''
        axes = [float(i) for i in axes]



        if(target == 'HD'):
            #new_axes, new_buttons = utils.gamepad.hd_maping(axes, buttons)
            joy_msg = Joy()
            joy_msg.axes = axes
            joy_msg.buttons = buttons
            self.HD_Gamepad_pub.publish(joy_msg)
        elif(target == 'NAV'):
            #new_axes, new_buttons = utils.gamepad.nav_maping(axes, buttons)
            joy_msg = Joy()
            joy_msg.axes = axes
            joy_msg.buttons = buttons
            self.NAV_Gamepad_pub.publish(joy_msg)
