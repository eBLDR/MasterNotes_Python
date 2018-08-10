"""
It is possible to pass command line arguments to processes launched with Popen().
To do so, pass a list as the sole argument, the first str in the list will be the executable filename
of the program to be launched; all the subsequent str will be the command line arguments,
in fact, this list will be the value of sys.argv.
"""

import subprocess

# Launching a python script as an independent process - variables won't be shared
# It's gonna run without ui
pyScript = subprocess.Popen(['python', 'launchedprocess.py'])  # shell=True), it opens a new python shell
pyScript.wait()

# Opening the file with the corresponding program
subprocess.Popen(['gedit', 'sample.txt'])

# Opening files with the default application
# Programs in charge of searching for default application corresponding to file's extension
# Windows - 'start'
# OS X - 'open'
# Ubuntu Linux - 'see'
# subprocess.Popen(['see', 'sample.txt'])  # , shell=True) - needed only in Windows
