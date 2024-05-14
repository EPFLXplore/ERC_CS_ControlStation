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
from django.http            import JsonResponse


import math

from MVC_node.new_controller import *
from manage          import setup

from MVC_node.models import gamepad

from std_msgs.msg import Int8MultiArray, Int8, Bool, String
from custom_msg.msg import ServoRequest, SpectroRequest

# ===============================================================
# Control Station setup

cs = setup().CONTROL_STATION

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

# ----------------------------------
# change system mode

def change_system_mode(request):
    system = request.POST.get("system")
    mode = request.POST.get("mode")
    cs.change_mode_system.send_request(system, mode)
    print("send service request to change the subsystem " + system + " to " + mode)
    return JsonResponse({})