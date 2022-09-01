#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           Roman Danylovych
#           roman.danylovych@epfl.ch
#
# @brief: This file contains the Model (following the Model View Controller
#         design pattern)
#         Here are created all the methods that perfrom the required computation
#         for various applications
# 
# -------------------------------------------------------------------------------

#================================================================================
# Libraries

import numpy as np 
import rospy

from multiprocessing.sharedctypes import Value
from unittest.loader    import VALID_MODULE_NAME
from actionlib_msgs.msg import GoalID
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Pose, Point
from sensor_msgs.msg    import JointState
from std_msgs.msg       import Int8, Int16, Bool, String, Int8MultiArray,  Int16MultiArray, UInt8MultiArray 

from rover_node import Rover


class Model:
    '''
        Monitoring of the state of the rover
    '''
    def __init__(self, rover):
        self.rover = rover

        self.Nav = Navigation(rover)
        self.HD = HandlingDevice(rover)
        self.SC = Science(rover)

        self.__state = np.zeros(2)
        self.__received = False

    def setState(self, task, instr):
        self.__state = np.array([task, instr])

    def getState(self):
        return self.__state


    def set_exception(self, exception):
        #self.rover.waiting = True
        self.rover.wait(self.rover.Exception_pub, exception)
        self.rover.Exception_pub.publish(exception.data)

        

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self, rover):

        self.rover = rover

        # next Navigation goal ID
        self.__currId = 0
        self.__currGoal = np.zeros(3)

        # rover position
        self.__pos = np.zeros(3)
        # rover linear velocity
        self.__linVel = np.zeros(3)
        # rover angular velocity
        self.__angVel = np.zeros(3)

    def setGoal(self, goal):

        self.rover.RoverConfirm_pub.publish("received NAV goal")
        self.__currId = goal.header.frame_id

        #self.__currGoal = goal
        self.rover.Nav_Goal_pub.publish(goal)
        

    def getId(self):
        return self.__currId

    def getGoal(self, id):
        return self.__currGoal

    '''def cancelGoal(self, given_id):
        self.__currGoal = np.zeros(0)
        self.__currId = -1
        self.rover.Nav_CancelGoal_pub.publish(GoalID(stamp = rospy.get_time(), id = given_id))
    '''
    def cancelGoal(self):

        self.rover.RoverConfirm_pub.publish("received NAV goal cancellation")
        
        self.__currGoal = np.zeros(0)
        self.rover.Nav_CancelGoal_pub.publish(GoalID(stamp = rospy.get_time(), id = self.__currId))

    
    #------------- Twist Data -------------
    
    def setPos(self, arr):
        self.__pos = arr

    def setLinVel(self, arr):
        self.__linVel = arr

    def setAngVel(self, arr):
        self.__angVel = arr


    def getPos(self):
        return self.__pos

    def getLinVel(self):
        return self.__linVel

    def getAngVel(self):
        return self.__angVel

    #-------------------------------------

    def nav_data(self, odometry_ros):
        odometry = odometry_ros.data

        # position (x,y,z)
        pos = odometry.pose.pose.position
        self.setPos([pos.x, pos.y, pos.z])

        # linear velocity
        twistLin = odometry.twist.twist.linear
        self.setLinVel([twistLin.x, twistLin.y, twistLin.z])

        # angular velocity
        twistAng = odometry.twist.twist.angular
        self.setAngVel([twistAng.x, twistAng.y, twistAng.z])

        self.rover.NAV_odometry_pub.publish(odometry)


class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self, rover):

        self.rover = rover

        # tube humidity
        self.__tubeHum = 0
        self.__params = []
        # total sample mass
        self.__sc_mass = 0
        self.__info = ""

    def set_text_info(self, str_ros):
        self.__info = str_ros.data
        self.rover.SC_state_pub.publish(self.__info)


    def set_sc_mass(self, mass):
        self.__sc_mass = mass
        self.rover.SC_mass_pub.publish(self.__sc_mass)
    
    def get_sc_mass(self):
        return self.__sc_mass


    def set_humidity(self, humidities_ros):
        humidity = humidities_ros.data
        self.__tubeHum = humidity

    def get_tube_hum(self):
        return self.__tubeHum


    def params(self, arr):
        self.__params = arr.data
        #self.rover.waiting = True
        self.rover.wait(self.rover.SC_params_pub, arr)



class HandlingDevice:
    
    ''' Monitoring Handling Device Data '''

    def __init__(self, rover):

        self.rover = rover

        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1
        self.__semiAutoId = -1
        self.__joint_positions = np.array(7)
        self.__joint_velocities = np.array(7)

        self.__distToElem = 0

    def setHDMode(self, mode_ros):

        self.rover.RoverConfirm_pub.publish("HD mode set")

        mode = mode_ros.data
        if(mode < 0 or mode > 3): 
            #raise ValueError("Invalid mode")
            self.rover.Exception_pub.publish("Invalid mode, must be between 0 and 3")
        else:
            self.__hd_mode = mode
            self.rover.HD_mode_pub.publish(mode)

    def getHDMode(self):
        return self.__hd_mode


    def set_semiAutoID(self, id_ros):

        self.rover.RoverConfirm_pub.publish("received HD element ID")

        id = id_ros.data
        #self.rover.HD_SemiAuto_Id_pub.publish(self.__semiAutoId)
        if(id < 0 or id > 14):
            self.rover.Exception_pub.publish("Invalid ID, must be between 0 and 14")
        else:
            self.__semiAutoId = id
            self.rover.HD_SemiAuto_Id_pub.publish(id)


    def getId(self):
        return self.__semiAutoId


    def set_joint_telemetry(self, telemetry_ros):
        telemetry = telemetry_ros.data
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        self.rover.HD_telemetry_pub.publish(telemetry)


    def set_joint_positions(self, positions):
        self.__joint_positions = positions

    def get_joint_positions(self):
        return self.__joint_positions


    def set_joint_velocities(self, velocities):
        self.__joint_velocities = velocities

    def get_joint_velocities(self):
        return self.__joint_velocities

    
    def set_tof(self, val):
        self.__distToElem = val.data
        self.rover.HD_tof_pub.publish(val.data)


    def setDetectedElement(self, elem):
        self.rover.HD_element_pub(elem)


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
#       - Retry  = 5 (HD and SC specific)
def checkArgs(task, instr):

    if (task < 1 or task > 4): raise ValueError("inexistent task")
    if(task != 4):
        if (instr < 1 or instr > 6): raise ValueError("inexistent instruction")
    else:
        if( (instr < 10 or instr > 11) or
            (instr < 20 or instr > 22) or
            (instr < 30 or instr > 32) or
            (instr < 40 or instr > 42) or
            (instr != 50) or
            (instr != 8) or
            (instr != 9) or
            (instr < 0 or instr > 3)
            ): raise ValueError("inexistent instruction")

    if(instr == 5):
        if(task != 3 and task != 4): raise ValueError("This task can't run Retry")


# TODO smthg to do with HD ... ?
def extract_bit(index, num):
    mask = 1
    mask = mask << index
    return num and mask



# ==========================================================================================
# instances

