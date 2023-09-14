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
import base64

from cv_bridge             import CvBridge

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),95]

bridge = CvBridge()  # bridge between OpenCV and ROS

im_0 = np.zeros((300, 300, 3))
im_1 = np.zeros((300, 300, 3))
im_2 = np.zeros((420, 360, 3))
im_3 = np.zeros((300, 300, 3))
im_4 = np.zeros((300, 300, 3))
im_5 = np.zeros((300, 300, 3))

# gripper camera
im_6 = np.zeros((300, 300, 3))



# ==================================================================
# callback functions definition

def encode_stream(s):
    
    result, imgencode = cv2.imencode('.jpg', s, encode_param)
    data = np.array(imgencode)
    img = data.tobytes()
    # base64 encoded transmission
    img = base64.b64encode(img).decode()
    return img

def display_cam_0(msg):
    global im0
    im0 = bridge.compressed_imgmsg_to_cv2(msg)
    img = encode_stream(im0)
    async_to_sync(channel_layer.group_send)("video0", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })


def display_cam_1(msg):
    global im1
    im1 = bridge.compressed_imgmsg_to_cv2(msg)
    img = encode_stream(im1)
    async_to_sync(channel_layer.group_send)("video1", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })



def display_cam_2(msg):
    global im2 
    im2 = bridge.compressed_imgmsg_to_cv2(msg)
    img = encode_stream(im2)
    async_to_sync(channel_layer.group_send)("video2", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })


    

def display_cam_3(msg):
    global im3
    im3 = bridge.compressed_imgmsg_to_cv2(msg)

    img = encode_stream(im3)
    async_to_sync(channel_layer.group_send)("video3", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })



def display_cam_4(msg):
    global im4 
    im4 = bridge.compressed_imgmsg_to_cv2(msg)

    img = encode_stream(im4)
    async_to_sync(channel_layer.group_send)("video4", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })



def display_cam_5(msg):
    print("display_cam_5 received msg")
    global im5 
    im5 = bridge.compressed_imgmsg_to_cv2(msg)

    img = encode_stream(im5)
    async_to_sync(channel_layer.group_send)("video5", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })
    

def display_cam_gripper(msg):
    global im6
    im6 = bridge.imgmsg_to_cv2(msg)

    img = encode_stream(im6)
    async_to_sync(channel_layer.group_send)("video6", {"type": "video_message",
                                                            'video_data' : "data:image/jpg;base64,"+ img })
