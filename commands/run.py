from cleo import Command
from bot.bot import CornellTechBot
import time

class RunCommand(Command):
    """
    Runs the chatbot

    run
    """

    def handle(self):
        self.line('<info>Starting up the chatbot</info>')
        ctechbot = CornellTechBot()
        server = ctechbot.connect()
        if server:
            self.line('<info>Connected! Now Reading/Responding</info>')
            while True:
                ctechbot.read_and_respond()
                time.sleep(1)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")
            return