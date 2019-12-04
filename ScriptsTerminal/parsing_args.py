# argparse module it's a parser for command-line options, arguments and sub commands
import argparse

# Instance of parses
parser = argparse.ArgumentParser(description='Some optional description for the module.')

# Positional arguments - @key_name_of_arg, @help='', @type=str)
parser.add_argument('echo', help='Custom help msg for echo', type=int)

# @choices=seq - adds a validation of argument
parser.add_argument('echo_2', help='Custom help msg for echo', choices=['wind', 'fire'])

# Optional arguments - if name starts with '--' or '-', argument is expected
# The order of arguments does not matter
parser.add_argument('--option', help='Custom help msg for --option', default=None)

# Mode - uses the @action arg, no extra argument is expected
# @action='store_true' will store the value True to the arg if the flag is used
parser.add_argument('-y', '--yes', help='Custom help msg for --yes', action='store_true')

# Parsing args - returns data
args = parser.parse_args()

print(args)
print('Echo:', args.echo)
print('Echo_2:', args.echo_2)
print('Option:', args.option)
print('Yes:', args.yes)
