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

import numpy as np 

import time
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.measure import regionprops, label
from scipy import ndimage
import numpy as np
import cv2 as cv
# from utils import *
import os

#================================================================================


NBR_BUTTONS = 14
ELEMENT_DATA_SIZE = 6


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


# =================================
#            NAVIGATION
# =================================
class Navigation:
    '''
        Monitoring of the navigation Data
    '''
    def __init__(self):
        # next Navigation goal ID
        self.__nextId = 0

        # keep track of goals
        #self.__goals = np.array([])
        
        # [x,y, yaw]
        self.__goal = np.zeros(3)

        # rover position
        self.__pos = np.zeros(3)
        # rover yaw
        self.__yaw = 0
        # rover linear velocity
        self.__linVel = np.zeros(3)
        # rover angular velocity
        self.__angVel = np.zeros(3)

    '''def addGoal(self, arr):
        if(len(arr) != 3): raise Exception("array length must be 3 -> (x,y,z)")

        np.append(self.__goals, arr)
        self.incrementId()
    '''
    # ---------GOAL----------
    def setGoal(self, arr):
        self.__goal[0] = arr[0]
        self.__goal[1] = arr[1]
        self.__goal[2] = arr[2]

    def cancelGoal(self):
        self.__goal = np.zeros(3)

    # increase id number by 1 (should be used when defining a new goal in order to assign it a new id)
    def incrementId(self):
        self.__nextId += 1

    def getId(self):
        return self.__nextId

    '''def getGoal(self, id):
        return self.__goals[id]
    '''

    def getGoal(self):
        return self.__goal


    #--------Orientation--------
    def setYaw(self, val):
        self.__yaw = val

    def getYaw(self):
        return self.__yaw

    '''def cancelGoal(self, id):
        len = len(self.__goals)
        if (id < 0 or id > len): raise ValueError("Invalid navigation goal id")
        np.delete(self.__goals, id, 0)'''
    

    # ========= TWIST DATA =========

    #--------Rover Position--------
    def setPos(self, arr):
        self.__pos = arr

    def getPos(self):
        return self.__pos

    #--------Rover Linear Velocity--------
    def setLinVel(self, arr):
        self.__linVel = arr

    def getLinVel(self):
        #return self.__linVel
        return np.linalg.norm(self.__linVel)

    #--------Rover Angular Velocity--------
    def setAngVel(self, arr):
        self.__angVel = arr

    def getAngVel(self):
        #return self.__angVel
        return np.linalg.norm(self.__angVel)
    

    #----------Distance to Goal----------
    def distToGoal(self):
        pos = self.getPos()
        diff = np.array([self.getGoal()[0], self.getGoal()[1]]) - np.array([pos[0], pos[1]])
        return np.linalg.norm(diff)


# ==================================
#              SCIENCE 
# ==================================
class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):
        # humidity of the specific tube
        self.__tubeHum = -1
        
        # parameters (11 elements):
        #   - disc position
        #   - whether tubes 0 to 2 are closed
        #   - whether tubes 0 to 2 are empty
        #   - whether trap is closed
        #   - mass of each tube
        self.__params = []

        # smthg to do with the picture analysis of images from the science bay
        # unfortunately it wasn't implemented this year
        self.__volumes = [0,0,0]
        self.__colors = [0,0,0]
        self.__particleSizes = [0,0,0]
        self.__densities = [0,0,0]

        self.__images = []

        # array of infos coming from the SC (in the form of Strings)
        self.__info = []

        # variable to know what operation we'd like to execute on which tube: [op, tube]
        # operations: 10 = sampling, 20 = rotation to camera, 30 = mass measurement
        self.__op_tube = np.zeros(2)
        # command we'd like the science bay to execute (in the case of a tube-specific operation: op + tube)
        self.__cmd = -1

    #--------SC Mass--------

    def setSCMass(self, mass):
        self.__masses[self.__op_tube[1]] = mass
    
    def getSCMass(self, idx):
        if(idx < 0 or 2 < idx): raise ValueError("impossible tube number chosen (can be either 0, 1 or 2)")
        return self.__sc_mass[idx]

    def getMasses(self):
        return self.__masses

    #--------Tube Humidity--------

    def setTubeHum(self, val):
        self.__tubeHum = val

    def getTubeHum(self):
        return self.__tubeHum

    #--------SC Operation--------

    def setOperation(self, op):
        self.__op_tube[0] = op
        self.setTubeCmd()

    def getOperation(self):
        return self.__op_tube[0]

    #--------Tube--------

    def selectTube(self, t):
        self.__op_tube[1] = t
        self.setTubeCmd()

    def getSelectedTube(self):
        return self.__op_tube[1]

    #--------Specific Tube Command--------

    def setTubeCmd(self):
        arr = self.__op_tube
        self.setCmd(arr[0] + arr[1])
    
    #--------Command--------

    def setCmd(self, cmd):
        self.__cmd = cmd

    def getCmd(self):
        return self.__cmd

    #--------Opened tubes--------

    def setTubeState(self, idx, val):
        self.__tubes_closed[idx] = bool(val)

    def getTubesState(self):
        return self.__tubes_closed

    #--------Densities--------
    def setDensity(self, idx, val):
        self.__densities[idx] = val

    def getDensities(self):
        return self.__densities

    #--------Volumes--------

    def setVolume(self, idx, val):
        self.__volumes[idx] = val

    def getVolumes(self):
        return self.__volumes
        
    #--------Trap--------

    def setTrapState(self, val):
        self.__trap_closed= bool(val)

    def getTrapState(self):
        return self.__trap_closed

    #--------Particle Size--------

    def setParticleSize(self, idx, val):
        self.__particleSizes[idx] = val

    def getParticleSizes(self):
        return self.__particleSizes

    #--------Filled--------

    def setTubeEmpty(self, idx, val):
        self.__empty[idx] = val

    def areEmpty(self):
        return self.__empty

    #--------Colors--------

    def setColor(self, idx, val):
        self.__colors[idx] = val

    def getColors(self):
        return self.__colors

    #--------INFO--------

    def addInfo(self, txt):
        self.__info.append(txt)

    def getInfos(self):
        return self.__info

    #--------STATE--------
    def setState(self, txt):
        self.__state = txt

    def getState(self):
        return self.__state

    #--------PARAMS#--------

    def setParams(self, arr): 
        self.__params = arr
    def getParams(self): 
        return self.__params

    #--------DESERIALIZATION--------
    def deSerializeState(self, save_list):
        '''
        Undo the serialization of serializeState and save the variables.
        Input: save_list (list of int) list to be deserialized
        Output: None
        '''

        #cast to ints
        #save_list = map(int,save_list)

        #desrializing
        #self.disc_position = save_list[0]

        '''self.__tubes_closed = map(bool,save_list[1:4])
        self.__empty = map(bool,save_list[4:7])
        self.__trap_closed = bool(save_list[7])
        self.__masses = save_list[8:] ''' # TODO il me semble que ça renvoit 4 nombres et pas 3
        self.__tubes_closed = np.array(save_list[1:4]).astype(bool).tolist()
        self.__empty = np.array(save_list[4:7]).astype(bool).tolist()
        self.__trap_closed = np.array(save_list[7]).astype(bool).tolist()
        self.__masses = save_list[8:]


    #--------IMAGE--------
    def addImage(self, im):
        self.__images.append(im)

    def getImages(self):
        return self.__images


# ==================================
#          HANDLING DEVICE 
# ==================================
class HandlingDevice:
    '''
        Monitoring Handling Device Data
    '''
    def __init__(self):
        # HD mode: Inverse, Direct, Debug TODO
        self.__hd_mode = -1

        # id of element we'd like to manipulate (inverse autonomous)
        self.__elemId = -1
        # ToF (time of flight)
        self.__distToElem = 0

        # the 6 joints + gripper
        self.__joint_positions = [0,0,0,0,0,0,0]
        self.__joint_velocities = [0,0,0,0,0,0,0]

        # matrix containing info on the movements each joint must do in order to reach an element
        # [x,y,z,a,b,c] (3 translations and 3 rotations)
        self.__elements = np.zeros((NBR_BUTTONS, ELEMENT_DATA_SIZE)) # 14x6 matrix

    #--------HD mode--------

    def setHDMode(self, mode):
        if(mode < 0 or mode > 3): raise ValueError("Invalid mode")
        self.__hd_mode = mode

    def getHDMode(self):
        return self.__hd_mode

    #--------ROS telemetry--------

    def set_joint_telemetry(self, telemetry):
        self.set_joint_positions(telemetry.position)
        self.set_joint_velocities(telemetry.velocity)
        #self.rover.HD_telemetry_pub.publish(telemetry)

    #--------Joint Positions--------

    def set_joint_positions(self, positions):
        self.__joint_positions = positions

    def get_joint_positions(self):
        return self.__joint_positions

    #--------Joint Velocities--------

    def set_joint_velocities(self, velocities):
        self.__joint_velocities = velocities

    def get_joint_velocities(self):
        return self.__joint_velocities

    #--------Velocity--------

    def getVelNorm(self):
        return np.linalg.norm(self.get_joint_velocities)

    #--------ID--------
    
    def setElemId(self, id):
        self.__elemId = id

    def getElemId(self):
        return self.__elemId

    #--------ToF--------

    def set_tof(self, tof):
        self.__distToElem = tof

    def get_tof(self):
        return self.__distToElem

    #--------Detected Elements--------
    
    def setDetectedElement(self, arr):
        data = np.zeros(ELEMENT_DATA_SIZE)
        for i in range(6):
            data[i] = arr[i+1]
        self.__elements[arr[0]-1] = data  # arr[0]-1 because ids are numbered 1 to 14 and array is indexed 0 to 13

    def getElements(self):
        return self.__elements


# TASK: 
#       - Manual      = 1 
#       - Navigation  = 2 
#       - Maintenance = 3
#       - Science     = 4
#
# INSTR:  
#       - Launch = 1 
#       - Abort  = 2 
#       - Wait   = 3 
#       - Resume = 4 
#       - Retry  = 5 (HD and SC specific)
def checkArgs(task, instr):

    if (task < 1 or task > 4): raise ValueError("inexistent task")
    if (instr < 1 or instr > 6): raise ValueError("inexistent instruction")

    if(instr == 5):
        if(task != 3 and task != 4): raise ValueError("This task can't run Retry")


# ==================================
#        SC - PICTURE ANALYSIS 
# ==================================
# code to run picture analysis on images from the science bay, but I never used it and don't know how it works ;)
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