from bot.bot import CornellTechBot

if __name__ == "__main__":
    ctechbot = CornellTechBot()
    server = ctechbot.connect()

    # TODO: fix infinite loop for read_and_respond
    if server:
        users = ctechbot.client.api_call('users.list')
        
        while True:
            ctechbot.read_and_respond(users)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")