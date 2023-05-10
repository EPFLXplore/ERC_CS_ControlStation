import json
from channels.generic.websocket import AsyncWebsocketConsumer

import MVC_node.models.utils as utils
from ..views import *



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
        buttons = json.loads(data)['buttons']
        axes = json.loads(data)['axes']
        views.cs.send_gamepad_data(axes, buttons)



    async def disconnect(self, close_code):
        utils.gamepad.id = ""
        utils.gamepad.buttons = []
        utils.gamepad.axes = []
