"""
There is 1 input pipe:
- Standard input - is used for all interactive input (including calls to input())

There are 2 output pipes:
- Standard output (stdout) - normal output pipe (print() prints here)
- Standard error (stderr) - debugging information goes to this pipe (traceback error)

sys.stdin is a file-like object with read-only methods

sys.stdout and sys.stderr are file-like objects with write-only methods
"""
import sys

# Reading from standard input
print('Type something:')
data = sys.stdin.readline()  # Reads data from stdin (similar to input())
print('You have type:', data)

string = 'Python'

# Printing in standard output
for i in range(3):
    sys.stdout.write(string)
    sys.stdout.flush()  # Will flush the data buffered
    """
    Python's standard out is buffered (meaning that it collects some of the data
    "written" to standard out before it writes it to the terminal).
    """

print()

# print() add a carriage return at the end of the str ('\n') and calls sys.stdout.write(),
# and sysstdout.write call stdout.flush() whenever the last character is '\n'.
for i in range(3):
    print(string)

print()

# Printing in error output
for i in range(3):
    sys.stderr.write(string)

# Redirecting print()'s output - stdout to file

save_out = sys.stdout  # Saving the default value in case we wish to reuse it later
log_file = open('outputpipes.log', 'w')  # Opening file
sys.stdout = log_file  # Assigning stdout to log file
print('This msg called using print() goes directly to file, it uses stdout.')
log_file.close()
sys.stdout = save_out  # Going back to default config

# Redirecting print()'s output - stderr to file
log_file = open('outputpipes.log', 'a')
sys.stderr = log_file
raise Exception('This error msg goes directly to file, it uses stderr.')

# The next syntax will redirect a single msg, works only from command line or Shell
# print >> sys.stderr, 'redirect this msg to sys.sterr'
