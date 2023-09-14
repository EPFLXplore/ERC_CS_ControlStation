import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

"""

Data format :

{
    "mass" : float32 * 2,
    "candidates" : ?,
    "npk_sensor" : float32 * 3,
    "four_in_one" : float32 * 4 (?),
    "spectrometer" : float32 * 17,
    "spectrometer_closest_candidate" : float32 * 17,

}

"""


class ScienceDataConsumer(WebsocketConsumer):
    
    def connect(self):
        
        self.tab_group_name = 'science_data'

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
                'type': 'science_data_message',
                'container_mass' : data_json['container_mass'],
                'drill_mass' : data_json['drill_mass'],
                'candidates' : data_json['candidates'],
                'npk_sensor' : data_json['npk_sensor'],
                'four_in_one' : data_json['four_in_one'],
                'spectrometer' : data_json['spectrometer'],
                'spectrometer_closest_candidate' : data_json['spectrometer_closest_candidate'],
            }
        )

    # Receive message from room group
    def science_data_message(self, event):

        self.send(text_data=json.dumps({
                'container_mass' : event['container_mass'],
                'drill_mass' : event['drill_mass'],
                'candidates' : event['candidates'],
                'npk_sensor' : event['npk_sensor'],
                'four_in_one' : event['four_in_one'],
                'spectrometer' : event['spectrometer'],
                'spectrometer_closest_candidate' : event['spectrometer_closest_candidate'],
        }))
