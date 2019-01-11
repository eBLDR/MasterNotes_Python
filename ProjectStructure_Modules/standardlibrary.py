print(dir())  # calling the directory of standard methods
# methods or variables that start with double underscore (__) are private by convention

# noinspection PyUnresolvedReferences
for m in dir(__builtins__):  # to show all the built-in methods
    print(m)

import shelve

help(shelve)  # to call documentation file
help(shelve.open)  # to call specific documentation of one method
