import phonenumbers
from phonenumbers import geocoder

text = input("Enter phone number: ")
number = phonenumbers.parse(text)
countryCode = geocoder.description_for_number(number, "en")

print(f"The detected country code is: {countryCode}")