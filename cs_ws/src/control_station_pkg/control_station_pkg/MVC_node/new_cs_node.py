import threading
import os
from .network_monitor import NetworkMonitor
import rclpy
from rclpy.action import ActionClient 
import sys
import django

from .controller import Controller
from .models.rover import Rover

from csApp.models         import *
from std_msgs.msg         import Int8MultiArray, Bool, String, Float32MultiArray
from std_srvs.srv import SetBool

from sensor_msgs.msg import Joy
from custom_msg.msg import MassArray, SpectroResponse, NPK, FourInOne, Voltage, LaserRequest, ServoRequest, SpectroRequest, AngleArray, MassCalibOffset, NodeStateArray, LEDRequest, Wheelstatus, Motorcmds

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()


class CS:
    '''
        Control Station node in the ROS network of the rover
    '''

    def __init__(self):

        if (not rclpy.ok()):
            rclpy.init(args=sys.argv)

        self.node = rclpy.create_node("CONTROL_STATION")

        self.controller = Controller(self)
        self.rover = Rover() # CHELOU ON USE PAS
        self.roverConnected = False
        
        print("Waiting for ROVER_ONLINE service...")
        self.onlineConfirmClient = self.node.create_client(
            SetBool, "ROVER_ONLINE")
        print("Sending Request...")
        self.sendRequest()

        # ==================================================
        # ==================================================
        
        # ===== Subscribers =====
        self.node.create_subscription(String, 'Rover/RoverState', self.controller.rover_state, 10)
        self.node.create_subscription(GamepadCmdsNavigation, 'CS/GamepadCmdsNavigation', , 10)
        self.node.create_subscription(GamepadCmdsHandlingDevice, 'CS/GamepadCmdsHandlingDevice', , 10)
        
        # ===== Services =====
        self.change_mode_system = self.node.create_client(ChangeModeSystem , 'change_mode_system') 
        
        # Doit etre remplacé par un service TODOOOOOOOOOOO ??
        self.Task_pub = self.node.create_publisher(
            Int8MultiArray,    'CS/Task',             1)
        self.CS_confirm_pub = self.node.create_publisher(
            Bool,              'CS/Confirm',          1)
        
        # ===== Actions =====
        self.handling_device_manipulation = ActionClient(self.node, HandlingDeviceManipulation, 'handling_device_manipulation')
        self.navigation_reach = ActionClient(self.node, NavigationReach, 'navigation_reach')
        self.drill_terrain = ActionClient(self.node, DrillTerrain, 'drill_terrain')

        # ==================================================
        # ==================================================

        thr = threading.Thread(target=rclpy.spin, args=(self.node,)).start()
        print("Start spinning CONTROL_STATION Node")

    # ===============================================================================================================================================
    # ===============================================================================================================================================

    def sendRequest(self):
        self.node.get_logger().info('Sending request, waiting for Rover...')
        while not self.onlineConfirmClient.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service ROVER_ONLINE not available, waiting again...')


        self.node.get_logger().info('Service ROVER_ONLINE is available')
        self.roverConnected = True # WEIRD?
        req = SetBool.Request()
        req.data = True
        future = self.onlineConfirmClient.call_async(req)
        future.add_done_callback(self.roverAnswerReceived)
        

    def roverAnswerReceived(self, future):
        self.node.get_logger().info('Received message from rover')
        self.roverConnected = future.result().success # WEIRD
        self.node.get_logger().info('ROVER is online')


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
