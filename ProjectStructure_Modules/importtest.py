"""
When importing a file, a new namespace is created, and everything in that file is executed
in that namespace.

Importing only ever loads a module once. Any imports of the same module from different
files after that simply add it to the current namespace.

USING UNDERSCORES
Python does NOT have private or hidden objects.
_whatever, by convention, means that the object should be protected, so not to be used
outside of the file where it exists, so when importing file, Python will NOT import
variables with a name starting with '_'.

__object__ this should never be touched.

Note: is totally fine to import multiple modules in a single line, like so:
import time, math, random
Though PEP-8 style guide recommends not to do so, and import every module on its own line:
import time
from math import pi, sqrt, pow
import random
"""

import sampleimported  # To import the whole module

# If we wish to change the name to reference to the module
# import sampleimported as <new_name>

# The next statement will import all (*) from the file, except for the methods that start with underscore (_),
# this is not advised because all the names become part of our namespace and can cause problems with duplicates
# from sampleimported import *

# We can import specific objects
from sampleimported import superKey

# __name__ is an attribute of the file
print('I am ' + __name__)
print('and I\'m importing ' + sampleimported.__name__)

print(type(sampleimported))

print('My attributes are:')
print(dir(sampleimported))  # To show all the data/method attributes in the module

# Calling a function inside the imported module, module.method()
sampleimported.hi()

# Calling a variable inside the imported module
print(sampleimported.key)

# It's now part of the namespace of this module - no need to specify the module
print(superKey)

print('=' * 20)

# Show global variables in this module, notice superKey from the imported module!!!
g = sorted(globals())
print('globals() are:')
for x in g:
    print(x)
    # actually g is also global now, but not at the moment of creating the list

print('=' * 20)

print('locals().keys() are:')
print(locals().keys())

print('=' * 20)

# vars() can take a dict as an argument
print('vars().keys() are:')
print(vars().keys())

print('=' * 20)

# If the file is not in the same folder, we can specify the path using . as tree structure
import subfolder.subsampleimported

print(subfolder.subsampleimported.subkey)
