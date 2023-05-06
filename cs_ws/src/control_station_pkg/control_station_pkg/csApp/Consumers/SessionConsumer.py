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
    'nb_users': int,
}

"""



class SessionConsumer(WebsocketConsumer):

    def connect(self):

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
           
        self.tab_name = 'homepage'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name, self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {"type": "broadcast", "nb_users": utils.session.nb_users}
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
            self.tab_group_name, {"type": "broadcast", "nb_users": utils.session.nb_users}
        )
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.tab_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, data):
        data_json = json.loads(data)
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name, {"type": "broadcast_session", "nb_users": data_json["current_tab"]}
        )

    # Receive message from room group
    def broadcast_session(self, data_json):

        self.send(text_data=json.dumps({"nb_users": data_json["nb_users"]}))