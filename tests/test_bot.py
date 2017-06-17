from unittest import TestCase
from expects import expect, equal

from cornell_tech_bot import CornellTechBot

ctechbot = None


class TestBot(TestCase):
    def setUp(self):
	    ctechbot = CornellTechBot()

    def test_can_be_created(self):
        expect(ctechbot.slack_client).not_to(equal(None))
        expect(ctechbot.BOT_ID).not_to(equal(None))
        expect(ctechbot.BOT_NAME).to(equal("cornelltechbot"))

    def test_can_read_messages(self):
        expect(ctechbot.connect()).not_to(equal(None))
