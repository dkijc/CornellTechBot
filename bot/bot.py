import os
from slackclient import SlackClient

class CornellTechBot:
    def __init__(self):
        self.BOT_NAME = 'cornelltechbot'
        self.client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.BOT_ID = SlackClient(os.environ.get('BOT_ID'))

    def connect(self):
        if self.client.rtm_connect():
            return self.client.server

    def read(self):
        messages = []
        while len(messages) == 0:
            messages = self.client.rtm_read()
        
        if len(messages) > 0:
            for message in messages:
                return message
        
        return None

    def send_message(self, msg_text, user):
        return self.client.api_call(
            "chat.postMessage",
            channel=user,
            text=msg_text,
        )
    
    def read_and_respond(self, users):
        msgJSON = self.read()
    
        if msgJSON != None:
            for member in users.get('members'):
                if member and member.get('id') == msgJSON.get('user') and msgJSON.get('type') != 'user_typing':
                    fName = member.get('profile').get('first_name')
                
                    self.client.api_call(
                        "chat.postMessage",
                        channel=msgJSON.get('channel'),
                        text="Hey " + fName + "!"
                    )