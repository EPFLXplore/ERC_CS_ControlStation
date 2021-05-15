'''
View.py
	@Author: Emile Janho Dit Hreich
'''
import gi
import cv2

from model 		   import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

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
		
		

		self.capture = cv2.VideoCapture("rtsp://xplore1:xplore@192.168.1.50:554/s1")
		self.capture2 = cv2.VideoCapture("rtsp://root:Plokmijn123!@192.168.1.57/axis-media/media.amp")
		self.frame = 0

		#Video capture
		fourcc 						= cv2.VideoWriter_fourcc(*'XVID')
		self.out 					= cv2.VideoWriter('output.avi', 
													  fourcc, 20.0,
													(int(self.capture.get(3)), 
													int(self.capture.get(4)))
													) 
		
		#Glade file setup
		gladeFile 					= "Main.glade"
		self.builder 				= Gtk.Builder()
		self.builder.add_from_file(gladeFile)
		#GUI Layout
		self.NAV 					= self.builder.get_object("navigationTab")
		self.SCIENCE 				= self.builder.get_object("scienceTab")
		self.AV 					= self.builder.get_object("avionicsTab")
		self.image1 				= self.builder.get_object("image1")
		self.image3 				= self.builder.get_object("image3")
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
		#HD
		self.controls_hd 			= self.builder.get_object("controls_hd")
		self.control_mode 			= self.builder.get_object("kinematics_mode_label")
		#NAV
		self.nav_state 				= self.builder.get_object("nav_state")
		#stopwatch data
		self.seconds_nav 			= self.builder.get_object("seconds_nav")
		self.minutes_nav 			= self.builder.get_object("minutes_nav")
		self.hours_nav 				= self.builder.get_object("hours_nav")
		self.seconds_sc 			= self.builder.get_object("seconds_sc")
		self.minutes_sc 			= self.builder.get_object("minutes_sc")
		self.hours_sc 				= self.builder.get_object("hours_sc")

	def show_frame(self,*args):

		#ret, self.frame = self.capture.read()
		ret2, frame2 = self.capture2.read()
		ims2 		 = cv2.resize(frame2, (640, 360))
		framecp2 	 = cv2.cvtColor(ims2, cv2.COLOR_BGR2RGB)

		#ims = cv2.resize(self.frame, (640, 360))
		#framecp = cv2.cvtColor(ims, cv2.COLOR_BGR2RGB)
		
		#if(ret == True):
			#self.out.write(self.frame)

		#pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])
		pb2=GdkPixbuf.Pixbuf.new_from_data(framecp2.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp2.shape[1], framecp2.shape[0], framecp2.shape[2]*framecp2.shape[1])

		#self.image1.set_from_pixbuf(pb.copy())
		self.image3.set_from_pixbuf(pb2.copy())
		


		return True

	def capture_image(self, index):
		name_format="nav_camera_capture%d.jpeg" % (index)
		print(name_format)
		cv2.imwrite(name_format, self.frame) 
		
	
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
		pressure = '{:05d}'.format(Model.barotemp[0])
		temperature = '{:05d}'.format(Model.barotemp[1])
		self.pressure_nav.set_text(str(pressure))
		self.pressure_av.set_text(str(pressure))
		self.pressure_sc.set_text(str(pressure))
		self.temperature_av.set_text(str(temperature))
		#TODO
		
		
		
		

	def display_navigation(self, *args):
		pass

	def display_science(self, *args):
		pass

	def display_handling_device(self, *args):
		pass
