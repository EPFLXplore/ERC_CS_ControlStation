'''
View.py
	@Author: Emile Janho Dit Hreich
'''
import gi
import cv2
import cairo
from model import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
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

		self.controller = controller
		screen = Gdk.Screen.get_default()
		provider = Gtk.CssProvider()
		style_context = Gtk.StyleContext()
		style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		#provider.load_from_data('/src/style.css')
		provider.load_from_path('style.css')
		

		self.capture = cv2.VideoCapture(-1)

		self.capture.set(3, 500)
		self.capture.set(4, 340)		
		################Video capture
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		self.out = cv2.VideoWriter('output.avi', fourcc, 20.0, ( int(self.capture.get(3)), int(self.capture.get(4)))) 
		##############################



		#Glade file setup
		gladeFile = "Main.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladeFile)
		#GUI Layout
		self.NAV = self.builder.get_object("navigationTab")
		self.SCIENCE = self.builder.get_object("scienceTab")
		self.AV = self.builder.get_object("avionicsTab")

		self.image1 = self.builder.get_object("image1")
		self.image2 = self.builder.get_object("image2")
		#Avionics
		self.battery_nav = self.builder.get_object("battery_nav")
		self.battery_sc = self.builder.get_object("battery_sc")
		self.battery_av = self.builder.get_object("battery_sc")
		self.battery_level = self.builder.get_object("battery_level_bar")

		self.temperature_av = self.builder.get_object("temperature_av")

		self.voltage_main_nav = self.builder.get_object("voltage_main_nav")
		self.voltage_main_sc = self.builder.get_object("voltage_main_sc")

		self.current_main_nav = self.builder.get_object("current_main_nav")
		self.current_main_sc = self.builder.get_object("current_main_sc")

		self.pressure_nav = self.builder.get_object("pressure_nav")
		self.pressure_sc = self.builder.get_object("pressure_sc")
		self.pressure_av = self.builder.get_object("pressure_av")

		#HD
		self.controls_hd = self.builder.get_object("controls_hd")
		self.control_mode =self.builder.get_object("kinematics_mode_label")
		

		#NAV
		self.nav_state = self.builder.get_object("nav_state")

		#stopwatch data
		self.seconds_nav = self.builder.get_object("seconds_nav")
		self.minutes_nav = self.builder.get_object("minutes_nav")
		self.hours_nav = self.builder.get_object("hours_nav")
		self.seconds_sc = self.builder.get_object("seconds_sc")
		self.minutes_sc = self.builder.get_object("minutes_sc")
		self.hours_sc = self.builder.get_object("hours_sc")

	def show_frame(self, *args):

		ret, frame = self.capture.read()
		framecp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		
		if(ret == True):
			self.out.write(frame)

		pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])

		self.image1.set_from_pixbuf(pb.copy())
		self.image2.set_from_pixbuf(pb.copy())

		return True

	
	def show_time(self, *args):
		self.seconds_nav.set_text(str(Model.time_array[2]))
		self.minutes_nav.set_text(str(Model.time_array[1]))
		self.hours_nav.set_text(str(Model.time_array[0]))
		self.seconds_sc.set_text(str(Model.time_array[2]))
		self.minutes_sc.set_text(str(Model.time_array[1]))
		self.hours_sc.set_text(str(Model.time_array[0]))
		return True
