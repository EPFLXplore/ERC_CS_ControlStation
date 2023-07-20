import json
from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :

{

    "candidates" : candidates,
    "npk-sensor" : npk-sensor,
    "four-in-one" : four-in-one

}

"""


class InfoScienceConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.tab_group_name = 'tab_info_drill'

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()



    # Receive message from WebSocket
    async def receive(self, data):

        data_json = json.loads(data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'broadcast_info_drill',
                'candidates' : data_json['candidates'],
                'npk-sensor' : data_json['npk-sensor'],
                'four-in-one' : data_json['four-in-one'],
            }
        )

    # Receive message from room group
    async def broadcast_info_science(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'candidates' : data_json['candidates'],
                'npk-sensor' : data_json['npk-sensor'],
                'four-in-one' : data_json['four-in-one'],
        }))
