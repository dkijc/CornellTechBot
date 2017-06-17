from unittest import TestCase
from expects import expect, equal, be_a

from cornell_tech_bot import CornellTechBot
from slackclient._server import Server


class TestCornellTechBot(TestCase):
    def test_can_be_created(self):
        ctechbot = CornellTechBot()
        expect(ctechbot.client).not_to(equal(None))
        expect(ctechbot.BOT_ID).not_to(equal(None))
        expect(ctechbot.BOT_NAME).to(equal("cornelltechbot"))

    def test_can_connect(self):
        ctechbot = CornellTechBot()
        ws_server = ctechbot.connect()
        expect(ws_server).to(be_a(Server))
    
    def test_can_read(self):
        ctechbot = CornellTechBot()
        ws_server = ctechbot.connect()
        hello_message = [{'type': 'hello'}]
        expect(ctechbot.read()).to(equal(hello_message))