#!/usr/bin/python
import time
import rospy

#from abc import ABC, abstractmethod #Abstract Base Class

from std_msgs.msg       import Int8, Int16, Int32, Bool, String, Int8MultiArray,  Int16MultiArray, Float32MultiArray, UInt8MultiArray 
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Twist, PoseStamped
from actionlib_msgs.msg import GoalID
from sensor_msgs.msg    import JointState
from nav_msgs.msg       import Odometry

from model     import *
from Globals   import *
from vision_no_ros.msg import *


#======================================================

'''
from 
    This class initializes all ROS publishers and subscribes to all the needed topics
'''

class Rover:

    def __init__(self):
        rospy.init_node('ROVER', anonymous=True)

        self.model = Model(self)

        # variables used for the timeout system
        self.received = False
        self.waiting  = False
        self.tries = 0

        # state of the rover (FSM)
        self.ROVER_STATE = Task.IDLE


        # The communication between the Rover and the CS is done in such a way that
        # all information other subsystems publish on different topics is read by this code
        # and is then retransmitted to the CS.
        # This has been done because local ROS communication between subsystems won't suffer 
        # information loss due to faulty connection (which can happen between the Rover and the CS).
        # => instead of having the CS listen to all the topics being published to by different subsystems.
        # The info is read by this code, stored by this code and retransmitted to the CS. In this way, we have one central ROVER node
        # dealing with connection problems => if CS doesn't receive an info it just asks for ROVER to resend it
        # instead of asking a concrete subsystem.


        # ==========================================================
        #              MESSAGES BETWEEN ROVER AND CS
        # ==========================================================

        # ===== PUBLISHERS =====

        # Rover --> CS
        self.RoverConfirm_pub  = rospy.Publisher('ROVER_RoverConfirm',            String,          queue_size=1)
        self.Exception_pub     = rospy.Publisher('ROVER_Exception',               String,          queue_size=1)
        self.TaskProgress_pub  = rospy.Publisher('ROVER_TaskProgress',            Int8,            queue_size=1)
        # Rover(SC) --> CS
        self.SC_state_pub      = rospy.Publisher('ROVER_SC_state',                String,          queue_size=1)
        self.SC_infos_pub      = rospy.Publisher('ROVER_SC_info',                 String,          queue_size=1)
        self.SC_humidities_pub = rospy.Publisher('ROVER_SC_measurements_humidity', Int16,          queue_size=1)
        self.SC_params_pub     = rospy.Publisher('ROVER_SC_params',               Int16MultiArray, queue_size=1)
        # Rover(HD) --> CS
        self.HD_telemetry_pub  = rospy.Publisher('ROVER_HD_telemetry',            JointState,      queue_size=1)
        self.HD_tof            = rospy.Publisher('ROVER_HD_tof',                  Int32,           queue_size=1)
        self.NAV_odometry_pub  = rospy.Publisher('ROVER_NAV_odometry',            Odometry,        queue_size=1)
        self.HD_element_pub    = rospy.Publisher('ROVER_HD_detected_element',     Float32MultiArray, queue_size=3)


        # ===== SUBSCRIBERS =====

        # messages from CS
        rospy.Subscriber('Task',              Int8MultiArray, self.task_instr)
        rospy.Subscriber('CS_Confirm',        Bool,           self.cs_confirm)
        # messages form CS (HD)
        rospy.Subscriber('CS_HD_mode',        Int8,           self.model.HD.setHDMode)
        rospy.Subscriber('CS_HD_SemiAuto_Id', Int8,           self.model.HD.set_semiAutoID)
        # messages from CS (NAV)
        rospy.Subscriber('CS_NAV_goal',       PoseStamped,    self.model.Nav.setGoal)

        # ==========================================================
        #           MESSAGES BETWEEN ROVER AND SUBSYSTEMS
        # ==========================================================

        # ===== PUBLISHERS =====

        # Rover --> HD
        self.Maintenance_pub    = rospy.Publisher('Maintenance',       Int8, queue_size=1)
        self.HD_mode_pub        = rospy.Publisher('HD_mode',           Int8, queue_size=1)
        self.HD_SemiAuto_Id_pub = rospy.Publisher('HD_SemiAuto_Id',    Int8, queue_size=1)
        # Rover --> NAV
        self.Nav_pub            = rospy.Publisher('Navigation',        Int8,        queue_size=1)
        self.Nav_Goal_pub       = rospy.Publisher('CS/NAV_goal',       PoseStamped, queue_size=1)
        self.Nav_CancelGoal_pub = rospy.Publisher('/move_base/cancel', GoalID,      queue_size=1)
        # Rover --> SC
        self.SC_pub = rospy.Publisher('sc_cmd', Int8, queue_size=1)

        # ===== SUBSCRIBERS =====

        # SC --> Rover
        rospy.Subscriber('sc_state',                     String,          self.model.SC.set_state_info)
        rospy.Subscriber('sc_info',                      String,          self.model.SC.set_text_info)  #self.SC_infos_pub.publish)
        rospy.Subscriber('sc_measurements_humidity',     Int16,           self.SC_humidities_pub.publish)
        rospy.Subscriber('sc_params',                    Int16MultiArray, self.model.SC.params)
        rospy.Subscriber('TaskProgress',                 Int8,            self.model.setProgress)
        # NAV --> Rover
        rospy.Subscriber('/odometry/filtered',           Odometry,        self.NAV_odometry_pub.publish)
        # HD --> Rover
        rospy.Subscriber('/arm_control/joint_telemetry', JointState,      self.HD_telemetry_pub.publish)
        rospy.Subscriber('/avionics_ToF',                Int32,           self.HD_tof.publish)
        rospy.Subscriber('/detected_elements',           object_list,     self.model.HD.pub_detected_elements)


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
            # LAUNCH
            if(instr == Instruction.LAUNCH.value):
                rospy.loginfo("goal launched")
                self.Nav_Goal_pub.publish(self.model.Nav.getGoal())
            # ABORT
            elif(instr == Instruction.ABORT.value): 
                self.model.Nav.cancelGoal()
                self.ROVER_STATE = Task.IDLE
            # WAIT/RESUME
            else:
                self.Nav_pub.publish(instr)

        # MAINTENANCE
        elif (task == Task.MAINTENANCE.value): 
            self.ROVER_STATE = Task.MAINTENANCE
            # LAUNCH
            if(instr == Instruction.LAUNCH.value): 
                self.HD_SemiAuto_Id_pub.publish(self.model.HD.getId())
            # ABORT
            elif(instr == Instruction.ABORT.value): 
                self.HD_SemiAuto_Id_pub.publish(-1)
                self.ROVER_STATE = Task.IDLE
            # WAIT/RESUME
            else:
                self.Maintenance_pub.publish(instr)

        # SCIENCE
        else: 
            self.ROVER_STATE = Task.SCIENCE
            # REQUEST TO RESEND PARAMETERS
            if(instr== ScienceTask.PARAMS.value):
                self.wait(self.SC_params_pub, Int16MultiArray(data=self.model.SC.getParams()))
            # REQUEST TO RESEND INFO
            elif(instr == ScienceTask.INFO.value):
                self.wait(self.SC_infos_pub, String(self.model.SC.get_text_info()))
            # REQUEST TO RESEND STATE
            elif(instr == ScienceTask.STATE.value):
                self.wait(self.SC_state_pub, String(self.model.SC.get_state_info()))
            # COMMANDS SENT TO SC
            else:
                self.SC_pub.publish(instr)
        
    # run ros
    def run(self):
        print("Listening")
        rospy.spin() 
 
    
    # ===== TIMEOUT MECANISM =====

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
