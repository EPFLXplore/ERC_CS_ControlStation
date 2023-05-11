import numpy as np

class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self):

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
    

    #----------Distance to Goal----------
    # def distToGoal(self):
    #     pos = self.getPos()
    #     diff = np.array([self.getGoal()[0], self.getGoal()[1]]) - np.array([pos[0], pos[1]])
    #     return np.linalg.norm(diff)

