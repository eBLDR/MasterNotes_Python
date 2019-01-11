import sys

print(sys.platform)  # String contains a platform identifier.

print(sys.copyright)  # Shows the copyright.

print(sys.version)  # Shows the python version being used to run the script.

print(sys.prefix)  # Shows the python installation path being used to run the script.

print(sys.flags)  # Exposes the status of command line flags.

print(sys.path)  # A list of strings that specifies the search path for modules.

print('=' * 30)

# sys.argv() - a list of command line arguments passed to the script, argv[0] is the script name.
# (it's operating system dependent whether this is a full pathname or not).
# If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'.

name_of_file = sys.argv[0]  # Full path and name of file.

print(name_of_file)

if len(sys.argv) > 2:
    arg_1 = sys.argv[1]
    print('arg is{}'.format(arg_1))

# Stops the program and returns specified code.
sys.exit(4)
