"""
Because mypackage has a __init__.py file, all the data inside
the folder can be treated as if it was a single module.
"""
# Importing the whole module
from mypackage import demomodule

# Specific object import
from mypackage.demomodule import demo2

demomodule.demo()

demo2()
