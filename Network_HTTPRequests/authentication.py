# HTTP Basic Auth for web services that require authentication
import requests
from requests.auth import HTTPBasicAuth

user_name = 'ebldr'
user_password = '##########'

url = 'https://api.github.com/user'

# Use @auth from get() method to send the authentication
response = requests.get(url, auth=HTTPBasicAuth(user_name, user_password))
response.raise_for_status()

print(response.json())
print('=' * 20)

# Shorthand form - there isn't even a need to import the HTTPBasicAuth
response_2 = requests.get(url, auth=(user_name, user_password))
response_2.raise_for_status()

print(response.json() == response_2.json())

"""
# Digest Authentication will follow the same process
from requests.auth import HTTPDigestAuth

url_digest = 'https://httpbin.org/digest-auth/auth/user/pass'
response_3 = requests.get(url_digest, auth=HTTPDigestAuth(user_name, user_password))
response_3.raise_for_status()
"""

"""
# OAuth 1 Authentication
from requests_oauthlib import OAuth1

url_oauth1 = ''
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

response_4 = requests.get(url, auth=auth)
response_4.raise_for_status()
"""
