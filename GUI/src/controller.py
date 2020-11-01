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
    self.view.window2.connect("delete-event", self.on_quit)
    self.view.window3.connect("delete-event", self.on_quit)
    self.view.builder.connect_signals(Controller())
    GLib.idle_add(self.view.show_frame)
    

  def do_activate(self):
    self.view.window.set_application(app)
    self.view.window2.set_application(app)
    self.view.window3.set_application(app)
    self.view.window.present()

  def on_quit(self, action, param):

    self.quit()


class Controller():

  def on_NAV_clicked(self, *args):
    
    app.view.window.present()
    App.get_active_window(app).hide()

  def on_HD_clicked(self, *args):

    app.view.window3.present()
    App.get_active_window(app).hide()

  def on_SCIENCE_clicked(self, *args):
    
    app.view.window2.present()
    App.get_active_window(app).hide()





app = App()
app.run(sys.argv)






