# ROS python part of communication with avionics. Receives messages from ROS cpp
# file talker.cpp and displays the content of the message.

import rospy
from std_msgs.msg import String

# publisher node created outside of loop, can be called whenever
# pub = rospy.Publisher('msg', String, queue_size=10)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    # pub.publish("Sending message back to sender \n")

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
