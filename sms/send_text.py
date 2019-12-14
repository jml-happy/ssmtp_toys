# IMPORTANT: This is just a toy script and is not meant to be robust, follow best practices, or anything like that.

import sys
import subprocess
import gateways

# TODO: make this a bash script because running bashscripts from python isn't best?
sms_num_str = input("Enter phonenumber as 10-digits, no spaces (0 to cancel): ")
if '0' == sms_num_str:
    sys.exit()

while not sms_num_str.isdigit() or 10 != len(sms_num_str):
    print("Phone number must be 10 digits with no spaces or dashes!")
    sms_num_str = input("Enter phone number(0 to cancel): ")
    if '0' == sms_num_str:
        sys.exit()

carrier_str = input("Select carrier: 1. Sprint, 2. AT&T, 3. Verizon 4.T-Mobile (0 to cancel): ")
if '0' == carrier_str:
    sys.exit()

while not carrier_str.isdigit() or 1 != len(carrier_str):
    print("Please enter a single digit [1-4].")
    carrier_str = input("Select carrier: 1. Sprint, 2. AT&T, 3. Verizon 4.T-Mobile (0 to cancel): ")
    if '0' == carrier_str:
        sys.exit()

carrier_int = int(carrier_str)
carrier_keys = {1: "SPRINT", 2: "ATT", 3: "VERIZON", 4: "TMOBILE"}

carrier = carrier_keys[carrier_int]
sms_gateway = gateways.carrier_dict[carrier]

# ##### Start sending message

ssmtp_address = sms_num_str + '@' + sms_gateway
print(ssmtp_address)

# I'm aware this is the wrong way to send an email from python.  The project is called ssmtp_toys !!!!
# See the snippet sendmail.py for an smtplib module example
print("Enter your message, then press Ctrl+D: ")
subprocess.run('ssmtp -v ' + ssmtp_address, shell=True, check=True)
