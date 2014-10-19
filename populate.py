import MySQLdb
import contextio as c
import itertools


CONSUMER_KEY = 'vq1jfna1'
CONSUMER_SECRET = '5pT7Uiujrtzcmcxd'
context_io = c.ContextIO(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET)
accounts = context_io.get_accounts()

db = MySQLdb.connect("localhost", "chris", "Chri$2pi", "hacktx")

cursor = db.cursor()


for account in accounts:

	account.post_sync()
	while 'True' != str(account.get_sync())[-7:-3]:
		hi = 0

	#sql = "create table " + str(account.id) + " (messageID varchar(1024), seen bool)"
	sql = ""
	print sql
	#cursor.execute(sql);

	messages = account.get_messages(limit = 10, include_flags = 1)
	for message in messages:
		flags = message.get_flags()
		seen = flags['seen']
		answered = flags['answered']
		print seen
		subject = message.subject
		sender = message.addresses['from']['email']
		messageID = message.message_id
		#sql = "INSERT INTO " + str(account.id) + " VALUES ('%s', '%s', '%s', '%b', '%b')" %(messageID,subject,sender,seen,answered)
		#cursor.execute(sql)


cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s " %data






db.close()