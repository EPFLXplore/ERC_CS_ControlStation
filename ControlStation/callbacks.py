from threading import Thread
import rospy


from std_msgs.msg import Int8MultiArray, Int8, Float32, Bool, String, Int16MultiArray
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Twist 
from actionlib_msgs.msg import GoalID

from DB_objects import *

from Controller import *
#The following callback functions update the db objects' values

#Rover sends a confirmation that it received an instruction
def rover_confirmation(boolean):
     rospy.loginfo("Rover Confirmation: " + str(boolean.data))
     confirm.received = boolean.data
     confirm.save(force_update=True)

#Notified on whether task is a failure (0), success (1) or we reached a checkpoint (2)
def task_progress(num):
    val = num.data
    if (0 <= val and val < 3):
        task_state.state = val
        task_state.save()
    else:
        #TODO how to handle this exception?
        exception("unacceptable number received: ", val)
        
#Science analysis failure (0) or success (1)
def science_progress(num):
    val = num.data
    if (val == 0 or val == 1):
        science_state.state = val
        science_state.save()
    else:
        exception("unacceptable number received: " + val)

#TODO on pourrait faire une liste d'exceptions comme ca on a un historique des problèmes qui ont eu lieu
#General topic on which subsystems can publish if an unexpected exception was thrown
def exception_clbk(str): 
    val = str.data
    exception.string = val
    exception.save() 