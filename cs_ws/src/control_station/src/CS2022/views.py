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


from tracemalloc import start
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
# utils

def parseState():
    
    s = cs.rover.getState()

    if s == Task.IDLE.value:
        state = "Idle"
    elif s == Task.NAVIGATION.value:
        state = "Navigation"
    elif s == Task.MAINTENANCE.value:
        state = "Maintenance"
    elif s == Task.SCIENCE.value:
        state = "Science"
    elif s == Task.WAITING.value:
        state = "Waiting"
    else :
        state = "ManualControl"

    return state
    



# ===============================================================
# Django views


# ------------------------------------
# General views

def handlingdevice(request):

    state = parseState()
    ws_hd.connect(HD_WS_URL)
    ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/handlingdevice.html', { 
        'tab_name': "handlingdevice",
        'current_state' : state
    }) 

def homepage(request):

    state = parseState()
    ws_hp.connect(HP_WS_URL)
    # ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/homepage.html', { 
        'tab_name': "homepage",
        'current_state' : state
    }) 

def manualcontrol(request):

    state = parseState()
    ws_man.connect(MAN_WS_URL)
    # ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/manualcontrol.html', { 
        'tab_name': "manual",
        'current_state' : state
    }) 

def navigation(request):

    state = parseState()

    ws_nav.connect(NAV_WS_URL)
    # ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/navigation.html', { 
        'tab_name': "navigation",
        'current_state' : state
    })  

def science(request):

    state = parseState()
    ws_sc.connect(SC_WS_URL)
    ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/science.html', { 
        'tab_name': "science",
        'current_state' : state
    }) 

def logs(request):

    state = parseState()
    ws_av.connect(AV_WS_URL)
    ws_time.connect(TIME_WS_URL)
    return render(request, 'pages/logs.html', { 
        'tab_name': "logs",
        'current_state' : state
    }) 

# -----------------------------------
# manual control views

def launch_manual(request):
    rospy.loginfo("Manual: Launch")
    cs.controller.pub_Task(1,1)
    cs.rover.setState(Task.MANUAL)
    return JsonResponse({})
    

def abort_manual(request):
    rospy.loginfo("Manual: Abort")
    cs.controller.pub_Task(1,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_manual(request):
    rospy.loginfo("Manual: Wait")
    cs.controller.pub_Task(1,3)
    return JsonResponse({})

def resume_manual(request):
    rospy.loginfo("Manual: Resume")
    cs.controller.pub_Task(1,4)
    
    return JsonResponse({})


# -----------------------------------
# navigation

def launch_nav(request):
    rospy.loginfo("Navigation: Launch")
    cs.controller.pub_Task(2,1)
    cs.rover.setState(Task.NAVIGATION)
    # return empty json response to update the page without refreshing
    return JsonResponse({})

def abort_nav(request):
    rospy.loginfo("Navigation: Abort")
    cs.controller.pub_Task(2,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_nav(request):
    rospy.loginfo("Navigation: Wait")
    cs.controller.pub_Task(2,3)
    return JsonResponse({})

def resume_nav(request):
    rospy.loginfo("Navigation: Resume")
    cs.controller.pub_Task(2,4)
    return JsonResponse({})

def set_nav(request):

    x = float(request.POST.get("x"))
    y = float(request.POST.get("y"))
    yaw = float(request.POST.get("yaw"))
    
    cs.controller.pub_nav_goal(x, y, yaw)
    goal = cs.rover.Nav.getGoal()
    print("the goal is (x = %.2f, y = %.2f, yaw = %.2f):", goal[0], goal[1], goal[2])

    return JsonResponse({})

# -----------------------------------
# Handling device views

def launch_hd(request):
    rospy.loginfo("Maintenance: Launch")
    cs.controller.pub_Task(3,1)
    cs.rover.setState(Task.MAINTENANCE)
    return JsonResponse({})

def abort_hd(request):
    rospy.loginfo("Maintenance: Abort")
    cs.controller.pub_Task(3,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_hd(request):
    rospy.loginfo("Maintenance: Wait")
    cs.controller.pub_Task(3,3)
    return JsonResponse({})

def resume_hd(request):
    rospy.loginfo("Maintenance: Resume")
    cs.controller.pub_Task(3,4)
    return JsonResponse({})

def retry_hd(request):
    rospy.loginfo("Maintenance: Retry")
    cs.controller.pub_Task(3,5)
    return JsonResponse({})

def set_id(request):
    id = int(request.POST.get("id"))
    print(cs.rover.HD.getElemId())
    cs.controller.pub_hd_elemId(id)
    return JsonResponse({})

# -----------------------------------
# Science views

# TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
def launch_science(request):
    rospy.loginfo("Science: ???")
    cs.controller.pub_Task(4,1)
    cs.rover.setState(Task.SCIENCE)
    return JsonResponse({})

def abort_science(request):
    cs.controller.pub_Task(4,2)
    cs.rover.setState(Task.IDLE)
    print("Aborting Science")
    return JsonResponse({})

def wait_science(request):
    cs.controller.pub_Task(4,3)
    return JsonResponse({})

def resume_science(request):
    cs.controller.pub_Task(4,4)
    return JsonResponse({})

def retry_science(request):
    cs.controller.pub_Task(4,5)
    return JsonResponse({})

def start_timer(request):

    
    # startThread()
    return JsonResponse({})

def set_tube_cmd(request):
    tube = int(request.POST.get("tube"))
    operation = int(request.POST.get("operation"))
    
    cs.controller.selectedTube(tube)
    cs.controller.selectedOp(operation)

    print("SC: (operation = ", operation, ", tube = ", tube, ")")
    print("cmd: ", cs.rover.SC.getCmd())

    #cs.controller.pub_Task(Task.SCIENCE.value, int(cs.rover.SC.getCmd()))
    #return JsonResponse({})
    return sc_send_cmd()


def get_humidity(request):
    cs.controller.set_sc_cmd(3)
    print("cmd:", cs.rover.SC.getCmd())

    cs.controller.pub_Task(Task.SCIENCE.value, int(cs.rover.SC.getCmd()))

    return JsonResponse({})


def get_parameters(request):
    cs.controller.set_sc_cmd(4)
    print("cmd:", cs.rover.SC.getCmd())

    return sc_send_cmd()


def sc_send_cmd():
    cs.controller.pub_Task(Task.SCIENCE.value, int(cs.rover.SC.getCmd()))
    return JsonResponse({})
