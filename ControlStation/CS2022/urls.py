from django.urls import path

from . import views

urlpatterns = [
    path('homepage/',		views.homepage,		  name='homepage'),
    path('navigation/',		views.navigation, 	  name='navigation'),
    path('manualcontrol/', 	views.manualcontrol,  name='manualcontrol'),
    path('handlingdevice/', views.handlingdevice, name='handlingdevice'),
    path('science/', 		views.science,		  name='science'),
    path('avionics/', 		views.avionics,		  name='avionics'),
    
    #STATE BUTTONS
    #Manualcontrol
    path('manualcontrol/launch/',  views.launch_manual,     name='launch_manual'),
    path('manualcontrol/wait/',    views.wait_manual,       name='wait_manual'),
    path('manualcontrol/abort/',   views.abort_manual,      name='abort_manual'),
    path('manualcontrol/resume/',  views.resume_manual,     name='resume_manual'),

    #Navigation
    path('navigation/launch/',  views.launch_nav,     name='launch_nav'),
    path('navigation/wait/',    views.wait_nav,       name='wait_nav'),
    path('navigation/abort/',   views.abort_nav,      name='abort_nav'),
    path('navigation/resume/',  views.resume_nav,     name='resume_nav'),

    #Handlingdevice
    path('handlingdevice/launch/',  views.launch_hd,     name='launch_hd'),
    path('handlingdevice/wait/',    views.wait_hd,       name='wait_hd'),
    path('handlingdevice/abort/',   views.abort_hd,      name='abort_hd'),
    path('handlingdevice/resume/',  views.resume_hd,     name='resume_hd'),
    path('handlingdevice/retry/',   views.retry_hd,      name='retry_hd'),
    
    #Science
    path('science/launch/',  views.launch_science,     name='launch_science'),
    #path('science/confirm/',    views.confirm_science,    name='confirm_science'),
    path('science/abort/',   views.abort_science,      name='abort_science'),
    path('science/retry/',   views.retry_science,      name='retry_science'),
    
    
]
