# ===============Past code being updated =================
## The code below is a copy paste of the previous code,
## All the calls to rospy functions have been updated (adding publishers and subscribers, initializing the node, and calls to the loginfo function)

import time
import rclpy
from rclpy.logging import LoggingSeverity
import sys

# from abc import ABC, abstractmethod #Abstract Base Class

from std_msgs.msg       import Int8, Int16, Int32, Bool, String, Int8MultiArray,  Int16MultiArray, Float32MultiArray, UInt8MultiArray

#from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg  import Twist, PoseStamped
from actionlib_msgs.msg import GoalID
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from diagnostic_msgs import DiagnosticStatus

from .model import *

# from .Globals   import *
# from vision_no_ros.msg import *


'''
from 
    This class initializes all ROS publishers and subscribes to all the needed topics
'''


class Rover():

    def __init__(self):
        # rospy.init_node('ROVER', anonymous=True)
        rclpy.init(args=sys.argv)
        self.node = rclpy.create_node('ROVER')

        self.model = Model(self)

        # variables used for the timeout system
        self.received = False
        self.waiting = False
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

        self.RoverConfirm_pub  = self.node.create_publisher(String,            'ROVER_RoverConfirm'            , 1)
        self.Exception_pub     = self.node.create_publisher(String,            'ROVER_Exception'               , 1)
        self.TaskProgress_pub  = self.node.create_publisher(Int8,              'ROVER_TaskProgress'            , 1)
        # Rover(SC) --> CS
        self.SC_state_pub      = self.node.create_publisher(String,            'ROVER_SC_state'                , 1)
        self.SC_infos_pub      = self.node.create_publisher(String,            'ROVER_SC_info'                 , 1)
        self.SC_humidities_pub = self.node.create_publisher(Int16,             'ROVER_SC_measurements_humidity', 1)
        self.SC_params_pub     = self.node.create_publisher(Int16MultiArray,   'ROVER_SC_params'               , 1)
        # Rover(HD) --> CS
        self.HD_telemetry_pub  = self.node.create_publisher(JointState,        'ROVER_HD_telemetry'            , 1)
        self.HD_tof            = self.node.create_publisher(Int32,             'ROVER_HD_tof'                  , 1)
        self.NAV_odometry_pub  = self.node.create_publisher(Odometry,          'ROVER_NAV_odometry'            , 1)
        self.HD_element_pub    = self.node.create_publisher(Float32MultiArray, 'ROVER_HD_detected_element'     , 3)
        self.diagnostic        = self.node.create_publisher(DiagnosticStatus,  'CS_log'                        ,10)

        # ===== SUBSCRIBERS =====

        # messages from CS
        self.node.create_subscription(Int8MultiArray, 'Task'             , self.task_instr             , 10)
        self.node.create_subscription(Bool,           'CS_Confirm'       , self.cs_confirm             , 10)
        # messages form CS (HD)
        self.node.create_subscription(Int8,           'CS_HD_mode'       , self.model.HD.setHDMode     , 10)
        self.node.create_subscription(Int8,           'CS_HD_SemiAuto_Id', self.model.HD.set_semiAutoID, 10)
        # messages from CS (NAV)
        self.node.create_subscription(PoseStamped,    'CS_NAV_goal'      , self.model.Nav.setGoal      , 10)

        # ==========================================================
        #           MESSAGES BETWEEN ROVER AND SUBSYSTEMS
        # ==========================================================

        # ===== PUBLISHERS =====

        # Rover --> HD
        self.Maintenance_pub    = self.node.create_publisher(Int8,        'Maintenance'      , 1)
        self.HD_mode_pub        = self.node.create_publisher(Int8,        'HD_mode'          , 1)
        self.HD_SemiAuto_Id_pub = self.node.create_publisher(Int8,        'HD_SemiAuto_Id'   , 1)
        # Rover --> NAV
        self.Nav_pub            = self.node.create_publisher(Int8,        'Navigation'       , 1)
        self.Nav_Goal_pub       = self.node.create_publisher(PoseStamped, 'CS/NAV_goal'      , 1)
        self.Nav_CancelGoal_pub = self.node.create_publisher(GoalID,      '/move_base/cancel', 1)
        # Rover --> SC
        self.SC_pub             = self.node.create_publisher(Int8,        'sc_cmd'           , 1)

        # ===== SUBSCRIBERS =====

        # SC --> Rover
        self.node.create_subscription(String,          'sc_state'                    , self.model.SC.set_state_info  , 10)
        self.node.create_subscription(String,          'sc_info'                     , self.model.SC.set_text_info   , 10)  # self.SC_infos_pub.publish)
        self.node.create_subscription(Int16,           'sc_measurements_humidity'    , self.SC_humidities_pub.publish, 10)
        self.node.create_subscription(Int16MultiArray, 'sc_params'                   , self.model.SC.params          , 10)
        self.node.create_subscription(Int8,            'TaskProgress'                , self.model.setProgress        , 10)
        # NAV --> Rover
        self.node.create_subscription(Odometry,        '/odometry/filtered'          , self.NAV_odometry_pub.publish , 10)
        # HD --> Rover
        self.node.create_subscription(JointState,      '/arm_control/joint_telemetry', self.HD_telemetry_pub.publish , 10)
        self.node.create_subscription(Int32,           '/avionics_ToF'               , self.HD_tof.publish           , 10)

    #        self.node.create_subscription(object_list,       '/detected_elements',           self.model.HD.pub_detected_elements)

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
        print('task_instr call !')
        task = array.data[0]
        instr = array.data[1]

        if not (1 <= task <= 4):
            self.Exception_pub.publish(String(data="Task number denied (allowed only 1-4), received: %d"% task))
            pass
        if not (1 <= instr <= 5):
            self.Exception_pub.publish(String(data="Instr number denied (allowed only 1-5), received: %d"% instr))
            pass

        self.node.get_logger().info("Rover: [task = %d, instr = %d] received" % (task, instr))

        self.RoverConfirm_pub.publish(String(data="Instructions received"))

        #-------------Processing the task received-------------

        # MANUAL TODO ADD ABORT
        if (task == Task.MANUAL.value):
            if (instr == Instruction.LAUNCH.value):
                if (self.ROVER_STATE == Task.IDLE):
                    self.ROVER_STATE = Task.MANUAL
                else:
                    # self.node.get_logger().info("Can't launch Manual if another task is still running!")
                    self.log_task_already_launched("Manual")
            elif (self.ROVER_STATE == Task.MANUAL):
                # ABORT
                if instr == Instruction.ABORT.value:
                    self.ROVER_STATE = Task.IDLE

        #--------------------------NAVIGATION-----------------------------
        if task == Task.NAVIGATION.value:
            # LAUNCH -------------------------
            if instr == Instruction.LAUNCH.value:
                if (self.ROVER_STATE == Task.IDLE):
                    self.ROVER_STATE = Task.NAVIGATION
                    self.node.get_logger().info("goal launched")
                    goal = self.model.Nav.getGoal()
                    self.Nav_Goal_pub.publish(PoseStamped(header=goal.header, pose=goal.pose))
                else:
                    self.log_task_already_launched("Navigation")
                    # self.node.get_logger().info("Can't launch Navigation if another task is still running!")

            elif (self.ROVER_STATE == Task.NAVIGATION):
                # ABORT
                if instr == Instruction.ABORT.value:
                    self.model.Nav.cancelGoal()
                    self.ROVER_STATE = Task.IDLE
                # WAIT/RESUME
                else:
                    self.Nav_pub.publish(Int8(data=instr))

        #-------------------------------MAINTENANCE----------------------------------
        if task == Task.MAINTENANCE.value:
            # LAUNCH---------------------------
            if (instr == Instruction.LAUNCH.value):
                if(self.ROVER_STATE == Task.IDLE):
                    self.ROVER_STATE = Task.MAINTENANCE
                    self.HD_SemiAuto_Id_pub.publish(Int8(data=self.model.HD.getId()))
                else:
                    self.log_task_already_launched("Maintenance")
                    #self.node.get_logger().info("Can't launch Maintenance if another task is still running!")


           elif(self.ROVER_STATE == Task.MAINTENANCE):
                # ABORT--------------------------------------
                if (instr == Instruction.ABORT.value):
                    self.HD_SemiAuto_Id_pub.publish(Int8(data=-1))
                    self.ROVER_STATE = Task.IDLE
                # WAIT/RESUME--------------------------------- TODO: see how to not be able to wait 2 times
                else:
                    self.Maintenance_pub.publish(Int8(data=instr))

        # -------------------------DRONE-------------------------------------------------
        if (task == Task.DRONE.value):
            # LAUNCH
            if (instr == Instruction.LATCH.value):
                if (self.ROVER_STATE == Task.IDLE):
                    self.ROVER_STATE = Task.DRONE
                else:
                    # self.node.get_logger().info("Can't launch Manual if another task is still running!")
                    self.log_task_already_launched("Drone")

            # OTHER Instructions
            elif (self.ROVER_STATE == Task.DRONE):
                if (instr == Instruction.ABORT.value):
                    self.ROVER_STATE = Task.IDLE
                if (instr == Instruction.OKDRONE.value):
                    self.ROVER_STATE = Task.IDLE
                else:
                    self.node.get_logger().info("Not allowed")

        # SCIENCE
        if (task == Task.SCIENCE.value):
            #LAUNCH
            if (instr == Instruction.LAUNCH.value):
                if(self.ROVER_STATE == Task.IDLE):
                    self.ROVER_STATE = Task.SCIENCE
                else:
                    self.node.get_logger().info("Can't launch Science if another task is still running!")
                    self.log_task_already_launched("Science")

            #OTHER SCIENCE INSTR TODO: ADD abort in science
            elif(self.ROVER_STATE == Task.SCIENCE):
                #ABORT
                if (instr == Instruction.ABORT.value):
                    self.ROVER_STATE = Task.IDLE
                # REQUEST TO RESEND PARAMETERS
                if (instr == ScienceTask.PARAMS.value):
                    self.wait(self.SC_params_pub, Int16MultiArray(data=self.model.SC.getParams()))
                # REQUEST TO RESEND INFO
                elif (instr == ScienceTask.INFO.value):
                    self.wait(self.SC_infos_pub, String(data=self.model.SC.get_text_info()))
                # REQUEST TO RESEND STATE
                elif (instr == ScienceTask.STATE.value):
                    self.wait(self.SC_state_pub, String(data=self.model.SC.get_state_info()))
                # COMMANDS SENT TO SC
                else:
                    self.SC_pub.publish(Int8(data=instr))

    # run ros
    def run(self):
        print("Listening")
        rclpy.spin(self.node)

        # ===== TIMEOUT MECANISM =====

    def cs_confirm(self, bool):
        if (self.waiting):
            self.node.get_logger().info("CS Confirmation Received")

            self.received = True

    def wait(self, pub, val):
        print("wait")
        self.waiting = True

        pub.publish(val)
        start = time.time()
        while (not self.received and ((time.time() - start) < 1)): continue

        if (not self.received and self.tries < 3):
            self.tries += 1
            self.wait(pub, val)

        if (not self.received):
            self.node.get_logger().info("Answer not received: TIMEOUT")


        self.waiting = False
        self.received = False

    def log_task_already_launched(self, task):
        status = DiagnosticStatus()
        status.level = DiagnosticStatus.ERROR
        status.msg = "Can't launch %s if another task is still running!" % task
        status.name = "Task already running"
        self.diagnostic.publish(status)


def main():
    rover = Rover()
    rover.run()
    print("running")
