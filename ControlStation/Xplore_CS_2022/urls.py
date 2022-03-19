from django.urls import path

from . import views

urlpatterns = [
    path('homepage/',		views.homepage,		  name='homepage'),
    path('navigation/',		views.navigation, 	  name='navigation'),
    path('manualcontrol/', 	views.manualcontrol,  name='manualcontrol'),
    path('handlingdevice/', views.handlingdevice, name='handlingdevice'),
    path('science/', 		views.science,		  name='science'),
    
]
