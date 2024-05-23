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
import queue

from std_msgs.msg import Int8MultiArray, Int8, Bool, String
from custom_msg.msg import ServoRequest, SpectroRequest
from geometry_msgs.msg import Pose2D

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
    system = int(request.POST.get("system"))
    mode = int(request.POST.get("mode"))

    q = queue.Queue()
    thr = threading.Thread(target=cs.controller.send_request_system, args=(system, mode, q))
    thr.start()
    thr.join()  # Wait for the thread to complete

    # Retrieve the result from the queue
    result = q.get()
    if result:

        system_state, error_type, error_message = result
        return JsonResponse({"status": system_state, "error_type": error_type, "error_message": error_message})
    else:
        raise Exception("error service")

# ----------------------------------
# cancel all actions



def cancel_all_actions():
    print("cancelling all goals")
    cancel_actions_(cs.controller.nav_action, "navigation")
    cancel_actions_(cs.controller.hd_action, "handling_device")
    cancel_actions_(cs.controller.drill_action, "drill")

    return JsonResponse({"status":[cs.controller.nav_action, cs.controller.hd_action, cs.controller.drill_action]})

def cancel_actions_(handle, name):
    if handle:
        print(f'Canceling goal {name}')
        cancel_future = handle.cancel_goal_async()
        cancel_future.add_done_callback(lambda f: cancel_done_callback(f, name, handle))

# ----------------------------------
# cancel single action

def cancel_action(request):
    name = request.POST.get("name")

    if name == "navigation":
        if cs.controller.nav_action:
            cs.node.get_logger().info('Canceling goal ' + name)
            cancel_future = cs.controller.nav_action.cancel_goal_async()
            cancel_future.add_done_callback(lambda f: cancel_done_callback(f, name, cs.controller.nav_action))
            return JsonResponse({"status", cs.controller.nav_action})
    
    if name == "handling_device":
        if cs.controller.hd_action:
            cs.node.get_logger().info('Canceling goal ' + name)
            cancel_future = cs.controller.hd_action.cancel_goal_async()
            cancel_future.add_done_callback(lambda f: cancel_done_callback(f, name, cs.controller.hd_action))
            return JsonResponse({"status", cs.controller.hd_action})

    if name == "drill":
        if cs.controller.drill_action:
            cs.node.get_logger().info('Canceling goal ' + name)
            cancel_future = cs.controller.drill_action.cancel_goal_async()
            cancel_future.add_done_callback(lambda f: cancel_done_callback(f, name, cs.controller.drill_action))
            return JsonResponse({"status", cs.controller.drill_action})
    

def cancel_done_callback(future, name, handle):
    cancel_response = future.result()
    if cancel_response.goal_id:
        print(f'Goal {name} successfully canceled')
        handle = True
    else:
        print(f'Goal {name} cancellation failed')
        handle - False

# ----------------------------------
# start an action

async def start_action(request):
    name = request.POST.get("name")

    if name == "navigation":
        mode = int(request.POST.get("mode"))

        goal = Pose2D()
        goal.x = float(request.POST.get("0"))
        goal.y = float(request.POST.get("1"))
        goal.theta = float(request.POST.get("2"))

        if not cs.controller.nav_action:
            (result, final_pos, error_type, error_message) = cs.controller.send_navigation_reach_goal(mode, goal)
            if(error_type == 0):
                # no error occured
                return JsonResponse({"status": True, "result": result, "final_pos": final_pos})
            else:

                return JsonResponse({"status": False, "error_messaage": error_message})

    if name == "handling_device":
        task_id = int(request.POST.get("task_id"))
        task_type = int(request.POST.get("task_type"))

        if not cs.controller.hd_action:
            (result, error_type, error_message) = cs.controller.send_handling_device_manipulation_goal(task_type, task_id)
            if(error_type == 0):
                # no error occured
                return JsonResponse({"status": True, "result": result})
            else:
                return JsonResponse({"status": False, "error_messaage": error_message})
    
    if name == "drill":
        if not cs.controller.drill_action:
            res = await cs.controller.send_drill_terrain_goal()
            if len(res) == 3 and res[1] == 0:
                result, error_type, error_message = res
            else:
                raise Exception("problem ")
            if(error_type == 0):
                # no error occured
                return JsonResponse({"status": True, "result": result})
            else:
                return JsonResponse({"status": False, "error_messaage": error_message})
    