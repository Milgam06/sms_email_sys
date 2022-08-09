from email import message
import os
import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

account_sid = 'AC650de3253b98cc92af5d6d960016ffc5'
auth_token = '49104196ae1254052fd39ee6b3bafc58'
client = Client(account_sid, auth_token)

print('WARNING : When writing your callnumber, you should write it like this -> 10 1234 1234')

callnum = str(input('Callnumber: '))
if callnum[0] == '0':
    print("Please read the WARNING")
    exit()

email = str(input('Email Address: '))
if "@" not in email:
    print("Please enter right email address")
    exit()

messageBody = str(input("Body of message to send : "))
messageTitle = str(input("Title of message to send : "))

message = client.messages.create(
    body=(messageTitle + "\n" + messageBody), 
    from_='+17432007538', 
    to='+82' + callnum
)

print(message.sid)


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("milgamfruit@gmail.com", "yoeslssmohneydgu")
msg = MIMEText(messageBody)
msg["Subject"] = messageTitle
s.sendmail('milgamfruit@gmail.com', email, msg.as_string())
s.quit()