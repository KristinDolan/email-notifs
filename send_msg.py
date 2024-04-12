import imaplib
import email
from twilio.rest import Client

account_sid = 'my_twilio_sid'
auth_token = 'placeholder_token'
twilio_phone_number = 'twilio_phone_number'
recipient_phone_number = 'my_phone_number'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('email@gmail.com', 'password')
mail.select('inbox')

# Specify to search only for unread emails
result, data = mail.search(None, 'UNSEEN')

for num in data[0].split():
    result, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)
    subject = msg['subject']

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'New email received: {subject}',
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f'SMS notification sent: {message.sid}')