
import rclpy
from rclpy.node import Node, Publisher
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import Int8MultiArray

import cv2
from cv_bridge import CvBridge
import threading


class CamerasPublisher(Node):

    def __init__(self):

        super().__init__('cameras_publisher')

        # ===== SUBSCRIBERS =====

        # turn on or off a camera of a given index
        self.camera_index = self.create_subscription(Int8MultiArray, 'CS/CAM_index', self.enable_camera, 10)

        # ===== PUBLISHERS =====

        # publishers for the 6 IMX290 cameras
        # self.cam_0_pub = self.create_publisher(CompressedImage, 'camera_0', 1)
        self.cam_2_pub = self.create_publisher(CompressedImage, 'camera_2', 1)
        self.cam_3_pub = self.create_publisher(CompressedImage, 'camera_3', 1)
        self.cam_4_pub = self.create_publisher(CompressedImage, 'camera_4', 1)
        self.cam_5_pub = self.create_publisher(CompressedImage, 'camera_5', 1)


        self.camera_publishers = [# self.cam_0_pub, 
                              self.cam_2_pub, 
                              self.cam_3_pub, 
                              self.cam_4_pub, 
                              self.cam_5_pub]

        global enabled
        enabled = [False] * 5


        # self.camera_0 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0))
        self.camera_2 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=2))
        self.camera_3 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=3))
        self.camera_4 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=4))
        self.camera_5 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=5))

        self.camera_list = [# self.camera_0, 
                            self.camera_2,
                            self.camera_3,
                            self.camera_4, 
                            self.camera_5]
        

        self.bridge = CvBridge()


        self.active_cameras = []
        
    def enable_camera(self, msg):
        camera_indices = msg.data
        for i in range(len(enabled)):
            if i in camera_indices and i < 6:
                print("Enable camera: " + str(i))
                # if the camera wasn't enabled then enable it, otherwise it is already turned on => thread already launched
                if enabled[i] == False:
                    enabled[i] = True
                    threading.Thread(target=run_camera, args=(self, self.camera_list[i], self.camera_publishers[i], i)).start()

            else:
                print("Disable camera: " + str(i))
                enabled[i] = False

    def publish_feeds(self):
        
        for i in range(len(self.active_cameras)):
            ret, frame = self.camera_list[self.active_cameras[i]].read()
            if ret:
                self.cam_publisher[i].publish(self.bridge.cv2_to_compressed_imgmsg(frame))

    def stop_camera(self):
        print("Stop camera...")
        for i in self.camera_list:
            i.release()
        self.camera_list = []



def gstreamer_pipeline(
    sensor_id=0,
    sensor_mode=0,
    capture_width=500,
    capture_height=500,
    display_width=500,
    display_height=500,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d sensor-mode=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            sensor_mode,
            capture_width,
            capture_height,
            30,
            flip_method,
            display_width,
            display_height,
        )
    )

def run_camera(cameras_publisher, camera, pub, i):
    print("Enter thread : " + str(i))
    while enabled[i]: # cameras_publisher.enabled[i] == True:
        ret, frame = camera.read()
        if (ret):
            frame = cameras_publisher.bridge.cv2_to_compressed_imgmsg(frame)
            pub.publish(frame)
        c = cv2.waitKey(1)
        if c == 27:
            enabled[i] = False
            camera.release()
            break

def main(args=None):

    print("Start cameras_publisher node...")
    
    rclpy.init(args=args)

    cameras_publisher = CamerasPublisher()
    
    print("Cameras ready")

    rclpy.spin(cameras_publisher)

    cameras_publisher.stop_camera()
    cameras_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()