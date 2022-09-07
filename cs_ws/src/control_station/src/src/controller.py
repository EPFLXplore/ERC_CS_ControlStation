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
#-------------------------------------------------------------------------------


#================================================================================
# Libraries

from turtle import pos
import rospy
import sys
import json
import websocket  
import time

from std_msgs.msg                         import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray, Header
# TODO
# from ros_package.src.custom_msg_python    import move_base_action_goal
from geometry_msgs.msg                    import Pose, Point, Twist, PoseStamped, Quaternion
from actionlib_msgs.msg                   import GoalID
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from Gamepad.Gamepad                      import Gamepad
from src.model                            import *

# TODO new (Twist too)
# from threading              import Thread
from nav_msgs.msg           import Odometry
from CS2022                 import models

#from src_ros_msg.custom_msg_python.msg import move_base_action_goal

#================================================================================
# Webscokets for ASGI

NAV_WS_URL  = "ws://127.0.0.1:8000/ws/CS2022/navigation/"
HD_WS_URL   = "ws://localhost:8000/ws/CS2022/handlingdevice/"
SC_WS_URL   = "ws://localhost:8000/ws/CS2022/science/"
AV_WS_URL   = "ws://localhost:8000/ws/CS2022/logs/"
MAN_WS_URL  = "ws://localhost:8000/ws/CS2022/manual/"
HP_WS_URL   = "ws://localhost:8000/ws/CS2022/homepage/"
TIME_WS_URL = "ws://localhost:8000/ws/CS2022/time/"


ws_nav  = websocket.WebSocket()
ws_hd   = websocket.WebSocket()
ws_sc   = websocket.WebSocket()
ws_av   = websocket.WebSocket()
ws_man  = websocket.WebSocket()
ws_hp   = websocket.WebSocket()
ws_time = websocket.WebSocket()

# ===============================================================================
# Controller (MVC)


class Controller():

    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):
        self.cs = cs
        self.gpad = Gamepad(self.cs)
        # ws_nav.connect("ws://localhost:8000/ws/robot/navigation/")


    # =================================================================================================================
    # CALLBACKS

    def test_joystick(self, twist):
        '''
            debug joystick
        '''
        tl = twist.linear
        ta = twist.angular
        rospy.loginfo("Linear %d %d %d", tl.x, tl.y, tl.z)
        rospy.loginfo("Angular %d %d %d", ta.x, ta.y, ta.z)



    def rover_confirmation(self, txt):
        '''
            receives 
            rover confirmation
        '''
        if(self.cs.rover.getInWait()):
            rospy.loginfo("Rover Confirmation: %s\n", txt.data)
            self.cs.rover.setReceived(True)
        else:
            rospy.loginfo("Received after timeout: %s\n", txt.data)

#OANDSMADSMAPKMDAMSDPA TODO
    def task_progress(self, num):
        '''
            Notified on whether task is a:
            failure (0)
            success (1) 
            checkpoint (2)
        '''
        val = num.data
        if (0 <= val and val < 3):
            TaskProgress.objects.update_or_create(name="TaskProgress", defaults={'state': val})
        else:
            str = "Impossible progress state: %s" % (val)
            self.cs.exception_clbk(String(str))
            

    def sc_humidity(self, hum):
        self.cs.rover.SC.setTubeHum(hum.data)


    def sc_mass(self, mass):
        '''
            receive the total mass of the 3 tubes
        '''
        val = mass.data
        rospy.loginfo("SC mass: %s", val)
        self.cs.rover.SC.setSCMass(val)
        #Science.objects.update_or_create(name="Science", defaults={'mass': val})


    def sc_text_info(self, info):
        '''
            info on what is going on in the Science Bay:
            ex: LED turned on, Picture taken, ...
        '''
        
        self.cs.CS_confirm_pub.publish(True)

        str = info.data
        #Science.objects.update_or_create(name="Science", defaults = {'sc_text': str})
        rospy.loginfo("Science: " + str)
        self.cs.rover.SC.addInfo(str)
        self.sendJson(Task.SCIENCE)


    #TODO
    def sc_state(self, state):
        #self.sc_text_info(state)
        print("tqt")
        


    def sc_params(self, arr):
        rospy.loginfo(arr)
        self.cs.CS_confirm_pub.publish(True)
        #self.cs.rover.SC.deSerializeState(arr.data)
        rospy.loginfo(arr.data)
        self.cs.rover.SC.setParams(arr.data)
        self.sendJson(Task.SCIENCE)
        

    # TODO
    # receive: [id, x, y, z, a, b, c]    (x,y,z) --> translations and (a,b,c) --> rotations
    def hd_detected_element(self, arr):
        elements = arr.data
        self.cs.rover.HD.setDetectedElement(elements)

        rospy.loginfo("received HD element info [%d, %d, %d, %d, %d, %d, %d]", elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6])

        self.sendJson(Task.MAINTENANCE)
        

    def hd_telemetry(self, jointstate):
        self.cs.rover.HD.set_joint_telemetry(jointstate)
        #pos = jointstate.position
        rospy.loginfo("displayed")
        self.sendJson(Task.MAINTENANCE)


    def hd_tof(self, val):
        self.cs.rover.HD.set_tof(val.data)
        self.sendJson(Task.MAINTENANCE)

        

    # receives an Odometry message from NAVIGATIO
    def nav_data(self, odometry):
        data = odometry
        nav =self.cs.rover.Nav

        # position (x,y,z)
        pos = data.pose.pose.position
        nav.setPos([pos.x, pos.y, pos.z])

        # orientation
        quaternion = data.pose.pose.orientation
        explicit_quat = [quaternion.x, quaternion.y, quaternion.z, quaternion.w]
        roll, pitch, yaw = euler_from_quaternion(explicit_quat)
        nav.setYaw(yaw)

        # linear velocity
        twistLin = data.twist.twist.linear
        nav.setLinVel([twistLin.x, twistLin.y, twistLin.z])

        # angular velocity
        twistAng = data.twist.twist.angular
        nav.setAngVel([twistAng.x, twistAng.y, twistAng.z])

        rospy.loginfo("linvel %d", nav.getLinVel())

        self.sendJson(Task.NAVIGATION)
            


    #TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
    # callback for exceptions thrown from rover or from the CS
    def exception_clbk(self, str): 
        val = str.data
        rospy.loginfo("Exception: " + val)
        #Exception.objects.update_or_create(name="Exception", defaults={'string': val})
        #e = models.Exception(string=val).save()
        self.cs.rover.addException(val)

        self.cs.CS_confirm_pub.publish(True)

        self.sendJson(Task.LOGS)


    # =================================================================================================================

    # sends array: [task, instr]:
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
        #checkArgs(task, instr)

        arr = [task, instr]
        #if(task == 4): arr[1] = self.cs.rover.SC.getCmd() #if Science then there are a bit more specific cmds

        self.cs.rover.setInWait(True)    
        self.cs.Task_pub.publish(Int8MultiArray(data = arr))

        self.wait()

        self.cs.rover.setState(Task(task))

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
            rospy.loginfo("Error: HD mode can be either 0 or 1 not %s", mode)

    # Send the id of the element the HD must reach in Autonomous mode
    def pub_hd_elemId(self, id) :
        rospy.loginfo("HD: object id - %d", id)
        print(type(id))
        self.cs.rover.HD.setElemId(id)
        self.cs.HD_SemiAuto_Id_pub.publish(data = id)


    ###############################
    #          NAVIGATION         #
    ###############################

    # give the coordinates the rover must reach
    def pub_nav_goal(self, x, y, yaw):
        rospy.loginfo("NAV: set goal (%.2f, %.2f) + %.2f (orientation)", x, y, yaw)
        
        self.cs.rover.Nav.setGoal([x, y, yaw])

        # PoseStamped message construction: Header + Pose
        # ----- Header -----
        nav = self.cs.rover.Nav
        h = Header()
        h.frame_id = str(nav.getId()) # goal has an id by which it is recognized

        # ----- Pose: Point + Quaternion -----
        pose = Pose()

        # z = 0.0 (the rover can't fly yet)
        point = Point(x, y, 0.0)
        pose.position = point

        # rover orientation
        q = quaternion_from_euler(0, 0, yaw)
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]

        # -----------------------------------
        
        self.cs.Nav_Goal_pub.publish(PoseStamped(header = h, pose = pose))


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
    #            SCIENCE         #
    ##############################

    # select tube on which we'll execute a selected operation
    def selectedTube(self, id):
        if(id < 0 or id > 2): raise ValueError("tube ids are: 0, 1, 2")
        self.cs.rover.SC.selectTube(id)

    # select operation to execute on a tube: mass calculation, sampling, rotation to camera
    def selectedOp(self, op):
        self.cs.rover.SC.setOperation(op)

    # set not tube-specific command: take picture, picture analysis, humidity.
    #(tube-specific commands are updated automatically as you do one of the above operations)
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
    def launch_Manual(self):
        rospy.loginfo("\nTrying manual controls\n")

        self.gpad.connect()
        self.gpad.run()

    # turns off Gamepad's 'running' flag
    def abort_Manual(self):
        rospy.loginfo("\nAborting manual controls\n")
        self.gpad._running = False



    # TIMEOUT system
    # invoked after sending a message to the rover and expecting a confirmation
    def wait(self):
        start = time.time()
        while(not self.cs.rover.getReceived() and ((time.time() - start) < 1)): 
            continue

        self.cs.rover.setInWait(False)

        if(not self.cs.rover.getReceived()):
            rospy.loginfo("Answer not received: TIMEOUT")
        
        self.cs.rover.setReceived(False)




    def elapsed_time(self, data):
        TimeDict = {
            'hor': data.data[0],
            'min': data.data[1],
            'sec': data.data[2]
        }

        message = json.dumps(TimeDict)

        if ws_time.connected:

            ws_time.send('%s' % message)


    # takes a Task enum as argument
    # invoked at the end of a callback after updating data that came from rover
    # sends the needed data to the front-end depending on the task
    def sendJson(self, subsyst):

        if(ws_man.connected):
            socket = ws_man

            nav = self.cs.rover.Nav
            hd = self.cs.rover.HD

            pos = nav.getPos()
            Dictionary = {
                'x'         : pos[0], 
                'y'         : pos[1], 
                'z'         : pos[2],
                'linVel'    : nav.getLinVel(), 
                'angVel'    : nav.getAngVel(),
                'joint_pos' : hd.get_joint_positions(),
                'joint_vel' : hd.get_joint_velocities()
            }

        elif(subsyst == Task.NAVIGATION):
            socket = ws_nav

            nav = self.cs.rover.Nav
            pos = nav.getPos()
            Dictionary = {
                'x'        : pos[0], 
                'y'        : pos[1], 
                'z'        : pos[2],
                'linVel'   : nav.getLinVel(), 
                'angVel'   : nav.getAngVel(),
                'distance' : nav.distToGoal(),
                'yaw'      : nav.getYaw()
            }

        elif(subsyst == Task.MAINTENANCE):
            socket = ws_hd

            hd = self.cs.rover.HD
            Dictionary = {
                'joint_pos' : hd.get_joint_positions(),
                'joint_vel' : hd.get_joint_velocities(),
                'detected_elems' : hd.getElements().flatten().tolist(),
                'tof'       : hd.get_tof()
            }

        elif(subsyst == Task.SCIENCE):
            socket = ws_sc

            sc = self.cs.rover.SC
            Dictionary = {
                'params'        : sc.getParams(),
                'particle_sizes' : sc.getParticleSizes(),
                'volumes'       : sc.getVolumes(),
                'densities'     : sc.getDensities(),
                'colors'        : sc.getColors(),
                'humidity'      : sc.getTubeHum(),
                #'pics'          : sc.getPics(),
                'infos'          : sc.getInfos()
                #'state'         : sc.getState()
                
            }

        elif(subsyst == Task.LOGS):
            socket = ws_av
            #l = list(models.Exception.objects.all())
            l = self.cs.rover.getExceptions()
            Dictionary = {
                'exceptions' : l
            }

        message = json.dumps(Dictionary)
        if(socket.connected):
            print("sent")
            socket.send('%s' % message)

            