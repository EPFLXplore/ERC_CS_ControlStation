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
from unittest.loader              import VALID_MODULE_NAME


class Rover:
    '''
        Monitoring of the state of the rover
    '''
    def __init__(self):

        self.Nav = Navigation()
        self.HD = HandlingDevice()
        self.SC = Science()

        self.__state = np.zeros(2)

    def setState(self, task, instr):
        self.__state = np.array([task, instr])
        

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
        return self.__linVel

    def getAngVel(self):
        return self.__angVel

    #-------------------------------------


class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):
        # humidities of the 3 tubes
        self.__tubesHum = np.zeros(3)
        # total sample mass
        self.__sc_mass = 0


    def setSCMass(self, mass):
        self.__sc_mass = mass
    
    def getSCMass(self):
        return self.__sc_mass

    def setTubeHum(self, idx, val):
        self.__tubesHum[idx] = val

    def getTubeHum(self, idx):
        return self.__tubesHum[idx]



class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

    def setHDMode(self, mode):
        if(mode < 0 or mode > 3): raise ValueError("Invalid mode")
        self.__hd_mode = mode

    def getHDMode(self):
        return self.__hd_mode



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

