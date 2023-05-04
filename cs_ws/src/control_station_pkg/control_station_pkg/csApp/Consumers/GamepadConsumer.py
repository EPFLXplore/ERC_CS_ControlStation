import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer
import MVC_node.models.utils as utils


"""
Data format :
{
    'buttons' : [button_1, button_2, ... , button_11],
    'axes' : [axis_1, axis_2, ... , axis_6]
}

ou

{
    'a': ,
    'b': ,
    'x': ,
    'y': ,
    'l1': ,
    'r1': ,
    'l2': ,
    'r2': ,
    'select': ,
    'start': ,
    ...



"""


class GamepadConsumer(RoverConsumer):
    
    async def connect(self):
        utils.gamepad.buttons = [False]*11
        utils.gamepad.axes = [0]*6
        await self.accept()

    # Receive message from WebSocket
    async def receive(self, text_data):
        utils.gamepad.buttons = json.loads(text_data)['buttons']
        utils.gamepad.axes = json.loads(text_data)['axes']

    async def disconnect(self, close_code):
        utils.gamepad.buttons = [False]*11
        utils.gamepad.axes = [0]*6
