from unittest import TestCase
from expects import expect, equal
from slackclient import SlackClient
import os

class TestBot(TestCase):
    def test_can_hit_slack_api(self):
        BOT_NAME = 'starterbot'
        slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        api_call = slack_client.api_call("users.list")
        expect(api_call.get('ok')).to(equal(True))
