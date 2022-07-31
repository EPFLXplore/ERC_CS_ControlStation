# CS2022/routing.py
from django.urls import re_path

from CS2022.RoverConsumer import RoverConsumer

websocket_urlpatterns = [
    re_path(r'ws/robot/(?P<tab_name>\w+)/$', RoverConsumer.as_asgi()),
]
