import cv2
import multiprocessing as mp



def show_cam_top():
	capture = cv2.VideoCapture('rtsp://xplore1:xplore@192.168.1.50:554/s1')
	capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)
	while 1:
		ret, frame = capture.read()
		ims = cv2.resize(frame, (640, 360))
		#ims = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)
		cv2.imshow('top', ims)
		cv2.waitKey(1)



def show_cam_butt():
	capture2 = cv2.VideoCapture('rtsp://xplore1:xplore@192.168.1.51:554/s1')
	while 1:
		ret, frame = capture2.read()
		ims = cv2.resize(frame, (640, 360))
		#ims = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)
		cv2.imshow('butt', ims)
		cv2.waitKey(1)

cam1 = mp.Process(target=show_cam_top)
cam2 = mp.Process(target=show_cam_butt)

cam1.start()
cam2.start()




