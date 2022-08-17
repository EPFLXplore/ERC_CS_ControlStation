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

# from multiprocessing.sharedctypes import Value
# from unittest.loader              import VALID_MODULE_NAME


class Rover:
    '''
        Monitoring of the state of the rover
    '''
    def __init__(self):

        self.Nav = Navigation()
        self.HD = HandlingDevice()
        self.SC = Science()
        

        self.__state = np.zeros(2)
        self.__inWait = False
        self.__received = False

    def setState(self, task, instr):
        self.__state = np.array([task, instr])

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
        self.__goals = np.array([])

        # rover position
        self.__pos = np.zeros(3)
        # rover linear velocity
        self.__linVel = np.zeros(3)
        # rover angular velocity
        self.__angVel = np.zeros(3)

    def addGoal(self, arr):
        if(len(arr) != 3): raise Exception("array length must be 3 -> (x,y,z)")

        np.append(self.__goals, arr)
        self.incrementId()

    def incrementId(self):
        self.__nextId += 1

    def getGoal(self, id):
        return self.__goals[id]

    def cancelGoal(self, id):
        len = len(self.__goals)
        if (id < 0 or id > len): raise ValueError("Invalid navigation goal id")
        np.delete(self.__goals, id, 0)
    
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

    def distToGoal(self, id):
        diff = self.getGoal(id) - self.getPos()
        return np.linalg.norm(diff)


class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):
        # humidity of the specific tube
        self.__tubeHum = 0
        # total sample mass
        self.__sc_mass = 0
        self.__masses = np.zeros(3)

        self.__op = -1
        self.__tube = -1
        self.__cmd = -1


    def setSCMass(self, mass):
        self.__sc_mass = mass
    
    def getSCMass(self):
        return self.__sc_mass

    def setTubeHum(self, val):
        self.__tubeHum = val

    def getTubeHum(self):
        return self.__tubeHum

    def selectTube(self, t):
        self.__tube = t
        self.setCmd(t + self.__op)

    def getSelectedTube(self):
        return self.__tube

    def setOperation(self, op):
        self.__op = op
        self.setCmd(op + self.__tube)

    def getOperation(self):
        return self.__op

    def setCmd(self, cmd):
        self.__cmd = cmd

    def getCmd(self):
        return self.__cmd



class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

        self.__joint_positions = np.array(7)
        self.__joint_velocities = np.array(7)

    def setHDMode(self, mode):
        if(mode < 0 or mode > 3): raise ValueError("Invalid mode")
        self.__hd_mode = mode

    def getHDMode(self):
        return self.__hd_mode


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



# ==========================================================================================
# instances

