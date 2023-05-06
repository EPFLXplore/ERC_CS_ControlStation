import json
from channels.generic.websocket import AsyncWebsocketConsumer

import MVC_node.models.utils as utils


"""

Data format :
{
    'id' : string,
    'buttons' : [button_1, button_2, ... , button_11] Array int,
    'axes' : [axis_1, axis_2, ... , axis_6] Array float
}

"""


class GamepadConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.tab_group_name = 'tab_gamepad'

        utils.gamepad.id = ""
        utils.gamepad.buttons = []
        utils.gamepad.axes = []
        await self.accept()

    # Receive message from WebSocket
    async def receive(self, data):
        utils.gamepad.id = json.loads(data)['id']
        utils.gamepad.buttons = json.loads(data)['buttons']
        utils.gamepad.axes = json.loads(data)['axes']

    async def disconnect(self, close_code):
        utils.gamepad.id = ""
        utils.gamepad.buttons = []
        utils.gamepad.axes = []
