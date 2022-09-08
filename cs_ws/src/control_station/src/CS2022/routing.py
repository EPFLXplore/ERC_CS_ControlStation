# CS2022/routing.py
from django.urls import re_path, path

from .Consumers import RoverConsumer, NavConsumer, HdConsumer, ScConsumer, AvConsumer, ManConsumer, TimeConsumer
import cameras.CameraConsumer

websocket_urlpatterns = [
    # re_path(r'ws/CS2022/(?P<tab_name>\w+)/$', NavConsumer.NavConsumer.as_asgi()),
    path('ws/CS2022/homepage/'      , RoverConsumer.RoverConsumer.as_asgi()),
    path('ws/CS2022/navigation/'    , NavConsumer.NavConsumer.as_asgi()),
    path('ws/CS2022/handlingdevice/', HdConsumer.HDConsumer.as_asgi()),
    path('ws/CS2022/logs/'      , AvConsumer.AVConsumer.as_asgi()),
    path('ws/CS2022/manual/'        , ManConsumer.MANConsumer.as_asgi()),
    path('ws/CS2022/science/'       , ScConsumer.SCConsumer.as_asgi()),
    path('ws/CS2022/time/'       , TimeConsumer.TimeConsumer.as_asgi()),

    re_path(r'ws/cameras/(?P<v_name>\w+)/$', cameras.CameraConsumer.CameraConsumer.as_asgi())
]
