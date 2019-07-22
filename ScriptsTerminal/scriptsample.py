#!/usr/bin/python3
"""
The first line is the 'shebang' line (see magiclines.txt).

--- LINUX & OS X ---
To run the script from the terminal, go to script directory and type:
./nameoffile.py

Execution permissions might be required to run the script, if so, type:
chmod +x nameoffile.py

To run the script as a command line command, delete the extension from file name and
add the directory to the PATH. In linux:

$ export PATH=$PATH":$HOME/bin"

This will add ~/bin to PATH temporary, any folder can be specified.
For a permanent addition, add the above line to .profile or .bash_profile in home directory
"""
import sys

module_name = sys.argv[0]
print('Hi, I am {}'.format(module_name))

try:
    print('Mode: {}'.format(sys.argv[1]))
except IndexError:
    print('ERROR - No mode specified.\nUsage:\n{} <mode>'.format(module_name))

sys.exit(12)
