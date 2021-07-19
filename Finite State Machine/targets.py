#nav target
import time
import rospy
from std_msgs.msg import Int32

def nav(running_flag, waiting_flag):
  print("waiting_flag")
  print(waiting_flag.value)
  rospy.init_node('nav_task', anonymous=True)
#   rospy.spin()
  confirmation_pub = rospy.Publisher('confirmation', Int32, queue_size=1)
  count = 0
  if(running_flag.value == 0):
    
    i = Int32(data=1)
    rospy.sleep(0.5)
    confirmation_pub.publish(i)
    running_flag.value = 1

  while True:
      while(waiting_flag.value == 1):
        time.sleep(0.1)
      count += 1
      print(count)
      time.sleep(1)
