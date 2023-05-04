import json
from channels.generic.websocket import AsyncWebsocketConsumer
import re       #import regrex functions to extract the video number from the url
import MVC_node.models.utils as utils





class CameraConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['v_name']
        utils.cameras.cameras_list[int(re.findall(r'\d+', self.room_name)[0])] += 1 
        print(utils.cameras.cameras_list)
        self.room_group_name = 'video_%s' % self.room_name
        await self.channel_layer.group_add(
             self.room_group_name,
             self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        utils.cameras.cameras_list[int(re.findall(r'\d+', self.room_name)[0])] -= 1 
        print(utils.cameras.cameras_list)
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        #print("websocket received : " + self.scope.get("path"))

        await self.send(text_data=json.dumps({
            'video_data': text_data
        }))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'video_message',
                'video_data': text_data,
            }
        )

    # Receive message from room group
    async def video_message(self, event):
        data = event['video_data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'video_data': data
        }))