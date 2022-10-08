import numpy as np

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
    # ---------GOAL----------
    def setGoal(self, arr):
        self.__goal[0] = arr[0]
        self.__goal[1] = arr[1]
        self.__goal[2] = arr[2]

    def cancelGoal(self):
        self.__goal = np.zeros(3)

    # increase id number by 1 (should be used when defining a new goal in order to assign it a new id)
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
    

    # ========= TWIST DATA =========

    #--------Rover Position--------
    def setPos(self, arr):
        self.__pos = arr

    def getPos(self):
        return self.__pos

    #--------Rover Linear Velocity--------
    def setLinVel(self, arr):
        self.__linVel = arr

    def getLinVel(self):
        #return self.__linVel
        return np.linalg.norm(self.__linVel)

    #--------Rover Angular Velocity--------
    def setAngVel(self, arr):
        self.__angVel = arr

    def getAngVel(self):
        #return self.__angVel
        return np.linalg.norm(self.__angVel)
    

    #----------Distance to Goal----------
    def distToGoal(self):
        pos = self.getPos()
        diff = np.array([self.getGoal()[0], self.getGoal()[1]]) - np.array([pos[0], pos[1]])
        return np.linalg.norm(diff)

