"""
Project skeleton basis.

Packages are just a convenience to organize modules hierarchically.

Because mypackage has a __init__.py file, all the data inside
the folder can be treated as if it was a single module.

__init__.py file will be the first one to be executed when importing any
module inside the package.
"""
# Importing the whole module
from mypackage import demomodule

# Specific object import
from mypackage.demomodule import demo2

demomodule.demo()

demo2()

# Importing a nested packaged
from mypackage.settings import local

print(local.SECRET_VAR)
