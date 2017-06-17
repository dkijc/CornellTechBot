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
        print("are you getting here")
        messages = []
        while len(messages) == 0:
            messages = self.client.rtm_read()
        return messages[0]

    def send_message(self, msg_text, user):
        return self.client.api_call(
            "chat.postMessage",
            channel=user,
            text=msg_text,
        )