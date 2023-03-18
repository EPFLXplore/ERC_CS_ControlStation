from enum import IntEnum
from .navigation import Navigation
from .handling_device import HandlingDevice
from .science import Science


"""
class Tab(IntEnum):
	NAV_MANUAL     = 0
	NAV_SEMIAUTO   = 1
	NAV_AUTO       = 2
	HD_MANUAL      = 3
	HD_AUTO        = 4
	SC_DATA        = 5
	SC_DRILL       = 6
	CAMERAS        = 7
	LOGS           = 8

class Instruction(IntEnum):
	LAUNCH  = 0
	WAIT    = 1
	RESUME  = 2
	ABORT   = 3
"""

#state de la FSM
class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    WAITING     = 5
    LOGS        = 6 #not really a task. Here just to display exceptions on GUI (it was convenient ;))

# =================================
#              ROVER
# =================================
class Rover:
    '''
        Monitoring of the state of the rover
    '''

    def __init__(self):

        # initialize each subsystem
        self.Nav = Navigation()
        self.HD  = HandlingDevice()
        self.SC  = Science()

        self.userIDs = []
        
        # current rover FSM state
        self.__state    = Task.IDLE

        # these two variables are useful in the wait() function of the controller
        # TODO (i think it'd be better to initialise them in the controller)
        self.__inWait   = False
        self.__received = False

        # array of infos on the exceptions thrown (in the form of a String)
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
