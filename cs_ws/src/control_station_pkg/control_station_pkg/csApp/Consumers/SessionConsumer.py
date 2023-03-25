# chat/consumers.py
import json
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.sessions.models import Session
import MVC_node.models.utils as utils



class SessionConsumer(WebsocketConsumer):
    def connect(self):
        #print(type(self.scope))
        #for key, value in self.scope.items():
         #   print(key + " : " + str(value))

        #self.scope["session"]["userID"]
        if(self.scope["session"].session_key != None):
            #print(str(Session.objects.get(session_key=self.scope["session"].session_key).get_decoded()))
            print("session key : " + str(self.scope["session"].session_key))
            try :
                print("exist deja : " + str(self.scope['session']['userID']))
                
            except :
                self.scope['session']['userID'] = utils.session.nb_users
                print("exist pas : " + str(self.scope['session']['userID']))
                utils.session.nb_users += 1
                #utils.session.sessions_list
                print("nb users : " + str(utils.session.nb_users))

        else :
            print("no session key")

        
        

        

           
        #self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        #self.room_group_name = "chat_%s" % self.room_name
        self.tab_name = 'homepage'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("disconected : " + str(close_code))
        # for key, value in self.scope.items():
        #     print(key + " : " + str(value))
        try :
            print("will remove : " + str(self.scope['session']["userID"]))
            del self.scope['session']["userID"]
            utils.session.nb_users -= 1
            print("nb users : " + str(utils.session.nb_users))
        except :
            pass
        self.scope['session'].save()
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.tab_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))