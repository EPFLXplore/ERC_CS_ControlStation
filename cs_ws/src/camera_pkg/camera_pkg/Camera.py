'''
@INFO
'''
# Libraries
import cv2
import rclpy
import sys
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge

device = rclpy.get_param('device')
pub_topic = rclpy.get_param('pubtopic')
print("----------------- device:", device, "------- type:", type(device))
print("----------------- pub_topic:", pub_topic, "------- type:", type(pub_topic))

# Constant
ROS_LOOP_RATE = 30

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

camera = cv2.VideoCapture(gstreamer_pipeline(device))

# ROS Node 
rclpy.init(args = sys.args)
node = rclpy.create_node('camera_node')
rate = node.create_rate(ROS_LOOP_RATE)
bridge = CvBridge()

# ROS Publishers
cam_pub = node.create_publisher(CompressedImage, pub_topic, 1)

# Feed compression & publishing

def publish_feeds():

    while rclpy.ok():

        ret, frame_cam = camera.read()
        if ret :
            cam_pub.publish(bridge.cv2_to_compressed_imgmsg(frame_cam))

if __name__ == '__main__':
    # Start publishing
    publish_feeds()
    
    # On quit
    camera.release()
