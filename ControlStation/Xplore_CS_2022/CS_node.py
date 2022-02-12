#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           ...
#
# @brief: This file contains the Application class of the backend. It will
#         create the ROS node for the Control Station and take care of creating
#         and subscribing to the needed ROS topic. It will also define and run 
#         the listening thread that will receive the data from the rover and store
#         it into the database.
#
#================================================================================
#!/usr/bin/env python
from threading import Thread
import rospy
import Controller

from models import *

from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID




#================================================================================
'''
    This class creates a listening thread, initializes all ROS publishers and subscribes
    to all the needed topics
'''
class Application(Thread):

    def __init__(self, threadID, name):

        Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        
        self.controller = Controller(self)
        rospy.init_node('CONTROL_STATION', anonymous=True)

        '''
        Define the ROS topics: subscriptions and publishers
        '''
        # --------------------- PUBLISHERS ---------------------

            ###### CS_node --> Rover node ######

        # publish array: [task, instruction] 
        Task_pub = rospy.Publisher('Task', Int8MultiArray, queue_size=1)


            ###### CS_node --> Handling Device node ######

        # publish HD_mode => Autonomous (0), Semi-Autonomous (1), Inverse Manual (2), Direct Manual (3)
        HD_mode_pub = rospy.Publisher('HD_mode', Int8, queue_size=1)

        # publish id of element we want to manipulate in Semi-Autonomous mode
        HD_SemiAuto_Id_pub = rospy.Publisher('HD_SemiAuto_Id', Int8, queue_size=1)

        # publish angles for Direct Manual or Inverse Manual
        HD_Angles_pub = rospy.Publisher('HD_Angles', Int8MultiArray, queue_size=1)

        # publish speed depending on pressure applied on buttons of joystick
        HD_ManualVelocity_pub = rospy.Publisher('HD_ManualVelocity', Float32, queue_size=1)

        # publish movement along x, y or z axis in Inverse Manual
        HD_InvManual_Coord_pub = rospy.Publisher('HD_InvManual_Coord', Int8MultiArray, queue_size=1)


            ###### CS_node --> Navigation node ######

        # publish goal the rover must reach
        Nav_Goal_pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=1)

        # publish request to cancel a specific goal
        Nav_CancelGoal_pub = rospy.Publisher('/move_base/cancel', GoalID, queue_size=1)

        # publish info from the joystick in the form of a Twist object
        Nav_Joystick_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        # publish debugging commands to individual wheels
        Nav_DebugWheels_pub = rospy.Publisher('/debug/wheel_cmds', Int16MultiArray, queue_size=1)


        # --------------------- SUBSCRIPTIONS ---------------------

            ###### Rover node --> CS_node ######

        # receive confirmation that rover received instruction
        rospy.Subscriber('RoverConfirm', Bool, rover_confirmation)

        # receive info if an exception was thrown
        rospy.Subscriber('Exception', String, exception)


            ###### [Task node] --> CS_node ######

        # receive info on task progress: failure(0), success(1), checkpoint(2)
        rospy.Subscriber('TaskProgress', Int8, task_progress)


            ###### Science node --> CS_node  ######

        # receive info on sample analysis progress: failure(0), success(1)
        rospy.Subscriber('ScienceProgress', Int8, science_progress)
        


    def run(self):
        print("Listening")
        rospy.spin() 

#================================================================================
'''
    Here you should create all the ROS callback functions that will receive the data
    and store it into the data base using django commands
'''

def rover_confirmation(val):
    confirm = RoverConfirmation.objects.create(received=True)
    confirm.save()

def task_progress(val):
    if (0 <= val and val < 3):
        state = TaskProgress.objects.create(state = val)
        state.save()
    else:
        exception("unacceptable number received: " + val)
        #TODO how to handle this exception?

def science_progress(val):
    if (val == 0 or val == 1):
        state = ScienceProgress.objects.create(state = val)
    else:
        exception("unacceptable number received: " + val)

def exception(val):
    exception = Exception.objects.create(string = val)
    exception.save() 



#================================================================================
#MAIN
if __name__ == '__main__':

  
  
  # Create The reception thread
  listener  = Application(1, "Reception loop")
  # Start the reception thread
  listener.start()


  
