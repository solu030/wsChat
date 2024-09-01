from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()
        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_add)(group,self.channel_name)

    def websocket_receive(self, message):
        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_send)(group,{"type": "single_send","message":message})

    def single_send(self, event):
        message = event['message']["text"]
        self.send(message)

    def websocket_disconnect(self, message):
        group = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_discard)(group,self.channel_name)
        raise StopConsumer()