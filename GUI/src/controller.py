import gi
import cv2
import sys
from threading import Thread
import evdev
from evdev import*

from model import Model 
from view import View 

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf


class App(Gtk.Application):

  def __init__(self):

    Gtk.Application.__init__(self)
    self.model = Model()
    self.view = View(self)
    GLib.idle_add(self.view.show_frame)
    
    


  def do_startup(self):
    Gtk.Application.do_startup(self)
    self.controller = Controller()
    
    self.view.window.connect("delete-event", self.on_quit)
    self.view.window2.connect("delete-event", self.on_quit)
    self.view.window3.connect("delete-event", self.on_quit)
    self.view.builder.connect_signals(self.controller)
    GLib.idle_add(self.view.show_frame)
    

  def do_activate(self):
    self.view.window.set_application(app)
    self.view.window2.set_application(app)
    self.view.window3.set_application(app)
    self.view.window.present()

  def on_quit(self, action, param):

    self.quit()


class Controller():
  def __init__(self):
    self.gamepad = Gamepad()
    self.gamepad.cmode('NAV')
    self.t_game = Thread(target = self.gamepad.run, daemon =True) 
    self.t_game.start()
    
    
  	
  def on_NAV_clicked(self, *args):
    
    app.view.window.present()
    App.get_active_window(app).hide()
    self.gamepad.cmode('NAV')

  def on_HD_clicked(self, *args):

    app.view.window3.present()
    App.get_active_window(app).hide()
    
    self.gamepad.cmode('HD')

  def on_SCIENCE_clicked(self, *args):
    
    app.view.window2.present()
    App.get_active_window(app).hide()
    self.gamepad.cmode('SC')
    

class Gamepad(Thread):


  def __init__(self):
  # ~ connect gamepad
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      if evdev.ecodes.EV_FF in self.control.capabilities():
        break
    else:
      sys.stderr.write('Failed to find the haptic motor.\n')
      sys.exit(1)
    self._running = True
    self.axe_HD=[0, 0, 0, 0, 0, 0, 0]
    self.axe_NAV=[0., 0.]

    
  def run (self):
    dec = Decode_manette()
    for event in self.control.read_loop():
      if event.type!=0:
        if (self._running)==0:
          break
        #Mode commun Changement Mode etc...
        if event.type == ecodes.EV_KEY:
            if event.value==1:
              if event.code==dec.shaBtn: #Touche A
                if self.mode == 'NAV':
                  app.controller.on_HD_clicked()
                elif self.mode == 'HD':
                  app.controller.on_SCIENCE_clicked()
                elif self.mode == 'SC':
                  app.controller.on_NAV_clicked()
                
        if (self.mode)== 'NAV':
          if event.type == ecodes.EV_KEY:
            # ~ print(categorize(event))
            if event.value==1:
              if event.code==dec.xBtn: #Touche A
                  print('NAV')
          elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            # ~ print (ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
              self.axe_NAV[0] = absevent.event.value/32768
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
              self.axe_NAV[1] = absevent.event.value/32768
          print(self.axe_NAV)
          
        elif (self.mode)== 'HD':
          if event.type == ecodes.EV_KEY:
            # ~ print(categorize(event))
            if event.value==1:
              if event.code==dec.l1Btn and self.axe_HD[4]==0: #Touche l1 axe 5
                self.axe_HD[4]=1
              elif event.code==dec.r1Btn and self.axe_HD[4]==0: #Touche r1 axe 5
                self.axe_HD[4]=-1
              elif event.code==dec.l2Btn and self.axe_HD[5]==0: #Touche l1 axe 6
                self.axe_HD[5]=1
              elif event.code==dec.r2Btn and self.axe_HD[5]==0: #Touche r1 axe 6
                self.axe_HD[5]=-1
              elif event.code==dec.cBtn and self.axe_HD[6]==0: #Touche r1 axe 6
                self.axe_HD[6]=1
              elif event.code==dec.tBtn and self.axe_HD[6]==0: #Touche r1 axe 6
                self.axe_HD[6]=-1
            elif event.value==0:
              if event.code==dec.l1Btn: #Touche l1 axe 5
                self.axe_HD[4]=0
              elif event.code==dec.r1Btn: #Touche r1 axe 5
                self.axe_HD[4]=0
              elif event.code==dec.l2Btn: #Touche l1 axe 6
                self.axe_HD[5]=0
              elif event.code==dec.r2Btn: #Touche r1 axe 6
                self.axe_HD[5]=0
              elif event.code==dec.cBtn: #Touche r1 pince
                self.axe_HD[6]=0
              elif event.code==dec.tBtn : #Touche r1 pince
                self.axe_HD[6]=0
          elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            # ~ print (ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
              self.axe_HD[0] = eval_axe(absevent.event.value)
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
              self.axe_HD[1] = eval_axe(absevent.event.value)
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
              self.axe_HD[2] = eval_axe(absevent.event.value)
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
              self.axe_HD[3] = eval_axe(absevent.event.value)
          print(self.axe_HD)
            
        elif (self.mode)== 'SC':
          if event.type == ecodes.EV_KEY:
            # ~ print(categorize(event))
            if event.value==1:
              if event.code==304: #Touche A
                  print('SC')
      

  def cmode(self, mode): 
    self.mode = mode
    
def eval_axe(axe_value):
  # ~ print(axe_value, 'ACE')
  value=0
  if axe_value <= -32000:
    # ~ print('-1 Evalluation')
    value = -1
    return value
  elif axe_value >= 32000:
    # ~ print('1 Evalluation')
    value = 1
    return value
  elif axe_value > -32000 and axe_value < 32000:
    return value


class Decode_manette():
  def __init__(self):
    self.xBtn = 304
    self.oBtn = 305
    self.tBtn = 307
    self.cBtn = 308
    self.l1Btn = 310
    self.r1Btn = 311
    self.l2Btn = 312
    self.r2Btn = 313
    self.optBtn = 315
    self.shaBtn = 314
    self.psBtn = 316
    self.l3Btn = 317
    self.r3Btn = 318

app = App()
app.run(sys.argv)






