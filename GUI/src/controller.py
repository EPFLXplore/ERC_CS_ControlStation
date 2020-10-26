import gi
import cv2
import sys


from model import Model 
from view import View 

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf


class App(Gtk.Application):

  def __init__(self):

    Gtk.Application.__init__(self)
    self.model = Model()
    self.view = View(self)


  def do_startup(self):
    Gtk.Application.do_startup(self)
    
    
    self.view.window.connect("delete-event", self.on_quit)
    
    GLib.idle_add(self.view.show_frame)
    

  def do_activate(self):
    self.view.window.set_application(app)
    self.view.window.present()

  def on_quit(self, action, param):

    self.quit()



app = App()
app.run(sys.argv)






