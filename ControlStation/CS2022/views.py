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
from django.http.response   import StreamingHttpResponse

from numpy import ndarray
from src.cs_node            import *
from src.controller         import *
from manage                 import setup
import threading
import cv2

# ===============================================================
# Control Station setup

cs = setup().CONTROL_STATION

# ===============================================================
# Django views

# ------------------------------------
# cameras

class VideoCamera(object):

    def __init__(self, capture):
        # self.video = capture

        self.frame = cs.cameras.cam_1
        threading.Thread(target=self.update, args=()).start()

    # def __del__(self):
    #     self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.frame = cs.cameras.cam_1


def gen(camera):
    while True:
        
        frame = camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera(cs.cameras.cam_1)),
                    content_type='multipart/x-mixed-replace; boundary=frame')

# ------------------------------------
# General views

def handlingdevice(request):
    return render(request, 'pages/handlingdevice.html')

def homepage(request):
    return render(request, 'pages/homepage.html')

def manualcontrol(request):
    return render(request, 'pages/manualcontrol.html')

def navigation(request):

    ws_nav.connect("ws://localhost:8000/ws/CS2022/navigation/")
    print("debug")
    return render(request, 'pages/navigation.html', { 
        'tab_name': "navigation"
    })  #TODO tab_name 

def science(request):
    return render(request, 'pages/science.html')

def avionics(request):
    return render(request, 'pages/avionics.html')

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

