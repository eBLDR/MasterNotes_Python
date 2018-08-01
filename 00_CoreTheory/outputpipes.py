"""
There are 2 output pipes in Python:
- Standard output (stdout) - normal output pipe (print() prints here)
- Standard error (stderr) - debugging information goes to this pipe (traceback error)

sys.stdout and sys.stderr are file-like objects with write-only methods
"""

import sys

string = 'Python'

# Printing in standard output
for i in range(3):
    sys.stdout.write(string)

print()

# print() add a carriage return at the end of the str ('\n') and calls sys.stdout.write
for i in range(3):
    print(string)

print()

# Printing in error output
for i in range(3):
    sys.stderr.write(string)

# Redirecting print()'s output - stdout to file

saveout = sys.stdout  # Saving the default value in case we wish to reuse it later
log_file = open('outputpipes.log', 'w')  # Openning file
sys.stdout = log_file  # Assigning stdout to log file
print('This msg called using print() goes directly to file, it uses stdout.')
log_file.close()
sys.stdout = saveout  # Going back to default config

# Redirecting print()'s output - stderr to file
log_file = open('outputpipes.log', 'a')
sys.stderr = log_file
raise Exception('This error msg goes directly to file, it uses stderr.')

# The next syntax will redirect a single msg, works only from command line or Shell
# print >> sys.stderr, 'redirect this msg to sys.sterr'
