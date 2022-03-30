from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import sys
from subprocess import run, PIPE


# Create your views here.

def s(out):
	return str(out)[2:-3]

def simple_function(request):
	out_a = run([sys.executable,'//home//xplore//Desktop//functions.py', 'pubTask','4','1'], shell=False, stdout=PIPE)
	
	context = {
		"output"			: s(out_a.stdout)
	}
	
	return render(request, 'testing/python.html', context)
	
def python(request):
	context = {
		"output" : "None"
	}
	return render(request, 'testing/python.html', context)
