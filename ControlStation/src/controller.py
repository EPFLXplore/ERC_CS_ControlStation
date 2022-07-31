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

import rospy
import sys
import json
import websocket  #TODO same synthax for python2 and 3 ?

import time
# from src.cs_node         import *
from std_msgs.msg        import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from src.custom_msg_python import move_base_action_goal
#from move_base_msgs.msg  import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg   import Pose, Point, Twist
from actionlib_msgs.msg  import GoalID
#from Gamepad.Gamepad     import Gamepad
from src.model           import *

# TODO new (Twist too)
from threading              import Thread
from nav_msgs.msg           import Odometry
from CS2022.models          import *

#================================================================================
# Webscokets for ASGI
# ws_homepage = websocket.WebSocket()
# ws_nav      = websocket.WebSocket()
# ws_sc       = websocket.WebSocket()
# ws_hd       = websocket.WebSocket()
# ws_man      = websocket.WebSocket()
# ws_av       = websocket.WebSocket()

# ===============================================================================
# Controller (MVC)


class Controller():

    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):

        self.cs = cs
        # ws_homepage.connect()
        #self.gpad = Gamepad(self.cs)


    # =================================================================================================================
    # CALLBACKS

    def test_joystick(self, twist):
        '''
            debug joysticl
        '''
        tl = twist.linear
        ta = twist.angular
        rospy.loginfo("Linear %d %d %d", tl.x, tl.y, tl.z)
        rospy.loginfo("Angular %d %d %d", ta.x, ta.y, ta.z)



    def rover_confirmation(self, boolean):
        '''
            receives 
            rover confirmation
        '''
        rospy.loginfo("Rover Confirmation: %s\n", boolean.data)


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
            



    def sc_humidity(self, hums):
        '''
            receive an Int16MultiArray: [tube number, humidity inside tube]
            tube number : arr[0]
            value       : arr[1]
        '''
        arr = hums.data
        self.cs.rover.SC.setTubeHum(arr[0], arr[1])



    def sc_mass(self, mass):
        '''
            receive the total mass of the 3 tubes
        '''
        rospy.loginfo("SC mass: %s", val)
        val = mass.data
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
    def hd_data(matrix):
        el1 = matrix[0]
        el2 = matrix[1]
        el3 = matrix[2]
        el4 = matrix[3]
        el5 = matrix[4]
        el6 = matrix[5]
        el7 = matrix[6]

        

    # TODO update the database everytime dist(pos1, pos2) > eps
    # TODO IL FAUT PASSER A POSTGRESQL POUR LES ARRAYFIELD STP (ou utiliser des Blob)
    def nav_data(self, odometry):
        data = odometry.data

        # position (x,y,z)
        pos = data.pose.pose.position
        
        self.cs.rover.Nav.setPos([pos.x, pos.y, pos.z])

        # linear velocity
        twistLin = data.twist.twist.linear
        
        self.cs.rover.Nav.setLinVel([twistLin.x, twistLin.y, twistLin.z])

        # angular velocity
        twistAng = data.twist.twist.angular
        
        self.cs.rover.Nav.setAngVel([twistAng.x, twistAng.y, twistAng.z])



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
        checkArgs(task, instr)

        arr = [task, instr]
        self.cs.Task_pub.publish(Int8MultiArray(data = arr))

        self.cs.rover.setState(task, instr)

        if(task == 1 and instr == 1) : self.launch_Manual() 
        if(task == 1 and instr == 2) : self.abort_Manual()

        self.wait()


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
        self.cs.HD_SemiAuto_Id_pub.publish(data = Int8(id))


    ###############################
    #          NAVIGATION         #
    ###############################

    # give the coordinates the self.cs.
    # rover must reach
    def pub_nav_goal(self, x, y, z):
        rospy.loginfo("NAV: set goal (%d, %d, %d)", x, y, z)
        #moveBaseGoal = MoveBaseGoal(target_pose = Pose(position = Point(x, y, z)))
        #self.cs.Nav_Goal_pub.publish(MoveBaseActionGoal(goal_id = self.cs.rover.currId, goal = moveBaseGoal))
        moveBaseGoal_var = Pose(position = Point(x, y, z))
        self.cs.Nav_Goal_pub.publish(move_base_action_goal(currId = self.cs.rover.currId, moveBaseGoal = moveBaseGoal_var))
        self.cs.rover.Nav.addGoal([x,y,z])


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
    #            MANUAL          #
    ##############################

    # launches Gamepad => enables Manual controls
    # is automatically launched from pub_Task when publishing Manual
    def launch_Manual(self):
        rospy.loginfo("\nTrying manual controls\n")

        #TODO ma boi
        #self.gpad.findJoystick()

        # TODO need to make it so that the control attribute of GamePad activates when plugging in joystick (patron Observateur?)
        # to avoid raising an Exception (if gamepad was found then launch)
        if(self.gpad.control != None) : 
            rospy.loginfo("\nLaunching manual controls\n")
            self.gpad.start()

    def abort_Manual(self):
        rospy.loginfo("\nAborting manual controls\n")
        self.gpad.join()




    def wait(self):
        time.sleep(1)
        #print(self.cs.rover.getReceived())
        if(not self.cs.rover.getReceived()):
            rospy.loginfo("Answer not received: TIMEOUT")
        self.cs.rover.setReceived(False)