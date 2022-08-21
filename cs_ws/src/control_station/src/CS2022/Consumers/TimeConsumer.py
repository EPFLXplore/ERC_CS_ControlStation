import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


class TimeConsumer(RoverConsumer):
    
    async def connect(self):
        
        self.tab_group_name = 'tab_timer'

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()



    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_1 = text_data_json['seconds']
        message_2 = text_data_json['minutes']
        message_3 = text_data_json['hours']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'seconds': message_1,
                'minutes': message_2,
                'hours'  : message_3
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        message_1 = event['seconds']
        message_2 = event['minutes']
        message_3 = event['hours']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'seconds': message_1,
            'minutes': message_2,
            'hours'  : message_3
        }))
