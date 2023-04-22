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
import websocket
import base64

from xplore_interfaces.msg import CameraError
from xplore_interfaces.srv import EnableCamera, DisableCamera

# ==================================================================

print("this file is running")

NUMBER_CAMERAS = 7

CAMERAS_WS_URL = []
ws = []

for i in range(NUMBER_CAMERAS):
    CAMERAS_WS_URL.append('ws://127.0.0.1:8000/ws/cameras/video' + str(i) + '/')
    ws.append(websocket.WebSocket())
    ws[i].connect(CAMERAS_WS_URL[i])

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),95]

# ==================================================================
# callback functions definition

def encode_stream(s):
    
    result, imgencode = cv2.imencode('.jpg', s, encode_param)
    data = np.array(imgencode)
    img = data.tobytes()

    # base64 encoded transmission
    img = base64.b64encode(img).decode()
    return img

def display_cam(msg, index):
    img = encode_stream(msg)
    ws[index].send("data:image/jpg;base64,"+ img)

"""
# ==================================================================

# ROS node definition
rospy.init_node("cameras_reciever", anonymous=False)

# ims = images()

# ROS subscribers

rospy.Subscriber('/intel_D405/color_image/compressed',               CompressedImage, display_cam_7) 
rospy.Subscriber('/intel_D405/color_image_detection/compressed',     CompressedImage, display_cam_8)
rospy.Subscriber('camera_1',                CompressedImage, display_cam_1 )
rospy.Subscriber('camera_2',                CompressedImage, display_cam_2 )
rospy.Subscriber('camera_3',                CompressedImage, display_cam_3 )
rospy.Subscriber('camera_4',                CompressedImage, display_cam_4 )
rospy.Subscriber('camera_5',                CompressedImage, display_cam_5 )
rospy.Subscriber('camera_6',                CompressedImage, display_cam_6 )


# ROS publishers
rospy.spin()
"""
        
gstreamer_str = "gst-launch-1.0 udpsrc port=8080 ! \"application/x-rtp, payload=127\" ! rtph264depay ! avdec_h264 ! videoconvert ! appsink"

#cap = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture(
    'gst-launch-1.0 udpsrc port=8080 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264"'
    ' ! rtph264depay'
    ' ! avdec_h264'
    ' ! videoconvert'
    ' ! appsink', cv2.CAP_GSTREAMER)

while(cap.isOpened()):
    ret, frame = cap.read()
    #print(type(frame))
    if(ret):
        display_cam(frame, 2)
        display_cam(frame, 0)
        display_cam(frame, 6)

NUMBER_CAMERAS = 6

class CamerasReceiver():
    
        def __init__(self):
            super().__init__('cameras_receiver')

            self.camerasIPList = [-1] * NUMBER_CAMERAS  # -1 means camera is disabled, otherwise it is the ip adress of the camera
            self.cameraStreamList = [] * NUMBER_CAMERAS 

            self.CameraDisconnectedSubscriber = self.create_subscription(CameraError, 'camera_disconnected')
            
            self.EnableCameraClient = self.create_client(EnableCamera, 'enable_camera')
            while not self.EnableCameraClient.wait_for_service(timeout_sec = 5.0):
                self.get_logger().info('service not available, waiting again...')
            self.req = EnableCamera.Request()

            self.DisableCameraClient = self.create_client(DisableCamera, 'disable_camera')
            while not self.DisableCameraClient.wait_for_service(timeout_sec = 5.0):
                self.get_logger().info('service not available, waiting again...')
            self.req = DisableCamera.Request()
