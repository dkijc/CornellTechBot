from cleo import Command
from server.app import app

class RunCommand(Command):
    """
    Runs the chatbot

    run
    """
    def handle(self):
        app.run(host="localhost", debug=True)