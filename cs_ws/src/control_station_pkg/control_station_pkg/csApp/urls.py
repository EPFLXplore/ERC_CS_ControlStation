from django.urls import path

from .views import *

urlpatterns = [
    # General
    # path('homepage/',		         homepage,		  name='homepage'),
    # path('navigation/',		         navigation, 	  name='navigation'),
    # path('manualcontrol/', 	         manualcontrol,  name='manualcontrol'),
    # path('handlingdevice/',          handlingdevice, name='handlingdevice'),
    # path('science/', 		         science,		  name='science'),
    # path('logs/', 		             logs,		      name='logs'),
    # path('capture_image/', 		     capture_image,  name='capture_image'),
    
    #STATE BUTTONS
    #Manualcontrol
    path('manualcontrol/launch',    launch_manual,  name='launch_manual'),
    path('manualcontrol/wait',      wait_manual,    name='wait_manual'),
    path('manualcontrol/abort',     abort_manual,   name='abort_manual'),
    path('manualcontrol/resume',    resume_manual,  name='resume_manual'),

    #Navigation
    path('navigation/launch',       launch_nav,     name='launch_nav'),
    path('navigation/wait',         wait_nav,       name='wait_nav'),
    path('navigation/abort',        abort_nav,      name='abort_nav'),
    path('navigation/resume',       resume_nav,     name='resume_nav'),
    path('navigation/add_goal_nav', add_goal_nav,   name="add_goal_nav"),

    #Handlingdevice
    path('handlingdevice/launch',   launch_hd,      name='launch_hd'),
    path('handlingdevice/wait',     wait_hd,        name='wait_hd'),
    path('handlingdevice/abort',    abort_hd,       name='abort_hd'),
    path('handlingdevice/resume',   resume_hd,      name='resume_hd'),
    path('handlingdevice/retry',    retry_hd,       name='retry_hd'),
    path('handlingdevice/set_id',   set_id,         name='set_id'),
    path('handlingdevice/set_hd_mode',   set_hd_mode,         name='set_hd_mode'),
    
    #Science
    path('science/launch',         launch_science, name='launch_science'),
    path('science/wait',            wait_science,   name='wait_science'),
    path('science/abort',           abort_science, name='abort_science'),
    path('science/resume',          resume_science,   name='resume_science'),

    #Cameras
    path('cameras/enable_cameras', enable_cameras, name='enable_cameras'),

    # path('science/confirm',         confirm_science, name='confirm_science'),
    # path('science/abort',           abort_science,  name='abort_science'),
    # path('science/retry',           retry_science,  name='retry_science'),
    # path('science/set_tube_cmd',    set_tube_cmd,   name='set_tube_cmd'),
    # path('science/get_humidity',    get_humidity,   name='get_humidity'),
    # path('science/get_parameters',  get_parameters, name='get_parameters'),
    # path('science/get_sc_info',     get_sc_info, name='get_sc_info'),
    # path('science/get_sc_state',    get_sc_state, name='get_sc_state'),

    # timer
    path('logs/timer',          start_timer,    name='start_timer')
    
    
]
