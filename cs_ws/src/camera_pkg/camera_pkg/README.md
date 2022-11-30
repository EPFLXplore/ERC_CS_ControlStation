# rover_cameras
This repository contains all scripts to process the feed from cameras and distribute it to the system

# to launch the cameras on the jetsons use the command:
gst-launch-1.0 nvarguscamerasrc sensor-id=4 ! 'video/x-raw(memory:NVMM), width=420, height=360, framerate=15/1' ! nvvidconv flip-method=0 ! 'video/x-raw, width=420, height=360', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink
