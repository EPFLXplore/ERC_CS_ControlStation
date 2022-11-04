#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           Roman Danylovych
#           roman.danylovych@epfl.ch
#
# @brief: This file contains the Model (following the Model View Controller
#         design pattern)
#         Here are created all the methods that perfrom the required computation
#         for various applications
# 
# -------------------------------------------------------------------------------

#================================================================================
# Libraries

from enum import IntEnum
from syslog import LOG_SYSLOG

from .systems import *

import time
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.measure import regionprops, label
from scipy import ndimage
import numpy as np
import cv2 as cv
import os

#================================================================================


class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    WAITING     = 5
    LOGS        = 6 #not really a task. Here just to display exceptions on GUI (it was convenient ;))

# =================================
#              ROVER
# =================================
class Rover:
    '''
        Monitoring of the state of the rover
    '''

    def __init__(self):

        # initialize each subsystem
        self.Nav = Navigation()
        self.HD  = HandlingDevice()
        self.SC  = Science()
        
        # current rover FSM state
        self.__state    = Task.IDLE

        # these two variables are useful in the wait() function of the controller
        # TODO (i think it'd be better to initialise them in the controller)
        self.__inWait   = False
        self.__received = False

        # array of infos on the exceptions thrown (in the form of a String)
        self.__exceptions = []

    #--------State--------

    def setState(self, task):
        self.__state = task

    def getState(self):
        return self.__state

    #--------Received Flag--------

    def setReceived(self, bool):
        self.__received = bool

    def getReceived(self):
        return self.__received

    #--------Waiting Flag--------

    def setInWait(self, bool):
        self.__inWait = bool

    def getInWait(self):
        return self.__inWait
        
    #--------Exception--------

    def addException(self, e):
        self.__exceptions.append(str(e))

    def getExceptions(self):
        return self.__exceptions


class Model:


	run_thread 		= True
	time_array 		=[0,0,0]

	#AVIONICS DATA
	barotemp 		= [-1,-1]
	accelmag 		= [-1, -1, -1, -1, -1, -1, -1, -1, -1] #(x,y,z) -> accel/giro/mag
	adc 			= 0
	#POWER
	voltages 		= [-1,-1,-1,-1]
	currents 		= [-1, -1, -1, -1]
	#NAVIGATION DATA
	waypoint 		= [-1, -1, -1]
	tags 			= []
	signal_AM 		= False
	rover_state 	= 0
	nav_logs 		= ""
	mission_state_d1 = 0
	#current position
	
	#SCIENCE DATA

	#HANDLING DEVICE DATA
	image = []


	#=======================================================================================
	#SCIENCE Analysis functions
	'''
		@Author: Gloria Mellinand (Matlab)
				 Aurelio Noca (Python)
	'''
	'''
		Particle size computation
	'''
	def compute_particle_size(name):
		#change directory
		# os.chdir(SCIENCE_CAPTURE_DIRECTORY)
		# load image
		image_rgb = plt.imread(name)

		# convert image to grayscale
		image_gray = rgb2gray(image_rgb) # values between 0 and 1

		# plt.imshow(image_gray)
		# print(image_gray)

		# definition of saturation
		Ibinary = image_gray > 150/255 # try different values for your problem, 
		# plt.imshow(Ibinary)

		# fill holes
		Ibinary = ndimage.binary_fill_holes(Ibinary).astype(int)
		# plt.imshow(Ibinary)

		# get labeled image and number of blobs
		# labeled image is made of integers, where each integer corresponds to one blob
		# https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.label
		labeledImage, numberOfBlobs = label(Ibinary, return_num=True)
		# plt.imshow(labeledImage)

		# 
		# https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops
		blobMeasurements = regionprops(labeledImage)

		C = 0.008; # Conversion factor m/pixel. 

		equivDiameter = []
		for item in blobMeasurements:
			if item.equivalent_diameter > 10:
				equivDiameter.append(item.equivalent_diameter*C)

		# plt.imshow(labels_im)
		plt.hist(equivDiameter)


		#plt.imshow(labels_im)
		plt.show()

	'''
	Particle volume computation
	'''
	def compute_particle_volume(name):
		# os.chdir(SCIENCE_CAPTURE_DIRECTORY)
		img = cv.imread(name)
		gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # between 0 and 255
		# print(gray)
		# gray = (gray>120)*255.0
		gray = (gray>120)

		# print(gray)

		# # fill holes
		Ibinary = np.uint8(ndimage.binary_fill_holes(gray))*255
		# # plt.imshow(Ibinary, , cmap="gray")

		# print(Ibinary)

		edges = cv.Canny(Ibinary,0,255,apertureSize = 3)

		average=0
		lines = cv.HoughLinesP(edges,1,np.pi/360,98,minLineLength=7,maxLineGap=5)
		for line in lines:
			x1,y1,x2,y2 = line[0]
			average+= (y1+y2)/2.0

		print(average/len(lines))

	'''
	Mean color Computation
	'''
	def compute_mean_color(name):
		# os.chdir(SCIENCE_CAPTURE_DIRECTORY)
		A = cv.imread(name)
		size_image = A.shape
		R = A[:, :, 0]
		G = A[:, :, 0]
		B = A[:, :, 0]

		black_index = 0
		maxy = size_image[0]
		maxx = size_image[1]

		increment = [0, 0, 0]

		for x in range(maxx):
			for y in range(maxy):
				color_vector = np.array([R(y, x), G(y, x), B(y, x)], dtype=np.int)
				color_vector_float = np.array(color_vector, dtype=np.float)
				if (color_vector[0] <= 60 & color_vector[1] <= 60 & color_vector[2] < 60):
					black_index += 1
				else:
					increment = increment + color_vector_float

		mean = increment / (maxx*maxy - black_index)
		print(round(mean))


	#=======================================================================================
			
	def get_time():
		s=0
		m=0
		h=0
		while s<=60:	
			time.sleep(1)
			s+=1
			if s==60:
				m+=1
				s=0
				if (m == 60):
					h += 1
					m = 0
			Model.time_array[0] = h
			Model.time_array[1] = m
			Model.time_array[2] = s
			if (Model.run_thread == False):
				break