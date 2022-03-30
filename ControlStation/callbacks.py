from threading import Thread
import rospy


from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID

from nav_msgs.msg import Odometry

from DB_objects import *

from Model import *

#from Controller import *
#The following callback functions update the db objects' values

#Rover sends a confirmation that it received an instruction
def rover_confirmation(boolean):
     rospy.loginfo("Rover Confirmation: " + str(boolean.data))
     db_confirm.received = boolean.data
     db_confirm.save(force_update=True)

#Notified on whether task is a failure (0), success (1) or we reached a checkpoint (2)
def task_progress(num):
    val = num.data
    if (0 <= val and val < 3):
        db_task_state.state = val
        db_task_state.save()
    else:
        #TODO how to handle this exception?
        exception_clbk("unacceptable number received: ", val)
        
#Science analysis failure (0) or success (1)
'''def sc_progress(num):
    val = num.data
    if (val == 0 or val == 1):
        db_science.state = val
        db_science.save()
    else:
        db_exception("unacceptable number received: " + val)
'''

def sc_text_info(info):
    str = info.data
    db_science.sc_text = str
    db_science.save()
    rospy.loginfo("Science: text_info: " + str)

def sc_humidity(hums):
    arr = hums.data
    tNum = arr[0]
    val = arr[1]

    if(tNum == 0):
        rospy.loginfo("Science: humidity tube 1: " + str(val))
        db_science.t1_hum = val
        db_science.save()
    elif(tNum == 1):
        rospy.loginfo("Science: humidity tube 2: " + str(val))
        db_science.t2_hum = val
        db_science.save()
    else:
        rospy.loginfo("Science: humidity tube 3: " + str(val))
        db_science.t3_hum = val
        db_science.save()


def sc_mass(mass):
    val = mass.data
    rospy.loginfo("Science: mass: " + str(val) + "[g]")
    db_science.mass = val
    db_science.save()


def hd_data(matrix):
    el1 = matrix[0]
    el2 = matrix[1]
    el3 = matrix[2]
    el4 = matrix[3]
    el5 = matrix[4]
    el6 = matrix[5]
    el7 = matrix[6]

    


# TODO update the database everytime dist(pos1, pos2) > eps
# TODO IL FAUT PASSER A POSTGRESQL POUR LES ARRAYFIELD STP
def nav_data(odometry):
    data = odometry.data
    pos = data.pose.pose.position
    posArr = [pos.x, pos.y, pos.z]

    db_navigation.posX = posArr[0]
    db_navigation.posY = posArr[1]
    db_navigation.posZ = posArr[2]

    twistLin = data.twist.twist.linear
    linArr = [twistLin.x, twistLin.y, twistLin.z]

    db_navigation.linVelX = linArr[0]
    db_navigation.linVelY = linArr[1]
    db_navigation.linVelZ = linArr[2]

    twistAng = data.twist.twist.angular
    angArr = [twistAng.x, twistAng.y, twistAng.z]

    db_navigation.angVelX = angArr[0]
    db_navigation.angVelY = angArr[1]
    db_navigation.angVelZ = angArr[2]


#TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
#General topic on which subsystems can publish if an unexpected exception was thrown
def exception_clbk(str): 
    val = str.data
    db_exception.string = val
    db_exception.save() 