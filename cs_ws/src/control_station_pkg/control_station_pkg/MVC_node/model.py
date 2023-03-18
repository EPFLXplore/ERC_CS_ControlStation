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

from .models import *

import time
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.measure import regionprops, label
from scipy import ndimage
import numpy as np
import cv2 as cv
import os

#================================================================================




class Model:

	userIDs = []

	run_thread 		= True		#c'est quoi ?
	time_array 		=[0,0,0]

	#AVIONICS DATA				#encore utilisé ?
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


	#comment modeliser les utilisateurs actuellement co ?


	

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