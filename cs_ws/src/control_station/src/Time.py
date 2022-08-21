#
# @file: Time.py
# 
# @date: 20/08/2022
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
# @brief: 
#-------------------------------------------------------------------------------

# ==============================================================================
# Libraries

import json
import time
import rospy

from std_msgs.msg import Int32MultiArray

# ==============================================================================
    
rospy.init_node("timer", anonymous=False)

timer_pub = rospy.Publisher('Time',            Int32MultiArray,           queue_size=1)


seconds = 0
minutes = 0
hours   = 0

t = [0, 0, 0]

while True:
    # update time
    seconds += 1
    if (seconds > 59):
        seconds = 0
        minutes += 1
    if (minutes > 59):
        minutes = 0
        hours += 1

    time.sleep(1)


    t=[hours, minutes, seconds]
    timer_pub.publish(data = t)





