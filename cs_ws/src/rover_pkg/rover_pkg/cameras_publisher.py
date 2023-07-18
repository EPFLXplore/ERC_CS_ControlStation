
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int8MultiArray

import cv2
from cv_bridge import CvBridge


CAMERA_FRAMERATE = 20


class CamerasPublisher(Node):

    def __init__(self):

        super().__init__('cameras_publisher')

        self.camera_index = self.create_subscription(Int8MultiArray, 'CS/CAM_index', self.enable_camera, 10)

        self.cam_1_pub = self.create_publisher(CompressedImage, 'camera_1', 1)
        self.cam_2_pub = self.create_publisher(CompressedImage, 'camera_2', 1)
        self.cam_3_pub = self.create_publisher(CompressedImage, 'camera_3', 1)
        self.cam_4_pub = self.create_publisher(CompressedImage, 'camera_4', 1)

        self.camera_0 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0))
        self.camera_1 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=1))
        self.camera_2 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=2))
        self.camera_3 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=3))
        self.camera_4 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=4))
        self.camera_5 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=5))

        self.bridge = CvBridge()

        self.camera_list = []
        self.camera_list.append(self.camera_0)
        self.camera_list.append(self.camera_1)
        self.camera_list.append(self.camera_2)
        self.camera_list.append(self.camera_3)
        self.camera_list.append(self.camera_4)
        self.camera_list.append(self.camera_5)


        self.cam_publisher = []
        self.cam_publisher.append(self.cam_1_pub)
        self.cam_publisher.append(self.cam_2_pub)
        self.cam_publisher.append(self.cam_3_pub)
        self.cam_publisher.append(self.cam_4_pub)

        self.update_camera = []

        self.timer = self.create_timer(1/CAMERA_FRAMERATE, self.publish_feeds)


    def enable_camera(self, camera_index):
        print("Enabling camera: ", camera_index.data)

        self.disable_camera()
        for i in camera_index.data:
            self.update_camera.append(self.camera_list[i])

    def disable_camera(self):
        self.update_camera = []

    def stop_camera(self):
        for i in self.camera_list:
            i.release()

    def publish_feeds(self):

        for i in range(len(self.update_camera)):
            ret, frame = self.update_camera[i].read()
            if ret:
                self.cam_publisher[i].publish(self.bridge.cv2_to_compressed_imgmsg(frame))
        

        # ret_0, frame_cam_0 = self.camera_0.read()
        # if ret_0 :
        #     self.cam_0_pub.publish(self.bridge.cv2_to_compressed_imgmsg(frame_cam_0))

        # ret, frame = self.camera_list[i].read()
        # if ret:
        #         self.cam_0_pub.publish(self.bridge.cv2_to_compressed_imgmsg(frame))


def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1080,
    capture_height=720,
    display_width=1080,
    display_height=720,
    framerate=CAMERA_FRAMERATE,
    flip_method=0,
):
    # return (
    #     "nvarguscamerasrc sensor-id=%d !"
    #     "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
    #     "nvvidconv flip-method=%d ! "
    #     "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    #     "videoconvert ! "
    #     "video/x-raw, format=(string)BGR ! appsink"
    #     % (
    #         sensor_id,
    #         capture_width,
    #         capture_height,
    #         framerate,
    #         flip_method,
    #         display_width,
    #         display_height,
    #     )
    # )

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
    return ('sudo gst-launch-1.0 v4l2src ! videoconvert ! video/x-raw, format=(string)BGR ! appsink')

def main(args=None):

    print("Start cameras_publisher node")
    
    rclpy.init(args=args)

    cameras_publisher = CamerasPublisher()

    rclpy.spin(cameras_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cameras_publisher.stop_camera()
    cameras_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



#'sudo gst-launch-1.0 v4l2src ! videoconvert ! x264enc pass=qual quantizer=20 tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=8080'






"""
gst-laumch-1.0 nvarguscamerasrc sensor-id=0 ! 'video/x-raw(memory:NVMM), width=(int)1948, height=(int)1096, framerate=(fraction)30/1' ! nvvidconv ! xvimagesink -e
"""























# import rclpy
# from rclpy.node import Node 
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge 
# import cv2
# from xplore_interfaces.msg import CameraError
# from xplore_interfaces.srv import EnableCamera, DisableCamera

# import os
# import subprocess

# NUMBER_CAMERAS = 6
# STARTING_PORT = 8000


# class CamerasPublisher(Node):

#     def __init__(self):

#         super().__init__('cameras_publisher')
#         self.publisher_ = self.create_publisher(Image, 'camera_0', 10)

#         self.camerasIPList = [-1] * NUMBER_CAMERAS  # -1 means camera is disabled, otherwise it is the ip adress of the camera
#         self.cameraStreamList = [] * NUMBER_CAMERAS 


#         self.CameraDisconnectedPublisher = self.create_publisher(CameraError, 'camera_disconnected', 10)  #change name of cameraError
#         self.EnableCameraService = self.create_service(EnableCamera, 'enable_camera', self.enable_camera_callback)
#         self.DisableCameraService = self.create_service(DisableCamera, 'disable_camera', self.disable_camera_callback)

#         #TO DO: error handling with error publisher

#         timer_period = 0.1  # seconds
#         self.timer = self.create_timer(timer_period, self.timer_callback)      
#         #self.cap = cv2.VideoCapture(0)
#         self.br = CvBridge()

#     def enable_camera_callback(self, request, response):

#         if(request.index < 0 or request.index >= NUMBER_CAMERAS):
#             #TO DO: Send error message to console
#             response.success = False
#             return response

#         if(self.cameraStreamList[request.index].isOpened()):
#             response.ip_adress = self.camerasList[request.index]
#             response.success = True
#             return response

#         #TO DO: Enable camera
#         self.start_camera(request.index)
#         cap = cv2.VideoCapture(request.index)
    
#         if(cap.isOpened()):
#             self.cameraStreamList[request.index] = cap
#             self.camerasList[request.index] = STARTING_PORT + request.index
#             response.ip_adress = self.camerasList[request.index]
#             response.success = True
#             return response

#         response.success = False
#         response.ip_adress = -1
#         return response

#     def disable_camera_callback(self, request, response):

#         if(request.index < 0 or request.index >= NUMBER_CAMERAS):
#             #TO DO: Send error message to console
#             response.success = False
#             return response

#         if(self.camerasList[request.index] == -1):
#             response.success = True
#             return response
        
#         self.cameraStreamList[request.index].release() #TO DO: Check if error could occur
#         self.cameraStreamList[request.index] = None
#         self.camerasIPList[request.index] = -1

#         response.success = True
#         return response

#     def timer_callback(self):
#         return

#         #ret, frame = self.cap.read()
            
#         #if ret == True:
#         #   self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

#         #self.get_logger().info('Publishing video frame')

#     def start_camera(self, index):
#             self.get_logger().warning('Camera started')
#             #gstreamer_str = 'sudo gst-launch-1.0 v4l2src ! videoconvert ! x264enc pass=qual quantizer=20 tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=8080'
#             #cap = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)
#             #ret, frame = cap.read()
            
#             cmd = self.gstreamer_pipeline()
#             subprocess.run(cmd, shell=True)
            

#     def gstreamer_pipeline(
#     sensor_id=5,
#     capture_width=1948,
#     capture_height=1096,
#     display_width=1948,
#     display_height=1096,
#     framerate=30,
#     flip_method=2):
#         """return (
#             "nvarguscamerasrc sensor-id=%d sensor-mode=1 !"
#             "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, format=(string)NV12, framerate=(fraction)%d/1 ! "
#             "nvvidconv ! xvimagesink -e"
#             "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
#             "videoconvert ! "
#             "x264enc pass=qual quantizer=20 tune=zerolatency ! "
#             "rtph264pay ! "
#             "udpsink host=127.0.0.1 port=8080"
#             % (
#                 sensor_id,
#                 capture_width,
#                 capture_height,
#                 framerate,
#                 display_width,
#                 display_height,
#             )
#         )"""
#         return 'sudo gst-launch-1.0 v4l2src ! videoconvert ! x264enc pass=qual quantizer=20 tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=8080'
#         """return (
#             "gst-launch-1.0 v4l2src !"  
#             "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, format=(string)NV12, framerate=(fraction)%d/1 ! "
#             "videoconvert ! "
#             "x264enc pass=qual quantizer=20 tune=zerolatency ! "
#             "rtph264pay ! "
#             "udpsink host=127.0.0.1 port=8080"
#             % (
#                 capture_width,
#                 capture_height,
#                 framerate,
#             )
#         )"""

  
# def main(args=None):
  
#   rclpy.init(args=args)
#   camerasPublisher = CamerasPublisher()
#   camerasPublisher.start_camera(1)
#   rclpy.spin(camerasPublisher)

#   #image_publisher.destroy_node()
#   #rclpy.shutdown()
  
# if __name__ == '__main__':
#   print("Starting cameras publisher")
#   main()