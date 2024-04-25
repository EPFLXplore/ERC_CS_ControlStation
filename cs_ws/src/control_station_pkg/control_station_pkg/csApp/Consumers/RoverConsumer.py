import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class RoverConsumer(WebsocketConsumer):
    
    def connect(self):

        self.tab_group_name = 'rover'

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
                'type': data_json['rover_message'],
                'rover_state': data_json['text_data'],
            }
        )

    # Receive message from room group
    def rover_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'rover_state' : event['rover_state']
        }))
