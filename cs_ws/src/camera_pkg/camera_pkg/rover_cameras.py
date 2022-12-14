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
import rclpy
import sys

from sensor_msgs.msg import Image, CompressedImage
form cv_bridge import CvBridge

# ============= Constants
ROS_LOOP_RATE = 30

# ============= Utilities
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=300,
    capture_height=300,
    display_width=300,
    display_height=300,
    framerate=10,
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

def publish_frame(publisher, image, compression_type='jpg'):
    publisher.publish(bridge.cv2_to_compressed_imgmsg(image, compression_type))

# ==================================================================
# ROS Node definition

rclpy.init(args = sys.args)
node = rclpy.create_node('cameras')
rate = node.create_rate(ROS_LOOP_RATE)
bridge = CvBridge()                 # bridge between OpenCV and ROS

# ==================================================================
# camera captures

camera_1 = cv2.VideoCapture(gstreamer_pipeline(0))
camera_2 = cv2.VideoCapture(gstreamer_pipeline(1))
camera_3 = cv2.VideoCapture(gstreamer_pipeline(2))
camera_4 = cv2.VideoCapture(gstreamer_pipeline(3))
camera_5 = cv2.VideoCapture(gstreamer_pipeline(4))
camera_6 = cv2.VideoCapture(gstreamer_pipeline(5))

# ==================================================================
# ROS2 publishers definition

cam_1_pub = node.create_publisher(CompressedImage, 'camera_1', 1)
cam_2_pub = node.create_publisher(CompressedImage, 'camera_2', 1)
cam_3_pub = node.create_publisher(CompressedImage, 'camera_3', 1)
cam_4_pub = node.create_publisher(CompressedImage, 'camera_4', 1)
cam_5_pub = node.create_publisher(CompressedImage, 'camera_5', 1)
cam_6_pub = node.create_publisher(CompressedImage, 'camera_6', 1)

# ==================================================================
# feed publishing

def publish_feeds():

    while rclpy.ok():

        ret_1, frame_cam_1 = camera_1.read()
        if ret_1:
            cam_1_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_1))
            #publish_frame(cam_1_pub, frame_cam_1, 'jpg')

        ret_2, frame_cam_2 = camera_2.read()
        if ret_2:
            cam_2_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_2))
           # publish_frame(cam_2_pub, frame_cam_2, 'jpg')

        ret_3, frame_cam_3 = camera_3.read()
        if ret_3:
            cam_3_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_3))
            # publish_frame(cam_3_pub, frame_cam_3, 'jpg')

        ret_4, frame_cam_4 = camera_4.read()
        if ret_4:
            cam_4_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_4))
            # publish_frame(cam_4_pub, frame_cam_4, 'jpg')

        ret_5, frame_cam_5 = camera_5.read()
        if ret_5:
            cam_5_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_5))
            #publish_frame(cam_5_pub, frame_cam_5, 'jpg')

        ret_6, frame_cam_6 = camera_6.read()
        if ret_6:
            cam_6_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam_6))
        #    publish_frame(cam_6_pub, frame_cam_6, 'jpg')
            
if (__name__ == "__main__"):

    # starts publishing
    publish_feeds()

    # on quit
    camera_1.release()
    camera_2.release()
    camera_3.release()
    camera_4.release()
    camera_5.release()
    camera_6.release()