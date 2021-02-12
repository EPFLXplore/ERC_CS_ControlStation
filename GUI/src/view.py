'''
View.py
	@Author: Emile Janho Dit Hreich
'''
import gi
import cv2
import cairo
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
		

		self.capture = cv2.VideoCapture(0)
		self.capture.set(3, 500)
		self.capture.set(4, 340)
		#Glade file setup
		gladeFile = "Main.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladeFile)
		#GUI Layout
		self.NAV = self.builder.get_object("navigationTab")
		self.SCIENCE = self.builder.get_object("scienceTab")

		self.image1 = self.builder.get_object("image1")
		self.image2 = self.builder.get_object("image2")

		self.battery = self.builder.get_object("battery")
		#self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.builder.get_object("compass").get_allocated_width(), self.builder.get_object("compass").get_allocated_height())

	def show_frame(self, *args):

		self.ret, self.frame = self.capture.read()
		self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

		framecp = self.frame.copy()

		pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])

		self.image1.set_from_pixbuf(pb.copy())
		self.image2.set_from_pixbuf(pb.copy())

		return True
