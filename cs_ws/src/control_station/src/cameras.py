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
import rospy
import websocket
import base64


from sensor_msgs.msg       import CompressedImage
from cv_bridge             import CvBridge

# ==================================================================

CAMERA_WS_URL = 'ws://127.0.0.1:8000/ws/video/wms/'

ws = websocket.WebSocket()
ws.connect(CAMERA_WS_URL)

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),95]

im_1 = np.zeros((300, 300, 3))
im_2 = np.zeros((300, 300, 3))
im_3 = np.zeros((300, 300, 3))
im_4 = np.zeros((300, 300, 3))
im_5 = np.zeros((300, 300, 3))
im_6 = np.zeros((300, 300, 3))

# ==================================================================
# callback functions definition


def display_cam_1(msg):
    global im1 
    im1 = bridge.compressed_imgmsg_to_cv2(msg)

    result, imgencode = cv2.imencode('.jpg', im1, encode_param)
    data = np.array(imgencode)
    img = data.tobytes()
    
    # base64 encoded transmission
    img = base64.b64encode(img).decode()
    
    ws.send("data:image/jpg;base64,"+ img)

    

def display_cam_2(msg):
    global im2 
    im2 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_3(msg):
    global im3 
    im3 = bridge.compressed_imgmsg_to_cv2(msg)
    

def display_cam_4(msg):
    global im4 
    im4 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_5(msg):
    global im5 
    im5 = bridge.compressed_imgmsg_to_cv2(msg)

def display_cam_6(msg):
    global im6 
    im6 = bridge.compressed_imgmsg_to_cv2(msg)



# ==================================================================

# ROS node definition
rospy.init_node("cameras_reciever", anonymous=False)

# ROS subscribers
rospy.Subscriber('camera_1',                CompressedImage, display_cam_1 )
rospy.Subscriber('camera_2',                CompressedImage, display_cam_2 )
rospy.Subscriber('camera_3',                CompressedImage, display_cam_3 )
rospy.Subscriber('camera_4',                CompressedImage, display_cam_4 )
rospy.Subscriber('camera_5',                CompressedImage, display_cam_5 )
rospy.Subscriber('camera_6',                CompressedImage, display_cam_6 )


# ROS publishers


bridge = CvBridge()  # bridge between OpenCV and ROS


      

        








