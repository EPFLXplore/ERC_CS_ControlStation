#!/usr/bin/python
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class

from std_msgs.msg       import Int8, Int16, Bool, String, Int8MultiArray,  Int16MultiArray, UInt8MultiArray 
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Twist 
from actionlib_msgs.msg import GoalID
from sensor_msgs.msg    import JointState
from nav_msgs.msg       import Odometry

from model     import *
from Globals   import *


#======================================================

'''
    This class initializes all ROS publishers and subscribes to all the needed topics
'''

class Rover:

    def __init__(self):
        rospy.init_node('ROVER', anonymous=True)

        self.model = Model(self)

        self.ROVER_STATE = Task.IDLE

        # +--------------------------------------------------------+
        # |                       PUBLISHERS                       |
        # +--------------------------------------------------------+

        # publish True if instruction receivd from CS (Rover node --> CS_node)
        self.RoverConfirm_pub  = rospy.Publisher('ROVER_RoverConfirm',            String,          queue_size=1)
        # publish info on exception if one was thrown (Rover node --> CS_node)
        self.Exception_pub     = rospy.Publisher('ROVER_Exception',               String,          queue_size=1)
        self.TaskProgress      = rospy.Publisher('ROVER_TaskProgress',            Int8,            queue_size=1)
        self.SC_state_pub      = rospy.Publisher('ROVER_SC_state',                String,          queue_size=1)
        self.SC_humidities_pub = rospy.Publisher('ROVER_SC_measurments_humidity', Int16MultiArray, queue_size=1)
        self.SC_mass_pub       = rospy.Publisher('ROVER_SC_measurments_mass',     Int16,           queue_size=1)
        self.HD_telemetry_pub  = rospy.Publisher('ROVER_HD_telemetry',            JointState,      queue_size=1)
        self.NAV_odometry_pub  = rospy.Publisher('ROVER_NAV_odometry',            Odometry,        queue_size=1)

        # publish instruction concerning the Maintenance task  (Rover node --> HD node)
        self.Maintenance_pub = rospy.Publisher('Maintenance', Int8, queue_size=1)
        # publish instruction concerning the Navigation task (Rover node --> Nav node)
        self.Nav_pub = rospy.Publisher('Navigation', Int8, queue_size=1)
        # publish instruction concerning the Science Bay (Rover node --> Science node)
        self.SC_pub = rospy.Publisher('sc_cmd', Int8, queue_size=1)


        # +------------------------------------------------------+
        # |                     SUBSCRIBERS                      |
        # +------------------------------------------------------+

        # receive an array = [task, instruction] (CS_node --> Rover node)
        rospy.Subscriber('Task',              Int8MultiArray,     self.task_instr)
        rospy.Subscriber('CS_HD_mode',        Int8,               self.model.HD.setHDMode)
        rospy.Subscriber('CS_HD_SemiAuto_Id', Int8,               self.model.HD.set_semiAutoID)
        rospy.Subscriber('CS_NAV_goal',       MoveBaseActionGoal, self.model.Nav.setGoal)
        #rospy.Subscriber('CS_NAV_cancel',     GoalID,             self.model.Nav.cancel_goal)


        self.HD_mode_pub        = rospy.Publisher('HD_mode',           Int8,               queue_size=1)
        self.HD_SemiAuto_Id_pub = rospy.Publisher('HD_SemiAuto_Id',    Int8,               queue_size=1)
        self.Nav_Goal_pub       = rospy.Publisher('/move_base/goal',   MoveBaseActionGoal, queue_size=1)
        self.Nav_CancelGoal_pub = rospy.Publisher('/move_base/cancel', GoalID,             queue_size=1)

        # LOCAL ROS COMMUNICATION

        rospy.Subscriber('Exception',                    String,          self.model.set_exception)
        rospy.Subscriber('/odometry/filtered',           Odometry,        self.model.Nav.nav_data)
        rospy.Subscriber('/arm_control/joint_telemetry', JointState,      self.model.HD.set_joint_telemetry)
        rospy.Subscriber('sc_state',                     String,          self.model.SC.set_text_info)
        rospy.Subscriber('sc_measurments_humidity',      Int16,           self.model.SC.set_humidities)
        rospy.Subscriber('sc_measurments_mass',          Int16,           self.model.SC.set_sc_mass)

        '''rospy.Subscriber('/odometry/filtered',           Odometry,     self.Nav_pub.publish)
        rospy.Subscriber('/arm_control/joint_telemetry', JointState,      self.HD_telemetry.publish)
        rospy.Subscriber('sc_state',                     String,          self.SC_state_pub.publish)
        rospy.Subscriber('sc_measurments_humidity',      Int16MultiArray, self.SC_humidities_pub.publish)
        rospy.Subscriber('sc_measurments_mass',          Int16,           self.SC_mass_pub.publish)'''


    # receives array: [task, instr]:
    #
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
    #       - Retry  = 5

    def task_instr(self, array):

        task = array.data[0]
        instr = array.data[1]

        if not(1 <= task <= 4):
            self.Exception_pub.publish("Task number denied (allowed only 1-4), received:", task) 
            pass
        if not(1 <= instr <= 5):
            self.Exception_pub.publish("Instr number denied (allowed only 1-5), received:", instr) 
            pass
        
        rospy.loginfo("Rover: [task = %d, instr = %d] received", task, instr)
        self.RoverConfirm_pub.publish("Instructions received")
        #self.RoverConfirm_pub.publish(Bool(True))

        if (task == 1):
            self.ROVER_STATE = Task.MANUAL

        elif (task == 2): #Navigation
            self.ROVER_STATE = Task.NAVIGATION
            if(instr == 2):
                self.model.Nav.cancelGoal()
                self.ROVER_STATE = Task.IDLE
            else:
                self.Nav_pub.publish(instr)

        elif (task == 3): #Maintenance
            self.ROVER_STATE = Task.MAINTENANCE
            self.Maintenance_pub.publish(instr)

        else:  #task == 4, Science
            self.ROVER_STATE = Task.SCIENCE
            self.SC_pub.publish(instr)
        
    # ros starts spinning and the node starts listening to info 
    # coming from topics it's subscribed to
    def run(self):
        print("Listening")
        rospy.spin() 
 

#==========================================================================
#MAIN
if __name__ == '__main__':
    rover = Rover()
    rover.run()
