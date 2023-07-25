import json
from channels.generic.websocket import AsyncWebsocketConsumer

import MVC_node.models.utils as utils
from ..views import *



"""

Data format :
{
    'id' : string,
    'target' : string,
    'buttons' : [button_1, button_2, ... , button_11] Array int,
    'axes' : [axis_1, axis_2, ... , axis_6] Array float
    'mode' : string, "NAV" or "HD"
}

"""


class GamepadConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.tab_group_name = 'gamepad'

        utils.gamepad.id = ""
        utils.gamepad.buttons = []
        utils.gamepad.axes = []
        await self.accept()

    # Receive message from WebSocket
    async def receive(self, text_data):
        json_data = json.loads(text_data)
        print("===========GamepadConsumer=============")
        print(json_data)
        cs.send_gamepad_data(json_data['axes'],
                            json_data['buttons'],
                            "",
                            json_data['mode'])
        



    async def disconnect(self, close_code):
        utils.gamepad.id = ""
        utils.gamepad.buttons = []
        utils.gamepad.axes = []
