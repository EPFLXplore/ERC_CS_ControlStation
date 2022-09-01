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

from enum import IntEnum
from syslog import LOG_SYSLOG

import numpy as np 

#================================================================================


NBR_BUTTONS = 14
ELEMENT_DATA_SIZE = 6


class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    WAITING     = 5
    LOGS        = 6 #not really a task. Here just to display exceptions on GUI

class Rover:
    '''
        Monitoring of the state of the rover
    '''

    def __init__(self):

        self.Nav = Navigation()
        self.HD  = HandlingDevice()
        self.SC  = Science()
        

        self.__state    = Task.IDLE
        self.__inWait   = False
        self.__received = False

        self.__exceptions = []

    #--------State--------

    def setState(self, task):
        self.__state = task

    def getState(self):
        return self.__state

    #--------Received Flag--------

    def setReceived(self, bool):
        self.__received = bool

    def getReceived(self):
        return self.__received

    #--------Waiting Flag--------

    def setInWait(self, bool):
        self.__inWait = bool

    def getInWait(self):
        return self.__inWait
        
    #--------Exception--------

    def addException(self, e):
        self.__exceptions.append(str(e))

    def getExceptions(self):
        return self.__exceptions

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self):
        # next Navigation goal ID
        self.__nextId = 0

        # keep track of goals
        #self.__goals = np.array([])
        
        # [x,y, yaw]
        self.__goal = np.zeros(3)

        # rover position
        self.__pos = np.zeros(3)
        # rover yaw
        self.__yaw = 0
        # rover linear velocity
        self.__linVel = np.zeros(3)
        # rover angular velocity
        self.__angVel = np.zeros(3)

    '''def addGoal(self, arr):
        if(len(arr) != 3): raise Exception("array length must be 3 -> (x,y,z)")

        np.append(self.__goals, arr)
        self.incrementId()
    '''
    def setGoal(self, arr):
        self.__goal[0] = arr[0]
        self.__goal[1] = arr[1]
        self.__goal[2] = arr[2]

    def incrementId(self):
        self.__nextId += 1

    def getId(self):
        return self.__nextId

    '''def getGoal(self, id):
        return self.__goals[id]
    '''

    def getGoal(self):
        return self.__goal


    #--------Orientation--------
    def setYaw(self, val):
        self.__yaw = val

    def getYaw(self):
        return self.__yaw

    '''def cancelGoal(self, id):
        len = len(self.__goals)
        if (id < 0 or id > len): raise ValueError("Invalid navigation goal id")
        np.delete(self.__goals, id, 0)'''

    def cancelGoal(self):
        self.__goal = np.zeros(3)
    
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
        #return self.__linVel
        return np.linalg.norm(self.__linVel)

    def getAngVel(self):
        #return self.__angVel
        return np.linalg.norm(self.__angVel)

    #-------------------------------------

    '''def distToGoal(self, id):
        diff = self.getGoal(id) - self.getPos()
        return np.linalg.norm(diff)'''

    def distToGoal(self):
        pos = self.getPos()
        diff = np.array([self.getGoal()[0], self.getGoal()[1]]) - np.array([pos[0], pos[1]])
        return np.linalg.norm(diff)

class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):
        # humidity of the specific tube
        self.__tubeHum = 0
        # total sample mass

        self.__masses = np.zeros(3)
        self.__tubes_closed = np.zeros(3)
        self.__volumes = np.zeros(3)
        self.__colors = np.zeros(3)
        self.__particleSizes = np.zeros(3)
        self.__densities = np.zeros(3)
        self.__trap_closed = True
        self.__filled = np.zeros(3)

        self.__info = []


        self.__op_tube = np.zeros(2)
        self.__cmd = -1

    #--------SC Mass--------

    def setSCMass(self, mass):
        self.__masses[self.__op_tube[1]] = mass
    
    def getSCMass(self, idx):
        if(idx < 0 or 2 < idx): raise ValueError("impossible tube number chosen (can be either 0, 1 or 2)")
        return self.__sc_mass[idx]

    def getMasses(self):
        return self.__masses

    #--------Tube Humidity--------

    def setTubeHum(self, val):
        self.__tubeHum = val

    def getTubeHum(self):
        return self.__tubeHum

    #--------SC Operation--------

    def setOperation(self, op):
        self.__op_tube[0] = op
        self.setTubeCmd()

    def getOperation(self):
        return self.__op_tube[0]

    #--------Tube--------

    def selectTube(self, t):
        self.__op_tube[1] = t
        self.setTubeCmd()

    def getSelectedTube(self):
        return self.__op_tube[1]

    #--------Specific Tube Command--------

    def setTubeCmd(self):
        arr = self.__op_tube
        self.setCmd(arr[0] + arr[1])
    
    #--------Command--------

    def setCmd(self, cmd):
        self.__cmd = cmd

    def getCmd(self):
        return self.__cmd

    #--------Opened tubes--------

    def setTubeState(self, idx, val):
        self.__tubes_closed[idx] = bool(val)

    def getTubesState(self):
        return self.__tubes_closed

    #--------Densities--------
    def setDensity(self, idx, val):
        self.__densities[idx] = val

    def getDensities(self):
        return self.__densities

    #--------Volumes--------

    def setVolume(self, idx, val):
        self.__volumes[idx] = val

    def getVolumes(self):
        return self.__volumes

        
    #--------Trap--------

    def setTrapState(self, val):
        self.__trap_closed= bool(val)

    def getTrapState(self):
        return self.__trap_closed

    #--------Particle Size--------

    def setParticleSize(self, idx, val):
        self.__particleSizes[idx] = val

    def getParticleSizes(self):
        return self.__particleSizes

    #--------Filled--------

    def setTubeFilled(self, idx, val):
        self.__filled[idx] = val

    def getFilled(self):
        return self.__filled

    #--------Colors--------

    def setTubeColor(self, idx, val):
        self.__colors[idx] = val

    def getTubeColor(self):
        return self.__colors

    #--------INFO--------

    def addInfo(self, txt):
        self.__info.append(txt)

    def getInfos(self):
        return self.__info

    #--------STATE--------
    def setState(self, txt):
        self.__state = txt

    def getState(self):
        return self.__state


    #--------DESERIALIZATION--------
    def deSerializeState(self, save_list):
        '''
        Undo the serialization of serializeState and save the variables.
        Input: save_list (list of int) list to be deserialized
        Output: None
        '''

        #cast to ints
        save_list = map(int,save_list)

        #desrializing
        #self.disc_position = save_list[0]
        self.__tubes_closed = map(bool,save_list[1:4])
        self.__filled = map(bool,save_list[4:7])
        self.__trap_closed = bool(save_list[7])
        self.__masses = save_list[8:] # TODO il me semble que ça renvoit 4 nombres et pas 3



class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

        self.__elemId = -1
        self.__distToElem = 0

        self.__joint_positions = [0,0,0,0,0,0,0]
        self.__joint_velocities = [0,0,0,0,0,0,0]

        self.__elements = np.zeros((NBR_BUTTONS, ELEMENT_DATA_SIZE)) # 14x6 matrix

    #--------HD mode--------

    def setHDMode(self, mode):
        if(mode < 0 or mode > 3): raise ValueError("Invalid mode")
        self.__hd_mode = mode

    def getHDMode(self):
        return self.__hd_mode

    #--------ROS telemetry--------

    def set_joint_telemetry(self, telemetry):
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        #self.rover.HD_telemetry_pub.publish(telemetry)

    #--------Joint Positions--------

    def set_joint_positions(self, positions):
        self.__joint_positions = positions

    def get_joint_positions(self):
        return self.__joint_positions

    #--------Joint Velocities--------

    def set_joint_velocities(self, velocities):
        self.__joint_velocities = velocities

    def get_joint_velocities(self):
        return self.__joint_velocities

    #--------Velocity--------

    def getVelNorm(self):
        return np.linalg.norm(self.get_joint_velocities)

    #--------ID--------
    
    def setElemId(self, id):
        self.__elemId = id

    def getElemId(self):
        return self.__elemId

    #--------ToF--------

    def set_tof(self, tof):
        self.__distToElem = tof

    def get_tof(self):
        return self.__distToElem

    #--------Detected Elements--------
    
    def setDetectedElement(self, arr):
        print("AHHHHHHHHHHHHHHHHHHHH")
        data = np.zeros(ELEMENT_DATA_SIZE)
        for i in range(6):
            data[i] = arr[i+1]
        self.__elements[arr[0]-1] = data  # arr[0]-1 because ids are numbered 1 to 14 and array is indexed 0 to 13

    def getElements(self):
        return self.__elements


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
    if (instr < 1 or instr > 6): raise ValueError("inexistent instruction")

    if(instr == 5):
        if(task != 3 and task != 4): raise ValueError("This task can't run Retry")


# TODO smthg to do with HD ... ?
def extract_bit(index, num):
    mask = 1
    mask = mask << index
    return num and mask




