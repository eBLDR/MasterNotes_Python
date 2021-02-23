# HTTP requests
import requests

# GET method
# httpbin.org is a free client testing service
response = requests.get('https://httpbin.org/get')

print(type(response))
print(response)  # <Response [status_code]>

# Code
print('Status code:', response.status_code)

# If status code is 4xx or 5xx (client or server errors), next method will raise an error
response.raise_for_status()

# Encoding used
print('Encoding:', response.encoding)  # it can be changed to any encoding needed

# Data as str
print(response.text[:100])

print('=' * 30)

# Passing parameters in URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

# To return the URL - notice the parameters construction
print('URL:', r.url)

# Headers contain the type of the response's content
print('content-type:', r.headers['content-type'])

"""
Common content-type headers are:
text/plain for plain text
application/json for json
application/octet-stream for binary

Headers can be sent in a request using:
r = requests.get(url, headers=headers)
headers is type dict
"""

print(type(r.content))

# Raw content
print(r.raw)

# JSON content
r2 = requests.get('http://httpbin.org/get')

r2 = r2.json()

print(r2)  # dictionary
print(r2.keys())

print('=' * 30)

# POST method - the end point is receiving the data, @data will send binary data
r3 = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r3.status_code)

# Posting JSON, @json will send json data, it will be converted into json automatically
r4 = requests.post('http://httpbin.org/post', json=payload)
print(r4.status_code)

# PUT method
r3 = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r3.status_code)

# DELETE method
r3 = requests.delete('http://httpbin.org/delete')
print(r3.status_code)

# HEAD method
r3 = requests.head('http://httpbin.org/get')
print(r3.status_code)

# OPTIONS method
r3 = requests.options('http://httpbin.org/get')
print(r3.status_code)
