import os
from slackclient import SlackClient
from utilities import modified_pop

class CornellTechBot:
    def __init__(self):
        self.BOT_NAME = 'cornelltechbot'
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.users = self.get_users_dict()
        self.channels = self.client.api_call("channels.list")
        self.server = None
        self.respond = { 
            # Other types of messages are: 
            # user_typing, hello, reconnect_url, presence_change, desktop_notification
            'message': self.respond_message
        }

    def connect(self):
        if self.client.rtm_connect():
            self.server = self.client.server
            return self.client.server

    def send_message(self, msg_text, user):
        return self.client.api_call(
            "chat.postMessage",
            channel=user,
            text=msg_text,
        )
    
    def get_users_dict(self):
        response = self.client.api_call('users.list')
        members = response['members']            

        return {   
            member['id']: modified_pop(member, 'id') 
            for member in members
            }

    def read_and_respond(self):
        messages = []

        while len(messages) == 0:
            messages = self.client.rtm_read()

        responses = [
            self.respond.get(message['type'], print)(message)
            for message in messages 
            # Filter out Nones and self-messages here
            if message and message.get('subtype') != 'bot_message'
            ]

        return responses
        

    def respond_message(self, msg):
        user = self.users.get(msg.get('user'))
        return self.client.api_call(
                "chat.postMessage",
                channel=msg.get('channel'),
                text="Hey " + user['profile']['first_name'] + "!"
            )