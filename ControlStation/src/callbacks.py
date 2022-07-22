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
# -------------------------------------------------------------------------------

#================================================================================
# Libraries

import rospy

from std_msgs.msg           import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg     import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg      import Twist 
from actionlib_msgs.msg     import GoalID
from threading              import Thread
from nav_msgs.msg           import Odometry
from CS2022.models          import *
from src.model              import *

#================================================================================
# Callback functions definition

def test_joystick(twist):
    '''
        debug joysticl
    '''
    tl = twist.linear
    ta = twist.angular
    rospy.loginfo("Linear %d %d %d", tl.x, tl.y, tl.z)
    rospy.loginfo("Angular %d %d %d", ta.x, ta.y, ta.z)



def rover_confirmation(boolean):
    '''
        receives rover confirmation
    '''
    rospy.loginfo("Rover Confirmation: %s\n", boolean.data)



def task_progress(num):
    '''
        Notified on whether task is a:
        failure (0)
        success (1) 
        checkpoint (2)
    '''
    val = num.data
    if (0 <= val and val < 3):
        TaskProgress.objects.update_or_create(name="TaskProgress", defaults={'state': val})
    else:
        str = "Impossible progress state: %s" % (val)
        exception_clbk(String(str))
        

def sc_text_info(info):
    '''
        info on what is going on in the Science Bay:
        ex: LED turned on, Picture taken, ...
    '''
    str = info.data
    Science.objects.update_or_create(name="Science", defaults = {'sc_text': str})
    rospy.loginfo("Science: text_info: " + str)


def sc_humidity(hums):
    '''
        receive an Int16MultiArray: [tube number, humidity inside tube]
        tube number : arr[0]
        value       : arr[1]
    '''
    arr = hums.data
    rover.SC.setTubeHum(arr[0], arr[1])



def sc_mass(mass):
    '''
        receive the total mass of the 3 tubes
    '''
    rospy.loginfo("SC mass: %s", val)
    val = mass.data
    rover.SC.setSCMass(val)
    #Science.objects.update_or_create(name="Science", defaults={'mass': val})


# TODO
def hd_data(matrix):
    el1 = matrix[0]
    el2 = matrix[1]
    el3 = matrix[2]
    el4 = matrix[3]
    el5 = matrix[4]
    el6 = matrix[5]
    el7 = matrix[6]

    

# TODO update the database everytime dist(pos1, pos2) > eps
# TODO IL FAUT PASSER A POSTGRESQL POUR LES ARRAYFIELD STP (ou utiliser des Blob)
def nav_data(odometry):
    data = odometry.data

    # position (x,y,z)
    pos = data.pose.pose.position
    rover.Nav.setPos([pos.x, pos.y, pos.z])

    # linear velocity
    twistLin = data.twist.twist.linear
    rover.Nav.setLinVel([twistLin.x, twistLin.y, twistLin.z])

    # angular velocity
    twistAng = data.twist.twist.angular
    rover.Nav.setAngVel([twistAng.x, twistAng.y, twistAng.z])



#TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
#General topic on which subsystems can publish if an unexpected exception was thrown
def exception_clbk(str): 
    val = str.data
    rospy.loginfo("Exception: " + val)
    Exception.objects.update_or_create(name="Exception", defaults={'string': val})