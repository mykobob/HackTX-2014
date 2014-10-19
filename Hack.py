import contextio as c
import itertools
import time
import run
import copy

t0 = time.time()
CONSUMER_KEY = 'vq1jfna1'
CONSUMER_SECRET = '5pT7Uiujrtzcmcxd'
context_io = c.ContextIO(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET)
accounts = context_io.get_accounts()
importantList = run.initiate()
important = False
print 'Import Complete'
while !important:
	for account in accounts:
		account.get()
		messageCount = account.nb_messages
		account_id = account.id
		account.post_sync()
		while 'True' != str(account.get_sync())[-7:-3]:
			blank = 0
		account.get()

		if account.nb_messages>messageCount:
			print 'Message Found'
			messages = account.get_messages(limit= account.nb_messages-messageCount, include_body = 1)
			for message in messages:
				message.get()
				sender = message.addresses['from']['email']
				if sender in importantList[account_id][0]:
					message.post_folder(add='\\Important')
					important = True
				else:
					subject = message.subject.split( )
					for word in subject:
						if subject in importantList[account_id][1]:
							message.post_folder(add='\\Important')
							important = True
				if important:
					output = open ('output.txt', 'w')
					output.write(message.addresses['from']['name']+'\n')
					output.write(message.subject+'\n')
					output.write(message.body[0]['content'])
					output.close()