"""
Hypertext Transfer Protocol (HTTP) is an application protocol which is the
foundation of data communication for the World Wide Web (www).

HTTP communication protocol is synchronous: that means that one request is sent
at a time and will wait for its response to arrive before continuining.

In the communication between client and server, Uniform Resource Identifier (URI) are used.

-- Request Methods --

GET method - used to request data from a specified resource.

HEAD method - almost identical to GET, but without the response body.

POST method - used to send data to a server to create/update a resource.

PUT method - used to send data to a server to create/update a resource.
PUT requests are idempotent.

DELETE method - deletes the specified resource.

OPTIONS method - describes the communication options for the target resource.
"""

import requests

# GET method
# httpbin.org is a free client testing service
response = requests.get('https://httpbin.org/get')

print(type(response))
print(response)  # <Response [status_code]>

# Code
print("Status code:", response.status_code)

# If status code is 4xx or 5xx (client or server errors), next method will raise an error
response.raise_for_status()

# Encoding used
print("Encoding:", response.encoding)  # it can be changed to any encoding needed

# Data as str
print(response.text[:100])

print("=" * 30)

# Passing parameters in URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

# To return the URL - notice the parameters construction
print("URL:", r.url)

# Headers containt the type of the response's content
print("content-type:", r.headers['content-type'])
"""
Common headers are:
text/plain for plain text
application/json for json
application/octet-stream for binary
"""

print(type(r.content))

# Raw content
print(r.raw)

# JSON content
r2 = requests.get('http://httpbin.org/get')

r2 = r2.json()

print(r2)  # dictionary
print(r2.keys())

print("=" * 30)

# POST method - the end point is receiving the data
r3 = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r3.status_code)

# Posting JSON
r4 = requests.post('http://httpbin.org/post', json=payload)  # will be encoded automatically
print(r4.status_code)

# PUT method
r3 = requests.put('http://httpbin.org/put', data = {'key':'value'})
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
