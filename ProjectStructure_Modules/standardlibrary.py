"""
When importing a module, the python interpreter searches for it in the
directories listed in its sys.path variable. If the module is found, then
the statements in the body of that module are run and the module is made
available in the current namespace.

sys.path includes the current working directory, among other paths.

Initialization is made only the first time that a module is imported.
"""
# Importing an existing module from standard library
import math

# Calling module's documentation
help(math)

# Calling a variable from inside the module
print(math.pi)

# Call specific documentation of one method
help(math.sqrt)
