import os
from slackclient import SlackClient

class CornellTechBot:
	def __init__(self):
		self.BOT_NAME = 'cornelltechbot'
		self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
		self.BOT_ID = SlackClient(os.environ.get('BOT_ID'))

# if __name__ == "__main__":
# 	api_call = slack_client.api_call("users.list")
# 	if api_call.get('ok'):
# 		users = api_call.get('members')
# 		i = 0
# 		for user in users:
# 			i += 1
# 			if 'name' in user and user.get('name') == BOT_NAME:
# 				print("Bot ID for '" + user['name'] + "' is " + user.get('id'))	
# 	else:
		# print("could not find bot user with the name " + BOT_NAME)
		
