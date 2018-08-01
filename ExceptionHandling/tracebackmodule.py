# allow to save the traceback from exceptions raised as str

import traceback

try:
    raise Exception("This is an error msg.")

except Exception:
    # the best way to keep track of errors raised is creating a file containing the info
    with open('errorInfo.txt', 'w') as errorFile:
        # traceback.format_exc() is a the str of traceback
        errorFile.write(traceback.format_exc())

    print(traceback.format_exc())
    print("The traceback info was written to errorInfo.txt.")
