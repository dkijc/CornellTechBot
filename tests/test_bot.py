from unittest import TestCase
from expects import expect, equal, be_a

from cornell_tech_bot import CornellTechBot
from slackclient._server import Server

ctechbot = CornellTechBot()

class TestCornellTechBot(TestCase):
    def test_can_be_created(self):
        global ctechbot

        expect(ctechbot.client).not_to(equal(None))
        expect(ctechbot.BOT_ID).not_to(equal(None))
        expect(ctechbot.BOT_NAME).to(equal("cornelltechbot"))

    def test_can_connect(self):
        ws_server = ctechbot.connect()
        expect(ws_server).to(be_a(Server))
    
    def test_can_read(self):
        global ctechbot

        hello_message = {'type': 'hello'}
        expect(ctechbot.read()).to(equal(hello_message))

    def test_can_send_message(self):
        global ctechbot

        toUser = '@cornelltechbot'
        message_text = 'Hey there James'
        incoming_message = ctechbot.send_message(message_text, toUser)
        
        expect(incoming_message['message']['text']).to(equal(message_text))
        expect(list(incoming_message.keys())).to(equal(['ok', 'channel', 'ts', 'message']))
        
        msg = {key: None for key in list(incoming_message.keys())}
        while msg.get('type') != 'message':
            msg = ctechbot.read()
        
        expect(msg.get('text')).to(equal(message_text))