# csApp/routing.py
from django.urls import re_path, path

from .Consumers import HdManualConsumer, InfoElecConsumer,InfoHDConsumer, InfoNavConsumer, InfoScienceConsumer, NavAutoConsumer, NavSemiAutoConsumer, RoverConsumer,ScienceDrillConsumer, CameraConsumer, GamepadConsumer, TimerConsumer
from .Consumers import SessionConsumer

websocket_urlpatterns = [
    # re_path(r'ws/csApp/(?P<tab_name>\w+)/$', NavConsumer.NavConsumer.as_asgi()),
    #path('ws/csApp/navigation/'    , NavAutoConsumer.NavAutoConsumer.as_asgi()),
    
    re_path(r'ws/cameras/(?P<v_name>\w+)/$', CameraConsumer.CameraConsumer.as_asgi()),

    path('ws/csApp/homepage/'      , RoverConsumer.RoverConsumer.as_asgi()),
    path('ws/csApp/navigation/'    , SessionConsumer.SessionConsumer.as_asgi()),
    path('ws/csApp/handlingdevice/', HdManualConsumer.HdManualConsumer.as_asgi()),
    path('ws/csApp/manual/'        , InfoNavConsumer.NavManualConsumer.as_asgi()),
    path('ws/csApp/science/'       , ScienceDrillConsumer.ScienceDrillConsumer.as_asgi()),

    path('ws/csApp/logs/'      , InfoElecConsumer.ElecConsumer.as_asgi()),
    path('ws/csApp/timer/'       , TimerConsumer.TimerConsumer.as_asgi()),
    path('ws/csApp/time/'       , TimerConsumer.TimerConsumer.as_asgi()),
    path('ws/csApp/gamepad/'       , GamepadConsumer.GamepadConsumer.as_asgi()),

    path('ws/csApp/science/'       , ScienceDrillConsumer.ScienceDrillConsumer.as_asgi()),

]
