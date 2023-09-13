#
# @date:    27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           Roman Danylovych
#           roman.danylovych@epfl.ch
#
#           Emma Gaia Poggiolini
#           emmagaia.poggiolini@epfl.ch
#
# @brief: This file contains the Controller (following the Model View Controller
#         design pattern)
#         Here are created all the methods that define the I/O behavior with the
#         user.
#
# -------------------------------------------------------------------------------


# ================================================================================
# Libraries

import datetime
from turtle import pos
import json
import time

import numpy as np

from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, Int16MultiArray, Header, String
from geometry_msgs.msg import Pose, Point, Twist, PoseStamped, Quaternion
from actionlib_msgs.msg import GoalID
from transforms3d.euler import euler2quat, quat2euler

from avionics_interfaces.msg import MassCalibOffset
from .models.rover   import Task

from .models.science import Science
from .models.handling_device import HandlingDevice
from .models.navigation import Navigation

from .models.utils import session


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


# ===============================================================================
# Controller (MVC)


class Controller():
    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):
        self.cs = cs
        self.science = Science()
        self.handling_device = HandlingDevice()
        self.navigation = Navigation()

    # ===============================
    #            CALLBACKS
    # ===============================

    # def test_joystick(self, twist):
    #     '''
    #         debug joystick
    #     '''
    #     tl = twist.linear
    #     ta = twist.angular
        # self.cs.node.get_logger().info("Linear %d %d %d", tl.x, tl.y, tl.z)
        # self.cs.node.get_logger().info("Angular %d %d %d", ta.x, ta.y, ta.z)

    # receiving a confirmation from rover after sending an instruction

    def rover_confirmation(self, txt):
        if (self.cs.rover.getInWait()):
            #self.cs.node.get_logger().info("Rover Confirmation: %s\n", txt.data)
            self.cs.rover.setReceived(True)
        else:
            self.cs.node.get_logger().info("Received after timeout: %s\n", txt.data)

    # receive info on progress of task (SUCCESS/FAIL)
    # TODO HASN'T BEEN USED ONCE => NEED TO TELL OTHER SUBSYSTEMS TO PUBLISH ON TaskProgress
    # def task_progress(self, num):
    #     val = num.data
    #     if (0 <= val and val < 3):
    #       #  TaskProgress.objects.update_or_create(name="TaskProgress", defaults={'state': val})
    #     #else:
    #         str = "Impossible progress state: %s" % (val)
    #         self.cs.exception_clbk(String(str))

    def rover_subsystem_state(self, data):
        session.subsystems_state = data.data
        async_to_sync(channel_layer.group_send)("session", {"type": "broadcast",
                                                            'nb_users': session.nb_users,
                                                            'rover_state': session.rover_state,
                                                            'subsystems_state': session.subsystems_state,
                                                            })

    def rover_state(self, data):
        session.rover_state = data.data
        async_to_sync(channel_layer.group_send)("session", {"type": "broadcast",
                                                            'nb_users': session.nb_users,
                                                            'rover_state': session.rover_state,
                                                            'subsystems_state': session.subsystems_state,
                                                            })

    # ========= SCIENCE CALLBACKS =========

    def science_state(self, data):
        print("wallah")
        self.science.state = data.data
        print("science drill state :" + str(self.science.state))
        self.science.UpdateScienceDrillSocket()

    def science_motors_pos(self, data):
        self.science.motors_pos = data.data
        self.science.UpdateScienceDrillSocket()

    def science_motors_vels(self, data):
        self.science.motors_speed = data.data
        self.science.UpdateScienceDrillSocket()

    def science_motors_currents(self, data):
        self.science.motors_currents = data.data
        self.science.UpdateScienceDrillSocket()

    def science_limit_switches(self, data):
        self.science.limit_switches = data.data
        self.science.UpdateScienceDrillSocket()

    # TODO problems with displaying mass, websocket can't serialize numpy.float32 error

    def science_mass(self, data):
        # elec uses channel 2 for the mass (MAY CHANGE IN THE FUTURE)
        self.science.mass = [data.mass[0],
                             data.mass[1], data.mass[2], data.mass[3]]
        self.science.UpdateScienceDataSocket()

    # TODO Chaimaa c'est pour toi, fais la moyenne wallah
    def science_spectrometer(self, data):
        self.science.spectrometer = data.data
        self.science.FindClosestCandidate()
        self.science.UpdateScienceDataSocket()

    def science_npk(self, data):
        self.science.npk_sensor = [data.nitrogen,
                                   data.phosphorus,
                                   data.potassium]

        self.science.UpdateScienceDataSocket()

    def science_4in1(self, data):
        self.science.four_in_one = [data.temperature,
                                    data.moisture,
                                    data.conductivity,
                                    data.ph]

        self.science.UpdateScienceDataSocket()

    # ========= HD CALLBACKS =========

    # receive: [id, x, y, z, a, b, c]    (x,y,z) --> translations and (a,b,c) --> rotations
    '''def hd_detected_element(self, arr):
        elements = arr.data
        self.cs.rover.HD.setDetectedElement(elements)

        self.cs.node.get_logger().info("received HD element info [%d, %d, %d, %d, %d, %d, %d]", elements[0],
                                       elements[1], elements[2], elements[3], elements[4], elements[5], elements[6])
        # publish to front-end
        self.sendJson(Task.MAINTENANCE)'''

    # receive: joint telemetry (info on angles and velocity of joints)
    # Jointstate is a ros message
    def hd_joint_state(self, JointState):

        self.handling_device.joint_positions = JointState.position
        self.handling_device.joint_velocities = JointState.velocity
        self.handling_device.joint_current = JointState.effort

        self.handling_device.UpdateHandlingDeviceSocket()

    # receive: voltage data from the handling device's voltmeter
    def hd_voltage(self, Voltage):
        self.handling_device.voltage = Voltage.voltage
        #self.handling_device.UpdateHandlingDeviceSocket()

    def hd_ARtags(self, ARtags):
        
        available_buttons = [0] * 16
        if(ARtags.data[0] == 1):
            available_buttons[0:6] = [1] * 7

        if(ARtags.data[1] == 1):
            available_buttons[6:12] = [1] * 6

        self.handling_device.available_buttons = available_buttons
        #self.handling_device.UpdateHandlingDeviceSocket()

    def hd_task_outcome(self, outcome):
        self.handling_device.task_outcome = outcome.data
        #self.handling_device.UpdateHandlingDeviceSocket()

    # ========= NAVIGATION CALLBACKS =========

    # receives an Odometry message from NAVIGATION
    # def nav_position(self, poseStamped):

    #     orientation = quat2euler(poseStamped.pose.orientation.w, poseStamped.pose.orientation.x, poseStamped.pose.orientation.y, poseStamped.pose.orientation.z)
    #     self.navigation.position = [poseStamped.pose.position.x, poseStamped.pose.position.y, poseStamped.pose.position.z]
    #     self.navigation.orientation = []
    #     #self.navigation.linVel = [odometry.twist.twist.linear.x, odometry.twist.twist.linear.y, odometry.twist.twist.linear.z]
    #     #self.navigation.angVel = [odometry.twist.twist.angular.x, odometry.twist.twist.angular.y, odometry.twist.twist.angular.z]

    #     self.navigation.UpdateNavSocket()

    def nav_odometry(self, odometry):

        self.navigation.position = [odometry.pose.pose.position.x, odometry.pose.pose.position.y, odometry.pose.pose.position.z]

        orientation = quat2euler([odometry.pose.pose.orientation.w, 
                                    odometry.pose.pose.orientation.x, 
                                    odometry.pose.pose.orientation.y, 
                                    odometry.pose.pose.orientation.z])[2]
        # clamp the orientation from [-pi; pi] to between [0;2 pi]
        if (orientation < 0):
            orientation = orientation + 2* np.pi
        # convert the orientation from radians to degrees
        orientation = orientation * 180 / np.pi
        print(orientation)
        self.navigation.orientation = [0,0, orientation]

        self.navigation.linVel = [odometry.twist.twist.linear.x, odometry.twist.twist.linear.y, odometry.twist.twist.linear.z]
        self.navigation.angVel = [odometry.twist.twist.angular.x, odometry.twist.twist.angular.y, odometry.twist.twist.angular.z]

        self.navigation.UpdateNavSocket()

    def nav_wheel(self, msg):
        """
        FRONT_LEFT_DRIVE = 0
        FRONT_RIGHT_DRIVE = 1
        BACK_RIGHT_DRIVE = 2
        BACK_LEFT_DRIVE = 3
        FRONT_LEFT_STEER = 4
        FRONT_RIGHT_STEER = 5
        BACK_RIGHT_STEER = 6
        BACK_LEFT_STEER = 7
        """
        #self.navigation.wheels_ang = []
        self.navigation.steering_wheel_ang = msg.data[0:4]
        self.navigation.driving_wheel_ang = msg.data[4:8]
        self.navigation.steering_wheel_state = msg.state[0:4]
        self.navigation.driving_wheel_state = msg.state[4:8]
    
        self.navigation.UpdateNavSocket()

    def nav_displacement(self, displacement):
        self.navigation.displacement_mode = displacement.modedeplacement
        self.navigation.info = displacement.info
        self.navigation.UpdateNavSocket()



    def nav_path(self, path):
        self.navigation.path = [[i.pose.position.x, i.pose.position.y, i.pose.position.z] for i in path.poses]
        self.navigation.UpdateNavSocket()



    # TODO important to display exceptions in log screen

    def log_clbk(self, data):

        return

        print("log_clbk ")

        # asyncio.set_event_loop(self.cs.loop)

        # asyncio.get_event_loop().run_until_complete(channel_layer.group_send("log", {"type": "log.message",'hours': str(datetime.datetime.now().hour),
        #                                                                 'minutes': str(datetime.datetime.now().minute),
        #                                                                 'seconds': str(datetime.datetime.now().second),
        #                                                                 'severity': int.from_bytes(data.level, "big"),
        #                                                                 'message': data.message,}))

        # asyncio.run(channel_layer.group_send("log", {"type": "log.message",'hours': str(datetime.datetime.now().hour),
        #                                                                 'minutes': str(datetime.datetime.now().minute),
        #                                                                 'seconds': str(datetime.datetime.now().second),
        #                                                                 'severity': int.from_bytes(data.level, "big"),
        #                                                                 'message': data.message,}))

        async_to_sync(channel_layer.group_send)("log", {"type": "log.message", 'hours': str(datetime.datetime.now().hour),
                                                        'minutes': str(datetime.datetime.now().minute),
                                                        'seconds': str(datetime.datetime.now().second),
                                                        'severity': int.from_bytes(data.level, "big"),
                                                        'message': data.message, })

    # =================================================================================================================
    #                                                    PUBLISHERS
    # =================================================================================================================

    # sends array to rover: [task, instr]:
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

    def pub_Task(self, task, instr):
        '''
            publishes task instructions to the self.cs.rover
        '''
        # checkArgs(task, instr)

        print("pub_Task called")

        arr = [task, instr]

        self.cs.rover.setInWait(True)
        self.cs.Task_pub.publish(Int8MultiArray(data=arr))

        self.wait()

        self.cs.rover.setState(Task(task))

        if (task == 1 and instr == 1):
            self.launch_Manual()
        if (task == 1 and instr == 2):
            self.abort_Manual()

    ###############################
    #       HANDLING DEVICE       #
    ###############################

    # Set HD mode:
    #  - 0 Autonomous
    #  - 1 SemiAutonomous
    #  - 2 Inverse Manual
    #  - 3 Direct Manual

    # Never used
    # Expects the mode to be an int

    def pub_hd_mode(self, mode):
        if (mode == 0 or mode == 1):
            self.cs.node.get_logger().info("Set HD mode %d", mode)
            self.cs.HD_mode_pub.publish(Int8(data=mode))
            self.cs.rover.HD.setHDMode(Int8(data=mode))
        else:
            self.cs.node.get_logger().info("Error: HD mode can be either 0 or 1 not %s", mode)

    # Send the id of the element the HD must reach in Autonomous mode
    # Expects the id to be an int
    def pub_hd_elemId(self, id):
        self.cs.node.get_logger().info("HD: object id - %d", id)
        print(type(id))
        self.cs.rover.HD.setElemId(id)
        self.cs.HD_SemiAuto_Id_pub.publish(Int8(data=id))

    # Tells HD to cancel goal and cease movement
    def pub_cancel_hd_goal(self):
        self.cs.node.get_logger().info("HD: cancelling goal")
        self.cs.HD_cancel_goal_pub.publish(Bool(data=True))


    ###############################
    #          NAVIGATION         #
    ###############################

    # send the coordinates the rover must reach and the orientation it must reach them in

    def pub_nav_goal(self, x, y, yaw):

        print("pub_nav_goal")

        h = Header()
        pose = Pose()

        point = Point(x=x, y=y, z=0.0)
        pose.position = point

        # rover orientation
        q = euler2quat(0, 0, yaw)
        pose.orientation.w = q[0]
        pose.orientation.x = q[1]
        pose.orientation.y = q[2]
        pose.orientation.z = q[3]

        self.cs.Nav_Goal_pub.publish(PoseStamped(header=h, pose=pose))

    def pub_cancel_nav_goal(self):
        self.cs.Nav_Status_pub.publish(String("cancel"))

    def pub_abort_nav_goal(self):
        self.cs.Nav_Status_pub.publish(String("abort"))

    def pub_nav_mode(self, mode):
        self.cs.Nav_Mode_pub.publish(mode)
    
    def pub_nav_kinematic(self, kinematic):
        self.cs.Nav_Kinematic_pub.publish(kinematic)
        
        #self.cs.rover.Nav.cancelGoal()

    def pub_nav_starting_point(self, x, y, yaw):

        h = Header()
        pose = Pose()

        point = Point(x=x, y=y, z=0.0)
        pose.position = point

        # rover orientation
        q = euler2quat(0, 0, yaw)
        pose.orientation.w = q[0]
        pose.orientation.x = q[1]
        pose.orientation.y = q[2]
        pose.orientation.z = q[3]

        self.cs.Nav_Starting_Point_pub(PoseStamped(header=h, pose=pose))


    # cancel a specific Navigation goal by giving the goal's id
    # def pub_cancel_nav_goal(self, given_id):
    #     self.cs.node.get_logger().info("NAV: cancel goal %d", given_id)
    #     self.cs.Nav_CancelGoal_pub.publish(GoalID(stamp=self.cs.node.get_clock().now().to_msg(), id=given_id))
    #     self.cs.rover.Nav.cancelGoal(given_id)

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
        self.cs.node.get_logger().info("Debug wheels")
        self.cs.Nav_DebugWheels_pub.publish(Int16MultiArray(data=[wheel_id, rot_vel, range]))

    ##############################
    #            SCIENCE         #
    ##############################

    # need to publish before placing an element in container to measure mass
    def pub_container_tare(self):
        calib_offset = MassCalibOffset()
        calib_offset.destination_id = 0
        calib_offset.channel = 0

        self.cs.ELEC_container_calib_pub.publish(calib_offset)


    # need to publish before drilling and collecting soil
    def pub_drill_tare(self):
        calib_offset = MassCalibOffset()
        calib_offset.destination_id = 0
        calib_offset.channel = 0

        self.cs.ELEC_drill_calib_pub.publish(calib_offset)
    

    ##############################
    #            MANUAL          #
    ##############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):  # Gamepad
        print("launch manual")
        self.cs.node.get_logger().info("\nTrying manual controls\n")
        # self.gpad.connect()
        # self.gpad.run()

    # turns off Gamepad's 'running' flag => stops reading commands from the gamepad
    # TODO this is not enough. When running manual and accidentally unplugging the joystick,
    # aborting didn't stop the gamepad from publishing the last remembered instruction
    # the problem could come from the abort or due to how the gamepad was coded
    def abort_Manual(self):
        self.cs.node.get_logger().info("\nAborting manual controls\n")
        # self.gpad._running = False

    # TIMEOUT system
    # invoked after sending a message to the rover and expecting a confirmation
    def wait(self):
        # see if any confirmation was received within 1 second
        start = time.time()
        while (not self.cs.rover.getReceived() and ((time.time() - start) < 1)):
            continue

        self.cs.rover.setInWait(False)

        if (not self.cs.rover.getReceived()):
            self.cs.node.get_logger().info("Answer not received: TIMEOUT")

        self.cs.rover.setReceived(False)

    # JSON msg describing the timer
    def elapsed_time(self, data):
        TimeDict = {
            'hor': data.data[0],
            'min': data.data[1],
            'sec': data.data[2]
        }

        message = json.dumps(TimeDict)

        #  if ws_time.connected:

        #      ws_time.send('%s' % message)

    def node_states(self, channel):
        def callback(self, data):
            states = data.node_states
            # async_to_sync(channel_layer.group_send)("session", {"type": "broadcast",
            #                                                     'nb_users': session.nb_users,
            #                                                     'rover_state': session.rover_state,
            #                                                     'subsystems_state': session.subsystems_state,
            #                                                     })
            print("node_states")
            print(states)
            print(channel)
