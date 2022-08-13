# Email, SMS send

from email import message
import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

account_sid = ""
auth_token = ""

def setting(sid, token):
    global account_sid
    global auth_token
    account_sid = sid
    auth_token = token
    return account_sid,auth_token


messageBody = str(input("Body of message to send : "))
messageTitle = str(input("Title of message to send : "))


def message():
    print('WARNING : When writing your callnumber, you should write it like this -> 10 1234 1234')  
    
    callnum = str(input('Callnumber: '))
    if callnum[0] == '0':
        print("Please read the WARNING")
        exit()
    
    message = Client(account_sid,auth_token).messages.create(
        to='+82 ' + callnum,
        from_='+17432007538',
        body=(messageTitle.upper() + "\n" + messageBody)
        )
    print(message.sid)  



email = str(input('Email Address: '))
if "@" not in email:
    print("Please enter right email address")
    exit()



s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("milgamfruit@gmail.com", "yoeslssmohneydgu")
msg = MIMEText(messageBody)
msg["Subject"] = messageTitle.upper()
s.sendmail('milgamfruit@gmail.com', email, msg.as_string())
s.quit()