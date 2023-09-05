import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from asgiref.sync import async_to_sync

"""

Data format :
{
    'joint_position' : [float] * 6
    'joint_velocity' : [float] * 6
    'joint_current' : [float] * 6
    'available_buttons' : [bool] * 16 (?)
    'task_outcome' : bool
}

"""


class HDConsumer(WebsocketConsumer):
    
    def connect(self):
        self.tab_group_name = 'hd'

        # Join tab group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave tab group
        async_to_sync(self.channel_layer.group_discard)(
            self.tab_group_name,
            self.channel_name
        )


    # Receive message from WebSocket
    def receive(self, text_data):

        data_json = json.loads(text_data)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'hd_message',
                'joint_position'   : data_json['joint_position'],
                'joint_velocity': data_json['joint_velocity'],
                'joint_current': data_json['joint_current'],
                'available_buttons': data_json['available_buttons'],
                'task_outcome': data_json['task_outcome'],
                'voltage': data_json['voltage'],
            }
        )


    # Receive message from room group
    def hd_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'joint_position'   : event['joint_position'],
                'joint_velocity': event['joint_velocity'],
                'joint_current': event['joint_current'],
                'available_buttons': event['available_buttons'],
                'task_outcome': event['task_outcome'],
                'voltage': event['voltage'],
            }))
