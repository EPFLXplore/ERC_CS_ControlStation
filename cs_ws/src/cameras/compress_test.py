import numpy as np
import cv2
from imutils.video import FPS

stream = cv2.VideoCapture('filesrc location=testVid.avi ! qtdemux ! queue ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw,format=BGRx ! queue ! videoconvert ! queue ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER)
fps = FPS().start()

while stream.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive stream. Exiting...")
        break

    cv2.imshow('Test Local Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

fps.stop()
stream.release()
cv2.destroyAllWindows()
