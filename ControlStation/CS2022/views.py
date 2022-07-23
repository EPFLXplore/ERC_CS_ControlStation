# =============================================================
# Libraries

from curses.ascii       import ctrl
from email.policy import HTTP
from urllib.request import HTTPRedirectHandler
from django.http        import HttpResponse
from django.shortcuts   import render
from django.shortcuts   import redirect
from django.template    import loader
from subprocess         import run, PIPE

from urllib3 import HTTPResponse
from src.cs_node        import *
from src.controller     import *

from manage import setup

import sys



# ===============================================================

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

# cs.controller = cs.controller()
cs = setup().CONTROL_STATION

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

# -----------------------------------
# manual control

def launch_manual(request):
    rospy.loginfo("Manual: Launch")
    cs.controller.pub_Task(1,1)
    return redirect('/CS2022/manualcontrol/')

def abort_manual(request):
    rospy.loginfo("Manual: Abort")
    cs.controller.pub_Task(1,2)
    return redirect('/CS2022/manualcontrol/')

def wait_manual(request):
    rospy.loginfo("Manual: Wait")
    cs.controller.pub_Task(1,3)
    return redirect('/CS2022/manualcontrol/')

def resume_manual(request):
    rospy.loginfo("Manual: Resume")
    cs.controller.pub_Task(1,4)
    return redirect('/CS2022/manualcontrol/')


# -----------------------------------
# navigation

def launch_nav(request):
    rospy.loginfo("Navigation: Launch")
    cs.controller.pub_Task(2,1)
    return redirect('/CS2022/navigation/')

def abort_nav(request):
    rospy.loginfo("Navigation: Abort")
    cs.controller.pub_Task(2,2)
    return redirect('/CS2022/navigation/')

def wait_nav(request):
    rospy.loginfo("Navigation: Wait")
    cs.controller.pub_Task(2,3)
    return redirect('/CS2022/navigation/')

def resume_nav(request):
    rospy.loginfo("Navigation: Resume")
    cs.controller.pub_Task(2,4)
    return redirect('/CS2022/navigation/')



# -----------------------------------
# handling device

def launch_hd(request):
    rospy.loginfo("Maintenance: Launch")
    cs.controller.pub_Task(3,1)
    return redirect('/CS2022/handlingdevice/')

def abort_hd(request):
    rospy.loginfo("Maintenance: Abort")
    cs.controller.pub_Task(3,2)
    return redirect('/CS2022/handlingdevice/')

def wait_hd(request):
    rospy.loginfo("Maintenance: Wait")
    cs.controller.pub_Task(3,3)
    return redirect('/CS2022/handlingdevice/')

def resume_hd(request):
    rospy.loginfo("Maintenance: Resume")
    cs.controller.pub_Task(3,4)
    return redirect('/CS2022/handlingdevice/')

def retry_hd(request):
    rospy.loginfo("Maintenance: Retry")
    cs.controller.pub_Task(3,5)
    return redirect('/CS2022/handlingdevice/')

# -----------------------------------
# science

# TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
def launch_science(request):
    rospy.loginfo("Science: ???")
    cs.controller.pub_Task(4,1)
    return redirect('/CS2022/science/')

def abort_science(request):
    cs.controller.pub_Task(4,2)
    return redirect('/CS2022/science/')

def wait_science(request):
    cs.controller.pub_Task(4,3)
    return redirect('/CS2022/science/')

def resume_science(request):
    cs.controller.pub_Task(4,4)
    return redirect('/CS2022/science/')

def retry_science(request):
    cs.controller.pub_Task(4,5)
    return redirect('/CS2022/science/')

