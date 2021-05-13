import evdev
from evdev import*
from threading import Thread
import rospy
from xplore_msg.msg import HandlingControl
from geometry_msgs.msg import Twist
import sys

'''
Class Gamepad

@Description: Thread to 

@Attributes:
    -

'''
class Gamepad(Thread):

  def __init__(self):
  # ~ connection search gamepad
    for path in evdev.list_devices():
      self.control = evdev.InputDevice(path)
      if evdev.ecodes.EV_FF in self.control.capabilities():
        self._running = True #variable to stop gamepad thread
        break
    else:
      sys.stderr.write('Failed to find the haptic motor.\n')
      self.control = None

    self.nav_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    self.msg_nav_dir=Twist()
    self.msg_nav_dir.linear.x=0
    self.msg_nav_dir.linear.y=0
    self.msg_nav_dir.linear.z=0
    self.msg_nav_dir.angular.x = 0
    self.msg_nav_dir.angular.y = 0
    self.msg_nav_dir.angular.z = 0
    self.rate =rospy.Rate(10)
    
    self.hd_pub = rospy.Publisher('cmd_hd',HandlingControl, queue_size=1)
    self.HD_control_msg= HandlingControl()
    self.HD_control_msg.mode=0
    self.HD_control_msg.active=clear_tab(self.HD_control_msg.active)
    self.axe_HD_old=[0, 0, 0, 0, 0, 0, 0]
    self.axe_NAV_old=[0., 0.]
    self.axe_HD_new=[0, 0, 0, 0, 0, 0, 0]
    self.axe_NAV_new=[0., 0.]
    
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
    advance = 0
    retreat = 0
    for event in self.control.read_loop():
      if event.type!=0:
        if (self._running)==0:
          break
        #Mode commun Changement Mode etc...
        if event.type == ecodes.EV_KEY:
          if event.value==1:
            if event.code==dec.shaBtn: #Touche Share
              if self.mode == 'NAV':
                self.cmode('HD')
                print(self.mode)
              elif self.mode == 'HD':
                self.cmode('NAV')
                print(self.mode)


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
                  self.HD_control_msg.mode=1
                  self.HD_control_msg.active=clear_tab(self.HD_control_msg.active)
                  self.axe_HD_old=[0, 0, 0, 0, 0, 0, 0]
                  self.axe_HD_new=[0, 0, 0, 0, 0, 0, 0]
                  self.hd_pub.publish(self.HD_control_msg)
                  print('AUTO')
                  self.modeHD='AUTO'
                else:
                  print('MAN')
                  self.modeHD='MAN'
                  self.HD_control_msg.mode=0
                  self.HD_control_msg.active=clear_tab(self.HD_control_msg.active)
                  self.axe_HD_old=[0, 0, 0, 0, 0, 0, 0]
                  self.axe_HD_new=[0, 0, 0, 0, 0, 0, 0]
                  self.hd_pub.publish(self.HD_control_msg)


        if (self.mode)== 'NAV': #PARTIE NAVIGATION--------------------
          if event.type == ecodes.EV_KEY:
            if event.value==1:
              if event.code==dec.xBtn: #Touche A
                  print('NAV')
          if self.modeNAV=='MAN': #MANUEL ----------------------------
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
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
                if (retreat==0):
                  self.axe_NAV_new[0] = round(absevent.event.value/255, 1)
                  advance = 1
                if absevent.event.value==0:
                  advance = 0
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
                if (advance==0):
                  self.axe_NAV_new[0] = round(-absevent.event.value/255, 1)
                  retreat = 1
                if absevent.event.value==0:
                  retreat =0
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":  #Direction sur l axe X du joystick gauche
                if (absevent.event.value>0):
                  self.axe_NAV_new[1] = round(absevent.event.value/32767, 1) #Max value :32768
                else:
                  self.axe_NAV_new[1] = round(absevent.event.value/32768, 1) #Max value :32768

              #Publish variation with round 0.1 to NAV only when it was changed
              if (compare_list(self.axe_NAV_old,self.axe_NAV_new, 0)!=1):
                print("envoi",self.axe_NAV_new ,' ',self.axe_NAV_old)
                self.axe_NAV_old[0] = self.axe_NAV_new[0]
                self.axe_NAV_old[1] = self.axe_NAV_new[1]
                self.msg_nav_dir.linear.x=self.axe_NAV_new[0]
                self.msg_nav_dir.angular.z = self.axe_NAV_new[1]
                self.nav_pub.publish(self.msg_nav_dir)
                
        #Handling Device 
        elif (self.mode)== 'HD': 
          if self.modeHD=='MAN':
            #BOUTON--------------------
            if event.type == ecodes.EV_KEY:
              #Push
              if event.value==1: 
                if event.code==dec.l1Btn and self.axe_HD_new[4]==0: #L1 axe 5 = 1
                  self.axe_HD_new[4]=1
                elif event.code==dec.r1Btn and self.axe_HD_new[4]==0: #R1 axe 5 = -1
                  self.axe_HD_new[4]=-1
                elif event.code==dec.cBtn and self.axe_HD_new[6]==0: #Square button open the gripper
                  self.axe_HD_new[6]=1
                elif event.code==dec.tBtn and self.axe_HD_new[6]==0: #Triangle button close the gripper
                  self.axe_HD_new[6]=-1
              #Release
              elif event.value==0: 
                if event.code==dec.l1Btn: #L1 axe 5 = 1
                  self.axe_HD_new[4]=0
                elif event.code==dec.r1Btn: #R1 axe 5 = -1
                  self.axe_HD_new[4]=0
                elif event.code==dec.cBtn: #Square button Stop the opening
                  self.axe_HD_new[6]=0
                elif event.code==dec.tBtn : #Triangle button Stop the closing
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
              #Axe 6
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#Axe4
                if absevent.event.value>=250:
                  self.axe_HD_new[5] = 1
                else:
                  self.axe_HD_new[5] = 0
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":#Axe4
                if absevent.event.value>=250:
                  self.axe_HD_new[5] = -1
                else:
                  self.axe_HD_new[5] = 0
      
              #envoi valeurs axe si et seulement si il y a eu un changement
            if compare_list(self.axe_HD_old,self.axe_HD_new, 0)!=1:
                print("envoi HD",self.axe_HD_new ,' ',self.axe_HD_old)
                for k in range(len(self.axe_HD_new)):
                  self.axe_HD_old[k] = self.axe_HD_new[k]
                  self.HD_control_msg.active[k]=self.axe_HD_new[k]
                self.hd_pub.publish(self.HD_control_msg)


          elif self.modeHD=='AUTO':#Direct Kinematics
            if event.type == ecodes.EV_KEY:
              if event.value==1:
                if event.code==dec.cBtn: #Touche r1 pince
                  self.axe_HD_new[6]=1
                elif event.code==dec.tBtn : #Touche r1 pince
                  self.axe_HD_new[6]=-1
                elif event.code==dec.l2Btn and self.axe_HD_new[5]==0: #Touche l2 axe Z
                  self.axe_HD_new[2]=1
                elif event.code==dec.r2Btn and self.axe_HD_new[5]==0: #Touche r2 axe Z
                  self.axe_HD_new[2]=-1
                elif event.code==dec.l1Btn : #Touche l1 rotationX
                  self.axe_HD_new[3]=1
                elif event.code==dec.r1Btn : #Touche r1 rotationX
                  self.axe_HD_new[3]=-1

              elif event.value==0:
                if event.code==dec.l2Btn: #Touche l2 axe 6 relacher
                  self.axe_HD_new[2]=0
                elif event.code==dec.r2Btn: #Touche r2 axe 6 relacher
                  self.axe_HD_new[2]=0
                elif event.code==dec.l1Btn: #Touche l1 rotationX
                  self.axe_HD_new[3]=0
                elif event.code==dec.r1Btn: #Touche r1 rotationX
                  self.axe_HD_new[3]=0
                elif event.code==dec.cBtn: #Touche r1 pince
                  self.axe_HD_new[6]=0
                elif event.code==dec.tBtn : #Touche r1 pince
                  self.axe_HD_new[6]=0

            elif event.type == ecodes.EV_ABS:
              absevent = categorize(event)
              if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":#Axe Y
                self.axe_HD_new[1] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#Axe X
                self.axe_HD_new[0] = eval_axe(absevent.event.value)
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":#Rotz
                self.axe_HD_new[5] = absevent.event.value
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":#RotY
                self.axe_HD_new[4] = absevent.event.value
              #Axe Z
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#AxeZ
                if absevent.event.value>=250:
                  self.axe_HD_new[2] = 1
                else:
                  self.axe_HD_new[2] = 0
              elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":#AxeZ
                if absevent.event.value>=250:
                  self.axe_HD_new[2] = -1
                else:
                  self.axe_HD_new[2] = 0


            #envoi valeurs axe si et seulement si il y a eu un changement
            if compare_list(self.axe_HD_old,self.axe_HD_new, 0)!=1:
                print("envoi HD",self.axe_HD_new ,' ',self.axe_HD_old)
                for k in range(len(self.axe_HD_new)):
                  self.axe_HD_old[k] = self.axe_HD_new[k]
                  self.HD_control_msg.active[k]=self.axe_HD_new[k]
                self.hd_pub.publish(self.HD_control_msg)

        elif (self.mode)== 'SC':
          if event.type == ecodes.EV_KEY:
            # ~ print(categorize(event))
            if event.value==1:
              if event.code==304: #Touche A
                  print('SC')


  def cmode(self, mode):
    self.mode = mode

def eval_axe(axe_value): #Donne le sens de rotation bras robot 32768 est la valeur max renvoyé par la manette
  if axe_value <= -32700:
    return -1
  elif axe_value >= 32700:
    return 1
  elif axe_value > -32700 and axe_value < 32700:
    return 0

def compare_list(list1, list2, tolerance):
  #compare deux liste avec une certaine tolerance
  for k in range(len(list1)):
    if (list1[k]+tolerance >= list2[k] and list1[k]-tolerance <= list2[k])!=1:
      return 0
  return 1

def clear_tab(tab):
  #Clear the tab
  for k in range(len(tab)):
    tab[k]=0
  return tab
  
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
