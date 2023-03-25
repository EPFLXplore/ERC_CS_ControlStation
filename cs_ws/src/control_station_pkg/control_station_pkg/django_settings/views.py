from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

def launcher(request):
    return render(request, 'launcher.html')

@ensure_csrf_cookie
def new_control_station(request):
    return render(request, 'index.html')