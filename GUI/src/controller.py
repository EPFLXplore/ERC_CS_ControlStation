import gi
import cv2
import sys
import cairo

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
    self.view.builder.connect_signals(Controller())
    GLib.idle_add(self.view.show_frame)


  def do_activate(self):
    self.view.window.set_application(app)
    self.view.window2.set_application(app)
    self.view.window.present()

  def on_quit(self, action, param):

    self.quit()


class Controller():

    def __init__(self):
        self.rotation = 0.0

    def on_NAV_clicked(self, *args):

      app.view.window.present()
      App.get_active_window(app).hide()

    def on_HD_clicked(self, *args):

      app.view.window3.present()
      App.get_active_window(app).hide()

    def on_SCIENCE_clicked(self, *args):

      app.view.window2.present()
      App.get_active_window(app).hide()

    def on_SWITCH_clicked(self, *args):
      self.rotation += 0.05
      app.view.builder.get_object("compass").queue_draw()
      app.view.battery.set_text("1.00")


    def draw_compass(self, widget, ctx):

         ctx.set_line_width(3)
         ctx.set_source_rgb(0.0,1.0,0.1)
         ctx.move_to(90, 78)
         ctx.rotate(self.rotation)
         ctx.rel_line_to(0, -65)
         ctx.stroke()





app = App()
app.run(sys.argv)
