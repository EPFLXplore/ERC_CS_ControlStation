# CS2022/routing.py
from django.urls import re_path

from . import RoverConsumer

websocket_urlpatterns = [
    re_path(r'ws/CS2022/(?P<tab_name>\w+)/$', RoverConsumer.RoverConsumer.as_asgi()),
]
