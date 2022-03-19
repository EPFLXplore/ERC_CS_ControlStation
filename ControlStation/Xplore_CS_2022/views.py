from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def handlingdevice(request):
    return render(request, 'pages/handlingdevice.html')

def homepage(request):
    return render(request, 'pages/homepage/homepage.html')

def manualcontrol(request):
    return render(request, 'pages/manualcontrol.html')

def navigation(request):
    return render(request, 'pages/navigation.html')

def science(request):
    return render(request, 'pages/science.html')


