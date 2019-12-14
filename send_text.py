import sys
import gateways

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

sms_num_int = int(sms_num_str)
sms_area_code_str = sms_num_str[0:3]
sms_area_code_int = int(sms_area_code_str)

sms_prefix_str = sms_num_str[3:6]
sms_prefix_int = int(sms_prefix_str)

sms_suffix_str = sms_num_str[6:10]
sms_suffix_int = int(sms_suffix_str)

carrier_keys = { 1: "SPRINT", 2: "ATT", 3: "VERIZON", 4: "TMOBILE" }
carrier = carrier_keys[carrier_int]
sms_gateway = gateways.carrier_dict[carrier]

print(carrier)
print(sms_gateway)
print(sms_area_code_int)
print(sms_prefix_int)
print(sms_suffix_int)
