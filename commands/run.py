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

        # TODO: fix infinite loop for read_and_respond
        while True:
            ctechbot.read_and_respond()