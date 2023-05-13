import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer

from asgiref.sync import sync_to_async

"""

Data format :
{
    'joint_position' : [float] * 6
    'joint_velocity' : [float] * 6
    'joint_current' : [float] * 6
    'detected_tags' : [bool] * 4
    'task_outcome' : bool
}

"""


class InfoHDConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):

        self.tab_group_name = 'tab_info_hd'

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave tab group
        await self.channel_layer.group_discard(
            self.tab_group_name,
            self.channel_name
        )



    # Receive message from WebSocket
    async def receive(self, text_data):
        return


    async def broadcast_info_hd(self, data_json):

        await self.send(text_data=json.dumps({
            'state': data_json['state']
        }))
