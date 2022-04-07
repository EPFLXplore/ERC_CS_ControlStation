from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader

import sys
from subprocess import run, PIPE

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


#STATE BUTTONS
#Manual
def launch_manual(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','1','1'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/manualcontrol/')
def abort_manual(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','1','2'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/manualcontrol/')
def wait_manual(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','1','3'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/manualcontrol/')
def resume_manual(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','1','4'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/manualcontrol/')

#Navigation
def launch_nav(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','2','1'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/navigation/')
def abort_nav(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','2','2'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/navigation/')
def wait_nav(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','2','3'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/navigation/')
def resume_nav(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','2','4'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/navigation/')

#Handlingdevice
def launch_hd(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','3','1'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')
def abort_hd(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','3','2'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')
def wait_hd(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','3','3'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')
def resume_hd(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','3','4'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')
def retry_hd(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','3','5'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')

#Science
def launch_science(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','4','1'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/science/')
def abort_science(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','4','2'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/science/')
def wait_science(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','4','3'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/science/')
def resume_science(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','4','4'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/science/')
def retry_science(request):
    print(run([sys.executable,CONTROLLER_PATH, 'pub_Task','4','5'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/science/')

