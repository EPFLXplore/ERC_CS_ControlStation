import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge

RATE = 30

rospy.init_node('video_node')

# opencv video captures

# nav_mast_text = 'rtsp://xplore1:xplore@192.168.1.50:554/s1'
# nav_butt_text = 'rtsp://xplore1:xplore@192.168.1.51:554/s1'

nav_mast_text = '/dev/cams/mast'
nav_butt_text = "/dev/cams/butt"

hd_arm_text = '/dev/cams/arm'
hd_gripper_text = "/dev/cams/gripper"
sc_text = 'rtsp://root:Plokmijn123!@192.168.1.57/axis-media/media.amp'

v1 = cv2.VideoCapture(nav_mast_text)
v2 = cv2.VideoCapture(nav_butt_text)

v3 = cv2.VideoCapture(hd_arm_text)
v4 = cv2.VideoCapture(hd_gripper_text)
v5 = cv2.VideoCapture(sc_text)


v1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
v1.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

v2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
v2.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

v3.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
v3.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

v4.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
v4.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)


# publishers

v1_pub = rospy.Publisher('camera_mast', Image, queue_size=1)
v2_pub = rospy.Publisher('camera_butt', Image, queue_size=1)

# v2.set(cv2.CAP_PROP_FPS, RATE)
# v2.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# v2.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# v2.set(cv2.CAP_PROP_POS_MSEC, 0)

v3_pub = rospy.Publisher('camera_arm', Image, queue_size=1)
v4_pub = rospy.Publisher('camera_gripper', Image, queue_size=1)

v5_pub = rospy.Publisher('camera_sc', Image, queue_size=1)


# define subscriber to receive whether to publish video
display = {'nav': True, 'hd': False, 'sc': False}

def cam_callback(msg):
    if msg.data == 0:
        display['nav'] = True
        display['hd'] = False
        display['sc'] = False

    elif msg.data == 1:
        display['nav'] = False
        display['hd'] = True
        display['sc'] = False

    if msg.data == 2:
        display['nav'] = False
        display['hd'] = False
        display['sc'] = True

    if msg.data == 3:
        display['nav'] = False
        display['hd'] = False
        display['sc'] = False


rospy.Subscriber("which_cam", Int32, cam_callback, queue_size=1)

bridge = CvBridge()

r=rospy.Rate(RATE)

def get_image():
    while not rospy.is_shutdown():
        if display['nav']:

            ret1, frame1 = v1.read()
            if ret1:
                v1_pub.publish(bridge.cv2_to_imgmsg(frame1, "bgr8"))

            ret2, frame2 = v2.read()
            if ret2: 
                v2_pub.publish(bridge.cv2_to_imgmsg(frame2, "bgr8"))

        if display['hd']:

            ret3, frame3 = v3.read()
            if ret3:
                v3_pub.publish(bridge.cv2_to_imgmsg(frame3, "bgr8"))

            ret4, frame4 = v4.read()
            if ret4: 
                v4_pub.publish(bridge.cv2_to_imgmsg(frame4, "bgr8"))

        if display['sc']:
            ret5, frame5 = v5.read()
            if ret5:
                v5_pub.publish(bridge.cv2_to_imgmsg(frame5, "bgr8"))

        r.sleep()
    
get_image()

v1.release()
v2.release()
v3.release()
v4.release()
v5.release()








