import cv2
from imutils.video import FPS

capture = cv2.VideoCapture("v4l2src device=/dev/video0 ! video /x-raw,framerate=30/1,width=640,height=480 ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
fps.start()

if (not capture.isOpened()) {
    print("Video capture failed to open !\n")
    quit()
}
frame = capture.read()

stream = cv2.VideoOutput("appsrc ! queue !  videoconvert ! video/x-raw ! x264enc tune=zerolatency ! h264parse ! rtph264pay ! udpsink host=localhost port=1234 sync=true", cv2.CAP_GSTREAMER, 0, 30, frame.size(), true)

frameNo = 0
while capture.isOpened() {
    ret_val, img = capture.read()
    cv2.imshow('Camera Feed Frame #'.format(frameNo), img)
    fps.update()

    stream.write(img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frameNo += 1
}

fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
capture.release()
cv2.destroyAllWindows()

