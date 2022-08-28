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
from tf.transformations import quaternion_from_euler

from Gamepad.Gamepad                      import Gamepad
from src.model                            import *

# TODO new (Twist too)
# from threading              import Thread
from nav_msgs.msg           import Odometry
from CS2022.models          import *

#from src_ros_msg.custom_msg_python.msg import move_base_action_goal

#================================================================================
# Webscokets for ASGI

NAV_WS_URL  = "ws://127.0.0.1:8000/ws/CS2022/navigation/"
HD_WS_URL   = "ws://localhost:8000/ws/CS2022/handlingdevice/"
SC_WS_URL   = "ws://localhost:8000/ws/CS2022/science/"
AV_WS_URL   = "ws://localhost:8000/ws/CS2022/avionics/"
MAN_WS_URL  = "ws://localhost:8000/ws/CS2022/manual/"
HP_WS_URL   = "ws://localhost:8000/ws/CS2022/homepage/"
TIME_WS_URL   = "ws://localhost:8000/ws/CS2022/time/"


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
        
        str = info.data
        Science.objects.update_or_create(name="Science", defaults = {'sc_text': str})
        rospy.loginfo("Science: text_info: " + str)
        

    # TODO
    # receive: [id, x, y, z, a, b, c]    (x,y,z) --> translations and (a,b,c) --> rotations
    def hd_detected_element(self, arr):
        element = arr.data
        self.cs.rover.HD.setDetectedElements(element)
        

    def hd_telemetry(self, jointstate):
        self.cs.rover.HD.set_joint_telemetry(jointstate)
        #pos = jointstate.position
        rospy.loginfo("displayed")
        self.sendJson(Task.MAINTENANCE)


    def hd_tof(self, val):
        self.cs.rover.HD.set_tof(val.data)

        '''HdDictionary = {
            'joint_pos' : self.cs.rover.HD.get_joint_positions(),
            'joint_vel' : self.cs.rover.HD.get_joint_velocities(),
            'tof'       : self.cs.rover.HD.get_tof()
        }

        message = json.dumps(HdDictionary)
        rospy.loginfo("tof my guy %d (mm):", val.data)

        if(ws_hd.connected):
            ws_hd.send('%s' % message)'''

        self.sendJson(Task.MAINTENANCE)

        


    def nav_data(self, odometry):
        data = odometry

        # position (x,y,z)
        pos = data.pose.pose.position
        
        self.cs.rover.Nav.setPos([pos.x, pos.y, pos.z])

        # linear velocity
        twistLin = data.twist.twist.linear
        
        self.cs.rover.Nav.setLinVel([twistLin.x, twistLin.y, twistLin.z])

        # angular velocity
        twistAng = data.twist.twist.angular
        #twistAng = data
        
        self.cs.rover.Nav.setAngVel([twistAng.x, twistAng.y, twistAng.z])

        rospy.loginfo("linvel %d", self.cs.rover.Nav.getLinVel())

        '''state = self.cs.rover.getState()
        if(state == Task.NAVIGATION):
            self.jsonMsg(state, ws_nav)
        elif(state == Task.MANUAL):
            self.jsonMsg(state, ws_man)'''

        '''if(ws_man.connected): self.jsonMsg(Task.MANUAL, ws_man)
        if(ws_nav.connected): self.jsonMsg(Task.NAVIGATION, ws_nav)'''
        self.sendJson(Task.NAVIGATION)
            


    #TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
    #General topic on which subsystems can publish if an unexpected exception was thrown
    def exception_clbk(self, str): 
        val = str.data
        rospy.loginfo("Exception: " + val)
        Exception.objects.update_or_create(name="Exception", defaults={'string': val})


    # =================================================================================================================

    # TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
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

        # self.cs.rover.setState(task, instr)
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
            #rospy.loginfo("Error: HD mode can either 0 or 1 not ")
            rospy.loginfo("Error: HD mode can be either 0 or 1 not %s", mode)

    # Send the id of the element the HD must reach 
    # when in Autonomous or SemiAutonomous mode
    def pub_hd_elemId(self, id) :
        rospy.loginfo("HD: object id - %d", id)
        print(type(id))
        self.cs.rover.HD.setElemId(id)
        self.cs.HD_SemiAuto_Id_pub.publish(data = id)


    ###############################
    #          NAVIGATION         #
    ###############################

    # give the coordinates the self.cs.
    # rover must reach
    def pub_nav_goal(self, x, y, yaw):
        rospy.loginfo("NAV: set goal (%.2f, %.2f) + %.2f (orientation)", x, y, yaw)
        #moveBaseGoal = MoveBaseGoal(target_pose = Pose(position = Point(x, y, z)))
        #self.cs.Nav_Goal_pub.publish(MoveBaseActionGoal(goal_id = self.cs.rover.currId, goal = moveBaseGoal))
        #moveBaseGoal_var = Pose(position = Point(x, y, 0))
        
        # TODO
        # self.cs.Nav_Goal_pub.publish(move_base_action_goal(currId = self.cs.rover.currId, moveBaseGoal = moveBaseGoal_var))
        self.cs.rover.Nav.setGoal([x, y, yaw])

        nav = self.cs.rover.Nav
        h = Header()
        h.frame_id = str(nav.getId())

        pose = Pose()

        point = Point(x, y, 0.0)
        pose.position = point

        q = quaternion_from_euler(0, 0, yaw)
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]
        
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

    def selectedTube(self, id):
        if(id < 0 or id > 2): raise ValueError("tube ids are: 0, 1, 2")
        self.cs.rover.SC.selectTube(id)

    def selectedOp(self, op):
        self.cs.rover.SC.setOperation(op)
        

    ##############################
    #            MANUAL          #
    ##############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):
        rospy.loginfo("\nTrying manual controls\n")

        #self.gpad.findJoystick()

        # TODO need to make it so that the control attribute of GamePad activates when plugging in joystick (patron Observateur?)
        # to avoid raising an Exception (if gamepad was found then launch)
        # if(self.gpad.control != None) : 
        #     rospy.loginfo("\nLaunching manual controls\n")
        #     self.gpad.start()

    def abort_Manual(self):
        rospy.loginfo("\nAborting manual controls\n")
        self.gpad.join()




    def wait(self):
        #time.sleep(1)
        #print(self.cs.rover.getReceived())
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


    '''def jsonMsg(self, tab, socket):
        print(socket.connected)
        if(socket.connected):
            #Dictionary = defaultdict()
            
            if(tab == Task.NAVIGATION):
                nav = self.cs.rover.Nav
                pos = nav.getPos()
                Dictionary = {
                    'x'        : pos[0], 
                    'y'        : pos[1], 
                    'linVel'   : nav.getLinVel(), 
                    'angVel'   : nav.getAngVel(),
                    'distance' : nav.distToGoal()
                }

            elif(tab == Task.MAINTENANCE):
                hd = self.cs.rover.HD
                Dictionary = {
                    'joint_pos' : hd.get_joint_positions(),
                    'joint_vel' : hd.get_joint_velocities(),
                    'tof'       : hd.get_tof()
                }

            elif(tab == Task.SCIENCE):
                sc = self.cs.rover.SC
                ###############################
                # BIG TODO !!!!!!!!!!!!!!!!!!!!
                ###############################

            elif(tab == Task.MANUAL):
                nav = self.cs.rover.Nav
                hd = self.cs.rover.HD

                pos = nav.getPos()
                Dictionary = {
                    'x'         : pos[0], 
                    'y'         : pos[1], 
                    'linVel'    : nav.getLinVel(), 
                    'angVel'    : nav.getAngVel(),
                    'joint_pos' : hd.get_joint_positions(),
                    'joint_vel' : hd.get_joint_velocities()
                }

            rospy.loginfo("oh nae %d", Dictionary['x'])
            message = json.dumps(Dictionary)
            socket.send('%s' % message)'''

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
                'distance' : nav.distToGoal()
            }

        elif(subsyst == Task.MAINTENANCE):
            socket = ws_hd

            hd = self.cs.rover.HD
            Dictionary = {
                'joint_pos' : hd.get_joint_positions(),
                'joint_vel' : hd.get_joint_velocities(),
                'tof'       : hd.get_tof()
            }

        elif(subsyst == Task.SCIENCE):
            socket = ws_sc

            sc = self.cs.rover.SC
            ###############################
            # BIG TODO !!!!!!!!!!!!!!!!!!!!
            ###############################

        message = json.dumps(Dictionary)
        socket.send('%s' % message)
