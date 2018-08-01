#! /usr/bin/python3

"""
.py for normal execution, .pyw for executing without showing terminal.

The first line is called 'shebang', it tells the os which program should be called to execute the script.

- Windows, the shebang line is  #! python3
- OS X, the shebang line is     #! /usr/bin/env python3
- Linux, the shebang line is    #! /usr/bin/python3
- Virtual environments          #! /myvenv/bin/python

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
