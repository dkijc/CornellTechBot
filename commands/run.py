from cleo import Command
from bot.bot import CornellTechBot

class RunCommand(Command):
    """
    Runs the chatbot

    run
    """

    def handle(self):
        ctechbot = CornellTechBot()
        server = ctechbot.connect()
        if server:
            users = ctechbot.client.api_call('users.list')
            ctechbot.read_and_respond(users)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")
            return