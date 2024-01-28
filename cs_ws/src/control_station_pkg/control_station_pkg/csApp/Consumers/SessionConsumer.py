# chat/consumers.py
import json
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.sessions.models import Session
import MVC_node.models.utils as utils


"""

Data format :

{
    nb_users : int,
    rover_state : int,
    subsystems_state : int,
    signal_strength : int,
}

"""



class SessionConsumer(WebsocketConsumer):

    def connect(self):

        if(self.scope["session"].session_key != None):
            #print(str(Session.objects.get(session_key=self.scope["session"].session_key).get_decoded()))
            print("session key : " + str(self.scope["session"].session_key))
            try :
                self.scope['session']['userID']
                
            except :
                self.scope['session']['userID'] = utils.session.nb_users
                utils.session.nb_users += 1


        self.tab_name = 'homepage'
        # self.tab_group_name = 'tab_%s' % self.tab_name
        self.tab_group_name = 'session'


        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name, self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {
                "type": "broadcast", 
                "nb_users": utils.session.nb_users,
                "rover_state": utils.session.rover_state,
                "subsystems_state": utils.session.subsystems_state,
                "signal_strength": utils.session.signal_strength,
                }
        )

        self.accept()

    def disconnect(self, close_code):
        try :
            print("will remove : " + str(self.scope['session']["userID"]))
            del self.scope['session']["userID"]
            utils.session.nb_users -= 1
            print("nb users : " + str(utils.session.nb_users))
        except :
            pass
        self.scope['session'].save()

        #update other users
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {
                "type": "broadcast", 
                "nb_users": utils.session.nb_users,
                "rover_state": utils.session.rover_state,
                "subsystems_state": utils.session.subsystems_state,
                "signal_strength": utils.session.signal_strength,
            }
        )
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.tab_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, data):
        data_json = json.loads(data)
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {
                "type": "broadcast", 
                "nb_users": data_json["current_tab"],
                "rover_state": data_json["rover_state"],
                "subsystems_state": data_json["subsystems_state"],
                "signal_strength": data_json["signal_strength"],
        })

    # Receive message from room group
    def broadcast(self, data_json):

        print("Received: ", data_json["signal_strength"])

        self.send(text_data=json.dumps({
            "nb_users": data_json["nb_users"],
            "rover_state": data_json["rover_state"],
            "subsystems_state": data_json["subsystems_state"],
            "signal_strength": data_json["signal_strength"],
        }))