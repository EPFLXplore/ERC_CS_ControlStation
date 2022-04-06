from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader

import sys
from subprocess import run, PIPE

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


#ACTIONS
def launch(request):
    print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','3','1'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')

def abort(request):
    print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','3','2'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')

def wait(request):
    print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','3','3'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')

def resume(request):
    print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','3','4'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')

def retry(request):
    print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','3','5'], shell=False, stdout=PIPE))
    return redirect('/Xplore_CS_2022/handlingdevice/')
