from django.http import HttpResponse
from django.shortcuts import render

def launcher(request):
    return render(request, 'launcher.html')
    


