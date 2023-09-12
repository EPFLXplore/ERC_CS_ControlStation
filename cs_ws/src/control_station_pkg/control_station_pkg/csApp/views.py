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

import threading
from time import sleep
from tracemalloc import start
from django.http            import HttpResponse, JsonResponse
from django.shortcuts       import render
from django.shortcuts       import redirect

from MVC_node.controller import *
from MVC_node.models.rover  import Task
from manage          import setup

from MVC_node.models import gamepad

from std_msgs.msg import Int8MultiArray, Int8, Bool
from avionics_interfaces.msg import LaserRequest, ServoRequest, SpectroRequest

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

# def handlingdevice(request):

#     state = parseState()
#     #ws_hd.connect(HD_WS_URL)
#     #ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/handlingdevice.html', { 
#         'tab_name': "handlingdevice",
#         'current_state' : state
#     }) 

# def homepage(request):
#     if not request.session.session_key:
#         request.session.create()
#     print("home page requested : " + request.session.session_key)
#     state = parseState()
#     #ws_hp.connect(HP_WS_URL)
#     # ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/homepage.html', { 
#         'tab_name': "homepage",
#         'current_state' : state
#     }) 

# def manualcontrol(request):

#     state = parseState()
#     #ws_man.connect(MAN_WS_URL)
#     #ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/manualcontrol.html', { 
#         'tab_name': "manual",
#         'current_state' : state
#     }) 

# def navigation(request):

#     state = parseState()
#     #ws_nav.connect(NAV_WS_URL)
#     # ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/navigation.html', { 
#         'tab_name': "navigation",
#         'current_state' : state
#     })  

# def science(request):

#     state = parseState()
#     #ws_sc.connect(SC_WS_URL)
#     #ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/science.html', { 
#         'tab_name': "science",
#         'current_state' : state
#     }) 

# def logs(request):

#     state = parseState()
#     #ws_av.connect(AV_WS_URL)
#     #ws_time.connect(TIME_WS_URL)
#     return render(request, 'pages/logs.html', { 
#         'tab_name': "logs",
#         'current_state' : state
#     }) 

# -----------------------------------
# manual control views

def launch_manual(request):
    cs.node.get_logger().info("Manual: Launch")
    cs.controller.pub_Task(1,1)
    cs.rover.setState(Task.MANUAL)
    return JsonResponse({})
    

def abort_manual(request):
    cs.node.get_logger().info("Manual: Abort")
    cs.controller.pub_Task(1,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_manual(request):
    cs.node.get_logger().info("Manual: Wait")
    cs.controller.pub_Task(1,3)
    return JsonResponse({})

def resume_manual(request):
    cs.node.get_logger().info("Manual: Resume")
    cs.controller.pub_Task(1,4)
    
    return JsonResponse({})


# -----------------------------------
# navigation

def launch_nav(request):

    #cs.controller.sendJson(Task.NAVIGATION)

    cs.node.get_logger().info("Navigation: Launch")
    cs.controller.pub_Task(2,1)
    cs.rover.setState(Task.NAVIGATION)
    return JsonResponse({})

def abort_nav(request):
    cs.node.get_logger().info("Navigation: Abort")
    cs.controller.pub_Task(2,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_nav(request):
    cs.node.get_logger().info("Navigation: Wait")
    cs.controller.pub_Task(2,3)
    return JsonResponse({})

def resume_nav(request):
    cs.node.get_logger().info("Navigation: Resume")
    cs.controller.pub_Task(2,4)
    return JsonResponse({})

#def set_nav(request):
#
#
#    
#    cs.controller.pub_nav_goal(x, y, yaw)
#    goal = cs.rover.Nav.getGoal()
#
#    return JsonResponse({})

def nav_goal(request):

    x = float(request.POST.get("x"))
    y = float(request.POST.get("y"))
    yaw = float(request.POST.get("yaw"))

    cs.controller.pub_nav_goal(x, y, yaw)
    return JsonResponse({})

def nav_cancel(request):

    cs.controller.pub_cancel_nav_goal()
    return JsonResponse({})

def nav_starting_point(request):

    x = float(request.POST.get("x"))
    y = float(request.POST.get("y"))
    yaw = float(request.POST.get("yaw"))

    cs.controller.pub_nav_starting_point(x, y, yaw)

    return JsonResponse({})


# -----------------------------------
# Handling device views

def launch_hd(request):
    cs.node.get_logger().info("Maintenance: Launch")
    cs.controller.pub_Task(3,1)
    cs.rover.setState(Task.MAINTENANCE)
    return JsonResponse({})

def abort_hd(request):
    cs.node.get_logger().info("Maintenance: Abort")
    cs.controller.pub_Task(3,2)
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_hd(request):
    cs.node.get_logger().info("Maintenance: Wait")
    cs.controller.pub_Task(3,3)
    return JsonResponse({})

def resume_hd(request):
    cs.node.get_logger().info("Maintenance: Resume")
    cs.controller.pub_Task(3,4)
    return JsonResponse({})

def cancel_hd(request):
    cs.node.get_logger().info("Maintenance: Cancel Goal")
    cs.controller.pub_Task()

def set_id(request):
    cs.rover.HD.set_joint_positions([10,0,0,0,0,0])
    #cs.controller.sendJson(Task.MAINTENANCE)
    id = int(request.POST.get("id")) + 20
    cs.rover.HD.setElemId(id)
    cs.HD_id.publish(Int8(data=id))
    cs.node.get_logger().info("Maintenance: Set HD id to " + str(id))
    #print(cs.rover.HD.getElemId())
    #cs.controller.pub_hd_elemId(id)
    return JsonResponse({})

def set_hd_mode(request):
    mode = int(request.POST.get("mode"))
    cs.rover.HD.setHDMode(mode)
    cs.HD_mode_pub.publish(Int8(data=mode))
    cs.node.get_logger().info("Maintenance: Set HD mode to " +  str(mode))
    return JsonResponse({})


def toggle_hd_laser(request):
    toggle = bool(request.POST.get("toggle"))
    cs.HD_toggle_laser_pub.publish(LaserRequest(enable=toggle))
    return JsonResponse({})

def deploy_hd_voltmeter(request):
    print("deploying voltmeter")
    servoRequest = ServoRequest()
    servoRequest.channel = 1
    if (request.POST.get("deployment") == "open"):
        servoRequest.angle = 110
    else :
        servoRequest.angle = 0
    cs.HD_deploy_voltmeter_pub.publish(servoRequest)

    return JsonResponse({})



# -----------------------------------
# Science views

# TODO STILL NEED TO ADAPT TO NEW SCIENCE COMMANDS
def launch_science(request):
    cs.controller.pub_Task(4,1)
    cs.rover.setState(Task.SCIENCE)
    return JsonResponse({})

def abort_science(request):
    cs.controller.pub_Task(4,2)     #0 -> 2 ?
    cs.rover.setState(Task.IDLE)
    return JsonResponse({})

def wait_science(request):
    cs.controller.pub_Task(4,3)
    return JsonResponse({})

def resume_science(request):
    cs.controller.pub_Task(4,4)
    return JsonResponse({})

# def confirm_science(request):
#     cs.controller.pub_Task(4,2)
#     return JsonResponse({})

# def retry_science(request):
#     cs.controller.pub_Task(4,1)
#     return JsonResponse({})

# def start_timer(request):
#     print("Starting timer")

#     # startThread()
#     return JsonResponse({})

# def set_tube_cmd(request):
#     tube = int(request.POST.get("tube"))
#     operation = int(request.POST.get("operation"))
    
#     cs.controller.selectedTube(tube)
#     cs.controller.selectedOp(operation)

#     print("SC: (operation = ", operation, ", tube = ", tube, ")")
#     cs.rover.setState(Task.SCIENCE)

#     return sc_send_cmd(cs.rover.SC.getCmd())


# def get_humidity(request):
#     return sc_send_cmd(3)


# def get_parameters(request):
#     return sc_send_cmd(4)

# def get_sc_info(request):
#     return sc_send_cmd(5)

# def get_sc_state(request):
#     return sc_send_cmd(6)


def sc_send_cmd(val):
    cs.controller.set_sc_cmd(val)
    print("cmd:", cs.rover.SC.getCmd())
    cs.controller.pub_Task(Task.SCIENCE.value, int(cs.rover.SC.getCmd()))
    return JsonResponse({})

spectro_call = False

def sc_mesure_spectro(request):
    global spectro_call
    if not spectro_call:
        cs.SC_spectro_req.publish(SpectroRequest(measure=True))
        spectro_call = True
        threading.Thread(target=wait_for_spectro).start()
    return JsonResponse(cs.rover.SC.nb_measures)

def wait_for_spectro():
    global spectro_call
    sleep(2)
    spectro_call = False

def sc_reset_spectro(request):
    #Yasmin call ta function
    return JsonResponse({})


# -----------------------------------
# gamepad views

def get_nav_gamepad_profile(request):

    return JsonResponse(gamepad.get_nav_profile())

def get_hd_gamepad_profile(request):

    return JsonResponse(gamepad.get_hd_profile())

def set_nav_gamepad_profile(request):

    return JsonResponse({})

def set_hd_gamepad_profile(request):

    return JsonResponse({})


# -----------------------------------
# cameras views

def enable_cameras(request):
    camera = request.POST.get("index")
    camera_list = list(map(int, camera.split(',')))
    cs.Cam_index_pub.publish(Int8MultiArray(data=camera_list))
    print("camera enabled")
    print(camera_list)
    return JsonResponse({})