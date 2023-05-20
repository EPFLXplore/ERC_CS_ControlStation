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
import websocket
import time

from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray, Header
from geometry_msgs.msg import Pose, Point, Twist, PoseStamped, Quaternion
from actionlib_msgs.msg import GoalID
from transforms3d.euler import euler2quat, quat2euler

from .models.rover   import Task

from nav_msgs.msg import Odometry
from csApp import models

# ================================================================================
# Webscokets for ASGI

# NAV_WS_URL = "ws://127.0.0.1:8000/ws/csApp/navigation/"
# HD_WS_URL = "ws://localhost:8000/ws/csApp/handlingdevice/"
# SC_WS_URL = "ws://localhost:8000/ws/csApp/science/"
# AV_WS_URL = "ws://localhost:8000/ws/csApp/logs/"
# MAN_WS_URL = "ws://localhost:8000/ws/csApp/manual/"
# HP_WS_URL = "ws://localhost:8000/ws/csApp/homepage/"
# TIME_WS_URL = "ws://localhost:8000/ws/csApp/time/"

# WEB SOCKETS used to publish info to front-end depending on the tab
# ws_nav = websocket.WebSocket()
# ws_hd = websocket.WebSocket()
# ws_sc = websocket.WebSocket()
# ws_av = websocket.WebSocket()
# ws_man = websocket.WebSocket()
# ws_hp = websocket.WebSocket()
# ws_time = websocket.WebSocket()



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


    # ===============================
    #            CALLBACKS
    # ===============================

    def test_joystick(self, twist):
        '''
            debug joystick
        '''
        tl = twist.linear
        ta = twist.angular
        # self.cs.node.get_logger().info("Linear %d %d %d", tl.x, tl.y, tl.z)
        # self.cs.node.get_logger().info("Angular %d %d %d", ta.x, ta.y, ta.z)

    # receiving a confirmation from rover after sending an instruction
    def rover_confirmation(self, txt):
        if (self.cs.rover.getInWait()):
            self.cs.node.get_logger().info("Rover Confirmation: %s\n", txt.data)
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

    # ========= SCIENCE CALLBACKS ========= 

    # receiving tube humidity from SC
    def sc_humidity(self, hum):
        self.cs.rover.SC.setTubeHum(hum.data)
        # publish to front-end
        self.sendJson(Task.SCIENCE)

    # receiving info from SC bay + state of SC (all in the form of Strings)
    def sc_text_info(self, info):
        '''
            info on what is going on in the Science Bay:
            ex: LED turned on, Picture taken, ...
        '''
        self.cs.CS_confirm_pub.publish(Bool(data=True))

        str = info.data
        # Science.objects.update_or_create(name="Science", defaults = {'sc_text': str})
        self.cs.node.get_logger().info("Science: " + str)
        self.cs.rover.SC.addInfo(str)
        # publish to front-end
        self.sendJson(Task.SCIENCE)

    # TODO
    def sc_state(self, state):
        # self.sc_text_info(state)
        print("tqt")

    # receiving value of tube parameters from SC (open/closed, full, position, mass)
    def sc_params(self, arr):
        self.cs.node.get_logger().info(arr)
        self.cs.CS_confirm_pub.publish(Bool(data=True))
        self.cs.node.get_logger().info(arr.data)
        self.cs.rover.SC.setParams(arr.data)
        # publish to front-end
        self.sendJson(Task.SCIENCE)

    # receiving an image from science bay after taking a picture
    def sc_image(self, im):
        self.cs.CS_confirm_pub.publish(Bool(data=True))
        self.cs.rover.SC.addImage(im)

    # ========= HD CALLBACKS ========= 

    # receive: [id, x, y, z, a, b, c]    (x,y,z) --> translations and (a,b,c) --> rotations
    def hd_detected_element(self, arr):
        elements = arr.data
        self.cs.rover.HD.setDetectedElement(elements)

        self.cs.node.get_logger().info("received HD element info [%d, %d, %d, %d, %d, %d, %d]", elements[0],
                                       elements[1], elements[2], elements[3], elements[4], elements[5], elements[6])
        # publish to front-end
        self.sendJson(Task.MAINTENANCE)

    # receive: joint telemetry (info on angles and velocity of joints)
    # Jointstate is a ros message
    def hd_telemetry(self, jointstate):
        self.cs.rover.HD.set_joint_telemetry(jointstate)
        #

        self.sendJson(Task.MAINTENANCE)

    # receive: distance to element
    def hd_tof(self, val):
        self.cs.rover.HD.set_tof(val)
        # publish to front-end
        self.sendJson(Task.MAINTENANCE)

    def hd_data(self, JointState):

        joint_positon = JointState.position
        joint_velocity = JointState.velocity
        joint_current = JointState.effort

        async_to_sync(channel_layer.group_send)("info_hd", {"type": "hd_message",
                                                            'joint_position': [joint_positon[0], joint_positon[1], joint_positon[2], joint_positon[3], joint_positon[4], joint_positon[5]],
                                                            'joint_velocity': [joint_velocity[0], joint_velocity[1], joint_velocity[2], joint_velocity[3], joint_velocity[4], joint_velocity[5]],
                                                            'joint_current': [joint_current[0], joint_current[1], joint_current[2], joint_current[3], joint_current[4], joint_current[5]],
                                                            'detected_tags' : [0,0,0,1],
                                                            'task_outcome' : False,
                                                                        })
    

    # ========= NAVIGATION CALLBACKS =========

    # receives an Odometry message from NAVIGATION
    def nav_data(self, odometry):

        print("nav data received")

        #data = odometry
        #nav = self.cs.rover.Nav

        # # position (x,y,z)
        # pos = data.pose.pose.position
        # nav.setPos([pos.x, pos.y, pos.z])

        # # orientation
        # quaternion = data.pose.pose.orientation
        # explicit_quat = [quaternion.w, quaternion.x, quaternion.y, quaternion.z]
        # roll, pitch, yaw = quat2euler(explicit_quat)
        # nav.setYaw(yaw)

        # # linear velocity
        # twistLin = data.twist.twist.linear
        # nav.setLinVel([twistLin.x, twistLin.y, twistLin.z])

        # # angular velocity
        # twistAng = data.twist.twist.angular
        # nav.setAngVel([twistAng.x, twistAng.y, twistAng.z])

        # self.cs.node.get_logger().info("linvel %d", nav.getLinVel())

        position = odometry.pose.pose.position
        orientation = odometry.pose.pose.orientation
        linVel = odometry.twist.twist.linear
        angVel = odometry.twist.twist.angular


        async_to_sync(channel_layer.group_send)("info_nav", {"type": "nav_message",
                                                            'position'   : [position.x, position.y, position.z],
                                                            'orientation': [orientation.w, orientation.x, orientation.y, orientation.z],
                                                            'linVel'     : [linVel.x, linVel.y, linVel.z],
                                                            'angVel'     : [angVel.x, angVel.y, angVel.z],
                                                            'current_goal' : "",
                                                            'wheel_ang' : [1,2,3,4]
                                                                        })

        # publish to front-end
        #self.sendJson(Task.NAVIGATION)

    # callback for exceptions thrown from rover or from the CS
    def exception_clbk(self, str):
        val = str.data
        self.cs.node.get_logger().info("Exception: " + val)
        self.cs.rover.addException(val)

        # confirm msg reception to rover
        self.cs.CS_confirm_pub.publish(Bool(data=True))
        # publish to front-end
        self.sendJson(Task.LOGS)

    def log_clbk(self, data):

        return

        print("log_clbk ")

        #asyncio.set_event_loop(self.cs.loop)

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
        
        
        async_to_sync(channel_layer.group_send)("log", {"type": "log.message",'hours': str(datetime.datetime.now().hour),
                                                                        'minutes': str(datetime.datetime.now().minute),
                                                                        'seconds': str(datetime.datetime.now().second),
                                                                        'severity': int.from_bytes(data.level, "big"),
                                                                        'message': data.message,})
        

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
    #       - Retry  = 5

    # if task == SCIENCE (4) then:
    #   - ABORT    = 0
    #   - RETRY    = 1
    #   - CONFIRM  = 2
    #   - HUMIDITY = 3
    #   - PARAMS   = 4
    #   - INFO     = 5
    #   - STATE    = 6
    #   - TAKE_PIC = 9

    #   - START_SAMPLING_0 = 10
    #   - START_SAMPLING_1 = 11
    #   - START_SAMPLING_2 = 12

    #   - ROT_TO_PIC_0   = 20
    #   - ROT_TO_PIC_1   = 21
    #   - ROT_TO_PIC_2   = 22

    #   - MASS_MEASURE_0 = 30
    #   - MASS_MEASURE_1 = 31
    #   - MASS_MEASURE_2 = 32

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

        if (task == 1 and instr == 1): self.launch_Manual()
        if (task == 1 and instr == 2): self.abort_Manual()

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

    ###############################
    #          NAVIGATION         #
    ###############################

    # send the coordinates the rover must reach and the orientation it must reach them in
    def pub_nav_goal(self, x, y, yaw):
        #self.cs.node.get_logger().info("NAV: set goal (%.2f, %.2f) + %.2f (orientation)", x, y, yaw)

        self.cs.rover.Nav.addGoal([x, y, yaw])

        # PoseStamped message construction: Header + Pose
        # ----- Header -----
        nav = self.cs.rover.Nav
        h = Header()
        #h.frame_id = str(nav.getId())  # goal has an id by which it is recognized

        # ----- Pose: Point + Quaternion -----
        pose = Pose()

        # z = 0.0 (the rover can't fly yet)
        point = Point(x=x, y=y, z=0.0)
        pose.position = point

        # rover orientation
        q = euler2quat(0, 0, yaw)
        pose.orientation.w = q[0]
        pose.orientation.x = q[1]
        pose.orientation.y = q[2]
        pose.orientation.z = q[3]


        #TODO: should be replaced by a service
        #pour avoir le goal, call self.cs.rover.Nav.getGoal()
        #apres avoir recu confirmation du rover, appeler self.cs.rover.Nav.popGoal()
        self.cs.Nav_Goal_pub.publish(PoseStamped(header=h, pose=pose))

    # cancel a specific Navigation goal by giving the goal's id
    def pub_cancel_nav_goal(self, given_id):
        self.cs.node.get_logger().info("NAV: cancel goal %d", given_id)
        self.cs.Nav_CancelGoal_pub.publish(GoalID(stamp=self.cs.node.get_clock().now().to_msg(), id=given_id))
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
        self.cs.node.get_logger().info("Debug wheels")
        self.cs.Nav_DebugWheels_pub(Int16MultiArray(data=[wheel_id, rot_vel, range]))

    ##############################
    #            SCIENCE         #
    ##############################

    # select tube on which we'll execute a selected operation
    def selectedTube(self, id):
        if (id < 0 or id > 2): raise ValueError("tube ids are: 0, 1, 2")
        self.cs.rover.SC.selectTube(id)

    # select operation to execute on a tube: mass calculation, sampling, rotation to camera
    def selectedOp(self, op):
        self.cs.rover.SC.setOperation(op)

    # set not tube-specific command: take picture, picture analysis, humidity.
    # (tube-specific commands are updated automatically as you do one of the above operations)
    def set_sc_cmd(self, cmd):
        self.cs.rover.SC.setCmd(cmd)

    # set humidity value of concerned tube
    def setHumidity(self, val):
        self.cs.rover.SC.setTubeHum(val)

    ##############################
    #            MANUAL          #
    ##############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):       #Gamepad 
        print("launch manual")
        self.cs.node.get_logger().info("\nTrying manual controls\n")
        #self.gpad.connect()
        #self.gpad.run()

    # turns off Gamepad's 'running' flag => stops reading commands from the gamepad
    # TODO this is not enough. When running manual and accidentally unplugging the joystick, 
    # aborting didn't stop the gamepad from publishing the last remembered instruction
    # the problem could come from the abort or due to how the gamepad was coded
    def abort_Manual(self):
        self.cs.node.get_logger().info("\nAborting manual controls\n")
        #self.gpad._running = False

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

    # takes a Task enum as argument
    # invoked at the end of a callback after updating data that came from rover
    # sends the needed data to the front-end depending on the task
    def sendJson(self, subsyst):

        print("Sending JSON " + subsyst.name)

        # async_to_sync(channel_layer.group_send)("nav_manual", {"type": "nav_manual_broadcast", "text": "Hello there!",
        #                                                    "x": 10, "y": 50,
        #                                                    "linVel": 30, "angVel": 20,
        #                                                    "joint_pos":0, "joint_vel":0,
        #                                                    "hd_mode":0})

        # Info to display on MANUAL tab
        if(subsyst == Task.MANUAL):

            consumer = "tab_info_nav"
            nav = self.cs.rover.Nav
            hd = self.cs.rover.HD

            pos = nav.getPos()
            Dictionary = {
                "type": "nav_manual_broadcast",
                'x': pos[0],
                'y': pos[1],
                'z': pos[2],
                'linVel': nav.getLinVel(),
                'angVel': nav.getAngVel(),
                'joint_pos': hd.get_joint_positions(),
                'joint_vel': hd.get_joint_velocities(),
                'hd_mode': self.gpad.modeHD
            }

        # Info to display on NAVIGATION tab
        elif (subsyst == Task.NAVIGATION):

            consumer = ""
            nav = self.cs.rover.Nav
            pos = nav.getPos()

            Dictionary = {
                "type": "",
                'x': pos[0],
                'y': pos[1],
                'z': pos[2],
                'linVel': nav.getLinVel(),
                'angVel': nav.getAngVel(),
                'distance': nav.distToGoal(),
                'yaw': nav.getYaw()
            }

        # Info to display on MAINTENANCE/HANDLING DEVICE tab
        elif (subsyst == Task.MAINTENANCE):

            consumer = ""
            hd = self.cs.rover.HD

            Dictionary = {
                "type": "",
                'joint_pos': hd.get_joint_positions(),
                'joint_vel': hd.get_joint_velocities(),
                'detected_elems': hd.getElements().flatten().tolist(),
                'tof': hd.get_tof()
            }

        # Info to display on SCIENCE tab
        elif (subsyst == Task.SCIENCE):

            consumer = ""
            sc = self.cs.rover.SC

            Dictionary = {
                "type": "",
                'params': sc.getParams(),
                'particle_sizes': sc.getParticleSizes(),
                'volumes': sc.getVolumes(),
                'densities': sc.getDensities(),
                'colors': sc.getColors(),
                'humidity': sc.getTubeHum(),
                # 'pics'          : sc.getPics(),
                'infos': sc.getInfos()
                # 'state'         : sc.getState()

            }

        # Info to display on LOGS tab
        elif (subsyst == Task.LOGS):

            consumer = ""
            l = self.cs.rover.getExceptions()

            Dictionary = {
                "type": "",
                'exceptions': l
            }

        # channel_layer = get_channel_layer()
        # # send info to front-end
        # message = json.dumps(Dictionary)
        # #async_to_sync(channel_layer.group_send)("chat", message)
        # async_to_sync(channel_layer.group_send)("log", {"type": "log.message",'hours': str(datetime.datetime.now().hour),
        #                                                                 'minutes': str(datetime.datetime.now().minute),
        #                                                                 'seconds': str(datetime.datetime.now().second),
        #                                                                 'severity': "",
        #                                                                 'message': "Emile <3",})
