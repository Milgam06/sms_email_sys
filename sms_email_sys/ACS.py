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

tw.setting('AC650de3253b98cc92af5d6d960016ffc5','e74ce99ace232b9f75adea2bb55503f2')