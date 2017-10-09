#! python3
# send_sms.py - Skeleton to sending sms using Twilio

from twilio.rest import Client

ACCOUNT_SID = 'AC1f0ccba8ff29f09818bf57480f4e1218'
AUTH_TOKEN = 'e931a9e357bcdd00fbb1744eb9941f36'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

myTwilioNumber = '+15017250604'
myCellPhone = '+380996078737'
text = 'Hello from Python'

message = client.messages.create(from_=myTwilioNumber, to=myCellPhone, body=text)

print(message.sid)
