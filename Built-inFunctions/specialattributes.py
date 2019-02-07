# Some of these are not reported by dir()

# A dictionary of class attributes
print('type.__dict__ is:', type.__dict__)

# The class to which the instance belongs
print('object.__class__ is:', object.__class__)

# Base class
print('type.__bases__ is:', type.__bases__)

# Name
print('type.__name__ is:', type.__name__)

# The qualified name - a dotted name showing the path from a module's global scope to the descriptor
print('type.__qualname__ is:', type.__qualname__)

# A tuple of classes that are considered when looking for base classes during method resolution
print('type.__mro__ is:', type.__mro__)

# A list of weak references to its immediate subclasses
print('int.__subclasses__ is:', int.__subclasses__())

# Module where class is found
print('type.__module__ is:', type.__module__)

# Docstring of class
print('type.__doc__ is:', type.__doc__)


# Annotations of class/method/object
def f(i: int):
    return i


print('f.__annotations__ is:', f.__annotations__)
