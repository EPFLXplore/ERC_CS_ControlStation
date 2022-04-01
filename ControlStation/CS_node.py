
# import django
# django.setup()

import os
from pickletools import uint8
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

from Xplore_CS_2022.models import *

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



import rospy
import sys
#from Controller import *

from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray, Int16
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID
from sensor_msgs.msg import Image 
from nav_msgs.msg import Odometry

from threading import Thread

from callbacks import *


#================================================================================

'''
Define the ROS topics: subscriptions and publishers
        '''
class CS:

        def __init__(self):

                rospy.init_node("CONTROL_STATION", anonymous=True)

                self.navID = [0]

                #Thread.__init__(self, target=rover_confirmation)

                # --------------------------------------------- PUBLISHERS ---------------------------------------------

                        ###### CS_node --> Rover node ######

                # publish array: [task, instruction] 
                self.Task_pub = rospy.Publisher('Task', Int8MultiArray, queue_size=1)


                        ###### CS_node --> Handling Device node ######

                # publish HD_mode => Autonomous (0), Semi-Autonomous (1), Inverse Manual (2), Direct Manual (3)
                self.HD_mode_pub = rospy.Publisher('HD_mode', Int8, queue_size=1)

                # publish id of element we want to manipulate in Semi-Autonomous mode
                self.HD_SemiAuto_Id_pub = rospy.Publisher('HD_SemiAuto_Id', Int8, queue_size=1)

                # publish angles for Direct Manual or Inverse Manual
                self.HD_Angles_pub = rospy.Publisher('HD_Angles', Int8MultiArray, queue_size=1)

                # publish speed depending on pressure applied on buttons of joystick
                self.HD_ManualVelocity_pub = rospy.Publisher('HD_ManualVelocity', Float32, queue_size=1)

                # publish movement along x, y or z axis in Inverse Manual
                self.HD_InvManual_Coord_pub = rospy.Publisher('HD_InvManual_Coord', Int8MultiArray, queue_size=1)


                        ###### CS_node --> Navigation node ######

                # publish goal the rover must reach
                self.Nav_Goal_pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=1)

                # publish request to cancel a specific goal
                self.Nav_CancelGoal_pub = rospy.Publisher('/move_base/cancel', GoalID, queue_size=1)

                # publish info from the joystick in the form of a Twist object
                self.Nav_Joystick_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

                # publish debugging commands to individual wheels
                self.Nav_DebugWheels_pub = rospy.Publisher('/debug/wheel_cmds', Int16MultiArray, queue_size=1)


                # --------------------------------------------- SUBSCRIPTIONS ---------------------------------------------

                        ###### Rover node --> CS_node ######

                # receive confirmation that rover received instruction
                rospy.Subscriber('RoverConfirm', Bool, rover_confirmation)
                        
                # receive info if an exception was thrown
                rospy.Subscriber('Exception', String, exception_clbk)


                        ###### [Task node] --> CS_node ######

                # receive info on task progress: failure(0), success(1), checkpoint(2)
                rospy.Subscriber('TaskProgress', Int8, task_progress)


                        ###### Science node --> CS_node  ######

                # receive info on sample analysis progress: failure(0), success(1)
                #rospy.Subscriber('ScienceProgress', Int8, sc_progress)

                # receive info on the executing state (if the motor pos is correct, if the LED is on/off) (if it's a verbose ??) 
                rospy.Subscriber('science_current_info', String, sc_text_info)
                
                # receive the measurments 
                rospy.Subscriber('sc_measurments_humidity', Int16MultiArray, sc_humidity)

                rospy.Subscriber('sc_measurments_mass', Int16, sc_mass)


                        ###### Handling Device --> CS_node ######
                
                ''' 
                rospy.Subscriber('detection/state', UInt8, detection_state)

                rospy.Subscriber('detection/bounding_boxes', Image, ...)

                rospy.Subscriber('detection/RGB_intel', Image, ...)

                rospy.Subscriber('detection/RGB_webcam_1', Image, ...)

                rospy.Subscriber('detection/RGB_webcam_2', Image, ...)
                '''
                        ###### Navigation --> CS_node ######

                #TODO callback func
                rospy.Subscriber('/odometry/filtered', Odometry, nav_data)

                
        def run(self):
                print("Listening")
                rospy.spin()


CStation = CS()
#c = Controller(CStation)

#================================================================================
#MAIN
if __name__ == '__main__':
        #print("reset")
        #sys.stdout.flush()  
        #rospy.init_node("CONTROL_STATION", anonymous=True)
        CStation.run()
  
