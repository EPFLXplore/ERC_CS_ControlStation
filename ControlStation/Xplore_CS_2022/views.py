from curses.ascii import ctrl
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader

import sys
from subprocess import run, PIPE

from CS_node import *
from Controller import *



#PATHS
CONTROLLER_PATH = '//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py'

def handlingdevice(request):
    return render(request, 'pages/handlingdevice.html')

def homepage(request):
    return render(request, 'pages/homepage.html')

def manualcontrol(request):
    return render(request, 'pages/manualcontrol.html')

def navigation(request):
    return render(request, 'pages/navigation.html')

def science(request):
    return render(request, 'pages/science.html')

def avionics(request):
    return render(request, 'pages/avionics.html')

ctrler = Controller()
#STATE BUTTONS

# TASK: 
    #       - Manual      = 1 
    #       - Navigation  = 2 
    #       - Maintenance = 3
    #       - Science     = 4
    #
    # INSTR:  
    #       - Launch = 1 
    #       - Abort  = 2 
    #       - Wait   = 3 
    #       - Resume = 4 
    #       - Retry  = 5


###############################
#             MANUAL          #
###############################

def launch_manual(request):
    rospy.loginfo("Manual: Launch")
    ctrler.pub_Task(1,1)
    return redirect('/Xplore_CS_2022/manualcontrol/')

def abort_manual(request):
    rospy.loginfo("Manual: Abort")
    ctrler.pub_Task(1,2)
    return redirect('/Xplore_CS_2022/manualcontrol/')

def wait_manual(request):
    rospy.loginfo("Manual: Wait")
    ctrler.pub_Task(1,3)
    return redirect('/Xplore_CS_2022/manualcontrol/')

def resume_manual(request):
    rospy.loginfo("Manual: Resume")
    ctrler.pub_Task(1,4)
    return redirect('/Xplore_CS_2022/manualcontrol/')


###############################
#          NAVIGATION         #
###############################

def launch_nav(request):
    rospy.loginfo("Navigation: Launch")
    ctrler.pub_Task(2,1)
    return redirect('/Xplore_CS_2022/navigation/')

def abort_nav(request):
    rospy.loginfo("Navigation: Abort")
    ctrler.pub_Task(2,2)
    return redirect('/Xplore_CS_2022/navigation/')

def wait_nav(request):
    rospy.loginfo("Navigation: Wait")
    ctrler.pub_Task(2,3)
    return redirect('/Xplore_CS_2022/navigation/')

def resume_nav(request):
    rospy.loginfo("Navigation: Resume")
    ctrler.pub_Task(2,4)
    return redirect('/Xplore_CS_2022/navigation/')



###############################
#       HANDLING DEVICE       #
###############################

def launch_hd(request):
    rospy.loginfo("Maintenance: Launch")
    ctrler.pub_Task(3,1)
    return redirect('/Xplore_CS_2022/handlingdevice/')

def abort_hd(request):
    rospy.loginfo("Maintenance: Abort")
    ctrler.pub_Task(3,2)
    return redirect('/Xplore_CS_2022/handlingdevice/')

def wait_hd(request):
    rospy.loginfo("Maintenance: Wait")
    ctrler.pub_Task(3,3)
    return redirect('/Xplore_CS_2022/handlingdevice/')

def resume_hd(request):
    rospy.loginfo("Maintenance: Resume")
    ctrler.pub_Task(3,4)
    return redirect('/Xplore_CS_2022/handlingdevice/')

def retry_hd(request):
    rospy.loginfo("Maintenance: Retry")
    ctrler.pub_Task(3,5)
    return redirect('/Xplore_CS_2022/handlingdevice/')

#Science
# TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
def launch_science(request):
    rospy.loginfo("Science: ???")
    ctrler.pub_Task(4,1)
    return redirect('/Xplore_CS_2022/science/')

def abort_science(request):
    ctrler.pub_Task(4,2)
    return redirect('/Xplore_CS_2022/science/')

def wait_science(request):
    ctrler.pub_Task(4,3)
    return redirect('/Xplore_CS_2022/science/')

def resume_science(request):
    ctrler.pub_Task(4,4)
    return redirect('/Xplore_CS_2022/science/')

def retry_science(request):
    ctrler.pub_Task(4,5)
    return redirect('/Xplore_CS_2022/science/')

