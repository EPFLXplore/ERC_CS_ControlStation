import rospy
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('power_control', Bool, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        var = False
        pub.publish(var)
        print("var sent\n")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass