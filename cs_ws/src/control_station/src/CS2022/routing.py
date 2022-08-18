# CS2022/routing.py
from django.urls import re_path, path

from .Consumers import NavConsumer
import cameras.CameraConsumer

websocket_urlpatterns = [
    re_path(r'ws/CS2022/(?P<tab_name>\w+)/$', NavConsumer.NavConsumer.as_asgi()),
    re_path(r'ws/video/(?P<v_name>\w+)/$', cameras.CameraConsumer.CameraConsumer.as_asgi())
]
