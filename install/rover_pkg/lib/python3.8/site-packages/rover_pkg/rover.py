# ===============Past code being updated =================
## The code below is a copy paste of the previous code,
## All the calls to rospy functions have been updated (adding publishers and subscribers, initializing the node, and calls to the loginfo function)

import time
import rclpy
from rclpy.logging import LoggingSeverity
import sys

from std_msgs.msg       import Int8, Int16, Int32, Bool, String, Int8MultiArray,  Int16MultiArray, Float32MultiArray, UInt8MultiArray

from geometry_msgs.msg  import Twist, PoseStamped
from actionlib_msgs.msg import GoalID
from sensor_msgs.msg import JointState, Joy
from nav_msgs.msg import Odometry
from diagnostic_msgs.msg import DiagnosticStatus

from std_srvs.srv import SetBool


from .model import *
from .launcher import *



'''
from 
    This class initializes all ROS publishers and subscribes to all the needed topics
'''


class Rover():

    def __init__(self):

        rclpy.init(args=sys.argv)
        self.node = rclpy.create_node('ROVER')

        self.launcher = Launcher()
        self.model = Model(self)

        # variables used for the timeout system
        self.received = False
        self.waiting = False
        self.tries = 0

        # state of the rover (FSM)
        self.ROVER_STATE: Task = Task.IDLE
        self.csConnected = False

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
        self.RoverConfirm_pub  = self.node.create_publisher(String,            'ROVER/RoverConfirm'            , 1)
        self.Exception_pub     = self.node.create_publisher(String,            'ROVER/Exception'               , 1)
        self.TaskProgress_pub  = self.node.create_publisher(Int8,              'ROVER/TaskProgress'            , 1)
        self.state_pub         = self.node.create_publisher(String,            'ROVER/State'                   , 1)

        # Rover(SC) --> CS
        #self.SC_fsm_state_pub  = self.node.create_publisher(Int8,                'ROVER/SC_fsm'            , 1)
        self.SC_cmd_pub        = self.node.create_publisher(Int8,                 'ROVER/SC_fsm'                  , 1)
        # self.SC_infos_pub      = self.node.create_publisher(String,            'ROVER/SC_info'                 , 1)
        # self.SC_humidities_pub = self.node.create_publisher(Int16,             'ROVER/SC_measurements_humidity', 1)
        # self.SC_params_pub     = self.node.create_publisher(Int16MultiArray,   'ROVER/SC_params'               , 1)

        # Rover(HD) --> CS
        self.HD_telemetry_pub  = self.node.create_publisher(JointState,        'ROVER/HD_telemetry'            , 1)
        self.NAV_odometry_pub  = self.node.create_publisher(Odometry,          'ROVER/NAV_odometry'            , 1)
        self.HD_element_pub    = self.node.create_publisher(Float32MultiArray, 'ROVER/HD_detected_element'     , 3)
        self.diagnostic        = self.node.create_publisher(DiagnosticStatus,  'ROVER/CS_log'                  ,10)

        # ===== SUBSCRIBERS =====

        # messages from CS
        self.node.create_subscription(Int8MultiArray, 'CS/Task'          , self.task_instr             , 10)
        self.node.create_subscription(Bool,           'CS/Confirm'       , self.cs_confirm             , 10)

        # messages form CS (HD)
        self.node.create_subscription(Int8,           'CS/HD_mode'       , self.model.HD.setHDMode     , 10)
        self.node.create_subscription(Int8,           'CS/HD_SemiAuto_Id', self.model.HD.set_semiAutoID, 10)
        self.node.create_subscription(Int8,           'CS/HD_element_id' , self.model.HD.send_element_id_hd     , 10)
        self.node.create_subscription(Bool,           'CS/HD_toggle_camera', self.model.HD.send_toggle_info     , 10)
        self.node.create_subscription(Bool,           'CS/HD_cancel_goal',   self.model.HD.cancel_goal,           10)

        # messages from CS (NAV)
        # self.node.create_subscription(PoseStamped, 'CS/NAV_goal',    self.model.Nav.sendGoal, 10)
        #self.node.create_subscription(Bool, 'CS/NAV_cancel',    self.model.Nav.cancelGoal, 10)
        self.node.create_subscription(String, 'CS/NAV_cancel',    self.model.Nav.cancelGoal, 10)
        self.node.create_subscription(PoseStamped, 'CS/NAV_goal',    self.model.Nav.sendGoal, 10)
        
        #self.node.create_subscription(Joy,    'Gamepad',   self.handle_gamepad,          1)
        #TODO: add cancel goal and other messages from CS to NAV

        # ==========================================================
        #           MESSAGES BETWEEN THE ROVER AND ITS SUBSYSTEMS 
        # ==========================================================

        # ===== PUBLISHERS =====
        
        #ROVER --> All
        # Rover --> HD
        self.Maintenance_pub         = self.node.create_publisher(Int8, 'ROVER/Maintenance'      , 1)
        self.HD_mode_pub             = self.node.create_publisher(Int8, 'ROVER/HD_mode'          , 1)
        self.HD_SemiAuto_Id_pub      = self.node.create_publisher(Int8, 'ROVER/HD_SemiAuto_Id'   , 1)
        self.send_HD_element_id_pub  = self.node.create_publisher(Int8, 'ROVER/HD_element_id'    , 1)
        self.send_toggle_info_pub    = self.node.create_publisher(Bool, 'ROVER/HD_toggle_camera' , 1)
        
        # Rover --> NAV
        self.Nav_Goal_pub     = self.node.create_publisher(PoseStamped, 'ROVER/NAV_goal'    , 1)
        self.Nav_Status_pub   = self.node.create_publisher(String,      'ROVER/NAV_status'  , 1)


        # Rover --> SC
        self.SC_pub = self.node.create_publisher(Int8,        'ROVER/SC_fsm'           , 1)

        # ===== SUBSCRIBERS =====

        # SC --> Rover
        self.node.create_subscription(Int8,              'SC/fsm_state_to_cs'          , self.model.SC.science_fsm_callback   , 10)  # self.SC_infos_pub.publish)

        # NAV --> Rover
        #self.node.create_subscription(PoseStamped,        '/lio_sam/current_pose'          , self.NAV_odometry_pub.publish , 10) # CS DIRECTLY SUBSCRIBED

        # HD --> Rover
        self.node.create_subscription(JointState,      'HD/motor_control/joint_telemetry', self.HD_telemetry_pub.publish , 10)

        # ========================================================== GAMEPAD FROM CS
        #self.node.create_subscription(Float32MultiArray,  'CS/HD_gamepad'    , self.HD_gamepad_pub.publish, 10)
        #self.node.create_subscription(Joy,               'CS/NAV_gamepad', self.model.Nav.gamepad, 10)

        # ======Services server=====
        self.onlineConfirm = self.node.create_service(SetBool, "ROVER_ONLINE", self.onlineConfirm)

    ''' Callback used for the rover to confirm it is online to the CS'''
    def onlineConfirm(self,request,response):
        self.node.get_logger().info('ROVER: Online confirmation received from CS')
        self.csConnected = request.data
        response.success = True
        self.state_pub.publish(String(data=str(Task.IDLE.name)))
        return response

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
        task = array.data[0]
        instr = array.data[1]

        self.node.get_logger().info("Rover: [task = %d, instr = %d] received" % (task, instr))
        self.RoverConfirm_pub.publish(String(data="Instructions received"))

        if not (1 <= task <= 4):
            self.Exception_pub.publish(String(data="Task number denied (allowed only 1-4), received: %d"% task))
            pass
        if not (1 <= instr <= 5):
            self.Exception_pub.publish(String(data="Instr number denied (allowed only 1-5), received: %d"% instr))
            pass

        #-------------Processing the task received-------------

        if (task == Task.MANUAL.value):
            if (instr == Instruction.LAUNCH.value):
                if (self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING MANUAL")
                    self.launcher.start_manual()
                    self.ROVER_STATE = Task.MANUAL
            elif instr == Instruction.ABORT.value:
                self.node.get_logger().info("ABORTING MANUAL")
                self.Maintenance_pub.publish(Int8(data = -1))
                #self.Nav_Status_pub.publish(String(data = "stop"))
                self.ROVER_STATE = Task.IDLE

        #--------------------------NAVIGATION-----------------------------
        if task == Task.NAVIGATION.value:
            # LAUNCH 
            if instr == Instruction.LAUNCH.value:
                if (self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING NAVIGATION ...")
                    self.launcher.start_auto_nav()
                    self.ROVER_STATE = Task.NAVIGATION
            if instr == Instruction.ABORT.value:
                self.node.get_logger().info("ABORTING NAVIGATION")
                #self.model.Nav.cancelGoal()
                self.Nav_Status_pub.publish(String(data="abort"))
                self.ROVER_STATE = Task.IDLE
            # CANCEL
            if instr == Instruction.CANCEL.value:
                self.node.get_logger().info("CANCEL NAVIGATION GOAL")
                #self.model.Nav.cancelGoal()
                self.Nav_Status_pub.publish(String(data="cancel"))
                
        #-------------------------------MAINTENANCE----------------------------------
        if task == Task.MAINTENANCE.value:
            # LAUNCH---------------------------
            if (instr == Instruction.LAUNCH.value):
                if(self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING MAINTENANCE")
                    self.HD_SemiAuto_Id_pub.publish(Int8(data=self.model.HD.getId()))
                    self.ROVER_STATE = Task.MAINTENANCE

            elif (instr == Instruction.ABORT.value):
                self.node.get_logger().info("ABORTING MAINTENANCE")
                self.HD_SemiAuto_Id_pub.publish(Int8(data=-1))
                self.ROVER_STATE = Task.IDLE

            elif (instr == Instruction.CANCEL.value):
                self.node.get_logger().info("CANCEL MAINTENANCE")
                self.Maintenance_pub.publish(Int8(data=instr))

        # ----------------------SCIENCE------------------------------------------
        if (task == Task.SCIENCE.value):
            # LAUNCH
            if (instr == Instruction.LAUNCH.value):
                self.node.get_logger().info("LAUNCHING SCIENCE")
                self.SC_pub.publish(Int8(data=instr))
                self.ROVER_STATE = Task.SCIENCE

            elif (instr == Instruction.ABORT.value):
                self.node.get_logger().info("ABORTING SCIENCE")
                self.SC_pub.publish(Int8(data=instr))
                self.ROVER_STATE = Task.IDLE

        self.state_pub.publish(String(data=str(self.ROVER_STATE.name)))


    # run ros
    def run(self):
        print("Rover node started !")
        rclpy.spin(self.node)
        rclpy.shutdown()

        # ===== TIMEOUT MECHANISM =====

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
        # status = DiagnosticStatus()
        # status.level = DiagnosticStatus.ERROR
        # status.msg = "Can't launch %s if another task is still running!" % task
        # status.name = "Task already running"
        # self.diagnostic.publish(status)
        return

def main():
    rover = Rover()
    rover.run()
