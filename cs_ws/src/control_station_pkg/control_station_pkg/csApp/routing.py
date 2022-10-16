# csApp/routing.py
from django.urls import re_path, path

from .Consumers import RoverConsumer, NavConsumer, HdConsumer, ScConsumer, AvConsumer, ManConsumer, TimeConsumer
import cameras.CameraConsumer

websocket_urlpatterns = [
    # re_path(r'ws/csApp/(?P<tab_name>\w+)/$', NavConsumer.NavConsumer.as_asgi()),
    path('ws/csApp/homepage/'      , RoverConsumer.RoverConsumer.as_asgi()),
    path('ws/csApp/navigation/'    , NavConsumer.NavConsumer.as_asgi()),
    path('ws/csApp/handlingdevice/', HdConsumer.HDConsumer.as_asgi()),
    path('ws/csApp/logs/'      , AvConsumer.AVConsumer.as_asgi()),
    path('ws/csApp/manual/'        , ManConsumer.MANConsumer.as_asgi()),
    path('ws/csApp/science/'       , ScConsumer.SCConsumer.as_asgi()),
    path('ws/csApp/time/'       , TimeConsumer.TimeConsumer.as_asgi()),

    re_path(r'ws/cameras/(?P<v_name>\w+)/$', cameras.CameraConsumer.CameraConsumer.as_asgi())
]
