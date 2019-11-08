"""
Numbers and strings alone are referred to as Literal Constants.
They use the value literally, and its value cannot be changed (constant).
In opposite to literal constants, we have variables, which can store anything.

A variable is a part of the computer's memory where some information is stored.
A method to access them is necessary, hence we assign them to names.

Every object has 3 characteristics:
    - DATA TYPE - class where object inherits attributes from.
    - VALUE - object with its content/s.
    - IDENTITY - memory location, id().

When creating an object, 3 things are happening:
    1. The object is created (with its content/s, if required) if it doesn't
    exist yet.
    2. The variable name (identifier) is created.
    3. It inserts the reference from the identifier to the object
    (this is the = symbol task).
"""
# Identifier assigned/referenced to an object - this is called "binding"
z = 1  # 1 is a literal constant

print('z = 1, z is the identifier (reference name),'
      'pointing to the corresponding object.')

# Variable type
print('Object to which z is referring to has type:', type(z))

# Variable value
print('Object to which z is referring to has value:', z)

# Variable identity
print('Object to which z is referring to has identity:', id(z))
