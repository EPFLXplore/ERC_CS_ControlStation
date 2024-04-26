# csApp/routing.py
from django.urls import path
from .Consumers import RoverConsumer, GamepadConsumer

websocket_urlpatterns = [
    path('ws/csApp/rover_state/', RoverConsumer.RoverConsumer.as_asgi()),
    path('ws/csApp/gamepad/', GamepadConsumer.GamepadConsumer.as_asgi())
]
