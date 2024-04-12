import imaplib, email

user = 'email@gmail.com'
password = 'app password'
imap_url = 'imap.gmail.com'

def search(key, value, con): 
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

def get_emails(result_bytes):
	msgs = [] 
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

con = imaplib.IMAP4_SSL(imap_url) 

con.login(user, password) 

con.select('Inbox') 

msgs = get_emails(search('FROM', 'email@email.com', con))

for msg in msgs[::-1]: 
	for sent in msg:
		if type(sent) is tuple: 

			msg = email.message_from_bytes(sent[1])

			sender = msg['From']
			subject = msg['Subject']
			date = msg['Date']

			print("Sender:", sender)
			print("Date received:", date)
			print("Subject:", subject)
