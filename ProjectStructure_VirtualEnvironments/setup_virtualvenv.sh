#!/usr/bin/env bash

# This file can be run as a sh script or line by line from the command line

# Remove previous virtualenv (if any)
$ rm  -v -rf <OLD_VENV_DIRECTORY>

# Create a new virtualenv
$ virtualenv -p PYTHON_EXE_ABSOLUTE_PATH <NEW_VENV_DIRECTORY>
# -p is optional, will take /usr/bin/python, version by default

# Activate virtualenv
$ source <NEW_VENV_DIRECTORY>/bin/activate

# Deactivate virtualenv
# $ deactivate

# pip upgrade and setuptools (upgrading to last version of pip and setuptools)
$ pip install --no-cache-dir --upgrade pip setuptools

# pip install required modules/packages (if <file_name.txt> (commonly named requirements.txt) is already existing)
# Will install all the modules/packages found in the file
$ pip install --no-cache-dir -r <file_name.txt> -I

# To install a specific module/package inside the virtualenv, from virtualenv folder run
$ pip install <package_name>

# will show the modules/packages used by the virtual environment
$ pip freeze

# will save the previous list into a new file
$ pip freeze > <new_file_name.txt>

