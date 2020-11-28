import gi
import cv2
import sys
import cairo

from model import Model
from view import View

#gamepad
from threading import Thread
import evdev
from evdev import*

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf


class App(Gtk.Application):

  def __init__(self):

    Gtk.Application.__init__(self)
    self.model = Model()
    self.view = View(self)


  def do_startup(self):
    Gtk.Application.do_startup(self)

    self.controller = Controller()

    self.view.window.connect("delete-event", self.on_quit)
    self.view.window2.connect("delete-event", self.on_quit)
    self.view.builder.connect_signals(self.controller)
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
      
      
      #Initialisation gamepad et thread
      self.gamepad = Gamepad()
      self.gamepad.cmode('NAV')
      if self.gamepad.control != None:
        self.t_game = Thread(target = self.gamepad.run, daemon =True) 
        self.t_game.start()

    def on_NAV_clicked(self, *args):

      app.view.window.present()
      App.get_active_window(app).hide()
      self.gamepad.cmode('NAV')

    def on_HD_clicked(self, *args):

      # ~ app.view.window3.present()
      # ~ App.get_active_window(app).hide()
      self.gamepad.cmode('HD')

    def on_SCIENCE_clicked(self, *args):

      app.view.window2.present()
      App.get_active_window(app).hide()
      self.gamepad.cmode('SC')

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
         
    def connect_gamepad(self):
      self.gamepad.connect()
      if self.gamepad.control != None:
        self.t_game = Thread(target = self.gamepad.run, daemon =True) 
        self.t_game.start()

class Gamepad(Thread):


  def __init__(self):
  # ~ connect gamepad
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      if evdev.ecodes.EV_FF in self.control.capabilities():
        self._running = True #variable arret thread
        break
    else:
      sys.stderr.write('Failed to find the haptic motor.\n')
      self.control = None
    
    # ~ self.nav_pub = rospy.Publisher('NAV_AXE', Nav, queue_size=10)
    # ~ rospy.init_node('control_station', anonymous=True)
    
    self.axe_HD_old=[0, 0, 0, 0, 0, 0, 0]
    self.axe_NAV_old=[0., 0.]
    self.axe_HD_new=[0, 0, 0, 0, 0, 0, 0]
    self.axe_NAV_new=[0., 0.]
    self.axe_HDA_new=[0, 0, 0, 0, 0, 0, 0]
    self.axe_HDA_old=[0, 0, 0, 0, 0, 0, 0]
    self.modeHD='MAN'
    self.modeNAV='MAN'

  def connect(self):
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      if evdev.ecodes.EV_FF in self.control.capabilities():
        self._running = True #variable arret thread
        break
    else:
      sys.stderr.write('Failed to find the haptic motor.\n')
      self.control = None
    
  def run (self):
    dec = Decode_manette()
    for event in self.control.read_loop():
      if event.type!=0:
        if (self._running)==0:
          break
        #Mode commun Changement Mode etc...
        if event.type == ecodes.EV_KEY:
          if event.value==1:
            if event.code==dec.shaBtn: #Touche Share
              if self.mode == 'NAV':
                app.controller.on_HD_clicked()
              elif self.mode == 'HD':
                app.controller.on_SCIENCE_clicked()
              elif self.mode == 'SC':
                app.controller.on_NAV_clicked()
                
                
            if event.code==dec.optBtn:
              if self.mode == 'NAV':
                if self.modeNAV == 'MAN':
                  print('AUTO')
                  self.modeNAV='AUTO'
                else:
                  print('MAN')
                  self.modeNAV='MAN'
              elif self.mode == 'HD':
                if self.modeHD == 'MAN':
                  print('AUTO')
                  self.modeHD='AUTO'
                else:
                  print('MAN')
                  self.modeHD='MAN'
            
                
        if (self.mode)== 'NAV': #PARTIE NAVIGATION--------------------
          if event.type == ecodes.EV_KEY:
            if event.value==1:
              if event.code==dec.xBtn: #Touche A
                  print('NAV')
          if self.modeNAV=='MAN': #MANUEL ----------------------------
            if event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
                self.axe_NAV_new[0] = absevent.event.value
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
                self.axe_NAV_new[0] = -absevent.event.value
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                self.axe_NAV_new[1] = absevent.event.value-127 #[0 255] -> [-127 127]
              
              #Envoi rotation et vitesse seulement quand il y a eu un changement
              if compare_list(self.axe_NAV_old,self.axe_NAV_new, 5)!=1:
                print("envoi",self.axe_NAV_new ,' ',self.axe_NAV_old)
                self.axe_NAV_old[0] = self.axe_NAV_new[0]
                self.axe_NAV_old[1] = self.axe_NAV_new[1]
                # ~ self.nav_pub.publish(self.axe_NAV_old)
              
          
        elif (self.mode)== 'HD': #PARTIE HANDLING DEVICE
          if self.modeHD=='MAN':
            # ~ print('HD')
            #BOUTON--------------------
            if event.type == ecodes.EV_KEY:
              if event.value==1:
                if event.code==dec.l1Btn and self.axe_HD_new[4]==0: #Touche l1 axe 5
                  self.axe_HD_new[4]=1
                elif event.code==dec.r1Btn and self.axe_HD_new[4]==0: #Touche r1 axe 5
                  self.axe_HD_new[4]=-1
                elif event.code==dec.l2Btn and self.axe_HD_new[5]==0: #Touche l1 axe 6
                  self.axe_HD_new[5]=1
                elif event.code==dec.r2Btn and self.axe_HD_new[5]==0: #Touche r1 axe 6
                  self.axe_HD_new[5]=-1
                elif event.code==dec.cBtn and self.axe_HD_new[6]==0: #Touche r1 axe 6
                  self.axe_HD_new[6]=1
                elif event.code==dec.tBtn and self.axe_HD_new[6]==0: #Touche r1 axe 6
                  self.axe_HD_new[6]=-1
              elif event.value==0:
                if event.code==dec.l1Btn: #Touche l1 axe 5
                  self.axe_HD_new[4]=0
                elif event.code==dec.r1Btn: #Touche r1 axe 5
                  self.axe_HD_new[4]=0
                elif event.code==dec.l2Btn: #Touche l2 axe 6
                  self.axe_HD_new[5]=0
                elif event.code==dec.r2Btn: #Touche r2 axe 6
                  self.axe_HD_new[5]=0
                elif event.code==dec.cBtn: #Touche r1 pince
                  self.axe_HD_new[6]=0
                elif event.code==dec.tBtn : #Touche r1 pince
                  self.axe_HD_new[6]=0
            #AXE-------------------------
            elif event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              # ~ print(ecodes.bytype[absevent.event.type][absevent.event.code])
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX": #Axe 1
                self.axe_HD_new[0] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":#Axe2
                self.axe_HD_new[1] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#Axe3
                self.axe_HD_new[2] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":#Axe4
                self.axe_HD_new[3] = eval_axe(absevent.event.value)
                  
              #envoi valeurs axe si et seulement si il y a eu un changement
              if compare_list(self.axe_HD_old,self.axe_HD_new, 0)!=1:
                  print("envoi HD",self.axe_HD_new ,' ',self.axe_HD_old)
                  for k in range(len(self.axe_HD_new)):
                    self.axe_HD_old[k] = self.axe_HD_new[k]
                    
                    
          elif self.modeHD=='AUTO':#Direct Kinematics
            if event.type == ecodes.EV_KEY:
              if event.value==1:
                if event.code==dec.cBtn: #Touche r1 pince
                  self.axe_HDA_new[6]=1
                elif event.code==dec.tBtn : #Touche r1 pince
                  self.axe_HDA_new[6]=-1
                elif event.code==dec.l2Btn and self.axe_HD_new[5]==0: #Touche l2 axe Z
                  self.axe_HDA_new[2]=1
                elif event.code==dec.r2Btn and self.axe_HD_new[5]==0: #Touche r2 axe Z
                  self.axe_HDA_new[2]=-1
                elif event.code==dec.l1Btn : #Touche l1 rotationX
                  self.axe_HDA_new[3]=1
                elif event.code==dec.r1Btn : #Touche r1 rotationX
                  self.axe_HDA_new[3]=-1
                
              elif event.value==0:
                if event.code==dec.l2Btn: #Touche l2 axe 6 relacher
                  self.axe_HDA_new[2]=0
                elif event.code==dec.r2Btn: #Touche r2 axe 6 relacher
                  self.axe_HDA_new[2]=0
                elif event.code==dec.l1Btn: #Touche l1 rotationX
                  self.axe_HDA_new[3]=0
                elif event.code==dec.r1Btn: #Touche r1 rotationX
                  self.axe_HDA_new[3]=0
                elif event.code==dec.cBtn: #Touche r1 pince
                  self.axe_HDA_new[6]=0
                elif event.code==dec.tBtn : #Touche r1 pince
                  self.axe_HDA_new[6]=0
                  
            elif event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":#Axe Y
                self.axe_HDA_new[1] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#Axe X
                self.axe_HDA_new[0] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":#Rotz
                self.axe_HDA_new[5] = absevent.event.value
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":#RotY
                self.axe_HDA_new[4] = absevent.event.value
                
                
            if compare_list(self.axe_HDA_old,self.axe_HDA_new, 0)!=1:
              print("envoi HD",self.axe_HDA_new ,' ',self.axe_HDA_old)
              for k in range(len(self.axe_HDA_new)):
                self.axe_HDA_old[k] = self.axe_HDA_new[k]

        elif (self.mode)== 'SC':
          if event.type == ecodes.EV_KEY:
            # ~ print(categorize(event))
            if event.value==1:
              if event.code==304: #Touche A
                  print('SC')
      

  def cmode(self, mode): 
    self.mode = mode
    
def eval_axe(axe_value): #Donne le sens de rotation bras robot
  value=0
  if axe_value <= 10:
    value = 1
    return value
  elif axe_value >= 245:
    value = -1
    return value
  elif axe_value > 10 and axe_value < 245:
    return value

def compare_list(list1, list2, tolerance):
  #compare deux liste avec une certaine tolerance 
  for k in range(len(list1)):
    if (list1[k]+tolerance >= list2[k] and list1[k]-tolerance <= list2[k])!=1:
      return 0
  return 1

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
