# Import-related module attributes
import math

print('__name__ is:', __name__)

print('__file__ is:', __file__)

print('__package__ is:', __package__)

# Only for a module that is a package
print('math.__loader__ is:', math.__loader__)

# Spec information used when importing the module
print('math.__spec__ is:', math.__spec__)
