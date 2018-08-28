#! /usr/bin/python3

"""
The first line is the 'shebang' line (see magiclines.txt).

--- LINUX & OS X ---
To run the script from the terminal, go to script directory and type:
./nameoffile.py

We may need execution permissions to run a script, if so, type:
chmod +x nameoffile.py
"""
import sys

print("Hi, I am {}".format(sys.argv[0]))

try:
    print("Mode: {}".format(sys.argv[1]))
except IndexError:
    print("No mode specified.")

sys.exit(12)
