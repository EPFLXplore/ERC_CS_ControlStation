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
from sensor_msgs.msg import JointState, Joy
from nav_msgs.msg import Odometry
from diagnostic_msgs.msg import DiagnosticStatus

from std_srvs.srv import SetBool


from .model import *
from .launcher import *

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

        self.launcher = Launcher()
        self.model = Model(self)

        # variables used for the timeout system
        self.received = False
        self.waiting = False
        self.tries = 0

        # state of the rover (FSM)
        self.ROVER_STATE = Task.IDLE
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

        # Rover(SC) --> CS
        self.SC_fsm_state_pub  = self.node.create_publisher(Int8,                'ROVER/SC_fsm_state'            , 1)
        # self.SC_cmd_pub        = self.node.create_publisher(String,            'ROVER/SC_cmd'                  , 1)
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

        # messages from CS (NAV)
        # self.node.create_subscription(PoseStamped, 'CS/NAV_goal',    self.model.Nav.setGoal, 10)
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
        #self.HD_gamepad_pub          = self.node.create_publisher(Float32MultiArray, 'ROVER/HD_gamepad' , 1)
        
        # Rover --> NAV
        self.Nav_Goal_pub     = self.node.create_publisher(PoseStamped, 'ROVER/NAV_goal'    , 1)
        self.Nav_Status       = self.node.create_publisher(String,      'ROVER/NAV_status'  , 1)
        #self.Nav_gamepad_pub  = self.node.create_publisher(Joy,         'ROVER/NAV_gamepad' , 1)


        # Rover --> SC
        self.SC_pub = self.node.create_publisher(Int8,        'ROVER/SC_cmd'           , 1)

        # ===== SUBSCRIBERS =====

        # SC --> Rover
        self.node.create_subscription(Int8,              'SC/fsm_state_to_cs'          , self.model.SC.science_fsm_callback   , 10)  # self.SC_infos_pub.publish)
        # self.node.create_subscription(String,          'sc_state'                    , self.model.SC.set_state_info  , 10)
        # self.node.create_subscription(String,          'sc_info'                     , self.model.SC.set_text_info   , 10)  # self.SC_infos_pub.publish)
        # self.node.create_subscription(Int16,           'sc_measurements_humidity'    , self.SC_humidities_pub.publish, 10)
        # self.node.create_subscription(Int16MultiArray, 'sc_params'                   , self.model.SC.params          , 10)
        # self.node.create_subscription(Int8,            'TaskProgress'                , self.model.setProgress        , 10)
        # NAV --> Rover
        self.node.create_subscription(Odometry,        '/lio_sam/current_pose'          , self.NAV_odometry_pub.publish , 10) # CS DIRECTLY SUBSCRIBED
        # HD --> Rover
        self.node.create_subscription(JointState,      'HD/motor_control/joint_telemetry', self.HD_telemetry_pub.publish , 10)


        # ==========================================================GAMEPAD FROM CS
        #self.node.create_subscription(Float32MultiArray,  'CS/HD_gamepad'    , self.HD_gamepad_pub.publish, 10)
        #self.node.create_subscription(Joy,               'CS/NAV_gamepad', self.model.Nav.gamepad, 10)


        # ======Services server=====
        self.onlineConfirm = self.node.create_service(SetBool, "ROVER_ONLINE", self.onlineConfirm)

    ''' Callback used for the rover to confirm it is online to the CS'''
    def onlineConfirm(self,request,response):
        self.node.get_logger().info('ROVER: Online confirmation received from CS')
        self.csConnected = request.data
        #res = SetBool.Response()
        response.success = True
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
        #print('task_instr call : ' + str(array.data))
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
                    self.node.get_logger().info("LAUNCHING MANUAL")
                    self.launcher.start_manual()
                    self.ROVER_STATE = Task.MANUAL
                else:
                    pass
                    # self.node.get_logger().info("Can't launch Manual if another task is still running!")
                    #self.log_task_already_launched("Manual")
            elif (self.ROVER_STATE == Task.MANUAL):
                # ABORT
                if instr == Instruction.ABORT.value:
                    self.node.get_logger().info("ABORTING MANUAL")
                    self.Maintenance_pub.publish(Int8(data = -1))
                    self.Nav_Status.publish(String(data = "stop"))
                    self.ROVER_STATE = Task.IDLE

        #--------------------------NAVIGATION-----------------------------
        if task == Task.NAVIGATION.value:
            # LAUNCH 
            if instr == Instruction.LAUNCH.value:
                if (self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING NAVIGATION ...")
                    self.ROVER_STATE = Task.NAVIGATION
                else:
                    self.node.get_logger().info("SEND GOAL :" + str(self.model.Nav.getGoal().pose.position.x) + " " + str(self.model.Nav.getGoal().pose.position.y) + " " + str(self.model.Nav.getGoal().pose.position.z))
                    goal = self.model.Nav.getGoal()
                    self.Nav_Goal_pub.publish(PoseStamped(header=goal.header, pose=goal.pose))
                    #self.log_task_already_launched("Navigation")

            elif (self.ROVER_STATE == Task.NAVIGATION):
                # ABORT
                if instr == Instruction.ABORT.value:
                    self.node.get_logger().info("ABORTING NAVIGATION")
                    self.model.Nav.cancelGoal()
                    self.Nav_Status.publish(String(data="stop"))
                    self.ROVER_STATE = Task.IDLE
                # WAIT
                if instr == Instruction.WAIT.value:
                    self.node.get_logger().info("PAUSING NAVIGATION")
                    self.Nav_Status.publish(String(data="pause"))
                    self.ROVER_STATE == Task.WAITING

            elif (self.ROVER_STATE == Task.WAITING):
                # RESUME
                if(instr == Instruction.RESUME.value):
                    self.node.get_logger().info("RESUMING NAVIGATION")
                    self.Nav_Status.publish(String(data="resume"))
                    self.ROVER_STATE = Task.NAVIGATION
                
        #-------------------------------MAINTENANCE----------------------------------
        if task == Task.MAINTENANCE.value:
            # LAUNCH---------------------------
            if (instr == Instruction.LAUNCH.value):
                if(self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING MAINTENANCE")
                    self.ROVER_STATE = Task.MAINTENANCE
                    self.HD_SemiAuto_Id_pub.publish(Int8(data=self.model.HD.getId()))
                else:
                    pass
                    #self.log_task_already_launched("Maintenance")
                    #self.node.get_logger().info("Can't launch Maintenance if another task is still running!")


            elif(self.ROVER_STATE == Task.MAINTENANCE):
                # ABORT
                if (instr == Instruction.ABORT.value):
                    self.node.get_logger().info("ABORTING MAINTENANCE")
                    self.HD_SemiAuto_Id_pub.publish(Int8(data=-1))
                    self.ROVER_STATE = Task.IDLE
                # WAIT--------------------------------- TODO: see how to not be able to wait 2 times
                elif (instr == Instruction.WAIT.value):
                    self.node.get_logger().info("PAUSING MAINTENANCE")
                    self.Maintenance_pub.publish(Int8(data=instr))
                    self.ROVER_STATE = Task.WAITING

            elif(self.ROVER_STATE == Task.WAITING):
                # RESUME
                if(instr == Instruction.RESUME.value):
                    self.node.get_logger().info("RESUMING MAINTENANCE")
                    self.Maintenance_pub.publish(Int8(data=instr))
                    self.ROVER_STATE = Task.MAINTENANCE

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

        # ----------------------SCIENCE------------------------------------------
        if (task == Task.SCIENCE.value):

            # LAUNCH
            if (instr == Instruction.LAUNCH.value):
                if(self.ROVER_STATE == Task.IDLE):
                    self.node.get_logger().info("LAUNCHING SCIENCE")
                    self.launcher.start_science()
                    self.ROVER_STATE = Task.SCIENCE
                else:
                    self.node.get_logger().info("Can't launch Science if another task is still running!")
                    self.log_task_already_launched("Science")

            #OTHER SCIENCE INSTR TODO: ADD abort in science
            elif(self.ROVER_STATE == Task.SCIENCE):
                # ABORT
                if (instr == Instruction.ABORT.value):
                    self.node.get_logger().info("ABORTING SCIENCE")
                    self.SC_pub.publish(Int8(data=instr))
                    self.ROVER_STATE = Task.IDLE

                # WAIT
                if(instr == Instruction.WAIT.value):
                    self.node.get_logger().info("PAUSING SCIENCE")
                    self.SC_pub.publish(Int8(data = instr))
                    self.ROVER_STATE = Task.WAITING

            elif(self.ROVER_STATE == Task.WAITING):
                # RESUME
                if(instr == Instruction.RESUME.value):
                    self.node.get_logger().info("RESUMING SCIENCE")
                    self.SC_pub.publish(Int8(data=instr))
                    self.ROVER_STATE = Task.SCIENCE

            else:
                msg = "Unhandled situation, task = " + str(task) + ", instr = " + str(instr) + ", rover state = " + str(self.ROVER_STATE.value)
                self.node.get_logger().info(msg)
                self.notify_cs(DiagnosticStatus.WARN, msg)


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

    def notify_cs(self, diagnostic_level, msg):
        status = DiagnosticStatus()
        status.name = "ROVER"
        status.level = diagnostic_level
        status.message = msg
        self.diagnostic.publish(status)


def main():
    rover = Rover()
    rover.run()
