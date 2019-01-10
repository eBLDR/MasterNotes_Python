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

module_name = sys.argv[0]
print('Hi, I am {}'.format(module_name))

try:
    print('Mode: {}'.format(sys.argv[1]))
except IndexError:
    print('ERROR - No mode specified.\nUsage:\n{} <mode>'.format(module_name))

sys.exit(12)

