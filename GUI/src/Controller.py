from threading              import Thread
from genpy.message import check_type
from model                  import Model
import Gamepad as gamepad
import rospy
import gi
from enum import IntEnum
import time
from std_msgs.msg           import Int32MultiArray

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#=====================================================
#FINITE STATE MACHINE

class task(IntEnum):
  IDLE        = 1
  MAINTENANCE = 2
  SCIENCE     = 3
  PROBING     = 4
  NAVIGATION  = 5
  MANUAL      = 6
  WAITING     = 7

class instruction(IntEnum):
  WORK   = 1
  WAIT   = 2
  STOP   = 3
  RESUME = 4

# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================
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
    
    #=======================================================
    ROVER_STATE    = task.IDLE
    INSTRUCTION    = instruction.WORK
    TASK_COMPLETED = False
    CONFIRMATION   = 0
    #=======================================================

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
      self.sc_state_switch = {
        0: "idle_label1",
        1: "maintenance_label1",
        2: "science_label1",
        3: "probing_label1",
        4: "navigation_label1",
        5: "manual_label1",
      }
      self.av_state_switch = {
        0: "idle_label2",
        1: "maintenance_label2",
        2: "science_label2",
        3: "probing_label2",
        4: "navigation_label2",
        5: "manual_label2",
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


    def on_navigation_clicked(self, *args):
      self.app.view.NAV.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('NAV')

    def on_HD_clicked(self, *args):
      self.gamepad.cmode('HD')

    def on_science_clicked(self, *args):
      self.app.view.SCIENCE.present()
      Gtk.Application.get_active_window(self.app).hide()
      self.gamepad.cmode('SC')

    def on_avionics_clicked(self, *args):
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
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(0.3)
        
        self.state = self.app.view.nav_state.get_active() +1
        Controller.ROVER_STATE = self.state +1
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(1.0)
      except:
        self.state = 0
        
    def on_capture_image_button_nav_clicked(self, *args):
      self.nav_image_index+=1
      self.app.view.capture_image(self.nav_image_index)

    def on_switch_cam_clicked(self, *args):
      pass

    def wait_confirmation():
      s=0
      while(s < 1):
        if(Controller.CONFIRMATION):
          s = 1
        else:
          s += 0.3
          time.sleep(0.3)

    def check_reception_error(self):
      if(Controller.CONFIRMATION == 0):
        
        self.app.view.warning_icon.set_opacity(1.0)
        self.app.view.ok_icon.set_opacity(0.3)
        Controller.ROVER_STATE = task.IDLE
        Controller.INSTRUCTION = instruction.WORK
        state = [Controller.ROVER_STATE, Controller.INSTRUCTION]
        state = Int32MultiArray(data = state)
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(0.3)
        self.state = 0
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(1.0)
        # self.nav_state_switch.set_active_id(0)
        
        self.app.state_pub.publish(state)


    def on_start_clicked(self, *args):
      
      if(Controller.ROVER_STATE != task.IDLE):
        self.app.view.warning_icon.set_opacity(0.3)
        self.app.view.ok_icon.set_opacity(1.0)
        Controller.INSTRUCTION = instruction.WORK.value
        array = [Controller.ROVER_STATE, Controller.INSTRUCTION]
        state = Int32MultiArray(data=array)
        self.app.state_pub.publish(state)
        Controller.wait_confirmation()
        self.check_reception_error()

    def on_wait_clicked(self, *args):

      if(Controller.ROVER_STATE != task.IDLE and Controller.ROVER_STATE != task.MANUAL):
        Controller.INSTRUCTION = instruction.WAIT
        state = [Controller.ROVER_STATE, Controller.INSTRUCTION]
        self.app.state_pub.publish(state)
        Controller.wait_confirmation()
        self.check_reception_error()

    def on_resume_clicked(self, *args):

      if(Controller.ROVER_STATE == task.WAITING):
        Controller.INSTRUCTION = instruction.RESUME
        state = [Controller.ROVER_STATE, Controller.INSTRUCTION]
        self.app.state_pub.publish(state)
        Controller.wait_confirmation()
        self.check_reception_error()

    def on_stop_clicked(self, *args):

      if(Controller.ROVER_STATE != task.MANUAL):
        Controller.INSTRUCTION = instruction.STOP
        state = [Controller.ROVER_STATE, Controller.INSTRUCTION]
        state = Int32MultiArray(data = state)
        self.app.state_pub.publish(state)
        Controller.ROVER_STATE = task.IDLE
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(0.3)
        self.state = 0
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(1.0)
        Controller.wait_confirmation()
        self.check_reception_error()
      
      

#=======================================================================
#ROS CALLBACKS
    #===================================================================
    #FINITE STATE MACHINE
    def callback_confirm(self, msg):
      if(msg.data):
        print("debug confirmed")
        Controller.CONFIRMATION = 1

    def callback_completed(self, msg):
      if(msg):
        Controller.ROVER_STATE = task.IDLE
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(0.3)
        self.state = 0
        self.app.view.builder.get_object(self.nav_state_switch.get(self.state)).set_opacity(1.0)

    #====================================================================
    #AVIONICS
    def callback_barotemp(self, msg):
      Model.barotemp[0] = msg.data[0]
      Model.barotemp[1] = msg.data[1]
      
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

    #====================================================================
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


