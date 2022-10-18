'''
@file  : rover_cameras.py 

@author: Emile Hreich
         emile.janhodithreich@epfl.ch

@date : 29/03/2022

@brief: 


'''
# ==================================================================
# libraries
import cv2
import rospy


from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge

device = rospy.get_param('device')
pub_topic = rospy.get_param('pubtopic')
print("----------------- device:", device, "------- type:", type(device))
print("----------------- pub_topic:", pub_topic, "------- type:", type(pub_topic))

# ==================================================================
# Constants
ROS_LOOP_RATE = 30

# ==================================================================
# utils

'''
This functions generates the command to launch the cameras.

sensor_id     :
capture_width :
...

'''
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=420,
    capture_height=360,
    display_width=420,
    display_height=360,
    framerate=15,
    flip_method=2,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height
        )
    )

'''

'''
def publish_frame(publisher, image, compression_type='jpg'):
    publisher.publish(bridge.cv2_to_compressed_imgmsg(image, compression_type))

# ==================================================================
# camera captures

# #########################################################################
# debug
# camera_1 = cv2.VideoCapture(0)
# #########################################################################

camera = cv2.VideoCapture(gstreamer_pipeline(device))

# ==================================================================
# ROS Publishers definition

cam_pub = rospy.Publisher(pub_topic, CompressedImage, queue_size=1)


# ==================================================================
# ROS Node definition

rate   = rospy.Rate(ROS_LOOP_RATE)
bridge = CvBridge()                 # bridge between OpenCV and ROS

# ==================================================================
# feed compression and publishing


'''
This functions 

'''
def publish_feeds():

    while not rospy.is_shutdown():

        ret, frame_cam = camera.read()
        if ret :
            cam_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam))
            # publish_frame(cam_pub, frame_cam, 'jpg')
        

# ==================================================================
# Main

if (__name__ == "__main__"):

    # starts publishing
    publish_feeds()

    # on quit
    camera.release()