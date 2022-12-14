'''
@file  : cameras_receiver.py 

@author: Emile Hreich
         emile.janhodithreich@epfl.ch

@date : 30/03/2022

@brief: 


'''
# ==================================================================
# libraries
import cv2
import rclpy
import numpy as np
import base64

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
# ==================================================================
# Constants

# ==================================================================
# utils


# ==================================================================
# ROS Node definition (to verify)

rclpy.init(args = sys.args)
node = rclpy.create_node('cameras_receiver')

bridge = CvBridge()                 # bridge between OpenCV and ROS


# ==================================================================
# ROS Subscribers and callback functions definition

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]

im1 = np.zeros((300, 300, 3))
im2 = np.zeros((300, 300, 3))
im3 = np.zeros((300, 300, 3))
im4 = np.zeros((300, 300, 3))
im5 = np.zeros((300, 300, 3))
im6 = np.zeros((300, 300, 3))
im7 = np.zeros((300, 300, 3))


def display_cam_1(msg):
    global im1, bridge
    im1 = bridge.compressed_imgmsg_to_cv2(msg)

    result, imgencode = cv2.imencode('.jpg', im1, encode_param)
    data = np.array(imgencode)
    img = data.tobytes()
    img = base64.b64encode(img).decode()


def display_cam_2(msg):
    global im2, bridge
    im2 = bridge.compressed_imgmsg_to_cv2(msg)


def display_cam_3(msg):
    global im3, bridge
    im3 = bridge.compressed_imgmsg_to_cv2(msg)


def display_cam_4(msg):
    global im4, bridge
    im4 = bridge.compressed_imgmsg_to_cv2(msg)


def display_cam_5(msg):
    global im5, bridge
    im5 = bridge.compressed_imgmsg_to_cv2(msg)


def display_cam_6(msg):
    global im6, bridge
    im6 = bridge.compressed_imgmsg_to_cv2(msg)


node.create_subscriber(CompressedImage, 'camera_1', display_cam_1)
node.create_subscriber(CompressedImage, 'camera_2', display_cam_2)
node.create_subscriber(CompressedImage, 'camera_3', display_cam_3)
node.create_subscriber(CompressedImage, 'camera_4', display_cam_4)
node.create_subscriber(CompressedImage, 'camera_5', display_cam_5)
node.create_subscriber(CompressedImage, 'camera_6', display_cam_6)


# ==================================================================
# Main

def display():
    while True:
        cv2.imshow('test', im1)
        cv2.imshow('test1', im2)
        cv2.imshow('test10', im3)
        # cv2.imshow('tesXGFHt', im4)
        # cv2.imshow('teAETHst', im5)
        #cv2.imshow('tesATEHt', im7)

        key = cv2.waitKey(20)
        if key == 27 or key == 1048603:
            break


display()
