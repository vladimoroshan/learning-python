#! python3
# send_sms.py - Skeleton to sending sms using Twilio

from twilio.rest import Client

ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxx'
AUTH_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

myTwilioNumber = '+*********************'
myCellPhone = '+*******************''
text = 'Hello from Python'

message = client.messages.create(from_=myTwilioNumber, to=myCellPhone, body=text)

print(message.sid)
