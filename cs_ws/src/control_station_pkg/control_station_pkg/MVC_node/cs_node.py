import asyncio
import threading
import os
import rclpy
import sys
import django
import numpy as np

from rclpy.qos import ReliabilityPolicy, QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

from .controller import Controller
from .models.rover import Rover


from csApp.models         import *
from std_msgs.msg         import Int8MultiArray    , Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from diagnostic_msgs.msg  import DiagnosticStatus
from nav_msgs.msg         import Path
from std_srvs.srv import SetBool
import MVC_node.models.utils as utils

import cameras_reciever

from geometry_msgs.msg import Twist, PoseStamped
from actionlib_msgs.msg import GoalID
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState, Image, Joy, CompressedImage


from avionics_interfaces.msg import MassArray, SpectroResponse, NPK, FourInOne, Voltage, LaserRequest, ServoRequest, SpectroRequest, AngleArray, MassCalibOffset, NodeStateArray, LEDRequest
from custom_msg.msg import Wheelstatus, Motorcmds

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

# ================================================================================

# from ../views import views


class CS:
    '''
        Control Station node in the ROS network of the rover
    '''

    def __init__(self):

        if (not rclpy.ok()):
            rclpy.init(args=sys.argv)

        self.node = rclpy.create_node("CONTROl_STATION")

        # self.loop = asyncio.get_event_loop()

        # self.loop = asyncio.get_event_loop().run_forever(rclpy.spin(self.node))
        # asyncio.create_task(rclpy.spin(self.node))

        # MVC pattern => model, view (front-end), controller

        self.controller = Controller(self)  # controller
        self.rover = Rover()          # model
        self.roverConnected = False
        # self.nav_mode_control = 1 # 1 is default

        # ==================Service CLIENT==========================
        print("Waiting for ROVER_ONLINE service...")
        self.onlineConfirmClient = self.node.create_client(
            SetBool, "ROVER_ONLINE")
        print("Sending Request...")
        self.sendRequest()

        # ---------------------------------------------------
        # ===== Publishers =====
        # CS --> ROVER

        # Doit etre remplacé par un service
        self.Task_pub = self.node.create_publisher(
            Int8MultiArray,    'CS/Task',             1)
        self.CS_confirm_pub = self.node.create_publisher(
            Bool,              'CS/Confirm',          1)

        # CS --> ROVER (HD)
        self.HD_mode_pub            = self.node.create_publisher(Int8,              'CS/HD_mode',          1)
        self.HD_SemiAuto_Id_pub     = self.node.create_publisher(Int8,              'CS/HD_SemiAuto_Id',   1)
        self.HD_Angles_pub          = self.node.create_publisher(Int8MultiArray,    'CS/HD_Angles',        1)
        self.HD_id                  = self.node.create_publisher(Int8,              'CS/HD_element_id',    1)
        self.HD_toggle_camera_pub   = self.node.create_publisher(Bool,              'CS/HD_toggle_camera', 1)
        self.HD_inverse_frame       = self.node.create_publisher(String,            'ROVER/HD_inverse_frame', 1)

        # CS --> ROVER (GAMEPAD)
        self.HD_Gamepad_pub = self.node.create_publisher(
            Float32MultiArray,  'CS/HD_gamepad',       1)
        self.NAV_Gamepad_pub = self.node.create_publisher(
            Joy,               'CS/NAV_gamepad',       1)

        #TODO necessary?
        #self.HD_ManualVelocity_pub  = self.node.create_publisher('HD_ManualVelocity',  Float32,        1)
        #self.HD_InvManual_Coord_pub     = self.node.create_publisher(Int8MultiArray,    'CS/HD_InvManual_Coord',  1)
        #self.HD_homeGo_pub              = self.node.create_publisher(Bool,              'CS/HD_reset_arm_pos',    1)
        #self.HD_homeSet_pub             = self.node.create_publisher(Bool,              'CS/HD_set_zero_arm_pos', 1)
        #self.HD_toggle_laser_pub        = self.node.create_publisher(LaserRequest,              'EL/laser_req',   1)
        self.HD_deploy_voltmeter_pub    = self.node.create_publisher(ServoRequest,              'EL/servo_req',   1)
        self.HD_cancel_goal_pub         = self.node.create_publisher(Bool,                      'CS/HD_cancel',   1)


        # CS --> ROVER (NAV)

        self.Nav_Goal_pub               = self.node.create_publisher(PoseStamped,       'CS/NAV_goal',         1)
        self.Nav_Cancel_pub             = self.node.create_publisher(String,            'ROVER/NAV_status',       1)
        self.Nav_Joystick_pub           = self.node.create_publisher(Twist,             '/cmd_vel',            1)
        self.Nav_Starting_Point_pub     = self.node.create_publisher(PoseStamped,       '/lio_sam/initial_pose', 1)
        self.Nav_Mode_pub               = self.node.create_publisher(String,            'ROVER/NAV_mode', 1)
        self.Nav_Kinematic_pub          = self.node.create_publisher(String,            'ROVER/NAV_kinematic', 1)
        #self.Nav_DebugWheels_pub    = self.node.create_publisher(Int16MultiArray,   '/debug/wheel_cmds',   1)

        # CS --> ROVER (SC)
        self.SC_spectro_req          = self.node.create_publisher(SpectroRequest,    'EL/spectro_req',    1)
        
        # CS --> ROVER (ELEC)
        self.ELEC_container_calib_pub = self.node.create_publisher(MassCalibOffset,  'EL/container/mass_calib_offset', 1)
        self.ELEC_drill_calib_pub     = self.node.create_publisher(MassCalibOffset,  'EL/drill/mass_calib_offset',     1)
        self.ELEC_led_req             = self.node.create_publisher(LEDRequest,       'EL/led_req',     1)

        # Cam
        self.Cam_index_pub      = self.node.create_publisher(Int8MultiArray,    'CS/CAM_index', 1)
        self.gripper_cam_pub    = self.node.create_publisher(Int8,              'ROVER/HD_toggle_cameras', 1)

        # ---------------------------------------------------
        # ===== Subscribers =====
        self.node.create_subscription(String,           'ROVER/RoverConfirm',               self.controller.rover_confirmation, 10)
        # self.node.create_subscription(Int8,             'ROVER/TaskProgress',              self.controller.task_progress      , 10)
        self.node.create_subscription(DiagnosticStatus, 'ROVER/CS_log',                     self.controller.log_clbk, 10)
        self.node.create_subscription(String,           'ROVER/State',                      self.controller.rover_state, 10)
        self.node.create_subscription(Int8,             'ROVER/subsystem_state',            self.controller.rover_subsystem_state, 10)

        # -- SC messages --
        self.node.create_subscription(Int8,               'SC/fsm_state_to_cs',      self.controller.science_state, 10)
        self.node.create_subscription(Float32MultiArray,  'SC/motors_pos',           self.controller.science_motors_pos, 10)
        self.node.create_subscription(Float32MultiArray,  'SC/motors_speed',         self.controller.science_motors_vels, 10)
        self.node.create_subscription(Float32MultiArray,  'SC/motors_currents',      self.controller.science_motors_currents, 10)
        self.node.create_subscription(Int8MultiArray,     'SC/limit_switches',       self.controller.science_limit_switches, 10)
        self.node.create_subscription(MassArray,         'EL/container/mass',        self.controller.science_container_mass, 10)
        self.node.create_subscription(MassArray,         'EL/drill/mass',            self.controller.science_drill_mass, 10)
        self.node.create_subscription(SpectroResponse,   'EL/spectro_response',   self.controller.science_spectrometer, 10)
        self.node.create_subscription(NPK,               'EL/npk',            self.controller.science_npk, 10)
        self.node.create_subscription(FourInOne,         'EL/four_in_one',    self.controller.science_4in1, 10)

        # -- HD messages --
        self.node.create_subscription(
            JointState,       '/HD/motor_control/joint_telemetry',   self.controller.hd_joint_state, 10)
        self.node.create_subscription(
            Int8MultiArray,   'HD/ar_tags',           self.controller.hd_ARtags, 10)
        self.node.create_subscription(
            Int8,             'HD/task_outcome',      self.controller.hd_task_outcome, 10)
        self.node.create_subscription(
            Voltage,          'EL/voltage',         self.controller.hd_voltage, 10)
        self.node.create_subscription(String,        '/detected_panel',            self.controller.hd_set_ready, 10)

        # -- NAV messages --
        self.node.create_subscription(Odometry,         '/lio_sam/odom',                self.controller.nav_odometry  , 10)
        self.node.create_subscription(Path,             '/plan',                        self.controller.nav_path      , 10)
        self.node.create_subscription(Wheelstatus,      '/NAV/absolute_encoders',       self.controller.nav_wheel, 10)
        self.node.create_subscription(Motorcmds,        '/NAV/displacement',            self.controller.nav_displacement, 10)


        # -- Camera messages --
        self.node.create_subscription(CompressedImage, '/camera_0', cameras_reciever.display_cam_0, 1)
        self.node.create_subscription(
            CompressedImage, '/camera_1', cameras_reciever.display_cam_1, 1)  # doesnt work
        self.node.create_subscription(
            CompressedImage, '/camera_2', cameras_reciever.display_cam_2, 1)
        self.node.create_subscription(
            CompressedImage, '/camera_3', cameras_reciever.display_cam_3, 1)
        self.node.create_subscription(
            CompressedImage, '/camera_4', cameras_reciever.display_cam_4, 1)
        self.node.create_subscription(
            CompressedImage, '/camera_5', cameras_reciever.display_cam_5, 1)


        self.node.create_subscription(Image, 'HD/vision/video_frames', cameras_reciever.display_cam_gripper, 10)#qos_profile=udp)
        
        self.node.create_subscription(Image, '/right/image_rect', cameras_reciever.display_cam_nav, 10)

        # -- Elec messages --
        self.node.create_subscription( NodeStateArray, '/can0/EL/node_state', self.controller.can0_node_states, 10)
        self.node.create_subscription( NodeStateArray, '/can1/EL/node_state', self.controller.can1_node_states, 10)

        thr = threading.Thread(target=rclpy.spin, args=(self.node,)).start()
        print("start spinning")

    def sendRequest(self):
        self.node.get_logger().info('Sending request, waiting for Rover...')
        while not self.onlineConfirmClient.wait_for_service(timeout_sec=1.0):
            continue

        self.node.get_logger().info('service is available')
        self.roverConnected = True
        req = SetBool.Request()
        req.data = True
        future = self.onlineConfirmClient.call_async(req)
        future.add_done_callback(self.roverAnswerReceived)

    def roverAnswerReceived(self, future):
        self.node.get_logger().info('Received message from rover')
        self.roverConnected = future.result().success
        self.node.get_logger().info('ROVER is online')

    # ===============================
    #            GAMEPAD
    # ===============================

    def send_gamepad_data(self, axes, buttons, id, target, speed=1):
        '''
            send gamepad data to rover
        '''
        axes = [float(i) for i in axes]

        # BEHAVIOR WHEN HD IS IN INVERSE_KINEMATICS
        if(target == 'IK'):

            # Need to interpolate axes 2 and 5 to go from range [-1,1] to binary values 0 or 1
            if (axes[2] >= 0):
                axes[2] = 1.    
            else:
                axes[2] = 0.

            if (axes[5] >= 0):
                axes[5] = 1.    
            else:
                axes[5] = 0.

            new_axes = [0.0 for i in range(9)]

            new_axes[0] = float(1 - abs(axes[1]))

            # ax 2 gives direction on y axis => -1 if circle is clicked, 1 if square is clicked
            new_axes[2] = float(buttons[1] - buttons[2]) # button 1 is circle and button 2 is square

            # ax 3 gives direction on z axis => -1 if x clickes, 1 if triangle
            new_axes[3] = float(buttons[3] - buttons[0])

            # ax 1 gives direction on x axis => -1 if L2 clicked, 1 if R2 clicked
            new_axes[1] = float(axes[2] - axes[5])

            directions = Float32MultiArray()
            print(new_axes)
            directions.data = new_axes
            self.HD_Gamepad_pub.publish(directions)


        if(target == 'FK'):
            print("HD GAMEPAD DATA")

            # Need to interpolate axes 2 and 5 to go from range [-1,1] to [0,1]
            axes[2] = (axes[2] + 1) / 2
            axes[5] = (axes[5] + 1) / 2

            # Buttons 4 and 5 tells if we are going forward or backward
            if (buttons[4] == 1):
                axes[2] = -axes[2]
            if (buttons[5] == 1):
                axes[5] = -axes[5]

            new_axes = axes.copy()
            # First join dir is given by ax 3 (r3 gauche droite)
            new_axes[0] = axes[3]
            new_axes[1] = -axes[4] #J2 <=> ax 4 (r3 haut bas)
            #J3 <=> R2 (ax 5) (negative if button 5 (R1 clicked))
            new_axes[2] = axes[5]
            #J4 <=> L2 (ax 2) (negative if button 4 (L1 clicked))
            new_axes[3] = axes[2]
            #J5 <=> L3 haut bas = ax 1 TODO: Check if 1 is up or down
            new_axes[4] = -axes[1]
            #J6 <=> L3 gauche droite = ax 0
            new_axes[5] = axes[0]

            directions = Float32MultiArray()
            directions.data = axes[:6]

            # Gripper are buttons 1 and 2
            # transform them into speeds
            if (buttons[2] == 1):
                directions.data.append(-1)
            elif (buttons[1] == 1):
                directions.data.append(1)
            else:
                directions.data.append(0)
            print(directions.data)
            self.HD_Gamepad_pub.publish(directions)

        elif (target == 'NAV'):
            print("NAV GAMEPAD DATA")
            # if(buttons[8] == 1):
            #     print("switching modes")
            #     if self.nav_mode_control == 1 :
            #         self.nav_mode_control = 0
            #     else:
            #         self.nav_mode_control = 1

            joy_msg = Joy()
            # new_axes = utils.gamepad.permute(axes, utils.gamepad.selected_nav_profile.axes)
            # new_buttons = utils.gamepad.permute(buttons, utils.gamepad.selected_nav_profile.buttons)

            # Need to interpolate axes 2 and 5 to go from [-1,1] to [0,2]
            # print("Axes before interpolation")
            # print(axes[2])

            axes[2] = (axes[2] + 1) / 2
            axes[5] = (axes[5] + 1) / 2

            # print("Axes after interpolation")
            # print(axes[2])
            # buttons[8] = self.nav_mode_control

            if (buttons[8] == 1):
                print("change state on")

            joy_msg.axes = axes
            joy_msg.buttons = buttons
            print(joy_msg)
            self.NAV_Gamepad_pub.publish(joy_msg)
