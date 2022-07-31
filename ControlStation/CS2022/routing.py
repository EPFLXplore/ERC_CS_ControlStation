# CS2022/routing.py
from django.urls import re_path

from CS2022.Rover.RoverConsumer import RoverConsumer

websocket_urlpatterns = [
    re_path(r'ws/rover/(?P<room_name>\w+)/$', RoverConsumer),
]
