import numpy as np

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self):

        self.channel_layer = get_channel_layer()

        self.position = [0,0,0]
        self.orientation = [0,0,0]
        self.linVel = [0,0,0]
        self.angVel = [0,0,0]

        self.steering_wheel_ang = [0,0,0,0]
        self.steering_wheel_state = [0,0,0,0]
        # self.driving_wheel_ang = [0,0,0,0]
        self.driving_wheel_state = [0,0,0,0]

        self.info = ""
        self.displacement_mode = ""

        self.path = [[]]

        #self.wheels_ang = [0,0,0,0]

        #pas besoin de les save, on les envoye directement au frontend
        #self.__nextId = 0
        # self.__goal = np.zeros(3)
        # self.__pos = np.zeros(3)
        # self.__yaw = 0
        # self.__linVel = np.zeros(3)
        # self.__angVel = np.zeros(3)

        self.__navGoalList = np.array([])
        self.__navCurrentGoal = np.zeros(3)

    def addGoal(self, arr):
        if(len(arr) != 3): raise Exception("array length must be 3 -> (x,y,z)")
        np.append(self.__navGoalList, arr)
        #self.incrementId()

    # ---------GOAL----------
    def setCurrentGoal(self, arr):
        return
    
    #return the current goal
    def getNextGoal(self):
        return self.__navGoalList[0]
    
    #return and remove the current goal, should be called when the rover send confirmation
    def popGoal(self):
        return self.__navGoalList.pop(0)

    def cancelGoal(self, id):
        len = len(self.__goals)
        if (id < 0 or id > len): raise ValueError("Invalid navigation goal id")
        np.delete(self.__goals, id, 0)
    
    def UpdateNavSocket(self):
        # async_to_sync(self.channel_layer.group_send)("nav", {"type": "nav_message",
        #                                                     'position'   : [self.position[0], self.position[1], self.position[2]],
        #                                                     'orientation': [self.orientation[0], self.orientation[1], self.orientation[2], self.orientation[3]],
        #                                                     'linVel'     : [self.linVel[0], self.linVel[1], self.linVel[2]],
        #                                                     'angVel'     : [self.angVel[0], self.angVel[1], self.angVel[2]],
        #                                                     'current_goal' : "",
        #                                                     'wheel_ang' : [self.wheels_ang[0], self.wheels_ang[1], self.wheels_ang[2], self.wheels_ang[3]],
        #                                                                 })
        
        async_to_sync(self.channel_layer.group_send)("nav", {"type": "nav_message",
                                                    'position'   : [str(val) for val in self.position],
                                                    'orientation': [str(val) for val in self.orientation],
                                                    'linVel'     : [self.linVel[0], self.linVel[1], self.linVel[2]],
                                                    'angVel'     : [self.angVel[0], self.angVel[1], self.angVel[2]],
                                                    'path' : [str(val) for val in self.path],
                                                    'steering_wheel_ang': [str(val) for val in self.steering_wheel_ang],
                                                    'steering_wheel_state': [str(val) for val in self.steering_wheel_state],
                                                    'driving_wheel_ang': [],
                                                    'driving_wheel_state': [str(val) for val in self.driving_wheel_state],
                                                    'info' : self.info,
                                                    'displacement_mode' : self.displacement_mode,
                                                    })