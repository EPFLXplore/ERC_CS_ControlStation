import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


class HDConsumer(RoverConsumer):
    
    async def connect(self):
        
        self.tab_name = 'handlingdevice'
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
        joint_position = text_data_json['joint_pos']
        joint_velocity = text_data_json['joint_vel']
        tof            = text_data_json['tof']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'joint_pos': joint_position,
                'joint_vel': joint_velocity,
                'tof'      : tof
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        joint_position = event['joint_pos']
        joint_velocity = event['joint_vel']
        tof            = event['tof']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'joint_pos': joint_position,
            'joint_vel': joint_velocity,
            'tof'      : tof
        }))
