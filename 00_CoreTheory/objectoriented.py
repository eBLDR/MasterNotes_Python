"""
EVERYTHING in Python is an object.

Python is a DYNAMICALLY TYPED language, this means that Python doesn't really
care about the types of the variables, it cares only for its behaviour.

- Static typing (languages like C, C++...) means that the type checking is performed during compile time.
- Dynamic typing (Python) means that the checking is performed at run time.

Every object has 3 characteristics:
- TYPE (class where object inherits attributes from).
- VALUE (content/s).
- IDENTITY (memory location, id()).

When creating an object, 3 things are happening:
1. The object is created (with its content/s, if required) if it doesn't exist yet.
2. The variable name is created.
3. It inserts the reference from the variable name to the object (this is the = symbol task).
"""

z = 1  # variable name/reference name assigned/referenced to an object
print("z = 1, z is the reference name, pointing to the corresponding object")
print("object which z is referring to has type:", type(z))    # type
print("object which z is referring to has value:", z)         # value
print("object which z is referring to has identity:", id(z))  # identity

print("=" * 20)

# OBJECT INHERITANCE

x = object()  # object() is the super class where objects inherit from in Python
print(x, "x is type:", type(x))

y = x.__str__()  # Every object has this method for printing representation

# equivalent to
print(x)  # calling the __str__ method

print(y, type(y))

print("=" * 20)

# operator + and method __add__ refer to the same builtin code, they are equivalents
print(z + b)
print(z.__add__(2))  # a, even declared as int, it's an object, and it has methods

print("=" * 20)


# CLASS INHERITANCE

class MyClass:
    pass


c = MyClass()
print("c is type:", type(c))

print("=" * 20)

# type METACLASS
# object is a class that inherits from its metaclass: type
print("type of object is", type(object))

print("MyClass is type:", type(MyClass))

print("int/float/list... are type:", type(int))  # absolutely all types of variables

print("type is type", type(type))  # circular reference, type instantiates itself

# SUMMARY: all objects inherit from object() class, and all classes (including object()) inherit
# from type() metaclass

# Creating an object is much faster using literal syntax
a = set([1, 2, 3])
a = {1, 2, 3}  # literal syntax
