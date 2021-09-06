import phonenumbers
from phonenumbers import carrier,geocoder,timezone

mobileNo=input('enter your phone number with your country code ')
mobileNo=phonenumbers.parse(mobileNo)

#get timezone a phone number 
print(f"your phone no#. timezone: {timezone.time_zones_for_number(mobileNo)}")

#getting a carrier for the phone number
print(f"your phone number carrier : {carrier.name_for_number(mobileNo,'en')}")

#getting Region Info
print(f"country : {geocoder.description_for_number(mobileNo,'en')}")

#validating a phone number
print('Valid Mobile Number :', phonenumbers.is_valid_number(mobileNo))

