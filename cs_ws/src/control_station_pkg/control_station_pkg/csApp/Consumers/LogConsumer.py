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
        print("receive")
        text_data_json = json.loads(text_data)
        message_1 = text_data_json['hor']
        message_2 = text_data_json['min']
        message_3 = text_data_json['sec']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'hor': message_1,
                'min': message_2,
                'sec'  : message_3
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        print("topic_message")
        message_1 = event['hor']
        message_2 = event['min']
        message_3 = event['sec']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'hor': message_1,
            'min': message_2,
            'sec'  : message_3
        }))
