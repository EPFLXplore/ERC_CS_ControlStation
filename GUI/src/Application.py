#!/usr/bin/env python
'''
@file Application.py

@breif MVC Template
  This file initializes the Application, defines I/O behaviours.
  It also initializes the ROS Control Station nodes along with the
  publisher and the subscribers.
  It contains a class to read inputs from a PS4 like controller.

@Author: Emile Hreich
         

@date 25/02/2021
'''
import gi

import rospy
import logging
from Controller import Controller
from Stopwatch              import Stopwatch as stp
from model                  import Model
from rospy.impl.tcpros_base import DEFAULT_BUFF_SIZE
from view                   import View
from std_msgs.msg           import String, Float32, Float32MultiArray, Bool, Int32, UInt8MultiArray
from nav_msgs.msg           import Odometry
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
#================================================================

'''
Class: App

@Description: The main Application

@Attributes:
    -model: Model class
    -view: view class
    -controller: controller class

    MVC Template
'''
class App(Gtk.Application):

  def __init__(self):
    
    Gtk.Application.__init__(self)
    self.model = Model()
    self.view  = View(self)
    self.controller = Controller(self) 
    #stopwatch initialization
    self.stopwatch = stp()

  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  def setup_logger(name, log_file, level):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(App.formatter)
    logger = logging.getLogger(str(name))
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


  def do_startup(self):
    
    Gtk.Application.do_startup(self)
    self.view.NAV.connect("delete-event", self.on_quit)
    self.view.SCIENCE.connect("delete-event", self.on_quit)
    self.view.AV.connect("delete-event", self.on_quit)
    self.view.builder.connect_signals(self.controller)
    self.view.camera_process_1.start()
    self.view.camera_process_2.start()
    GLib.idle_add(self.view.show)
    GLib.idle_add(self.view.show_time)
    GLib.idle_add(self.view.display_avionics)
    GLib.idle_add(self.view.display_science)
    GLib.idle_add(self.view.display_handling_device)
    GLib.idle_add(self.view.display_navigation)
    self.stopwatch.start()

    #=========================================================================================================
    #ROS TOPICS
    #FINITE STATE MACHINE
    rospy.Subscriber('confirmation',    Int32,             self.controller.callback_confirm          )
    rospy.Subscriber('completed',       Int32,             self.controller.callback_completed        )
    self.state_pub        = rospy.Publisher('state'    ,        UInt8MultiArray,   queue_size=1      )

    #AVIONICS
    rospy.Subscriber('barotemp',        Float32MultiArray, self.controller.callback_barotemp         )
    rospy.Subscriber('accelmag',        Float32MultiArray, self.controller.callback_accelmag         )
    rospy.Subscriber('adc',             Float32MultiArray, self.controller.callback_gripper          )
    rospy.Subscriber('mass',            Float32,           self.controller.callback_measures         )

    ##Power suplly avionics commands
    self.power_reset_pub   = rospy.Publisher('reset_power',      Bool,    queue_size=1)
    self.power_switch_pub  = rospy.Publisher('switch_power',     Bool,    queue_size=1)
    self.raman_switch_pub  = rospy.Publisher('switch_raman',     Bool,    queue_size=1)
    self.jetson_switch_pub = rospy.Publisher('switch_jetson',    Bool,    queue_size=1)
    self.LIDAR_switch_pub  = rospy.Publisher('switch_LIDAR',     Bool,    queue_size=1)
    self.ethernet_switch   = rospy.Publisher('switch_ethernet',  Bool,    queue_size=1)
    rospy.Subscriber('system',          Float32MultiArray, self.controller.callback_system           )
    rospy.Subscriber('voltages',        Float32MultiArray, self.controller.callback_voltages         )
    rospy.Subscriber('currents',        Float32MultiArray, self.controller.callback_currents         )

    #NAVIGATION
    rospy.Subscriber('waypoint',         Float32MultiArray, self.controller.callback_waypoint        )
    rospy.Subscriber('tags',             Float32MultiArray, self.controller.callback_tags            )
    rospy.Subscriber('signal_AM',        Bool,              self.controller.callback_signal_AM       )
    rospy.Subscriber('rover_state',      Int32,             self.controller.callback_rover_state     )
    rospy.Subscriber('nav_logs',         String,            self.controller.callback_nav_logs        )
    rospy.Subscriber('mission_state_d1', Int32,             self.controller.callback_mission_state_d1)
    rospy.Subscriber('current_position', Odometry,          self.controller.callback_current_position)
    #SCIENCE
    #TODO: Controls for science
    #HANDLING DEVICE

    #==========================================================================================================
    #LOGGERS
    avionics_logger       = App.setup_logger('avlogger', "../Logs/avionics.log",    logging.INFO)
    navigation_logger     = App.setup_logger('navlogger', "../Logs/navigation.log", logging.INFO)
    hd_logger             = App.setup_logger('hdlogger', "../Logs/HD.log",          logging.INFO)
    science_logger        = App.setup_logger('sclogger', "../Logs/science.log",     logging.INFO)


 
  def do_activate(self):
    self.view.NAV.set_application(self.controller.app)
    self.view.SCIENCE.set_application(self.controller.app)
    self.view.AV.set_application(self.controller.app)
    self.view.NAV.present()

  def on_quit(self, action, param):
    Model.run_thread = False
    self.stopwatch.join()
    # self.view.capture.release()
    # self.view.out.release()
    self.quit()

'''
Main
'''
app = App()
app.run(sys.argv)    
  

