
import rclpy
from rclpy.node import Node, Publisher
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import Int8MultiArray

import cv2
from cv_bridge import CvBridge
import threading

from gripper_camera import CameraFluxPublisher


CAMERA_FRAMERATE = 100


class CamerasPublisher(Node):

    def __init__(self):

        super().__init__('cameras_publisher')

        # ===== SUBSCRIBERS =====

        # turn on or off a camera of a given index
        self.camera_index = self.create_subscription(Int8MultiArray, 'CS/CAM_index', self.enable_camera, 10)

        # ===== PUBLISHERS =====

        # publishers for the 6 IMX290 cameras
        self.cam_0_pub = self.create_publisher(CompressedImage, 'camera_0', 1)
        self.cam_1_pub = self.create_publisher(CompressedImage, 'camera_1', 1)
        self.cam_2_pub = self.create_publisher(CompressedImage, 'camera_2', 1)
        self.cam_3_pub = self.create_publisher(CompressedImage, 'camera_3', 1)
        self.cam_4_pub = self.create_publisher(CompressedImage, 'camera_4', 1)
        self.cam_5_pub = self.create_publisher(CompressedImage, 'camera_5', 1)


        self.camera_publishers = [self.cam_0_pub, 
                              self.cam_1_pub, 
                              self.cam_2_pub, 
                              self.cam_3_pub, 
                              self.cam_4_pub, 
                              self.cam_5_pub]

        global enabled
        enabled = [False] * 7

        
        # self.cam_publisher.append(self.cam_1_pub)
        # self.cam_publisher.append(self.cam_2_pub)
        # self.cam_publisher.append(self.cam_3_pub)
        # self.cam_publisher.append(self.cam_4_pub)


        self.camera_0 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=0))
        self.camera_1 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=1))
        self.camera_2 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=2))
        self.camera_3 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=3))
        self.camera_4 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=4))
        self.camera_5 = None #cv2.VideoCapture(gstreamer_pipeline(sensor_id=5))
        self.cam_hd = CameraFluxPublisher(self)


        self.camera_list = [self.camera_0, 
                            self.camera_1,
                            self.camera_2,
                            self.camera_3,
                            self.camera_4, 
                            self.camera_5,
                            self.cam_hd]
        

        self.bridge = CvBridge()


        self.active_cameras = []
        
        #self.timer = self.create_timer(1/CAMERA_FRAMERATE, self.publish_feeds)

    # turn on a camera's publisher if its index is listed in the received array
    # otherwise, turn it off
    def enable_camera(self, msg):
        camera_indices = msg.data
        print("Enabling camera: ", camera_indices)
        # self.active_cameras = []
        for i in range(len(enabled)):
            if i in camera_indices and i < 7: 
                print("enabled ", i)
                # if the camera wasn't enabled then enable it, otherwise it is already turned on => thread already launched
                if enabled[i] == False:
                    enabled[i] = True
                    # Handle the gripper camera differently (index = 6)
                    if (i == 6) :
                        self.camera_list[i].enabled_ = True
                        threading.Thread(target=run_gripper, args= (self,self.camera_list[i])).start()
                    else:
                        threading.Thread(target=run_camera, args=(self, self.camera_list[i], self.camera_publishers[i], i)).start()

            else:
                enabled[i] = False
                #Handles the gripper camera differently (index = 3)
                if i == 6:
                    self.camera_list[i].enabled_ = False


        '''for i in camera_indices:
            if(i > 3):
                print("Camera index out of range")
                continue
            # self.active_cameras.append(i)

        print("Active cameras: ", self.active_cameras)'''


    def publish_feeds(self):
        
        for i in range(len(self.active_cameras)):
            ret, frame = self.camera_list[self.active_cameras[i]].read()
            if ret:
                #self.cam_publisher[i].publish(self.bridge.cv2_to_compressed_imgmsg(frame))
                self.cam_publisher[i].publish(self.bridge.cv2_to_compressed_imgmsg(frame))

    def stop_camera(self):
        print("camera stop called")
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
    framerate=CAMERA_FRAMERATE,
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

    # return (
    #         "gst-launch-1.0 v4l2src !"  
    #         "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, format=(string)NV12, framerate=(fraction)%d/1 ! "
    #         "videoconvert ! "
    #         "x264enc pass=qual quantizer=20 tune=zerolatency ! "
    #         "appsink"
    #         % (
    #             capture_width,
    #             capture_height,
    #             framerate,
    #         )
    # )
    #return ('sudo gst-launch-1.0 v4l2src ! videoconvert ! x264enc pass=qual quantizer=20 tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=8080')
    #return ('sudo gst-launch-1.0 v4l2src ! videoconvert ! video/x-raw, format=(string)BGR ! appsink')

def run_gripper(self, camera: CameraFluxPublisher):
    rate = self.create_rate(1)  # 1hz
    # While the gripper is enabled
    while enabled[6]:
        camera.publish_frame()
        rate.sleep()

def run_camera(cameras_publisher, camera, pub, i):
    print(enabled[i])
    print("enter thread")
    while enabled[i]: # cameras_publisher.enabled[i] == True:
        ret, frame = camera.read()
        if (ret):
            frame = cameras_publisher.bridge.cv2_to_compressed_imgmsg(frame)
            pub.publish(frame)
            #cv2.imshow('Input', frame)
        
        c = cv2.waitKey(1)
        if c == 27:
            break

    print("off ", i)


def main(args=None):

    print("Start cameras_publisher node .sdfsdf<ASGASGDAFGDASGFHAS")
    
    rclpy.init(args=args)

    cameras_publisher = CamerasPublisher()
    

    
    #threading.Thread(target=rclpy.spin, args=(cameras_publisher,)).start()

    #threading.Thread(target=run_camera, args=(cameras_publisher, cameras_publisher.camera_0, cameras_publisher.cam_1_pub, )).start()
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    # threading.Thread(target=run_camera, args=(cameras_publisher, cameras_publisher.camera_0, cameras_publisher.cam_0_pub, 0)).start()
    # threading.Thread(target=run_camera, args=(cameras_publisher, cameras_publisher.camera_1, cameras_publisher.cam_1_pub, 1)).start()
    # threading.Thread(target=run_camera, args=(cameras_publisher, cameras_publisher.camera_2, cameras_publisher.cam_2_pub, 2)).start()
    # threading.Thread(target=run_camera, args=(cameras_publisher, cameras_publisher.camera_3, cameras_publisher.cam_3_pub, 3)).start()

    #threading.Thread(target=rclpy.spin, args=(cameras_publisher,)).start()

    rclpy.spin(cameras_publisher)

    # while True:
        
    #     ret, frame = cameras_publisher.camera_0.read()
    #     frame = cameras_publisher.bridge.cv2_to_compressed_imgmsg(frame)
    #     cameras_publisher.cam_1_pub.publish(frame)
    #     #cv2.imshow('Input', frame)
        
    #     c = cv2.waitKey(1)
    #     if c == 27:
    #         break

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically

    # when the garbage collector destroys the node object)
    cameras_publisher.stop_camera()
    cameras_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
