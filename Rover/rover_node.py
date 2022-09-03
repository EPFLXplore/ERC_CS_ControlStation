#!/usr/bin/python
import time
import rospy

from abc import ABC, abstractmethod #Abstract Base Class

from std_msgs.msg       import Int8, Int16, Int32, Bool, String, Int8MultiArray,  Int16MultiArray, UInt8MultiArray 
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Twist, PoseStamped
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

        self.received = False
        self.waiting  = False
        self.tries = 0

        self.ROVER_STATE = Task.IDLE

        # +--------------------------------------------------------+
        # |                       PUBLISHERS                       |
        # +--------------------------------------------------------+

        # publish True if instruction receivd from CS (Rover node --> CS_node)
        self.RoverConfirm_pub  = rospy.Publisher('ROVER_RoverConfirm',            String,          queue_size=1)
        # publish info on exception if one was thrown (Rover node --> CS_node)
        self.Exception_pub     = rospy.Publisher('ROVER_Exception',               String,          queue_size=1)
        self.TaskProgress_pub  = rospy.Publisher('ROVER_TaskProgress',            Int8,            queue_size=1)
        self.SC_state_pub      = rospy.Publisher('ROVER_SC_state',                String,          queue_size=1)
        self.SC_infos_pub      = rospy.Publisher('ROVER_SC_info',                 String,          queue_size=1)
        self.SC_humidities_pub = rospy.Publisher('ROVER_SC_measurements_humidity', Int16,          queue_size=1)
        self.SC_params_pub     = rospy.Publisher('ROVER_SC_params',               Int16MultiArray, queue_size=1)
        self.HD_telemetry_pub  = rospy.Publisher('ROVER_HD_telemetry',            JointState,      queue_size=1)
        self.NAV_odometry_pub  = rospy.Publisher('ROVER_NAV_odometry',            Odometry,        queue_size=1)
        self.HD_tof            = rospy.Publisher('ROVER_HD_tof',                  Int32,           queue_size=1)
        self.HD_element_pub    = rospy.Publisher('ROVER_HD_detected_element',     Int16MultiArray, queue_size=3)

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
        rospy.Subscriber('Task',              Int8MultiArray, self.task_instr)
        rospy.Subscriber('CS_HD_mode',        Int8,           self.model.HD.setHDMode)
        rospy.Subscriber('CS_HD_SemiAuto_Id', Int8,           self.model.HD.set_semiAutoID)
        rospy.Subscriber('CS_NAV_goal',       PoseStamped,    self.model.Nav.setGoal)
        rospy.Subscriber('CS_Confirm',        Bool,           self.cs_confirm)


        self.HD_mode_pub        = rospy.Publisher('HD_mode',           Int8,        queue_size=1)
        self.HD_SemiAuto_Id_pub = rospy.Publisher('HD_SemiAuto_Id',    Int8,        queue_size=1)
        self.Nav_Goal_pub       = rospy.Publisher('CS/NAV_goal',       PoseStamped, queue_size=1)
        self.Nav_CancelGoal_pub = rospy.Publisher('/move_base/cancel', GoalID,      queue_size=1)

        # LOCAL ROS COMMUNICATION
        # TODO DO NOT DELETE YET
        '''rospy.Subscriber('Exception',                    String,          self.model.set_exception)
        rospy.Subscriber('sc_state',                     String,          self.model.SC.set_text_info)
        rospy.Subscriber('sc_info',                      String,          self.model.SC.set_text_info)
        rospy.Subscriber('sc_measurements_humidity',     Int16,           self.model.SC.set_humidity)
        rospy.Subscriber('sc_params',                    Int16MultiArray, self.model.SC.params)'''
        rospy.Subscriber('sc_state',                     String,          self.model.SC.set_text_info)
        rospy.Subscriber('sc_info',                      String,          self.model.SC.set_text_info)  #self.SC_infos_pub.publish)
        rospy.Subscriber('sc_measurements_humidity',     Int16,           self.SC_humidities_pub.publish)
        rospy.Subscriber('sc_params',                    Int16MultiArray, self.model.SC.params)
        rospy.Subscriber('TaskProgress',                 Int8,            self.model.setProgress)


        # IMMEDIATE RETRANSMIT TO CS
        rospy.Subscriber('/odometry/filtered',           Odometry,        self.NAV_odometry_pub.publish)
        rospy.Subscriber('/arm_control/joint_telemetry', JointState,      self.HD_telemetry_pub.publish)
        rospy.Subscriber('/avionics_ToF',                Int32,           self.HD_tof.publish)
        rospy.Subscriber('detection/detected_elements',  Int16MultiArray, self.HD_element_pub.publish)


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

        '''if not(1 <= task <= 4):
            self.Exception_pub.publish("Task number denied (allowed only 1-4), received:", task) 
            pass
        if not(1 <= instr <= 5):
            self.Exception_pub.publish("Instr number denied (allowed only 1-5), received:", instr) 
            pass'''
        
        rospy.loginfo("Rover: [task = %d, instr = %d] received", task, instr)
        self.RoverConfirm_pub.publish("Instructions received")
        #self.RoverConfirm_pub.publish(Bool(True))

        # MANUAL
        if (task == Task.MANUAL.value):
            self.ROVER_STATE = Task.MANUAL

        # NAVIGATION
        elif (task == Task.NAVIGATION.value): 
            self.ROVER_STATE = Task.NAVIGATION

            if(instr == Instruction.ABORT.value): 
                self.model.Nav.cancelGoal()
                self.ROVER_STATE = Task.IDLE

            else:
                self.Nav_pub.publish(instr)

        # MAINTENANCE
        elif (task == Task.MAINTENANCE.value): 
            self.ROVER_STATE = Task.MAINTENANCE

            if(instr == Instruction.LAUNCH.value): 
                self.HD_SemiAuto_Id_pub.publish(self.model.HD.getId())

            elif(instr == Instruction.ABORT.value): 
                self.HD_SemiAuto_Id_pub.publish(-1)
                self.ROVER_STATE = Task.IDLE

            else:
                self.Maintenance_pub.publish(instr)

        # SCIENCE
        else: 
            self.ROVER_STATE = Task.SCIENCE
            if(task == ScienceTask.PARAMS.value):
                self.wait(self.SC_params_pub, Int16MultiArray(data=self.model.SC.getParams()))
                #self.SC_params_pub.publish(Int16MultiArray(data=self.model.SC.getParams()))

            else:
                self.SC_pub.publish(instr)
        
    # ros starts spinning and the node starts listening to info 
    # coming from topics it's subscribed to
    def run(self):
        print("Listening")
        rospy.spin() 
 
    
    def cs_confirm(self, bool):
        if(self.waiting): 
            rospy.loginfo("CS Confirmation Received")
            self.received = True


    def wait(self, pub, val):

        self.waiting = True

        pub.publish(val)
        start = time.time()
        while(not self.received and ((time.time() - start) < 1)): continue

        if(not self.received and self.tries < 3): 
            self.tries += 1
            self.wait(pub, val)

        if(not self.received):
            rospy.loginfo("Answer not received: TIMEOUT")

        self.waiting = False
        self.received = False


#==========================================================================
#MAIN
if __name__ == '__main__':
    rover = Rover()
    rover.run()
