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
		fourcc = cv2.VideoWriter_fourcc('m','p','4','v') 
		self.out = cv2.VideoWriter('output.avi', fourcc, 24.0, (500, 340)) 
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
		self.details_button = self.builder.get_object("avionics_details")
		self.details_pop_sc = self.builder.get_object("details_pop_sc")
		self.details_pop = self.builder.get_object("av_details")
		self.battery = self.builder.get_object("battery")

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

		self.ret, self.frame = self.capture.read()
		self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
		hs2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
		self.out.write(hs2)

		framecp = self.frame.copy()

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
