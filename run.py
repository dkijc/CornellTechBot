from bot.bot import CornellTechBot

if __name__ == "__main__":
    ctechbot = CornellTechBot()
    server = ctechbot.connect()

    # TODO: fix infinite loop for read_and_respond
    while True:
        ctechbot.read_and_respond()