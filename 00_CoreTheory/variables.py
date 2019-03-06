"""
Every variable/object has 3 characteristics:
- TYPE (class where object inherits attributes from).
- VALUE (content/s).
- IDENTITY (memory location, id()).

When creating an object, 3 things are happening:
1. The object is created (with its content/s, if required) if it doesn't exist yet.
2. The variable name is created.
3. It inserts the reference from the variable name to the object (this is the = symbol task).
"""

z = 1  # Variable name/reference name assigned/referenced to an object

print('z = 1, z is the reference name, pointing to the corresponding object.')

print('object which z is referring to has type:', type(z))  # type
print('object which z is referring to has value:', z)  # value
print('object which z is referring to has identity:', id(z))  # identity
