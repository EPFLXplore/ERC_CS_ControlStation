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

import numpy as np 

#================================================================================

class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    WAITING     = 5

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

    def setState(self, task):
        self.__state = task

    def getState(self):
        return self.__state

    def setReceived(self, bool):
        self.__received = bool

    def getReceived(self):
        return self.__received

    def setInWait(self, bool):
        self.__inWait = bool

    def getInWait(self):
        return self.__inWait
        

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self):
        # next Navigation goal ID
        self.__nextId = 0

        # keep track of goals
        #self.__goals = np.array([])
        self.__goal = np.zeros(3)

        # rover position
        self.__pos = np.zeros(3)
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
        self.__goal = arr

    def incrementId(self):
        self.__nextId += 1

    '''def getGoal(self, id):
        return self.__goals[id]
    '''

    def getGoal(self):
        return self.__goal

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
        diff = self.getGoal() - self.getPos()
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

        self.__op_tube = np.zeros(2)
        self.__cmd = -1

    #--------------------------

    def setSCMass(self, mass):
        self.__masses[self.__op_tube[1]] = mass
    
    def getSCMass(self, idx):
        if(idx < 0 or 2 < idx): raise ValueError("impossible tube number chosen (can be either 0, 1 or 2)")
        return self.__sc_mass[idx]

    #--------------------------

    def setTubeHum(self, val):
        self.__tubeHum = val

    def getTubeHum(self):
        return self.__tubeHum

    #--------------------------

    def setOperation(self, op):
        self.__op_tube[0] = op
        self.setTubeCmd()

    def getOperation(self):
        return self.__op_tube[0]


    #--------------------------

    def selectTube(self, t):
        self.__op_tube[1] = t
        self.setTubeCmd()

    def getSelectedTube(self):
        return self.__op_tube[1]

    #--------------------------

    def setTubeCmd(self):
        arr = self.__op_tube
        self.setCmd(arr[0]*10 + arr[1])
    
    #--------------------------

    def setCmd(self, cmd):
        self.__cmd = cmd

    def getCmd(self):
        return self.__cmd

    #--------------------------


class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

        self.__joint_positions = np.array(7)
        self.__joint_velocities = np.array(7)

    #--------------------------

    def setHDMode(self, mode):
        if(mode < 0 or mode > 3): raise ValueError("Invalid mode")
        self.__hd_mode = mode

    def getHDMode(self):
        return self.__hd_mode

    #--------------------------

    def set_joint_telemetry(self, telemetry):
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        #self.rover.HD_telemetry_pub.publish(telemetry)

    #--------------------------

    def set_joint_positions(self, positions):
        self.__joint_positions = positions

    def get_joint_positions(self):
        return self.__joint_positions

    #--------------------------

    def set_joint_velocities(self, velocities):
        self.__joint_velocities = velocities

    def get_joint_velocities(self):
        return self.__joint_velocities

    #--------------------------

    def getVelNorm(self):
        return np.linalg.norm(self.get_joint_velocities)

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




