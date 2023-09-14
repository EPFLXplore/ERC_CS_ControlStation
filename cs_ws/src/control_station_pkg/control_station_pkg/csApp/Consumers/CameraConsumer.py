import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import re       #import regrex functions to extract the video number from the url
import MVC_node.models.utils as utils
from asgiref.sync import async_to_sync

"""

Data format :
{

    'video_data_1' : string,
    'video_data_2' : string,
    ...
}

"""


class CameraConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['v_name']
        self.room_group_name = self.room_name

        async_to_sync(self.channel_layer.group_add)(
             self.room_group_name,
             self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):

        print("message received in cameras consumer")

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'video_message',
                'video_data': text_data,
            }
        )

    # Receive message from room group
    def video_message(self, event):
        data = event['video_data']
        print("received message in room group")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'data': data
        }))