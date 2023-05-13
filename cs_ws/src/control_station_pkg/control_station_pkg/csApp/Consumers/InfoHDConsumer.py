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
    'detected_tags' : [bool] * 4
    'task_outcome' : bool
}

"""


class InfoHDConsumer(WebsocketConsumer):
    
    def connect(self):


        self.tab_group_name = 'info_hd'

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

        print("received in hd")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'hd_message',
                'joint_position'   : data_json['joint_position'],
                'joint_velocity': data_json['joint_velocity'],
                'joint_current': data_json['joint_current'],
                'detected_tags': data_json['detected_tags'],
                'task_outcome': data_json['task_outcome'],
            }
        )


    # Receive message from room group
    def hd_message(self, event):

        print("broadcast_info_nav")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'joint_position'   : event['joint_position'],
                'joint_velocity': event['joint_velocity'],
                'joint_current': event['joint_current'],
                'detected_tags': event['detected_tags'],
                'task_outcome': event['task_outcome'],
            }))
