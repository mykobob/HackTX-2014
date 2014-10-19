import contextio as c
import itertools
import time

CONSUMER_KEY = 'vq1jfna1'
CONSUMER_SECRET = '5pT7Uiujrtzcmcxd'
context_io = c.ContextIO(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET)
accounts = context_io.get_accounts()

def initiate():
	bad_words = []
	dictionary = open('Dictionary.txt', 'r')
	for line in dictionary:
		bad_words.append(line[0:-2])
	toReturn = {}
	for account in accounts:

		account.post_sync()
		while 'True' != str(account.get_sync())[-7:-3]:
			hi = 0
		most_sent = []
		most_received = []
		most_replied = []
		dict = {}
	


		toReturn[account.id] = {}

		contacts = account.get_contacts(limit = 10, sort_by = 'sent_count')
		for contact in contacts:
			most_sent.append(contact.email)

		contacts = account.get_contacts(limit = 10, sort_by = 'received_count')
		for contact in contacts:
			most_received.append(contact.email)
	

		messages = account.get_messages(limit = 10, include_flags = 1)
		for message in messages:
			flags = message.get_flags()
			if len(flags) > 0:
				if flags['seen'] or flags['answered']:
					most_replied.append(message.addresses['from']['email'])
			subject = message.subject
			for word in subject.split():
				word = word.lower()
				if word in dict.keys():
					dict[word]+=1
				else:
					dict[word]=1
	
		for word in dict.keys():
			if dict[word] <= 20 / 10:
				del dict[word]
		for word in dict.keys():
			for bad_word in bad_words:
				if word == bad_word:
					del dict[word]


		combined_list = list(set(itertools.chain(most_sent,most_received,most_replied)))
		toReturn[account.id][0] = combined_list
		toReturn[account.id][1] = dict
		

	return toReturn