from sensor_msgs.msg import Image, CompressedImage
from std_msgs.msg import Int8
from pyrealsense2 import pyrealsense2 as rs
import numpy as np


import cv2 as cv
from cv_bridge import CvBridge

import numpy as np

import rclpy
from rclpy.node import Node
import threading

# =========================================================================================================
def main(args=None):
    rclpy.init()

    vision_node = Node("HD_vision_node")

    ############
    # PUBLISHERS
    ############
    camera_publisher = CameraFluxPublisher(vision_node)

    ############
    # SUBSCRIBERS
    ############
    toggle_cameras_subscriber = HDToggleCamerasSubscriber(vision_node, camera_publisher)

    print("Publishing gripper flux")

    threading.Thread(target=rclpy.spin, args=(vision_node,), daemon=True).start()

    rate = vision_node.create_rate(1)  # 1hz


    while True:
        camera_publisher.publish_frame()
        rate.sleep()


if __name__ == '__main__':
    main()





class CameraFluxPublisher:
    def __init__(self, node):
        self.parent_node = node
        self.publisher_ = node.create_publisher(CompressedImage, 'HD/camera_flux', 10)
        self.bridge_ = CvBridge()
        self.enabled_ = False  # Flag to indicate if the publisher is enabled

        # Configure Realsense camera
        self.pipeline_ = rs.pipeline()
        self.config_ = rs.config()

        # enable_stream(rs2_stream stream_type, int width, int height, rs2_format format=RS2_FORMAT_ANY, int framerate=0)
        self.config_.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        self.pipeline_.start(self.config_)

    def get_logger(self):
        return self.parent_node.get_logger()
    
    def publish_frame(self):

        if not self.enabled_:
            return
        
        frames = self.pipeline_.wait_for_frames()
        color_frame = frames.get_color_frame()

        if color_frame:

            # Convert the Realsense frame to an OpenCV image
            img = np.asanyarray(color_frame.get_data())

            # Convert the OpenCV image to a ROS Image message
            img_msg = self.bridge_.cv2_to_imgmsg(img, encoding='bgr8')

            # Set the header information of the Image message
            img_msg.header.stamp = self.parent_node.get_clock().now().to_msg()
            img_msg.header.frame_id = 'camera_frame'

            # Publish the Image message
            #self.publisher_.publish(img_msg)
            self.publisher_.publish(self.bridge_.cv2_to_compressed_imgmsg(img))


class HDToggleCamerasSubscriber:
    def __init__(self, node, publisher):
        self.parent_node = node
        self.publisher_ = publisher
        self.subscription_ = node.create_subscription(
            Int8,
            'ROVER/HD_toggle_cameras',
            self.callback,
            10
        )

    def callback(self, msg):
        if msg.data == 0: # Off
            self.publisher_.enabled_ = False
            print("Camera publisher disabled")
        elif msg.data == 1: # On
            self.publisher_.enabled_ = True
            print("Camera flux enabled")