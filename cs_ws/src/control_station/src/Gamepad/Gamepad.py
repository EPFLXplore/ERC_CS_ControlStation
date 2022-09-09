'''
@File  :

@Author: Emma Gaia Poggiolini
'''
import evdev
from   evdev           import *

import sys

from   threading       import Thread
from   time            import sleep, time

from   Gamepad.keyMap          import *

from geometry_msgs.msg import Twist
from std_msgs.msg      import Int8MultiArray, Int8, Bool
import threading

from src.model import Task


'''
Class Gamepad

@Description: Thread to Command the Rover  

@Attributes:
    -

'''

# ------global variables------ 
max_val   = 32767
max_L2_R2 = 255
scale     = 100
  


class Inft_Timer:
  """infinity thread timer to run a target function at constant time intervals"""

  def __init__(self, t, target):
    self.t = t
    self.target = target
    self.thread = threading.Timer(self.t, self.handler)
  
  def handler(self):
    self.target()
    self.thread = threading.Timer(self.t, self.handler)
    self.thread.start()
  
  def start(self):
    self.thread = threading.Timer(self.t, self.handler)
    self.thread.start()
  
  def cancel(self):
    self.thread.cancel()



class Gamepad(Thread):

  def __init__(self, cs):  
    self.cs = cs     
    #------------------variables-------------------
    # start-up mode = NAV 
    self.mode = 'NAV' #or 'HD'

    #------------------NAVIGATION------------------
    # declare and initialize msg_nav_dir
    self.msg_nav_dir = Twist()
    self.msg_nav_dir.linear.x  = 0
    self.msg_nav_dir.linear.y  = 0  # always zero
    self.msg_nav_dir.linear.z  = 0  # always zero
    self.msg_nav_dir.angular.x = 0  # always zero
    self.msg_nav_dir.angular.y = 0  # always zero
    self.msg_nav_dir.angular.z = 0

    #self.axe_NAV_old = [0., 0., 0.]  # [.linear.x, .linear.y, .angular.z]
    self.axe_NAV_new = [0., 0., 0.]  # [.linear.x, .linear.y, .angular.z]

    # cutoff value: within this epsilon around zero, we don't get reliable signals => set signal to 0.
    self.deadval = 5e-2

    #---------------HANDLING DEVICE----------------
    self.zero_HD    = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_old = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_new = [0, 0, 0, 0, 0, 0, 0]
    self.joint      = 0  # joint 1 as default joint
    self.voltmeter  = 0
    
    self.modeHD = 'DIR' #or 'INV' or 'DEBUG' 
    self.modeHDmsg = 2  
      # DEBUG == 1
      # DIR   == 2
      # INV   == 3

    self.homeGo  = Bool()
    self.homeGo  = 0
    self.homeSet = Bool()
    self.homeSet = 0
    self.homeSet_temp = 0 

    self.last_switch_time = time()
    self.last_hd_mode_switch_time = time()

    self.connect()
    dt = 1/20
    self.publish_timer = Inft_Timer(dt, self.publish_commands)

  def publish_commands(self):
    if self.mode == "HD":
      #if self.modeHD == "DIR" or self.modeHD == "DEBUG":
        newAxeVal(self)

  def connect(self):
    # ~ connection search gamepad
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      # device.capabilities() returns all possible (KEY, value) pairs 
      # representing the actions linked to device   
      # .EV_FF sends force feedback commands to an input device
      if evdev.ecodes.EV_FF in self.control.capabilities():
        self._running = True # variable to stop gamepad thread => when set to False
        break
      else: # error in connecting to gamepad 
        sys.stderr.write('Failed to find the haptic motor.\n')
        self.control = None

  def run (self):
    advance = 0  # control: if advancing can't retreat and vice versa
    retreat = 0
    self.publish_timer.start()
    for event in self.control.read_loop():

      if self.mode == 'NAV':
      # TODO
        print(self.axe_NAV_new)
        # publish values
        self.cs.Nav_Joystick_pub.publish(self.msg_nav_dir)

      if event.type != 0:
        #if (self._running) == 0: # when self._running == False  run() stops
        if(self._running == False):
          self.axe_HD_old = [0]*7
          self.axe_HD_new = [0]*7
          self.publish_timer.cancel()
          break
        # EV_KEY describes state changes of device
        if event.type == ecodes.EV_KEY:
          if event.value == 1:

          #---------------SWITCH NAV <=> HD------------------------------------------------------------------
            if event.code == Keymap.BTN_SHARE.value:    # Share Button => switch NAV <=> HD
              if time()-self.last_switch_time > 0.5:
                self.last_switch_time = time()
                self.switchNAV_HD()

            # switching  DIR => INV => DEBUG => DIR  only when in HD     
            if event.code == Keymap.BTN_OPTIONS.value:  # Option Button
              if self.mode == 'HD':
                if time()-self.last_hd_mode_switch_time > 0.5:
                  self.last_hd_mode_switch_time = time()
                  self.switchHDmode()



        #------------------NAVIGATION------------------------------------------------------------------------
        if (self.mode) == 'NAV':       
          if event.type == ecodes.EV_ABS:
            absevent = categorize(event)
          #---------------ANGULAR.Z--------------------------------------------------------------------------
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":  # x-axis of R3 
              #-----------increase/decrease-------------
              # push joystick to the right for positive value
              self.axe_NAV_new[2] = -round(absevent.event.value/max_val, 5) # Max value :32768
          #---------------LINEAR.Y--------------------------------------------------------------------------
            #------------crab mode------------
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":  # x-axis of L3 
              #-----------increase/decrease-------------
              # push joystick to the right for positive value
              self.axe_NAV_new[1] = -round(absevent.event.value/max_val, 5) # Max value :32768

          #---------------LINEAR.X---------------------------------------------------------------------------
            #-------------advance--------------
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":  # button R2
              if (retreat == 0):  # advance (only if not retreating)
                self.axe_NAV_new[0] = round(absevent.event.value/max_L2_R2, 5)
                advance = 1
              if absevent.event.value == 0:  # stay still
                advance = 0
            #-------------retreat--------------
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":  # button L2
              if (advance == 0):  # go backwards (only if not retreating)
                self.axe_NAV_new[0] = round(-absevent.event.value/max_L2_R2, 5)
                retreat = 1
              if absevent.event.value == 0:  # stay still
                retreat = 0

            # update values of linear.x, linear.y and angular.z
            self.msg_nav_dir.linear.x  = 0. if abs(self.axe_NAV_new[0] / 2) < self.deadval else (self.axe_NAV_new[0] / 2)
            self.msg_nav_dir.linear.y  = 0. if abs(self.axe_NAV_new[1] / 2) < self.deadval else (self.axe_NAV_new[1] / 2)
            self.msg_nav_dir.angular.z = 0. if abs(self.axe_NAV_new[2] / 2) < self.deadval else (self.axe_NAV_new[2] / 2)
              
            #     TODO
          print(self.axe_NAV_new)
          # publish values
          self.cs.Nav_Joystick_pub.publish(self.msg_nav_dir)
          print("Nav published")
              


        #-----------------HANDLING DEVICE--------------------------------------------------------------------
        elif (self.mode) == 'HD':
          #---------------INVERSE----------------------------------------------------------------------------
          if self.modeHD == 'INV':
            # buttons
            if event.type == ecodes.EV_KEY:
              if event.value == 1: 
                #----------voltmeter------------
                if event.code == Keymap.BTN_PS.value:         # PS button 
                  self.switchVoltmeter()

            if event.type == ecodes.EV_ABS:  
                absevent = categorize(event) 
                #-----------x-axis------------- 
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":  # R3 up & down 
                  self.axe_HD_new[0] = -scale * round(absevent.event.value/max_val, 5) # Max value: 32768
                #-----------y-axis------------- 
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":  # R3 left (positive) & right (negative)
                  self.axe_HD_new[1] = -scale * round(absevent.event.value/max_val, 5) # Max value: 32768
                #-----------z-axis------------- 
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":  # R2 (positive)
                  self.axe_HD_new[2] = scale * round(absevent.event.value/max_L2_R2, 5) # Max value: 255
                #-----------z-axis------------- 
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":   # L2 (negative)
                  self.axe_HD_new[2] = scale * round(-absevent.event.value/max_L2_R2, 5) # Max value: 255

            # send 0. when values are close to 0. 
            resetAxe(self)


          #---------------DEBUG----------------------------------------------------------------------------
          elif self.modeHD == 'DEBUG':
            if event.type == ecodes.EV_KEY:
              if event.value == 1:
                #-----------joints 3, 4, 5, 6, gripper-------------
                if event.code == Keymap.BTN_L1.value:         # joint 3
                  self.joint = 2
                elif event.code == Keymap.BTN_R1.value:       # joint 4
                  self.joint = 3
                elif event.code == Keymap.BTN_TRIANGLE.value: # joint 5
                  self.joint = 4
                elif event.code == Keymap.BTN_CIRCLE.value:   # joint 6
                  self.joint = 5
                elif event.code == Keymap.BTN_CROSS.value:    # joint 7: gripper
                  self.joint = 6
                #----------voltmeter------------
                if event.code == Keymap.BTN_PS.value:         # PS button 
                  self.switchVoltmeter()
              
            if event.type == ecodes.EV_ABS:  
              absevent = categorize(event) 
              #-----------joint 1-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":  # d-pad x            
                self.joint = 0
              #-----------joint 2-------------  
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":  # d-pad y
                #---------go home-------------
                if event.value == 1:
                    self.goHome()
                else:                
                    self.joint = 1
              #-------------velocity-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":  # joint R3 up & down
                #-----------increase/decrease-------------
                # push joystick up for positive velocity      
                self.axe_HD_new[self.joint] = scale * round(-absevent.event.value/max_val, 5) # Max value: 32768
              #-----------set home------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":  # R2
                self.homeSet_temp = 1  # Max value: 255 
              if (ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z") and (self.homeSet_temp == 1):   # L2 
                self.setHome()     

            # send 0. when values are close to 0. 
            resetAxe(self)


          #---------------DIRECT---------------------------------------------------------------------------
          elif self.modeHD == 'DIR': 
            if event.type == ecodes.EV_KEY:
              if event.value == 1:
                #-----------gripper------------
                if event.code == Keymap.BTN_TRIANGLE.value:   # gripper = +100
                  self.axe_HD_new[6] = -10.
                elif event.code == Keymap.BTN_CIRCLE.value:   # gripper = +10
                  self.axe_HD_new[6] = 10.
                elif event.code == Keymap.BTN_CROSS.value:    # gripper = -100
                  self.axe_HD_new[6] = 100.
                elif event.code == Keymap.BTN_SQUARE.value:   # gripper = -10
                  self.axe_HD_new[6] = -100.
                #-----------joint 3------------
                elif event.code == Keymap.BTN_R1.value:       # R1 - joint 3 advance 
                  self.axe_HD_new[3] = 100.
                elif event.code == Keymap.BTN_L1.value:       # L1 - joint 3 retreat
                  self.axe_HD_new[3] = -100.              
                #----------voltmeter------------
                if event.code == Keymap.BTN_PS.value:         # PS button 
                  self.switchVoltmeter()
              #-----------reset joint 3, gripper------------
              elif event.value == 0:
                self.axe_HD_new[6] = 0
                self.axe_HD_new[3] = 0
      
            #---------------velocity---------------  
            if event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              #-----------joint 2-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":  # R3 up & down 
                self.axe_HD_new[1] = -scale * round(absevent.event.value/max_val, 5) # Max value: 32768
              #-----------joint 1------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":  # R3 left & right
                self.axe_HD_new[0] = -scale * round(absevent.event.value/max_val, 5) # Max value: 32768
              #-----------joint 5-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":  # L3 up & down 
                self.axe_HD_new[4] = scale * round(absevent.event.value/max_val, 5) # Max value: 32768
              #-----------joint 6------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":  # L3 left & right
                self.axe_HD_new[5] = scale * round(absevent.event.value/max_val, 5) # Max value: 32768
              #-----------joint 4------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":  # R2
                self.axe_HD_new[2] = scale * round(absevent.event.value/max_L2_R2, 5) # Max value: 255
              #-----------joint 4------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":   # L2 
                self.axe_HD_new[2] = scale * round(-absevent.event.value/max_L2_R2, 5) # Max value: 255
              #-----------go home-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":  # d-pad y
                if event.value == 1:
                    self.goHome()            

            # send 0. when values are close to 0. 
            resetAxe(self)

            
    #self.publish_timer.cancel()
        

  #-------Gamepad auxiliary methods-------

  # Set self.mode
  def cmode(self, mode):
    self.mode = mode


  # Switching NAV <=> HD
  def switchNAV_HD(self):
    # switching mode  NAV <=> HD
    if self.mode == 'NAV':
      self.cmode('HD')
      self.modeHD = 'DIR'  # reset to DIR 
      print(self.mode, ': ', self.modeHD)
    elif self.mode == 'HD':
      self.cmode('NAV')
      print(self.mode)


  # Switching DIR => INV => DEBUG => DIR
  # when in HD mode
  def switchHDmode(self):  
    #------DIR => INV------
    if self.modeHD == 'DIR':
      self.modeHDmsg = 3
      print('INV')
      self.modeHD = 'INV'
    #-----INV => DEBUG-----
    elif self.modeHD == 'INV':
      self.modeHDmsg = 1
      print('DEBUG')
      self.modeHD = 'DEBUG'
    #-----DEBUG => DIR-----
    elif self.modeHD == 'DEBUG':
      self.modeHDmsg = 2
      print('DIR')
      self.modeHD = 'DIR'  

    # ====== DISPLAY NEW HD MODE ON GUI ======
    self.cs.controller.sendJson(Task.MAINTENANCE)

    self.axe_HD_old = clear_tab(self.axe_HD_old)
    self.axe_HD_new = clear_tab(self.axe_HD_new)

    self.cs.HD_mode_pub.publish(Int8(data = self.modeHDmsg))
    self.cs.HD_Angles_pub.publish(Int8MultiArray(data = self.axe_HD_new))
    

  # Voltmeter:  Extend <=> Retreat
  def switchVoltmeter(self):
    if self.voltmeter == 0:
      self.voltmeter = 1
    else:
      self.voltmeter = 0
      #     TODO 
    print(self.voltmeter)  
    self.cs.HD_voltmeter_pub.publish(Int8(data = self.voltmeter))


  # HD: send arm to home position
  def goHome(self):
    self.homeGo = 1
    print(self.homeGo)
    self.cs.HD_homeGo_pub.publish(self.homeGo)
    # reset bool
    self.homeGo = 0
    
  # HD: set arm home position 
  def setHome(self):
    self.homeSet = 1
    print(self.homeSet)
    self.cs.HD_homeSet_pub.publish(self.homeSet)
    # reset bool(s)
    self.homeSet = 0
    self.homeSet_temp = 0  
    
    
#-------External auxiliary methods-------

# Compare 2 arrays with a tolerance 
def compare_list(list1, list2, tolerance):
  for k in range(len(list1)):
    if (list1[k]+tolerance >= list2[k] and list1[k]-tolerance <= list2[k])!=1:
      return 0
  return 1


# Values small enough to reset to 0 
def reset_small(list1):
  for k in range(len(list1)):
    if (list1[k] >= -2 and list1[k] <= 2):
      list1[k] = 0
  return list1


# Clear array 
def clear_tab(tab):
  for k in range(len(tab)):
    tab[k] = 0
  return tab
  

# Send new Joint velocities for HD
def newAxeVal(self):
  for k in range(len(self.axe_HD_new)):
    self.axe_HD_old[k] = self.axe_HD_new[k]

  #     TODO 
  print(self.axe_HD_new, "AAAAAAAAAAAAAA")

  print(self.axe_HD_new)
  self.cs.HD_Angles_pub.publish(Int8MultiArray(data = list(map(int, self.axe_HD_new))))
                               
      
# Send new Joint velocities for HD
# if and only if abs(value) > 2
def resetAxe(self):
  reset_small(self.axe_HD_old)
  reset_small(self.axe_HD_new)


