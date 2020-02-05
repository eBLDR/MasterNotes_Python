#!/usr/bin/env bash

# This file can be run as a sh script or line by line from the command line

VENV_FOLDER="venv"
PYTHON_PATH="/usr/bin/python3"
REQ_FILE="requirements.txt"

# Remove previous virtualenv (if any)
rm  -v -rf ${VENV_FOLDER}

# Create a new virtualenv
virtualenv -p ${PYTHON_PATH} ${VENV_FOLDER}
# -p, --python flag is optional, will take /usr/bin/python, version by default

# Activate virtualenv
source ${VENV_FOLDER}/bin/activate

# Deactivate virtualenv
# deactivate

# pip upgrade and setuptools (upgrading to last version of pip and setuptools)
pip install --no-cache-dir --upgrade pip setuptools

# pip install required modules/packages (if <file_name.txt> (commonly named
# requirements.txt) is already existing)
# Will install all the modules/packages found in the file
pip install --no-cache-dir -r ${REQ_FILE} -I

# To install a specific module/package inside the virtualenv, from virtualenv
# folder run
# pip install <package_name>

# Show the modules/packages used by the virtual environment
pip freeze

# Save the previous list into a new file
pip freeze > ${REQ_FILE}
