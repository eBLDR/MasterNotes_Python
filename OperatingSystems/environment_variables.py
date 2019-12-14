"""
Accessing environment variables.
In some code editors (like Pycharm), it's possible to add them to the
project's configuration.
"""
import os

# List all env variable
print(os.environ)

# os.getenv() is equivalent to os.environ.get()
print('HOME is ', os.getenv('HOME', 'Not found'))

# Create new env variable - it will be erased after killing the process.
os.environ['NEW_KEY'] = 'NEW_VALUE'
print(os.getenv('NEW_KEY'))
