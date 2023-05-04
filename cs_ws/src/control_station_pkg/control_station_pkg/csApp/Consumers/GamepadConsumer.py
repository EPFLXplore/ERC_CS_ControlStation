import json
from channels.generic.websocket import AsyncWebsocketConsumer

import MVC_node.models.utils as utils


"""
Data format :
{
    'name' : string,
    'buttons' : [button_1, button_2, ... , button_11] Array int,
    'axes' : [axis_1, axis_2, ... , axis_6] Array float
}


"""


class GamepadConsumer(AsyncWebsocketConsumer):
    
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
