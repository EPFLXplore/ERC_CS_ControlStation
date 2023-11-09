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

from multiprocessing.sharedctypes import Value
from unittest.loader    import VALID_MODULE_NAME
from actionlib_msgs.msg import GoalID
#from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Pose, Point, PoseStamped
from sensor_msgs.msg    import JointState
from std_msgs.msg       import Int8, Int16, Bool, String, Int8MultiArray,  Int16MultiArray, UInt8MultiArray, Float32MultiArray 

#from .rover import Rover
from .Globals import *


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

    #--------ROVER STATE--------
    def setState(self, task, instr):
        self.__state = np.array([task, instr])

    def getState(self):
        return self.__state

    def getTask(self):
        return self.__state[0]

    #--------Exception--------
    # callback for received exceptions (transmits directly to CS)
    # Exception should be of type std.msg.String()
    def set_exception(self, exception):
        self.rover.wait(self.rover.Exception_pub, exception)
        self.rover.Exception_pub.publish(exception)

    # callback for task progress (success/fail) and transmits it to CS
    # val should be of type std.msg.Int8()
    def setProgress(self, val):
        #if NAV task then topic 'TaskProgress' received a success msg => goal is basically cancelled (??? TODO)
        if(self.getTask() == Task.NAVIGATION.value):
            self.Nav.setCancelled(True)
        
        self.rover.TaskProgress_pub.publish(val)
        

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self, rover):

        self.rover = rover

        # next Navigation goal ID
        self.__currId = 0
        self.__currGoal = PoseStamped()

        # rover position
        self.__pos = np.zeros(3)
        # rover linear velocity
        self.__linVel = np.zeros(3)
        # rover angular velocity
        self.__angVel = np.zeros(3)

        self.__cancelled = True 

    def setCancelled(self, bool):
        self.__cancelled = bool


    # -------callback for received PoseStamped from the CS-------
    def sendGoal(self, data):
        print(data.pose.position.x)
        print(data.pose.position.y)
        print(data.pose.position.z)
        self.rover.Nav_Goal_pub.publish(data)
        
    # -------get goal id-------
    def getId(self):
        return self.__currId

    # -------get the PoseStamped msg-------
    def getGoal(self):
        return self.__currGoal

    # -------called when CS sends an ABORT instruction to NAV task --> it cancels the goal and the rover stops-------
    # -------Also called when the CS sends a cancel instruction to the rover-------
    def cancelGoal(self, msg):
        # self.rover.RoverConfirm_pub.publish(String(data="received NAV goal cancellation"))

        # if(not self.__cancelled): 
        #     self.setCancelled(True)
        #     self.__currGoal = np.zeros(0)
        #     self.rover.Nav_Status.publish(String(data="cancel"))
        self.rover.Nav_Cancel_pub.publish(msg)

    #-------------------------------------
    def gamepad(self, joy):
        self.rover.Nav_gamepad_pub.publish(joy)


class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self, rover):

        self.rover = rover

        # tube humidity
        self.__tubeHum = 0
        self.__params = [0]*11
        self.__info = "info"
        self.__state = "state"

    def science_fsm_callback(self, state):
        self.__state = state.data #TODO: Check if .data is needed
        self.rover.SC_fsm_state_pub.publish(state)
    #---------------------------FUNCTIONS BELOW ARE NOT USED------------------------------
    # -------text info from SC-------
    def set_text_info(self, str_ros):
        self.__info = str_ros.data
        self.rover.wait(self.rover.SC_infos_pub, str_ros)

    def get_text_info(self):
        return self.__info

    # -------state of SC's FSM-------
    def set_state_info(self, str_ros):
        self.__state = str_ros.data
        self.rover.wait(self.rover.SC_infos_pub, str_ros)

    def get_state_info(self):
        return self.__state

    # -------SC tube humidity-------
    def set_humidity(self, humidities_ros):
        humidity = humidities_ros.data
        self.__tubeHum = humidity

    def get_tube_hum(self):
        return self.__tubeHum

    # -------parameters (11 elements):-------
        #   - disc position
        #   - whether tubes 0 to 2 are closed
        #   - whether tubes 0 to 2 are empty
        #   - whether trap is closed
        #   - mass of each tube
    def params(self, arr):
        self.__params = arr.data
        self.rover.wait(self.rover.SC_params_pub, arr)

    def getParams(self):
        return self.__params


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

    # -------HD mode: autonomous, direct manual, inverse manual-------
    # Expects mode_ros to be an std.msg.Int8
    def setHDMode(self, mode_ros):

        self.rover.RoverConfirm_pub.publish(String(data="HD mode set"))

        mode = mode_ros.data
        if(mode < 0 or mode > 3):
            #raise ValueError("Invalid mode")
            self.rover.Exception_pub.publish(String(data="Invalid mode, must be between 0 and 3"))
        else:
            self.__hd_mode = mode
            self.rover.HD_mode_pub.publish(mode_ros)
            self.rover.node.get_logger().info("mode HD :" + str(mode))


    def send_element_id_hd(self, id):
        self.rover.send_HD_element_id_pub.publish(id)
        self.rover.node.get_logger().info("HD element ID :" + str(id))

    def send_toggle_info(self, toggle):
        self.rover.send_toggle_info_pub.publish(Bool(data=toggle))

    def getHDMode(self):
        return self.__hd_mode

    # -------ID of element we want to manipulate autonomously-------
    def set_semiAutoID(self, id_ros):

        self.rover.RoverConfirm_pub.publish(String(data="received HD element ID"))

        id = id_ros.data
        #self.rover.HD_SemiAuto_Id_pub.publish(self.__semiAutoId)
        if(id < 0 or id > 14):
            self.rover.Exception_pub.publish(String(data="Invalid ID, must be between 0 and 14"))
        else:
            self.__semiAutoId = id
            #self.rover.HD_SemiAuto_Id_pub.publish(id) TODO: SEE WHY THIS IS USEFUL

    
    def cancel_goal(self, val):
        self.rover.node.get_logger().info("HD: sending cancel goal")
        self.rover.Maintenance_pub.publish(Int8(data = 5))

    
    def handle_hd_gamepad(self, axes):
        self.rover.HD_Gamepad_pub.publish(axes)

    def set_joint_telemetry(self, telemetry_ros):
        telemetry = telemetry_ros.data
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        self.rover.HD_telemetry_pub.publish(telemetry)

    def getId(self):
        return self.__semiAutoId

    # -------HD joints' positions (rad) and velocity (rad/s ??? TODO)-------
    #Jointstate is a ROS message
    def set_joint_telemetry(self, telemetry_ros):
        telemetry = telemetry_ros.data
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        self.rover.HD_telemetry_pub.publish(telemetry)

    # -------HD joints' positions-------
    def set_joint_positions(self, positions):
        self.__joint_positions = positions

    def get_joint_positions(self):
        return self.__joint_positions

    # HD joints' velocities
    def set_joint_velocities(self, velocities):
        self.__joint_velocities = velocities

    def get_joint_velocities(self):
        return self.__joint_velocities

    # ToF (time of flight): distance to element
    #Expects a ros message
    def set_tof(self, val):
        self.__distToElem = val.data
        self.rover.HD_tof_pub.publish(val)

    # retransmit info of an element of the control panel: [id, x, y, z, a, b, c] 
    # we receive these infos progressively as HD scans the control panel and detects new elements
    def setDetectedElement(self, elem):
        self.rover.HD_element_pub(elem)

    # transmit id + translations + rotations in the form of a Float32MultiArray to the CS
    def pub_detected_elements(self, obj_list):
        for i in range(len(obj_list)):
            panel = obj_list[i]
            msg = Float32MultiArray(data= [panel.id, panel. x_pos, panel.y_pos, panel.z_pos, panel.x_rot, panel.y_rot, panel.z_rot])
            self.rover.HD_element_pub.publish(msg)

    def gamepad(self, joy):
        self.rover.HD_gamepad_pub.publish(joy)


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