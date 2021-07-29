#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import sys

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("You must give an argument to open a video stream.")
#         print("  It can be a number as video device, e.g.: 0 would be /dev/video0")
#         print("  It can be a url of a stream,        e.g.: rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")
#         print("  It can be a video file,             e.g.: myvideo.mkv")
#         exit(0)

#     resource = sys.argv[1]
#     # If we are given just a number, interpret it as a video device
#     if len(resource) < 3:
#         resource_name = "/dev/video" + resource
#         resource = int(resource)
#     else:
#         resource_name = resource
#     print("Trying to open resource: ", resource_name)
#     cap = cv2.VideoCapture(resource)
#     if not cap.isOpened():
#         print("Error opening resource: " + str(resource))
#         print("Maybe opencv VideoCapture can't open it")
#         exit(0)

#     print("Correctly opened resource, starting to show feed.")
#     rval, frame = cap.read()
#     while rval:
#         cv2.imshow("Stream: " + resource_name, frame)
#         rval, frame = cap.read()
#         key = cv2.waitKey(20)
#         # print "key pressed: " + str(key)
#         # exit on ESC, you may want to uncomment the print to know which key is ESC for you
#         if key == 27 or key == 1048603:
#             break
#     cv2.destroyWindow("preview")



# import rospy
# from sensor_msgs.msg import Image as msg_Image
# from cv_bridge import CvBridge, CvBridgeError
# import cv2
# import time

# cv_image = 0

# def callback(data):
# 	cv_image = CvBridge().imgmsg_to_cv2(data, data.encoding)
# 	cv2.imshow('hdcameraimage', cv_image)
# 	cv2.waitKey(1)

# rospy.init_node("jaj")
# topic = '/HD_camera/image_raw'

# sub = rospy.Subscriber(topic, msg_Image, callback)
# rospy.spin()

if __name__ == '__main__':

    hd = '/dev/cams/mast'
    butt = '/dev/cams/butt'

    cap = cv2.VideoCapture(hd)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap2 = cv2.VideoCapture(butt)
    # cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        rval, frame = cap.read()
        
        cv2.imshow("hd: ", frame)
        rval, frame = cap2.read()
        frame = cv2.flip(frame, 0)
        cv2.imshow("butt: ", frame)
        key = cv2.waitKey(1)
        # print "key pressed: " + str(key)
        # exit on ESC, you may want to uncomment the print to know which key is ESC for you
        if key == 27 or key == 1048603:
            break


    # # GOPRO cam
    # gpCam = GoProCamera.GoPro()
    # cap = cv2.VideoCapture("udp://127.0.0.1:10000")

    # while True:
    #     rval, frame = cap.read()
    #     cv2.imshow("gopro: ", frame)
    #     key = cv2.waitKey(1)
    #     # print "key pressed: " + str(key)
    #     # exit on ESC, you may want to uncomment the print to know which key is ESC for you
    #     if key == 27 or key == 1048603:
    #         break

# ATTRS{ID_FOR_SEAT}=="video4linux-platform-3610000_xhci-usb-0_2_4_1_0", SYMLINK+="gripper_cam"
# ATTRS{ID_FOR_SEAT}=="video4linux-platform-3610000_xhci-usb-0_1_4_1_0", SYMLINK+="butt_cam"
# ATTRS{ID_FOR_SEAT}=="video4linux-platform-3610000_xhci-usb-0_3_2_1_3", SYMLINK+="mast_cam"
# ATTRS{ID_FOR_SEAT}=="video4linux-platform-3610000_xhci-usb-0_2_2_1_1_3", SYMLINK+="arm_cam"




	

