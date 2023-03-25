import json
from re import X
from zlib import Z_NO_COMPRESSION
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


class NavAutoConsumer(RoverConsumer):
    
    async def connect(self):
        
        self.tab_name = 'navigation'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()



    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        x_pos           = text_data_json['x']
        y_pos           = text_data_json['y']
        z_pos           = text_data_json['z']
        linearVelocity  = text_data_json['linVel']
        angularVelocity = text_data_json['angVel']
        yaw             = text_data_json['yaw']
        distance        = text_data_json['distance']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type'    : 'topic_message',
                'x'       : x_pos,
                'y'       : y_pos,
                'z'       : z_pos,
                'linVel'  : linearVelocity,
                'angVel'  : angularVelocity,
                'yaw'     : yaw,
                'distance': distance
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        x_pos           = event['x']
        y_pos           = event['y']
        z_pos           = event['z']
        linearVelocity  = event['linVel']
        angularVelocity = event['angVel']
        yaw             = event['yaw']
        distance        = event['distance']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'x'       : x_pos,
            'y'       : y_pos,
            'z'       : z_pos,
            'linVel'  : linearVelocity,
            'angVel'  : angularVelocity,
            'yaw'     : yaw,
            'distance': distance
        }))
