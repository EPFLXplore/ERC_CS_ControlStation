from django.http import HttpResponse
from django.shortcuts import render

def launcher(request):
    return render(request, 'launcher.html')

def new_control_station(request):
    return render(request, 'index.html')