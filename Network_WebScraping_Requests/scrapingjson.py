"""
Program that tells us who is in the space right now.

A web service has an address (url) just like a web page does.
Instead of returning HTML for a web page it returns data.

The data is live, different results every refresh.
The format is (usually) JSON (JavaScript Object Notation).
"""

# import json  # this is the encoder & decoder, it's included in requests module
import requests

# url where to take the data from
url = 'http://api.open-notify.org/astros.json'

# collecting data from web service and decoding it
response = requests.get(url).json()
# .json() is actually converting json-formatted data to a python value from the response.text object
# we could do it manually with json.loads(response.text) from json module

print(response)         # it's a dictionary
print(response.keys())  # to get the keys

print('=' * 20)

# showing data
print("\nPeople in Space: {}\n".format(response['number']))

for human in response['people']:
    print("{} in {}".format(human['name'], human['craft']))
