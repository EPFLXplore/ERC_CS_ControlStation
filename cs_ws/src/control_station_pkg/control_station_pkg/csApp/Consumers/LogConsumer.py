import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync

"""

Data format :
{
    'hours' : hours,
    'minutes' : minutes,
    'seconds' : seconds,
    'type' : type
    'message' : message
}

"""


# class LogConsumer(AsyncWebsocketConsumer):
    
#     async def connect(self):
#         self.tab_group_name = 'log'
    

#         print("channels name : " + self.channel_name)

#         # Join tab group
#         await self.channel_layer.group_add(
#             self.tab_group_name,
#             self.channel_name
#         )

#         await self.accept()



#     # Receive message from WebSocket
#     async def receive(self, text_data):

#         print("data received ")

#         data_json = json.loads(text_data)

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.tab_group_name,
#             {
#                 'type': 'broadcast_log',
#                 'hours': data_json['hours'],
#                 'minutes': data_json['minutes'],
#                 'seconds': data_json['seconds'],
#                 'severity': data_json['type'],
#                 'message': data_json['message'],

#             }
#         )

#     # Receive message from room group
#     async def broadcast_log(self, event):

#         print("data broadcast")

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#                 'type': 'broadcast_log',
#                 'hours': event['hours'],
#                 'minutes': event['minutes'],
#                 'seconds': event['seconds'],
#                 'type': event['severity'],
#                 'message': event['message'],

#         }))

import asyncio

class LogConsumer(WebsocketConsumer):
    
    def connect(self):

        self.tab_group_name = "log"

        print("channels name : " + self.channel_name)

        

        # Join tab group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name,
            self.channel_name
        )

        self.accept()



    # Receive message from WebSocket
    def receive(self, text_data):

        print("data received ")

        data_json = json.loads(text_data)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'log_message',
                'hours': data_json['hours'],
                'minutes': data_json['minutes'],
                'seconds': data_json['seconds'],
                'severity': data_json['type'],
                'message': data_json['message'],

            }
        )

    # Receive message from room group
    def log_message(self, event):

        print("data broadcast")


        # Send message to WebSocket
        async_to_sync(self.send(text_data=json.dumps({
                'hours': event['hours'],
                'minutes': event['minutes'],
                'seconds': event['seconds'],
                'type': event['severity'],
                'message': event['message'],

        })))



# This example uses WebSocket consumer, which is synchronous, and so
# needs the async channel layer functions to be converted.
# from asgiref.sync import async_to_sync
# import asyncio

# class LogConsumer(WebsocketConsumer):

#     def connect(self):
#         async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)

#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)

#     def receive(self, text_data):

#         print("received call")
#         async_to_sync(self.channel_layer.group_send)(
#             "chat",
#             {
#                 "type": "chat.message",
#                 "text": text_data,
#             },
#         )

#     def chat_message(self, event):

#         print("broadcast call")
#         self.send(text_data=event["text"])