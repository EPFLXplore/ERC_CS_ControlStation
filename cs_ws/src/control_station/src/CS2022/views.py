#
# 24/07/2022
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           Roman Danylovych
#           roman.danylovych@epfl.ch
#
# @brief: 
# 
# -------------------------------------------------------------------------------

# =============================================================
# Libraries


from django.http            import HttpResponse, JsonResponse
from django.shortcuts       import render
from django.shortcuts       import redirect

from src.cs_node            import *
from src.controller         import *
from manage                 import setup



# ===============================================================
# Control Station setup

cs = setup().CONTROL_STATION

# ===============================================================
# Django views


# ------------------------------------
# General views

def handlingdevice(request):

    ws_hd.connect(HD_WS_URL)
    return render(request, 'pages/handlingdevice.html', { 
        'tab_name': "handlingdevice"
    }) 

def homepage(request):

    ws_hp.connect(HP_WS_URL)
    return render(request, 'pages/homepage.html', { 
        'tab_name': "homepage"
    }) 

def manualcontrol(request):

    ws_man.connect(MAN_WS_URL)
    return render(request, 'pages/manualcontrol.html', { 
        'tab_name': "manualcontrol"
    }) 

def navigation(request):

    ws_nav.connect(NAV_WS_URL)
    return render(request, 'pages/navigation.html', { 
        'tab_name': "navigation",
        'debug' : "debug_data"
    })  

def science(request):

    ws_sc.connect(SC_WS_URL)
    return render(request, 'pages/science.html', { 
        'tab_name': "science"
    }) 

def avionics(request):

    ws_av.connect(AV_WS_URL)
    return render(request, 'pages/avionics.html', { 
        'tab_name': "avionics"
    }) 

# -----------------------------------
# manual control views

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

    # return empty json response to update the page without refreshing
    return JsonResponse({})

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
# Handling device views

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
# Science views

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

