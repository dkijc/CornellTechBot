import nose
from cleo import Command

class TestCommand(Command):
    """
    Tests the chatbot

    test
    """

    def handle(self):
        result = nose.run(argv=['', '--with-specplugin', '--exe'])