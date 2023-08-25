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
        # self.nav_mode_control = 1 # 1 is default
    


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
        self.Task_pub               = self.node.create_publisher(Int8MultiArray,    'CS/Task',             1)
        self.CS_confirm_pub         = self.node.create_publisher(Bool,              'CS/Confirm',          1)


        # CS --> ROVER (HD)
        self.HD_mode_pub            = self.node.create_publisher(Int8,              'CS/HD_mode',          1)
        self.HD_SemiAuto_Id_pub     = self.node.create_publisher(Int8,              'CS/HD_SemiAuto_Id',   1)
        self.HD_Angles_pub          = self.node.create_publisher(Int8MultiArray,    'CS/HD_Angles',        1)
        self.HD_id                  = self.node.create_publisher(Int8,              'CS/HD_element_id',    1)
        self.HD_toggle_camera_pub   = self.node.create_publisher(Bool,              'CS/HD_toggle_camera', 1)

        # CS --> ROVER (GAMEPAD)
        self.HD_Gamepad_pub         = self.node.create_publisher(Float32MultiArray,  'CS/HD_gamepad',       1)
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
        self.gripper_cam_pub = self.node.create_publisher(Int8, 'ROVER/HD_toggle_cameras', 1)

        # ---------------------------------------------------
        # ===== Subscribers =====
        self.node.create_subscription(String,           'ROVER/RoverConfirm',              self.controller.rover_confirmation , 10)
       # self.node.create_subscription(Int8,             'ROVER/TaskProgress',              self.controller.task_progress      , 10)
        self.node.create_subscription(DiagnosticStatus, 'ROVER/CS_log',                    self.controller.log_clbk   , 10)
        
        # -- SC messages --
        self.node.create_subscription(Int8,               'ROVER/SC_fsm_state',      self.controller.science_state        , 10)
        self.node.create_subscription(Float32MultiArray,  'ROVER/module_motors_pos', self.controller.science_motors_pos   , 10)
        self.node.create_subscription(Float32MultiArray,  'ROVER/motors_velocities', self.controller.science_motors_vels  , 10)
        self.node.create_subscription(Float32MultiArray,  'ROVER/motors_currents',   self.controller.science_motors_currents, 10)
        self.node.create_subscription(Int8MultiArray,     'ROVER/limit_switches',    self.controller.science_limit_switches, 10)
        

        # -- EL(SC) messages --
        self.node.create_subscription(Float32MultiArray,               'EL/mass',                    self.controller.science_mass         , 10)
        self.node.create_subscription(Float32MultiArray,               'EL/spectrometer',            self.controller.science_spectrometer , 10)
        self.node.create_subscription(Float32MultiArray,               'EL/npk',                     self.controller.science_npk          , 10)
        self.node.create_subscription(Float32MultiArray,               'EL/four_in_one',             self.controller.science_4in1         , 10)

        # -- HD messages --
        self.node.create_subscription(JointState,       'HD/arm_control/joint_telemetry',  self.controller.hd_data       , 10)
        
        # -- NAV messages --
        #self.node.create_subscription(Twist,            '/cmd_vel',                        self.controller.test_joystick      , 10) 
        #self.node.create_subscription(Odometry,         'ROVER_NAV_odometry',              self.controller.nav_data           , 10)
        self.node.create_subscription(Odometry,         'NAV/odometry/filtered',            self.controller.nav_data           , 10)

        # -- Camera messages --
        self.node.create_subscription(CompressedImage,            '/camera_0',                 cameras_reciever.display_cam_0   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_1',                 cameras_reciever.display_cam_1   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_2',                 cameras_reciever.display_cam_2   , 1)
        self.node.create_subscription(CompressedImage,            '/camera_3',                 cameras_reciever.display_cam_3   , 1)

        self.node.create_subscription(CompressedImage, 'HD/camera_flux', cameras_reciever.display_cam_gripper, 10)
        
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

    def send_gamepad_data(self, axes, buttons, id, target, speed= 0.5):
        '''
            send gamepad data to rover
        '''
        axes = [float(i) for i in axes]

        if(target == 'HD'):
            print("HD DEBUG")
            #new_axes = utils.gamepad.permute(axes, utils.gamepad.selected_hd_profile.axes)
            #new_buttons = utils.gamepad.permute(buttons, utils.gamepad.selected_hd_profile.buttons)

            # Need to interpolate axes 2 and 5 to go from range [-1,1] to [0,1]
            axes[2] = (axes[2] + 1) / 2
            axes[5] = (axes[5] + 1) / 2

            # Buttons 4 and 5 tells if we are going forward or backward
            if (buttons[4] == 1):
                axes[2] = -axes[2]
            if (buttons[5] == 1):
                axes[5] = -axes[5]

            speed = Float32MultiArray()
            speed.data = axes[:6]

             # Gripper are buttons 1 and 2
            # transform them into speeds
            if (buttons[2] == 1):
                speed.data.append(-1)
            elif (buttons[1] == 1):
                speed.data.append(1)
            else:
                speed.data.append(0)

            self.HD_Gamepad_pub.publish(speed)

        elif(target == 'NAV'):

            # if(buttons[8] == 1):
            #     print("switching modes")
            #     if self.nav_mode_control == 1 :
            #         self.nav_mode_control = 0
            #     else:
            #         self.nav_mode_control = 1

            joy_msg = Joy()
            #new_axes = utils.gamepad.permute(axes, utils.gamepad.selected_nav_profile.axes)
            #new_buttons = utils.gamepad.permute(buttons, utils.gamepad.selected_nav_profile.buttons)

            # Need to interpolate axes 2 and 5 to go from [-1,1] to [0,2]
            # print("Axes before interpolation")
            # print(axes[2])
            
            axes[2] = (axes[2] + 1 ) 
            axes[5] = (axes[5] + 1) 

            # print("Axes after interpolation")
            # print(axes[2])
            # buttons[8] = self.nav_mode_control

            if (buttons[8] == 1):
                print("change state on")

            joy_msg.axes = axes
            joy_msg.buttons = buttons
            self.NAV_Gamepad_pub.publish(joy_msg)

            
