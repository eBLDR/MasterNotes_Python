"""
A traceback is a report containing the function calls made in your code at
a specific point.
Traceback is also refer to as 'stack trace' or 'backtrace'.
"""
# Allows to save the traceback from exceptions raised as string
import traceback

try:
    raise Exception('This is an error msg.')

except Exception:
    # The best way to keep track of errors raised is creating a file containing the info
    with open('error_info.txt', 'w') as errorFile:
        # traceback.format_exc() returns the str of the traceback
        errorFile.write(traceback.format_exc())

    print(traceback.format_exc())
    print('Traceback info was written to error_info.txt.')
