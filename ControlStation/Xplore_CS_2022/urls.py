from django.urls import path

from . import views

urlpatterns = [
    path('homepage/',		views.homepage,		  name='homepage'),
    path('navigation/',		views.navigation, 	  name='navigation'),
    path('manualcontrol/', 	views.manualcontrol,  name='manualcontrol'),
    path('handlingdevice/', views.handlingdevice, name='handlingdevice'),
    path('science/', 		views.science,		  name='science'),
    
    path('action/launch/',  views.launch,         name='launch'),
    path('action/wait/',    views.wait,         name='wait'),
    path('action/abort/',   views.abort,         name='abort'),
    path('action/resume/',  views.resume,         name='resume'),
    path('action/retry/',   views.retry,         name='retry')
]
