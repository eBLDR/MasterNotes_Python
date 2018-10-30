import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print('Number must be an integer')

        # This error is raised whe user pressed Ctrl+D in Linux or Windows, or Cmd+D in Mac
        # Ctrl+D jumps to the end of the file
        except EOFError:  # End Of File Error
            print('Don\'t try to crash my code')
            sys.exit(12)  # this will terminate the program
            # parameter is the exit code - 0 is the default (normal termination)


user_number = get_int('Give me a number:\n')

