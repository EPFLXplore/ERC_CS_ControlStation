import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync

"""

Data format :

{
    "mass" : float32 * 2,
    "candidates" : ?,
    "npk-sensor" : float32 * 3,
    "four-in-one" : float32 * 4 (?),
    "spectrometer" : float32 * 17,
    "spectrometer-closest-candidate" : float32 * 17,

}

"""


class ScienceDataConsumer(WebsocketConsumer):
    
    def connect(self):

        print("connect to science")
        
        self.tab_group_name = 'info_science'

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

        print("received in science")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'science_message',
                'mass' : data_json['mass'],
                'candidates' : data_json['candidates'],
                'npk-sensor' : data_json['npk-sensor'],
                'four-in-one' : data_json['four-in-one'],
            }
        )

    # Receive message from room group
    def science_message(self, event):

        print("broadcast_info_science")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'mass' : event['mass'],
                'candidates' : event['candidates'],
                'npk-sensor' : event['npk-sensor'],
                'four-in-one' : event['four-in-one'],
        }))
