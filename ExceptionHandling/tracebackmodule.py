# Allows to save the traceback from exceptions raised as string

import traceback

try:
    raise Exception('This is an error msg.')

except Exception:
    # The best way to keep track of errors raised is creating a file containing the info
    with open('errorInfo.txt', 'w') as errorFile:
        # traceback.format_exc() returns the str of the traceback
        errorFile.write(traceback.format_exc())

    print(traceback.format_exc())
    print('Traceback info was written to errorInfo.txt.')
