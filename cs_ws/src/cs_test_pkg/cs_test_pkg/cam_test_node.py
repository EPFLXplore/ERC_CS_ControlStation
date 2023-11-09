
import math
import random

import numpy
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage, Image

import cv2
from cv_bridge import CvBridge

FRAME_RATE = 30
IMAGE_SIZE = 900

class CamTestNode(Node):

    def __init__(self):
        super().__init__('cam_test_publisher')

        self.bridge = CvBridge()
        # Log publisher

        self.cam_0_pub = self.create_publisher(CompressedImage, 'camera_0', 1)
        #self.cam_0_pub = self.create_publisher(Image, 'camera_0', 1)

        timer_period = 1/FRAME_RATE # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = int((IMAGE_SIZE/2) * (IMAGE_SIZE/2) + IMAGE_SIZE/2)

        self.img = numpy.zeros([IMAGE_SIZE,IMAGE_SIZE,3])

        self.img[:,:,0] = numpy.ones([IMAGE_SIZE,IMAGE_SIZE])*0
        self.img[:,:,1] = numpy.ones([IMAGE_SIZE,IMAGE_SIZE])*0
        self.img[:,:,2] = numpy.ones([IMAGE_SIZE,IMAGE_SIZE])*0


        print('Cam test is running with FRAME_RATE = ' + str(FRAME_RATE) + ' Hz')

    def timer_callback(self):
        msg = CompressedImage()
        self.img[self.i%IMAGE_SIZE, math.floor(self.i/IMAGE_SIZE)] = 255
        msg = self.bridge.cv2_to_compressed_imgmsg(self.img)
        #msg = self.bridge.cv2_to_imgmsg(self.img)
        self.cam_0_pub.publish(msg)

        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = CamTestNode()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
