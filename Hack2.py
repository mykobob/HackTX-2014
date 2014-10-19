import contextio as c
import itertools
import time
import run

t0 = time.time()
CONSUMER_KEY = 'vq1jfna1'
CONSUMER_SECRET = '5pT7Uiujrtzcmcxd'
context_io = c.ContextIO(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET)
accounts = context_io.get_accounts()
#importantList = run.initiate()
print 'done importing'
while True:
	for account in accounts:
		print account.created
		important = False
		if account.nb_messages is None:
			messageCount = 0
		else:
			messageCount = account.nb_messages
		print messageCount
		account_id = account.id
		account.post_sync()
		while 'True' != str(account.get_sync())[-7:-3]:
			blank = 0
		print 'synced'
		if account.nb_messages is None:
			compare = 0
		else:
			compare = account.nb_messages
		if compare>messageCount:
			print 'sup'
			message = account.getMessages(limit= accout.nb_messages-messageCount)
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
				#return str(message)
				print message

