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
node = rclpy.create_node('compression')

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


def receive_cam_1(msg):
    global im1, bridge
    im1 = bridge.compressed_imgmsg_to_cv2(msg)

    result, imgencode = cv2.imencode('.jpg', im1, encode_param)
    data = np.array(imgencode)
    img = data.tobytes()
    img = base64.b64encode(img).decode()


def receive_cam_2(msg):
    global im2, bridge
    im2 = bridge.compressed_imgmsg_to_cv2(msg)


def receive_cam_3(msg):
    global im3, bridge
    im3 = bridge.compressed_imgmsg_to_cv2(msg)


def receive_cam_4(msg):
    global im4, bridge
    im4 = bridge.compressed_imgmsg_to_cv2(msg)


def receive_cam_5(msg):
    global im5, bridge
    im5 = bridge.compressed_imgmsg_to_cv2(msg)


def receive_cam_6(msg):
    global im6, bridge
    im6 = bridge.compressed_imgmsg_to_cv2(msg)

# |> Create subscribers for each feed from the camera node <|
# =================================================================
node.create_subscriber(CompressedImage, 'camera_1', receive_cam_1)
node.create_subscriber(CompressedImage, 'camera_2', receive_cam_2)
node.create_subscriber(CompressedImage, 'camera_3', receive_cam_3)
node.create_subscriber(CompressedImage, 'camera_4', receive_cam_4)
node.create_subscriber(CompressedImage, 'camera_5', receive_cam_5)
node.create_subscriber(CompressedImage, 'camera_6', receive_cam_6)

# |> Create publishers for each feed of compressed streaming <|
# =================================================================
comp_1_pub = node.create_publisher(CompressedImage, 'compressed_1', 1)
comp_2_pub = node.create_publisher(CompressedImage, 'compressed_2', 1)
comp_3_pub = node.create_publisher(CompressedImage, 'compressed_3', 1)
comp_4_pub = node.create_publisher(CompressedImage, 'compressed_4', 1)
comp_5_pub = node.create_publisher(CompressedImage, 'compressed_5', 1)
comp_6_pub = node.create_publisher(CompressedImage, 'compressed_6', 1)

############### TODO: compress images from im(i) -> cim(i)

def publish_compressed_frame(publisher, image, compression_type='jpg'):
    publisher.publish(bridge.cv2_to_compressed_imgmsg(image, compression_type))

def publish_compressed_feeds():
    while rclpy.ok():
        publish_compressed_frame(comp_1_pub, cim1, 'jpg')
        publish_compressed_frame(comp_2_pub, cim2, 'jpg')
        publish_compressed_frame(comp_3_pub, cim3, 'jpg')
        publish_compressed_frame(comp_4_pub, cim4, 'jpg')
        publish_compressed_frame(comp_5_pub, cim5, 'jpg')
        publish_compressed_frame(comp_6_pub, cim6, 'jpg')

if __name__ == '__main__':
    # start publishing
    publish_compressed_feeds()


