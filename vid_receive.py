import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

rospy.init_node('cs_node')

bridge = CvBridge()
bridge2 = CvBridge()
bridge3 = CvBridge()
im1 = np.zeros((300, 300, 3))
im2 = np.zeros((300, 300, 3))
im3 = np.zeros((300, 300, 3))
im4 = np.zeros((300, 300, 3))
im5 = np.zeros((300, 300, 3))



def display_cam(msg):
    global im1 
    im1 = bridge.imgmsg_to_cv2(msg, "bgr8")
    

v1_sub = rospy.Subscriber('camera_mast', Image, display_cam)

def display_cam2(msg):
    global im2 
    im2 = bridge2.imgmsg_to_cv2(msg, "bgr8")

v2_sub = rospy.Subscriber('camera_butt', Image, display_cam2)

def display_cam3(msg):
    global im3
    im3 = bridge3.imgmsg_to_cv2(msg, "bgr8")
    
v3_sub = rospy.Subscriber('camera_arm', Image, display_cam3)

def display_cam4(msg):
    global im4 
    im4 = bridge2.imgmsg_to_cv2(msg, "bgr8")

v4_sub = rospy.Subscriber('camera_gripper', Image, display_cam4)

def display_cam5(msg):
    global im5
    im5 = bridge3.imgmsg_to_cv2(msg, "bgr8")
    
v5_sub = rospy.Subscriber('camera_sc', Image, display_cam5)




def fn():
    while 1:
        im = np.concatenate((im3, im4),  axis=1)
        cv2.imshow('both', im)
        #cv2.imshow('sc', im5)
        key = cv2.waitKey(20)
        if key == 27 or key == 1048603:
            break
        

fn()