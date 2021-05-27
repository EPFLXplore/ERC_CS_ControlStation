from threading              import Thread
from model                  import Model
import Gamepad as gamepad
import rospy
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
'''
Class Controller

@Description: The class responsible for the input/output logic

@Attributes:
    -Gamepad gamepad ->
    -Thread t-game ->
    -Dictionnary(int, str) controls_hd_switch -> Dictionnary for a switch case to choose the controls type
    -str controls -> the chosen control mode to be sent in ROS msg

'''
class Controller():
    
    def __init__(self, Application):
      rospy.init_node('control_station', anonymous=True)
      self.rotation = 0.0
      self.nav_image_index=1
      self.app = Application
      #NAV
      self.nav_state_switch = {
        0: "idle_label",
        1: "maintenance_label",
        2: "science_label",
        3: "probing_label",
        4: "navigation_label",
        5: "manual_label",
      }
      self.state = 0

      #HD
      self.controls_hd_switch = {
        0: "Automatic",
        1: "Manual",
        2: "Inverse"
      }
      self.controls = None

      #Initialisation gamepad et thread
      self.gamepad = gamepad.Gamepad()
      self.gamepad.cmode('NAV')
      if self.gamepad.control != None:
        self.t_game = Thread(target = self.gamepad.run, daemon =True)
        self.t_game.start()

    def on_NAV_clicked(self, *args):
      self.app.view.NAV.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('NAV')

    def on_NAV2_clicked(self, *args):
      self.app.view.NAV.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('NAV')

    def on_HD_clicked(self, *args):
      self.gamepad.cmode('HD')

    def on_SCIENCE_clicked(self, *args):
      self.app.view.SCIENCE.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('SC')

    def on_SCIENCE2_clicked(self, *args):
      self.app.view.SCIENCE.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('SC')

    def on_AV1_clicked(self, *args):
      self.app.view.AV.present()
      Gtk.Application.get_active_window(self.app).hide()

    def on_AV2_clicked(self, *args):
      self.app.view.AV.present()
      Gtk.Application.get_active_window(self.app).hide()

    def on_SWITCH_clicked(self, *args):
      self.rotation += 0.05
      self.app.view.builder.get_object("compass").queue_draw()
      print(self.app.model.time_array[2])

    def draw_compass(self, widget, ctx):
         ctx.set_line_width(3)
         ctx.set_source_rgb(1.0,0.0,0.1)
         ctx.move_to(90, 78)
         ctx.rotate(self.rotation)
         ctx.rel_line_to(0, -65)
         ctx.stroke()

    def connect_gamepad(self):
      self.gamepad.connect()
      if self.gamepad.control != None:
        self.t_game = Thread(target = self.gamepad.run, daemon =True)
        self.t_game.start()

    def on_controls_hd_changed(self, *args):
      self.controls = self.controls_hd_switch.get(self.app.view.controls_hd.get_active(), "invalid index")
      self.app.view.control_mode.set_text(self.controls)

    def on_nav_state_changed(self, *args):
      try:
        print(self.state)
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(0.3)
        self.state = self.app.view.nav_state.get_active()
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(1.0)
      except:
        self.state = 0
        
    def on_capture_image_button_nav_clicked(self, *args):
      self.nav_image_index+=1
      self.app.view.capture_image(self.nav_image_index)
      
      

#=======================================================================
#ROS CALLBACKS

    #AVIONICS
    def callback_barotemp(self, msg):
      Model.barotemp[0] = msg.data[0]
      Model.barotemp[1] = msg.data[1]
      
      # Controller.barotemp[0] = msg.data[0]
      # Controller.barotemp[1] = msg.data[1]

    def callback_accelmag(msg):
        pass

    def callback_gripper(msg):
        pass

    def callback_system(msg):
        pass

    def callback_voltages(msg):
        pass

    def callback_currents(msg):
        pass

    def callback_measures(msg):
        pass

    def callback_reset_power(msg):
      pass
    def callback_switch_power(msg):
      pass
    def callback_switch_raman(msg):
      pass
    def callback_switch_jetson(msg):
      pass
    def callback_switch_LIDAR(msg):
      pass
    def callback_switch_ethernet(msg):
      pass
    #NAVIGATION
    def callback_waypoint(msg):
      pass

    def callback_tags(msg):
      pass

    def callback_signal_AM(msg):
      pass

    def callback_rover_state(msg):
      pass

    def callback_nav_logs(msg):
      pass

    def callback_mission_state_d1(msg):
      pass

    def callback_current_position(msg):
      pass
    #SCIENCE

    #HANDLING DEVICE


