import os
from flask import Flask, request, Response
from bot.bot import CornellTechBot

app = Flask(__name__)
SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')

ctechbot = CornellTechBot()
server = ctechbot.connect()

if server:
    users = ctechbot.client.api_call('users.list')
else:
    print("Connection failed. Invalid Slack token or bot ID?")

@app.route('/', methods=['GET'])
def test():
    return Response('I am the Cornell Tech Chatbot!')

@app.route("/message", methods=['POST'])
def message():
    # if request.form.get('token') == SLACK_WEBHOOK_SECRET:
    channel = request.form.get('channel_name')
    username = request.form.get('user_name')
    text = request.form.get('text')
    inbound_message = username + " in " + channel + " says: " + text
    print(inbound_message)
    return Response(), 200
    # else:
    #     return Response(), 403