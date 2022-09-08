'''
@File  :

@Author: Emma Gaia Poggiolini
'''
import evdev
from   evdev           import *

import rospy
import sys

from   threading       import Thread
from   time            import sleep

#decomment 
#from   CS_node         import CS
from   keyMap          import *

from geometry_msgs.msg import Twist
from std_msgs.msg      import Int8MultiArray, Int8, Bool


'''
Class Gamepad

@Description: Command the Rover indenedently of the Control Station Backend  

@Attributes:
    -

'''

## To Launch File Independently - with NAV commands 
#     0. delete  from   CS_node         import CS 
#     1. delete  cs  from the arguments of __init__( )  and comment  self.cs = cs
#     2. add in __init__( ): 
#           rospy.init_node("CONTROL_STATION", anonymous=True)
#           self.Nav_Joystick_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#           self.HD_Angles_pub    = rospy.Publisher('HD_joints', Int8MultiArray, queue_size=1) 
#           self.HD_voltmeter_pub = rospy.Publisher('HD_oltmeter', Int8, queue_size=1)
#           self.HD_mode_pub      = rospy.Publisher('HD_mode', Int8, queue_size=1)
#     3. add at the end of the file:
#           gamepad = Gamepad()
#           gamepad.run()


max_val   = 32767
max_L2_R2 = 255
scale     = 100
  

class Gamepad(Thread):

  def __init__(self):  #add cs
    #self.cs = cs      #decomment
    rospy.init_node("Control_Station")
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
    #self.rate = rospy.Rate(10)

    self.axe_NAV_old = [0., 0., 0.]  # [.linear.x, .linear.y, .angular.z]
    self.axe_NAV_new = [0., 0., 0.]

    #---------------HANDLING DEVICE----------------
    self.zero_HD    = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_old = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_new = [0, 0, 0, 0, 0, 0, 0]
    self.joint = 0  # joint 1 as default joint
    self.voltmeter  = 0
    
    self.modeHD = 'DIR' #or 'INV' or 'DEBUG' 
    self.modeHDmsg = 2  
      # DEBUG == 1
      # DIR   == 2
      # INV   == 3

    #self.joint3 = 1
    #self.joint4 = 1
    self.homeGo  = Bool()
    self.homeGo  = 0
    self.homeSet = Bool()
    self.homeSet = 0
    self.homeSet_temp = 0 


    #delete
    self.Nav_Joystick_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.HD_Angles_pub    = rospy.Publisher('HD_joints', Int8MultiArray, queue_size=1) 
    self.HD_voltmeter_pub = rospy.Publisher('HD_voltmeter', Int8, queue_size=1)
    self.HD_mode_pub      = rospy.Publisher('HD_mode', Int8, queue_size=1)
    self.HD_homeGo_pub    = rospy.Publisher('HD_reset_arm_pos', Bool, queue_size=1)
    self.HD_homeSet_pub   = rospy.Publisher('HD_set_zero_arm_pos', Bool, queue_size=1)

    self.connect()



  def connect(self):
    # ~ connection search gamepad
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      # device.capabilities() returns all possible (KEY, value) pairs 
      # representing the actions linked to device   
      # .EV_FF sends force feedback commands to an input device
      if evdev.ecodes.EV_FF in self.control.capabilities():
        self._running = True # variable to stop gamepad thread => when set to False
        
        #self.publisher_thread = threading.Timer(1/self.rate, self.Nav_Joystick_pub.publish(self.msg_nav_dir))
        #self.publisher_thread.start()
        
        break
      else: # error in connecting to gamepad 
        sys.stderr.write('Failed to find the haptic motor.\n')
        self.control = None



  def run (self):
    advance = 0  # control: if advancing can't retreat and vice versa
    retreat = 0
    for event in self.control.read_loop():
      if self.mode == 'NAV':
      # TODOmko
          print(self.axe_NAV_new)
      # publish values
          self.Nav_Joystick_pub.publish(self.msg_nav_dir)
      #resetAxeNAV(self)

      if event.type != 0:
        if (self._running) == 0: # when self._running == False  run() stops
          break
        # EV_KEY describes state changes of device
        if event.type == ecodes.EV_KEY:
          if event.value == 1:

          #---------------SWITCH NAV <=> HD------------------------------------------------------------------
            if event.code == Keymap.BTN_SHARE.value:  # Share Button => switch NAV <=> HD
              self.switchNAV_HD()

            # switching  DIR => INV => DEBUG => DIR  only when in HD     
            if event.code == Keymap.BTN_OPTIONS.value:  # Option Button
              if self.mode == 'HD':
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
            self.msg_nav_dir.linear.x = self.axe_NAV_new[0] / 2
            self.msg_nav_dir.linear.y = self.axe_NAV_new[1] / 2
            self.msg_nav_dir.angular.z = self.axe_NAV_new[2] / 2
              
            #     TODO
          print(self.axe_NAV_new)
          # publish values
          self.Nav_Joystick_pub.publish(self.msg_nav_dir)
          print("Nav published")
          #resetAxeNAV(self)
              


        #-----------------HANDLING DEVICE--------------------------------------------------------------------
        elif (self.mode) == 'HD':
          #---------------INVERSE----------------------------------------------------------------------------
          if self.modeHD == 'INV':
            # buttons
            # if event.type == ecodes.EV_KEY:
            #   if event.value == 1: 
            #     if event.code == Keymap.BTN_R1.value and self.axe_HD_new[4] == 0: # R1 joint 4 = 1
            #       self.axe_HD_new[3] = 1
            #     elif event.code == Keymap.BTN_L1.value and self.axe_HD_new[4] == 0: # L1 joint 4 = -1
            #       self.axe_HD_new[3] = -1
            #     elif event.code == Keymap.BTN_SQUARE.value and self.axe_HD_new[6] == 0: # Square button open the gripper
            #       self.axe_HD_new[6] = 1
            #     elif event.code == Keymap.BTN_CROSS.value and self.axe_HD_new[6] == 0: # Cross button close the gripper
            #       self.axe_HD_new[6] = -1
            #     # R2 => gripper rise: positive z
            #     elif event.code == Keymap.BTN_R2.value: 
            #       if event.type == ecodes.EV_ABS:
            #         absevent = categorize(event)
            #         if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":  # is this correct? 
            #           self.gripper_new[2] = eval_axe(absevent.event.value)
            #     # L2 => gripper drop: negative z
            #     elif event.code == Keymap.BTN_L2.value: 
            #       if event.type == ecodes.EV_ABS:
            #         absevent = categorize(event)
            #         if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":
            #           self.gripper_new[2] = eval_axe(-absevent.event.value)
            #   # Release
            #   elif event.value == 0: 
            #     if event.code == Keymap.BTN_R1.value: # R1 joint 4 = 1
            #       self.axe_HD_new[3] = 0
            #     elif event.code == Keymap.BTN_L1.value: # L1 joint 4 = -1
            #       self.axe_HD_new[3] = 0
            #     elif event.code == Keymap.BTN_SQUARE.value: # Square button Stop the opening
            #       self.axe_HD_new[6] = 0
            #     elif event.code == Keymap.BTN_CROSS.value: # Triangle button Stop the closing
            #       self.axe_HD_new[6] = 0
            # # AXE-------------------------
            # elif event.type == ecodes.EV_ABS:
            #   absevent = categorize(event)
            #   if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X": # joint 5 L3 left & right 
            #     self.axe_HD_new[4] = eval_axe(absevent.event.value)
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y": # joint 6 L3 up & down
            #     self.axe_HD_new[5] = eval_axe(absevent.event.value)
            #   if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX": # gripper move along x-axis
            #     self.gripper_new[0] = eval_axe(absevent.event.value)
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY": # gripper move along y-axis
            #     self.gripper_new[1] = eval_axe(absevent.event.value)



              # ~ print(ecodes.bytype[absevent.event.type][absevent.event.code])
              # if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX": #Axe 1
              #   self.axe_HD_new[0] = eval_axe(absevent.event.value)
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":#Axe2
              #   self.axe_HD_new[1] = eval_axe(absevent.event.value)
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#Axe3
              #   self.axe_HD_new[2] = eval_axe(absevent.event.value)
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":#Axe4
              #   self.axe_HD_new[3] = eval_axe(absevent.event.value)
              #Axe 6
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#Axe4
              #   if absevent.event.value >= 250:
              #     self.axe_HD_new[5] = 1
              #   else:
              #     self.axe_HD_new[5] = 0
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":#Axe4
              #   if absevent.event.value >= 250:
              #     self.axe_HD_new[5] = -1
              #   else:
              #     self.axe_HD_new[5] = 0

            # sends new values if and only if changed from previous
            newAxeVal(self)

          #---------------DEBUG----------------------------------------------------------------------------
          elif self.modeHD == 'DEBUG':
            #print(event)
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
            #self.homeSet_temp = 0    
            # sends new values if and only if changed from previous
            resetAxe(self)
            newAxeVal(self)

          #---------------DIRECT---------------------------------------------------------------------------
          elif self.modeHD == 'DIR': 
            if event.type == ecodes.EV_KEY:
              if event.value == 1:
                #-----------gripper------------
                if event.code == Keymap.BTN_TRIANGLE.value:   # gripper = +100
                  self.axe_HD_new[6] = -100.
                elif event.code == Keymap.BTN_CIRCLE.value:   # gripper = +10
                  self.axe_HD_new[6] = 10.
                elif event.code == Keymap.BTN_CROSS.value:    # gripper = -100
                  self.axe_HD_new[6] = 100.
                elif event.code == Keymap.BTN_SQUARE.value:   # gripper = -10
                  self.axe_HD_new[6] = -10.
                #-----------joint 3------------
                elif event.code == Keymap.BTN_R1.value:       # R1 - joint 3 advance 
                  #self.joint3 = -1
                    self.axe_HD_new[3] = 100.
                elif event.code == Keymap.BTN_L1.value:       # L1 - joint 3 advance
                  #self.joint4 = -1
                    self.axe_HD_new[3] = -100.              
                #----------voltmeter------------
                if event.code == Keymap.BTN_PS.value:       # PS button 
                  self.switchVoltmeter()
              #-----------reset joint 3, gripper------------
              elif event.value == 0:
                self.axe_HD_new[6] = 0
                self.axe_HD_new[3] = 0
                #if event.code == Keymap.BTN_R1.value:         # R1 - joint 3 retreat
                #  self.joint3 = 1
                #elif event.code == Keymap.BTN_L1.value:       # L1 - joint 4 retreat
                #  self.joint4 = 1
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
                #self.axe_HD_new[2] = scale * round(self.joint3 * absevent.event.value/max_L2_R2, 5) # Max value: 32768
                self.axe_HD_new[2] = scale * round(absevent.event.value/max_L2_R2, 5) # Max value: 255
              #-----------joint 4------------- 
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":   # L2 
                #self.axe_HD_new[3] = scale * round(self.joint4 * absevent.event.value/max_L2_R2, 5) # Max value: 32768
                self.axe_HD_new[2] = scale * round(-absevent.event.value/max_L2_R2, 5) # Max value: 255
              #-----------go home-------------
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":  # d-pad y
                if event.value == 1:
                    self.goHome()            

            # sends new values if and only if changed from previous
            resetAxe(self)
            newAxeVal(self)
        


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
#     TODO publish!!!!!!  


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

    self.axe_HD_old = clear_tab(self.axe_HD_old)
    self.axe_HD_new = clear_tab(self.axe_HD_new)

#     self.cs.HD_mode_pub.publish(Int8(data = self.modeHDmsg))
#     self.cs.HD_Angles_pub.publish(Int8MultiArray(data = self.axe_HD_new))
    self.HD_mode_pub.publish(Int8(data = self.modeHDmsg))
    self.HD_Angles_pub.publish(Int8MultiArray(data = list(map(int, self.axe_HD_new))))


  # Voltmeter:  Extend <=> Retreat
  def switchVoltmeter(self):
    if self.voltmeter == 0:
      self.voltmeter = 1
    else:
      self.voltmeter = 0
      #     TODO 
    print(self.voltmeter)  
#     self.cs.HD_voltmeter_pub.publish(Int8(data = self.voltmeter))
    self.HD_voltmeter_pub.publish(self.voltmeter)


  def goHome(self):
    self.homeGo = 1
    print(self.homeGo)
    self.HD_homeGo_pub.publish(self.homeGo)
    # reset bool
    self.homeGo = 0
    

  def setHome(self):
    self.homeSet = 1
    print(self.homeSet)
    self.HD_homeSet_pub.publish(self.homeSet)
    # reset bool(s)
    self.homeSet = 0
    self.homeSet_temp = 0  
    
    
    
def eval_axe(axe_value): #Donne le sens de rotation bras robot 32768 est la valeur max renvoyé par la manette
  if axe_value <= -32700:
    return -1
  elif axe_value >= 32700:
    return 1
  elif axe_value > -32700 and axe_value < 32700:
    return 0


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
# if and only if changed from previous
def newAxeVal(self):
  #if (compare_list(self.axe_HD_old, self.axe_HD_new, 1) != 1):
    #print("send HD - angles:\nold:", self.axe_HD_old , ' new:', self.axe_HD_new)
    for k in range(len(self.axe_HD_new)):
      self.axe_HD_old[k] = self.axe_HD_new[k]

    #     TODO 
    print(self.axe_HD_new)

    #     self.cs.HD_Angles_pub.publish(Int8MultiArray(data = self.axe_HD_new))
    self.HD_Angles_pub.publish(Int8MultiArray(data = list(map(int, self.axe_HD_new))))
                               
    
    
# Send new Joint velocities for HD
# if and only if abs(value) > 2
def resetAxe(self):
  reset_small(self.axe_HD_old)
  reset_small(self.axe_HD_new)



if __name__ == "__main__" : 
    gamepad = Gamepad()
    gamepad.run()

    exit()


