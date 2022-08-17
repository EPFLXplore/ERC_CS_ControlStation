'''
@file  : cameras.py 

@author: Emile Hreich
         emile.janhodithreich@epfl.ch

@date : 30/03/2022

@brief: exectuable in the control_station ros package to recieve 
        camera streams


'''
# ==================================================================
# libraries
import cv2
import numpy as np
# import threading
# from flask import Flask, render_template, Response

from cv_bridge import CvBridge


# ==================================================================

        # TODO
        # rospy.Subscriber('camera_1',                CompressedImage, self.controller.display_cam_1      , self.cameras)
        # rospy.Subscriber('camera_2',                CompressedImage, self.controller.display_cam_2      , self.cameras)
        # rospy.Subscriber('camera_3',                CompressedImage, self.controller.display_cam_3      , self.cameras)
        # rospy.Subscriber('camera_4',                CompressedImage, self.controller.display_cam_4      , self.cameras)
        # rospy.Subscriber('camera_5',                CompressedImage, self.controller.display_cam_5      , self.cameras)
        # rospy.Subscriber('camera_6',                CompressedImage, self.controller.display_cam_6      , self.cameras)

class Cameras:

    def __init__(self):        
        self.cam_1 = cv2.imread('/home/emile/Documents/CS_workspace/ControlStation/CS2022/static/common/logo-black2.png')
        self.cam_2 = np.zeros((300, 300, 3))
        self.cam_3 = np.zeros((300, 300, 3))
        self.cam_4 = np.zeros((300, 300, 3))
        self.cam_5 = np.zeros((300, 300, 3))
        self.cam_6 = np.zeros((300, 300, 3))
        


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


bridge = CvBridge()  # bridge between OpenCV and ROS

# cameras = Cameras()
# ==================================================================
# callback functions definition


def display_cam_1(msg, cameras):
    # global im1 
    # im1 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_1 = bridge.compressed_imgmsg_to_cv2(msg)
    

def display_cam_2(msg, cameras):
    # global im2 
    # im2 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_2 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_3(msg, cameras):
    # global im3 
    # im3 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_3 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_4(msg, cameras):
    # global im4 
    # im4 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_4 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_5(msg, cameras):
    # global im5 
    # im5 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_5 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_6(msg, cameras):
    # global im6 
    # im6 = bridge.compressed_imgmsg_to_cv2(msg)
    cameras.cam_6 = bridge.compressed_imgmsg_to_cv2(msg)







