'''
View.py
	@Author: Emile Hreich
'''
import gi
import cv2
import multiprocessing as mp
from model 		   import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import numpy as np
import cv2 as cv
import os
from utils import *
#=========================================================

NAV_CAMERA_1_ADDRESS 	  = "rtsp://xplore1:xplore@192.168.1.50:554/s1"
NAV_CAMERA_2_ADDRESS 	  = "rtsp://xplore1:xplore@192.168.1.51:554/s1"
SCIENCE_CAMERA_ADDRESS 	  = "rtsp://root:Plokmijn123!@192.168.1.57/axis-media/media.amp"
# NAV_CAPTURE_DIRECTORY 	  = ""
# SCIENCE_CAPTURE_DIRECTORY = ""#to be determined on the raspberry
#=========================================================

'''
View Class


	@Attributes
		controller -> Controller
		capture
		builder

'''
class View:

	#Constructor
	def __init__(self, controller):

		self.controller 			= controller
		screen 						= Gdk.Screen.get_default()
		provider 					= Gtk.CssProvider()
		style_context 				= Gtk.StyleContext()
		style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		#provider.load_from_data('/src/style.css')
		provider.load_from_path('style.css')

		#==================================================================================
		#streams processes
		self.parent_conn_1, self.child_conn_1 = mp.Pipe()#NAV CAM 1
		self.parent_conn_2, self.child_conn_2 = mp.Pipe()#NAV CAM 2
		self.parent_conn_3, self.child_conn_3 = mp.Pipe()#SC  CAM

		self.camera_process_1 = mp.Process(target=self.get_frame_1, args=(self.child_conn_1,))
		self.camera_process_2 = mp.Process(target=self.get_frame_2, args=(self.child_conn_2,))
		self.camera_process_3 = mp.Process(target=self.get_frame_3, args=(self.child_conn_3,))

		self.frame_1 = 0
		self.frame_2 = 0
		self.frame_3 = 0
		#==================================================================================


		#Video capture
		# fourcc 						= cv2.VideoWriter_fourcc(*'XVID')
		# self.out 					= cv2.VideoWriter('output.avi', 
		# 											  fourcc, 20.0,
		# 											(int(self.capture.get(3)), 
		# 											int(self.capture.get(4)))
		# 											) 
		
		#===================================================================================
		#Glade file setup
		gladeFile 					= "Main.glade"
		self.builder 				= Gtk.Builder()
		self.builder.add_from_file(gladeFile)
		#===================================================================================
		#GUI Layout
		self.NAV 					= self.builder.get_object("navigationTab")
		self.SCIENCE 				= self.builder.get_object("scienceTab")
		self.AV 					= self.builder.get_object("avionicsTab")
		self.image1 				= self.builder.get_object("image1")
		self.image2 				= self.builder.get_object("image1")
		self.image3 				= self.builder.get_object("image3")
		#===================================================================================
		#Avionics
		self.battery_nav 			= self.builder.get_object("battery_nav")
		self.battery_sc 			= self.builder.get_object("battery_sc")
		self.battery_av 			= self.builder.get_object("battery_sc")
		self.battery_level 			= self.builder.get_object("battery_level_bar")
		self.temperature_av	 		= self.builder.get_object("temperature_av")
		self.voltage_main_nav 		= self.builder.get_object("voltage_main_nav")
		self.voltage_main_sc 		= self.builder.get_object("voltage_main_sc")
		self.current_main_nav 		= self.builder.get_object("current_main_nav")
		self.current_main_sc 		= self.builder.get_object("current_main_sc")
		self.pressure_nav 			= self.builder.get_object("pressure_nav")
		self.pressure_sc 			= self.builder.get_object("pressure_sc")
		self.pressure_av 			= self.builder.get_object("pressure_av")
		#===================================================================================
		#HD
		self.controls_hd 			= self.builder.get_object("controls_hd")
		self.control_mode 			= self.builder.get_object("kinematics_mode_label")
		#===================================================================================
		#NAV
		self.nav_state 				= self.builder.get_object("nav_state")
		self.ok_icon 				= self.builder.get_object("ok_icon_nav")
		self.warning_icon 			= self.builder.get_object("warning_icon_nav")
		self.error_icon 			= self.builder.get_object("error_icon_nav")
		self.cam1 					= self.builder.get_object("CAMERA1")
		#===================================================================================
		#stopwatch data
		self.seconds_nav 			= self.builder.get_object("seconds_nav")
		self.minutes_nav 			= self.builder.get_object("minutes_nav")
		self.hours_nav 				= self.builder.get_object("hours_nav")
		self.seconds_sc 			= self.builder.get_object("seconds_sc")
		self.minutes_sc 			= self.builder.get_object("minutes_sc")
		self.hours_sc 				= self.builder.get_object("hours_sc")
		self.sc_state 				= self.builder.get_object("sc_state")
		#===================================================================================
		#SCIENCE
		file = np.load("weights.npz")
		self.mtx = file["arr_0"]
		self.dist = file["arr_1"]
		#===================================================================================

		


	def show(self, *args, show_flag, sc_flag):
		framecp = self.parent_conn_1.recv()
		framecp2 = self.parent_conn_2.recv()
		framecp3 = self.parent_conn_3.recv()
		#unconditional
		pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])
		self.image1.set_from_pixbuf(pb.copy())
		if(show_flag):
			pb2=GdkPixbuf.Pixbuf.new_from_data(framecp2.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp2.shape[1], framecp2.shape[0], framecp2.shape[2]*framecp2.shape[1])
			self.image2.set_from_pixbuf(pb2.copy())
		if(sc_flag):
			pb3=GdkPixbuf.Pixbuf.new_from_data(framecp3.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp3.shape[1], framecp3.shape[0], framecp3.shape[2]*framecp3.shape[1])
			self.image3.set_from_pixbuf(pb3.copy())
		else:
			try:
				self.image3.set_from_file(self.controller.tube_filename)
			except:
				print("No such file in directory")

		return True

	#NAV_CAM_1
	def get_frame_1(self, conn):

		capture = cv2.VideoCapture(NAV_CAMERA_1_ADDRESS)
		while True:
			ret, self.frame_1 = capture.read()
			ims = cv2.resize(self.frame_1, (640, 360))
			framecp = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)
			
			# if(ret == True):
			# 	self.out.write(self.frame)
			conn.send(framecp)

	#NAV_CAM_2
	def get_frame_2(self, conn):

		capture2 = cv2.VideoCapture(NAV_CAMERA_2_ADDRESS)

		while True:

			ret2, self.frame_2 = capture2.read()
			ims2 		 = cv2.resize(self.frame_2, (640, 360))
			framecp2 	 = cv2.cvtColor(ims2, cv2.COLOR_BGR2RGB)
			conn.send(framecp2)

	#SCIENCE CAM UNDISTORTED		
	def get_frame_3(self, conn):
		capture = cv2.VideoCapture(SCIENCE_CAMERA_ADDRESS)
		while True:
			ret, self.frame_3 = capture.read()
			ims = cv2.resize(self.frame_3, (640, 360))
			framecp = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)
			#undistortion
			#img = cv.imread('img1.jpg')
			h,  w = framecp.shape[:2]
			newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.mtx, self.dist, (w,h), 1, (w,h))

			dst = cv.undistort(framecp, self.mtx, self.dist, None, newcameramtx)
			print("jaj-")
			# crop the image
			x, y, w, h = roi
			dst = dst[y:y+h, x:x+w]
			# if(ret == True):
			# 	self.out.write(self.frame)
			conn.send(dst)		

	#HANDLING DEVICE CAMERA
	def show_handling_device_cam(self, show_flag):
		if(len(Model.image) != 0 and not show_flag):
			ims2 = cv2.resize(Model.image, (640, 360))
			framecp2 = cv2.cvtColor(ims2, cv2.COLOR_BGR2RGB)
			pb = GdkPixbuf.Pixbuf.new_from_data(framecp2.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp2.shape[1], framecp2.shape[0], framecp2.shape[2]*framecp2.shape[1])
			self.image2.set_from_pixbuf(pb.copy())
		return True
	

	#NAVIGATION CAMERA CAPTURE
	def capture_image_nav(self, index):
		
		os.chdir(NAV_CAPTURE_DIRECTORY)#fill the NAV_CAPTURE_DIRECTORY BEFORE USE
		name_format_1="nav_bottom_capture%d.jpeg" % (index)
		name_format_2="nav_top_capture%d.jpeg" % (index)
		cv2.imwrite(name_format_1, self.frame_1)
		cv2.imwrite(name_format_2, self.frame_2)

	#SCIENCE CAMERA CAPTURE
	def capture_image_sc(self, index):
		
		os.chdir(SCIENCE_CAPTURE_DIRECTORY)
		name_format="tube_%d.png" % (index)
		cv2.imwrite(name_format, self.frame_3) 	
	
	def show_time(self, *args):
		seconds ='{:02d}'.format(Model.time_array[2])
		minutes ='{:02d}'.format(Model.time_array[1]) 
		hours = '{:02d}'.format(Model.time_array[0])

		self.seconds_nav.set_text(seconds)
		self.minutes_nav.set_text(minutes)
		self.hours_nav.set_text(hours)
		self.seconds_sc.set_text(seconds)
		self.minutes_sc.set_text(minutes)
		self.hours_sc.set_text(hours)
		return True

	def display_avionics(self, *args):
		pressure = round(Model.barotemp[0],2)
		temperature = round(Model.barotemp[1], 2)
		self.pressure_nav.set_text(str(pressure))
		self.pressure_av.set_text(str(pressure))
		self.pressure_sc.set_text(str(pressure))
		self.temperature_av.set_text(str(temperature))
		#TODO
		return True
		

	def display_navigation(self, *args):
		pass

	def display_science(self, *args):
		pass

	def display_handling_device(self, *args):
		pass
