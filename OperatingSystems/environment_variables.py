"""
Environment variables are variables declared in the os, it's a dictionary like.
In Linux we can see them with the command 'export' or 'printenv' in the
terminal.
They are useful for avoiding having to write passwords in the scripts.

Setting env variables:
    - Adding them on the system variables.
    - MYOSENV=VAR <file_name>, at the moment of running the .py script
    - Using a bash script, they will be erased after restart.
    - Using os.environ['NEW_KEY'] = 'NEW_VALUE' in Python, they will be erased
    after killing the process.
    - In some code editors (like Pycharm), it's possible to add them to the
    project's configuration.
"""
import os

# List all env variable
print(os.environ)

# os.getenv() is equivalent to os.environ.get()
print('HOME is ', os.getenv('HOME', 'Not found'))
