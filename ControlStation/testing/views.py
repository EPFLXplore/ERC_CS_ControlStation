from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import sys
from subprocess import run, PIPE


# Create your views here.

def s(out):
	return str(out)[2:-3]

def simple_function(request):
	print(run([sys.executable,'//home//rocknd79//Xplore//CS_workspace//ControlStation//Controller.py', 'pubTask','4','1'], shell=False, stdout=PIPE))
	
	context = {
		"output"			: "test" #s(out_a.stdout)
	}
	
	return render(request, 'testing/python.html', context)
	
def python(request):
	context = {
		"output" : "None"
	}
	return render(request, 'testing/python.html', context)
