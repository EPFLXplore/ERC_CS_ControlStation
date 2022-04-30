'''
@File  :

@Author: Emma Gaia Poggiolini
'''
import evdev
import rospy
from evdev             import*
from threading         import Thread

# from xplore_msg.msg    import HandlingControl
from geometry_msgs.msg import Twist

import sys

# from CS_node import CS
from keyMap            import *
from std_msgs.msg import Int8MultiArray, Int8


'''
Class Gamepad

@Description: Thread to 

@Attributes:
    -

'''
class Gamepad(Thread):
  print("coucou")
  
  devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
  #### print("#### debug(1): check list of devices connected") 
  # for device in devices:
  #  print(device.path, device.name, device.phys)     

  def __init__(self, cs):

    self.cs = cs

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

    # define ROS topics to publish 
    self.rate = rospy.Rate(10)

    self.mode = 'NAV' #or 'HD'

    # NAV : 
    #self.modeNAV = 'MAN' #or 'AUTO' 

    # self.nav_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) # need to publish topic  #TODO
    # declare and initialize msg_nav_dir
    self.msg_nav_dir = Twist()
    self.msg_nav_dir.linear.x  = 0
    self.msg_nav_dir.linear.y  = 0  # always zero
    self.msg_nav_dir.linear.z  = 0  # always zero
    self.msg_nav_dir.angular.x = 0  # always zero
    self.msg_nav_dir.angular.y = 0  # always zero
    self.msg_nav_dir.angular.z = 0
    self.rate = rospy.Rate(10)

    self.axe_NAV_old = [0., 0.]  # [.linear.x, .angular.z]
    self.axe_NAV_new = [0., 0.]

    # HD :
    # self.hd_pub = rospy.Publisher('cmd_hd', Int8MultiArray, queue_size=1) #Object Roman #TODO
    # self.HD_control_msg = HandlingControl()
    # self.HD_control_msg.mode = 3  # 2='INV', 3='DIR' 
    #self.HD_control_msg.active = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # intialize every joint to 0 
    self.axe_HD_old = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_new = [0, 0, 0, 0, 0, 0, 0]
    self.gripper_old = [0, 0, 0]
    self.gripper_new = [0, 0, 0]
    
    self.modeHD = 'DIR' #or 'INV'



  # what is this for ??
  # def connect(self):
  #   for path in evdev.list_devices():
  #     self.control = evdev.InputDevice(path)
  #     if evdev.ecodes.EV_FF in self.control.capabilities():
  #       self._running = True #variable arret thread
  #       break
  #   else:
  #     sys.stderr.write('Failed to find the haptic motor.\n')
  #     self.control = None


  def run (self):
    #dec = Decode_manette()
    advance = 0
    retreat = 0
    for event in self.control.read_loop():
      if event.type != 0:
        if (self._running) == 0: # when self._running == False  run() stops
          break
        # EV_KEY describes state changes of device
        if event.type == ecodes.EV_KEY:
          if event.value == 1:
            print("before SHARE button") #TODO
            print(event.code) #TODO
            print(Keymap.BTN_SHARE.value) #TODO
            if event.code == Keymap.BTN_SHARE.value: #Keymap.BTN_SHARE: # Share Button => switch NAV <=> HD
              print("SHARE pressed") #TODO
              self.switchNAV_HD()

            # switching  DIR <=> INV only when in HD     
            if event.code == Keymap.BTN_OPTIONS.value:
              if self.mode == 'HD':
                self.switchDIR_INV()


        if (self.mode) == 'NAV': # NAVIGATION--------------------
          if event.type == ecodes.EV_KEY:
            if event.value == 1:
              # R2 => advance: positive .linear.x
              print(event.code)
              if event.code == Keymap.BTN_R2.value: 
                print("Button R2") #TODO 
                if event.type == ecodes.EV_ABS:
                  absevent = categorize(event)
                  if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":  # is this correct? 
                    if (retreat == 0):  # advance (only if not retreating)
                      self.axe_NAV_new[0] = round(absevent.event.value/255, 1)  # why /255 ?
                      advance = 1
                    if absevent.event.value == 0:  # stay still
                      advance = 0
              # L2 => retreat: negative .linear.x
              if event.code == Keymap.BTN_L2.value: 
                if event.type == ecodes.EV_ABS:
                  absevent = categorize(event)
                  if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":
                    if (advance == 0):  # go backwards (only if not retreating)
                      self.axe_NAV_new[0] = round(-absevent.event.value/255, 1)
                      retreat = 1
                    if absevent.event.value == 0:  # stay still
                      retreat = 0
          #     if event.code == Keymap.BTN_CROSS: #Touche A
          #         print('NAV')
          # if self.modeNAV == 'MAN': #MANUEL ----------------------------
            # ~ Configuration 2 for NAV
            # ~ if event.type == ecodes.EV_ABS:
              # ~ absevent = categorize(event)
              # ~ if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                # ~ self.axe_NAV_new[0] = -absevent.event.value
              # ~ if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
                # ~ self.axe_NAV_new[1] = -absevent.event.value
                
            # ~ Configuration 1 for NAV
          if event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":  # x-axis of R3 
              if (absevent.event.value > 0):
                self.axe_NAV_new[1] = round(absevent.event.value/32767, 1) # Max value :32768
              else:
                self.axe_NAV_new[1] = round(absevent.event.value/32768, 1) # Max value :32768

            # if event.type == ecodes.EV_ABS:
            #   absevent = categorize(event)
              # if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
              #   if (retreat == 0):  # advance (only if not retreating)
              #     self.axe_NAV_new[0] = round(absevent.event.value/255, 1)
              #     advance = 1
              #   if absevent.event.value == 0:  # stay still
              #     advance = 0
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
              #   if (advance == 0):  # go backwards (only if not retreating)
              #     self.axe_NAV_new[0] = round(-absevent.event.value/255, 1)
              #     retreat = 1
              #   if absevent.event.value == 0:  # stay still
              #     retreat = 0
              # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":  #Direction sur l axe X du joystick gauche
              #   if (absevent.event.value > 0):
              #     self.axe_NAV_new[1] = round(absevent.event.value/32767, 1) #Max value :32768
              #   else:
              #     self.axe_NAV_new[1] = round(absevent.event.value/32768, 1) #Max value :32768

              # Publish variation with round 0.1 to NAV only when it was changed
              if (compare_list(self.axe_NAV_old, self.axe_NAV_new, 0) != 1):
                print("send", self.axe_NAV_new , ' ', self.axe_NAV_old)  
                self.axe_NAV_old[0] = self.axe_NAV_new[0]
                self.axe_NAV_old[1] = self.axe_NAV_new[1]
                self.msg_nav_dir.linear.x = self.axe_NAV_new[0]
                self.msg_nav_dir.angular.z = self.axe_NAV_new[1]
                self.cs.Nav_Joystick_pub.publish(self.msg_nav_dir) #-------------------TODO
                
        # Handling Device 
        elif (self.mode) == 'HD': 
          if self.modeHD == 'INV':
            # BUTTON--------------------
            if event.type == ecodes.EV_KEY:
              # Push
              if event.value == 1: 
                if event.code == Keymap.BTN_R1.value and self.axe_HD_new[4] == 0: # R1 joint 4 = 1
                  self.axe_HD_new[3] = 1
                elif event.code == Keymap.BTN_L1.value and self.axe_HD_new[4] == 0: # L1 joint 4 = -1
                  self.axe_HD_new[3] = -1
                elif event.code == Keymap.BTN_SQUARE.value and self.axe_HD_new[6] == 0: # Square button open the gripper
                  self.axe_HD_new[6] = 1
                elif event.code == Keymap.BTN_CROSS.value and self.axe_HD_new[6] == 0: # Cross button close the gripper
                  self.axe_HD_new[6] = -1
                # R2 => gripper rise: positive z
                elif event.code == Keymap.BTN_R2.value: 
                  if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":  # is this correct? 
                      self.gripper_new[2] = eval_axe(absevent.event.value)
                # L2 => gripper drop: negative z
                elif event.code == Keymap.BTN_L2.value: 
                  if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":
                      self.gripper_new[2] = eval_axe(-absevent.event.value)
              # Release
              elif event.value == 0: 
                if event.code == Keymap.BTN_R1.value: # R1 joint 4 = 1
                  self.axe_HD_new[3] = 0
                elif event.code == Keymap.BTN_L1.value: # L1 joint 4 = -1
                  self.axe_HD_new[3] = 0
                elif event.code == Keymap.BTN_SQUARE.value: # Square button Stop the opening
                  self.axe_HD_new[6] = 0
                elif event.code == Keymap.BTN_CROSS.value: # Triangle button Stop the closing
                  self.axe_HD_new[6] = 0
            # AXE-------------------------
            elif event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X": # joint 5 L3 left & right 
                self.axe_HD_new[4] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y": # joint 6 L3 up & down
                self.axe_HD_new[5] = eval_axe(absevent.event.value)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX": # gripper move along x-axis
                self.gripper_new[0] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY": # gripper move along y-axis
                self.gripper_new[1] = eval_axe(absevent.event.value)

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


          elif self.modeHD == 'DIR': # Direct Kinematics
            if event.type == ecodes.EV_KEY:
              if event.value == 1:
                joint = 6
                if event.code == Keymap.BTN_R1.value: # joint 1
                  joint = 0
                elif event.code == Keymap.BTN_L1.value: # joint 2
                  joint = 1
                elif event.code == Keymap.BTN_SQUARE.value: # joint 3
                  joint = 2
                elif event.code == Keymap.BTN_CROSS.value: # joint 4
                  joint = 3
                elif event.code == Keymap.BTN_TRIANGLE.value: # joint 5
                  joint = 4
                elif event.code == Keymap.BTN_CIRCLE.value: # joint 6
                  joint = 5
                elif event.code == Keymap.BTN_SQUARE.value and self.axe_HD_new[6] == 0: # Square button open the gripper
                  self.axe_HD_new[6] = 1
                elif event.code == Keymap.BTN_CROSS.value and self.axe_HD_new[6] == 0: # Cross button close the gripper
                  self.axe_HD_new[6] = -1
                # R2 => gripper rise: positive z
                elif event.code == Keymap.BTN_R2.value: 
                  if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":  # is this correct? 
                      self.gripper_new[2] = eval_axe(absevent.event.value)
                # L2 => gripper drop: negative z
                elif event.code == Keymap.BTN_L2.value: 
                  if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_PRESSURE":
                      self.gripper_new[2] = eval_axe(-absevent.event.value)
              # release gripper buttons
              elif event.value == 0: 
                if event.code == Keymap.BTN_SQUARE.value: # Square button Stop the opening
                  self.axe_HD_new[6] = 0
                elif event.code == Keymap.BTN_CROSS.value: # Triangle button Stop the closing
                  self.axe_HD_new[6] = 0
            # AXE-------------------------  
            if event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y": # joint L3 up & down
                print(-eval_axe(absevent.event.value))
                self.axe_HD_new[joint] = -eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX": # gripper move along x-axis
                self.gripper_new[0] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY": # gripper move along y-axis
                self.gripper_new[1] = eval_axe(absevent.event.value)

              # if event.value == 1:
              #   if event.code == dec.cBtn: #Touche r1 pince
              #     self.axe_HD_new[6]=1
              #   elif event.code==dec.tBtn : #Touche r1 pince
              #     self.axe_HD_new[6]=-1
              #   elif event.code==dec.l2Btn and self.axe_HD_new[5]==0: #Touche l2 axe Z
              #     self.axe_HD_new[2]=1
              #   elif event.code==dec.r2Btn and self.axe_HD_new[5]==0: #Touche r2 axe Z
              #     self.axe_HD_new[2]=-1
              #   elif event.code==dec.l1Btn : #Touche l1 rotationX
              #     self.axe_HD_new[3]=1
              #   elif event.code==dec.r1Btn : #Touche r1 rotationX
              #     self.axe_HD_new[3]=-1

              # elif event.value==0:
              #   if event.code==dec.l2Btn: #Touche l2 axe 6 relacher
              #     self.axe_HD_new[2]=0
              #   elif event.code==dec.r2Btn: #Touche r2 axe 6 relacher
              #     self.axe_HD_new[2]=0
              #   elif event.code==dec.l1Btn: #Touche l1 rotationX
              #     self.axe_HD_new[3]=0
              #   elif event.code==dec.r1Btn: #Touche r1 rotationX
              #     self.axe_HD_new[3]=0
              #   elif event.code==dec.cBtn: #Touche r1 pince
              #     self.axe_HD_new[6]=0
              #   elif event.code==dec.tBtn : #Touche r1 pince
              #     self.axe_HD_new[6]=0

            # elif event.type == ecodes.EV_ABS:
            #   absevent = categorize(event)
            #   if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":#Axe Y
            #     self.axe_HD_new[1] = eval_axe(absevent.event.value)
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#Axe X
            #     self.axe_HD_new[0] = eval_axe(absevent.event.value)
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":#Rotz
            #     self.axe_HD_new[5] = absevent.event.value
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":#RotY
            #     self.axe_HD_new[4] = absevent.event.value
            #   #Axe Z
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#AxeZ
            #     if absevent.event.value>=250:
            #       self.axe_HD_new[2] = 1
            #     else:
            #       self.axe_HD_new[2] = 0
            #   elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":#AxeZ
            #     if absevent.event.value>=250:
            #       self.axe_HD_new[2] = -1
            #     else:
            #       self.axe_HD_new[2] = 0

            # sends new values if and only if changed from previous
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

  # Switching MAN <=> AUTO 
  # when in HD mode
  def switchDIR_INV(self):  # NOT IDEAL TO PASS SELF !!!!!!
    if self.modeHD == 'INV':
      # self.HD_control_msg.mode = 1
      print('DIR')
      self.modeHD = 'DIR'
    else:
      # self.HD_control_msg.mode = 0
      print('INV')
      self.modeHD = 'INV'
    # self.HD_control_msg.active = clear_tab(self.HD_control_msg.active)
    self.axe_HD_old = [0, 0, 0, 0, 0, 0, 0]
    self.axe_HD_new = [0, 0, 0, 0, 0, 0, 0] 
    self.gripper_old = [0, 0, 0]
    self.gripper_new = [0, 0, 0]
    # self.hd_pub.publish(self.HD_control_msg)


    # self.cs.HD_mode_pub.publish(Int8(data=self.HD_control_msg.mode))
    self.cs.HD_Angles_pub.publish(Int8MultiArray(data = self.axe_HD_new))
    # ADDED 
    self.cs.HD_InvManual_Coord_pub.publish(Int8MultiArray(data = self.gripper_new))




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

# Clear array 
def clear_tab(tab):
  for k in range(len(tab)):
    tab[k]=0
  return tab
  
# WHAT IS THIS FOR ????????
# class Decode_manette():
#   def __init__(self):
#     self.xBtn = 304
#     self.oBtn = 305
#     self.tBtn = 307
#     self.cBtn = 308
#     self.l1Btn = 310
#     self.r1Btn = 311
#     self.l2Btn = 312
#     self.r2Btn = 313
#     self.optBtn = 315
#     self.shaBtn = 314
#     self.psBtn = 316
#     self.l3Btn = 317
#     self.r3Btn = 318

# Send new Axe values for HD
# if and only if changed from previous
def newAxeVal(self):
  if (compare_list(self.axe_HD_old, self.axe_HD_new, 0) != 1) or (compare_list(self.gripper_old, self.gripper_new, 0) != 1):
    print("send HD - angles: old:", self.axe_HD_old , ' new: ', self.axe_HD_new, "gripper: old:", self.gripper_old, ' new: ', self.gripper_new)
    for k in range(len(self.axe_HD_new)):
      self.axe_HD_old[k] = self.axe_HD_new[k]
      # self.HD_control_msg.active[k] = self.axe_HD_new[k]
    for k in range(len(self.gripper_old)):
      self.gripper_new = self.gripper_old
      # self.HD_control_msg.active[k + len(self.axe_HD_new)] = self.gripper_new[k]
    #self.hd_pub.publish(self.HD_control_msg)

    self.cs.HD_Angles_pub.publish(Int8MultiArray(data = self.axe_HD_new))
    self.cs.HD_InvManual_Coord_pub.publish(Int8MultiArray(data = self.gripper_new))


# send zero when stop increasing velocity 