# AutoCertificateSystem

import random
from twilio.rest import Client
from time import sleep
import twilio_sms as tw

codes = []

for _ in range(3):
    code = random.randint(1, 50)
    codes.append(code)

print(codes)

tw.setting(account_sid, auth_token)
