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
import numpy as np
import sys

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge

NUMBER_CAMERAS = 6

# ==================================================================
# ROS Subscribers and callback functions definition



#im1 = np.zeros((300, 300, 3))


# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]

# def display_cam_1(msg):
#     global im1, bridge
#     im1 = bridge.compressed_imgmsg_to_cv2(msg)

#     result, imgencode = cv2.imencode('.jpg', im1, encode_param)
#     data = np.array(imgencode)
#     img = data.tobytes()
#     img = base64.b64encode(img).decode()

#node.create_subscriber(CompressedImage, 'camera_1', display_cam_1)



# ==================================================================
# Main



class CamerasReceiver(Node):

    def __init__(self):
        super().__init__('cameras_receiver')
        #self.node = rclpy.create_node('cameras_receiver')

        self.bridge = CvBridge()                 # bridge between OpenCV and ROS

        self.images = np.zeros((NUMBER_CAMERAS, 720, 1280, 3))
        self.subscription = [] #= self.create_subscription(CompressedImage, 'camera_1', lambda msg : self.display_cam(msg, 0), 0)
        self.create_subscription(Image, 'camera_0', self.Test, 0)

        #for i in range(NUMBER_CAMERAS):
            #self.subscription.append(self.create_subscription(Image, 'camera_' + str(i), lambda msg : self.display_cam(msg, i), 0))

    def Test(self, msg):
        print("call")
        self.images[0] = self.bridge.imgmsg_to_cv2(msg)
        self.display()

    #def display_cam(self, msg, index):
        #self.images[index] = self.bridge.compressed_imgmsg_to_cv2(msg)


    def display(self):
        print("displaying images")
        cv2.imshow('test', self.images[0])
        key = cv2.waitKey(1)



def main():
    print("starting cameras receiver")
    rclpy.init(args=sys.argv)
    camerasReceiver = CamerasReceiver()
    rclpy.spin(camerasReceiver)
    #camerasReceiver.run()


if __name__ == "__main__":
    main()