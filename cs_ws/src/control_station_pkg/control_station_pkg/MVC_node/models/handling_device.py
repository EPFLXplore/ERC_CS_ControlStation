import numpy as np

NBR_BUTTONS = 14
ELEMENT_DATA_SIZE = 6

class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

        # id of element we'd like to manipulate (inverse autonomous)
        self.__elemId = -1
        # ToF (time of flight)
        self.__distToElem = 0

        # the 6 joints + gripper
        self.__joint_positions = [0,0,0,0,0,0,0]
        self.__joint_velocities = [0,0,0,0,0,0,0]

        # matrix containing info on the movements each joint must do in order to reach an element
        # [x,y,z,a,b,c] (3 translations and 3 rotations)
        self.__elements = np.zeros((NBR_BUTTONS, ELEMENT_DATA_SIZE)) # 14x6 matrix

        self.voltage = 0.0

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
