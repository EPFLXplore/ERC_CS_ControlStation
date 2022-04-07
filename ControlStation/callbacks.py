#
# 02/2021
#
# @author:  Roman Danylovych
#           roman.danylovych@epfl.ch
#
# @brief: This file contains all the callback functions used by the CS
#
#         The callback functions are called when the CS receives an info
#         on a topic it is subcribed to
#
#================================================================================

from threading import Thread
import rospy


from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID

from nav_msgs.msg import Odometry

from Xplore_CS_2022.models import *

from Model import *



def test_joystick(twist):
    tl = twist.linear
    ta = twist.angular
    rospy.loginfo("Linear %d %d %d", tl.x, tl.y, tl.z)
    rospy.loginfo("Angular %d %d %d", ta.x, ta.y, ta.z)


#The following callback functions update the db objects' values

#Rover sends a confirmation that it received an instruction
def rover_confirmation(boolean):
     rospy.loginfo("Rover Confirmation: %s", boolean.data)
     RoverConfirmation.objects.update_or_create(name="RoverConfirm", defaults={'received': boolean.data})


###############################
#        TASK PROGRESS        #
###############################

#Notified on whether task is a:
#   - failure (0)
#   - success (1) 
#   - checkpoint (2)
def task_progress(num):
    val = num.data
    if (0 <= val and val < 3):
        TaskProgress.objects.update_or_create(name="TaskProgress", defaults={'state': val})
    else:
        str = "Impossible progress state: %s" % (val)
        exception_clbk(String(str))
        

###############################
#           SCIENCE           # 
###############################

# info on what is going on in the Science Bay:
#    ex: LED turned on, Picture taken, ...
def sc_text_info(info):
    str = info.data
    Science.objects.update_or_create(name="Science", defaults = {'sc_text': str})
    rospy.loginfo("Science: text_info: " + str)


# receive an Int16MultiArray: [tube number, humidity inside tube]
def sc_humidity(hums):
    arr = hums.data
    tNum = arr[0]
    val = arr[1]

    #db_science = Science.objects.update_or_create(name="Science", defaults={})[0]
    db_science = Science.objects.get_or_create(name="Science")[0]

    if(tNum == 0): #tube 1
        rospy.loginfo("Science: humidity tube 1: " + str(val))
        db_science.t1_hum = val
        db_science.save()
    elif(tNum == 1): #tube 2
        rospy.loginfo("Science: humidity tube 2: " + str(val))
        db_science.t2_hum = val
        db_science.save()
    else: #tube 3
        rospy.loginfo("Science: humidity tube 3: " + str(val))
        db_science.t3_hum = val
        db_science.save()

# receive the total mass of the 3 tubes
def sc_mass(mass):
    val = mass.data
    rospy.loginfo("SC mass: %s", val)
    Science.objects.update_or_create(name="Science", defaults={'mass': val})


###############################
#       HANDLING DEVICE       #
###############################

def hd_data(matrix):
    el1 = matrix[0]
    el2 = matrix[1]
    el3 = matrix[2]
    el4 = matrix[3]
    el5 = matrix[4]
    el6 = matrix[5]
    el7 = matrix[6]

    

###############################
#          NAVIGATION         #
###############################

# TODO update the database everytime dist(pos1, pos2) > eps
# TODO IL FAUT PASSER A POSTGRESQL POUR LES ARRAYFIELD STP (ou utiliser des Blob)
def nav_data(odometry):
    data = odometry.data
    pos = data.pose.pose.position
    posArr = [pos.x, pos.y, pos.z]

    db_navigation = Navigation.objects.get_or_create(name="Navigation", defaults = 
        {'posX': 0.0, 'posY': 0.0, 'posZ': 0.0,
         'linVelX': 0.0, 'linVelY': 0.0, 'linVelZ': 0.0,
         'angVelX': 0.0, 'angVelY': 0.0, 'angVelZ': 0.0})


    # update position coordinates
    db_navigation.posX = posArr[0]
    db_navigation.posY = posArr[1]
    db_navigation.posZ = posArr[2]

    twistLin = data.twist.twist.linear
    linArr = [twistLin.x, twistLin.y, twistLin.z]

    # update linear velocity values
    db_navigation.linVelX = linArr[0]
    db_navigation.linVelY = linArr[1]
    db_navigation.linVelZ = linArr[2]

    twistAng = data.twist.twist.angular
    angArr = [twistAng.x, twistAng.y, twistAng.z]

    # update angular velocity values
    db_navigation.angVelX = angArr[0]
    db_navigation.angVelY = angArr[1]
    db_navigation.angVelZ = angArr[2]

    db_navigation.save()


###############################
#          EXCEPTION          #
###############################

#TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
#General topic on which subsystems can publish if an unexpected exception was thrown
def exception_clbk(str): 
    val = str.data
    rospy.loginfo("Exception: " + val)
    Exception.objects.update_or_create(name="Exception", defaults={'string': val})