"""
EVERYTHING in Python is an object.

Python is a DYNAMICALLY TYPED language, this means that Python doesn't really
care about the types of the variables, it cares only for its behaviour.

- Static typing (languages like C, C++...) means that the type checking is performed during compile time.
- Dynamic typing (Python) means that the checking is performed at run time.
"""
# OBJECT INHERITANCE

x = object()  # object() is the super class where objects inherit from in Python
print(x, 'x is type:', type(x))

y = x.__str__()  # Every object has this method for printing representation

# Equivalent to
print(x)  # calling the __str__ method

print(y, type(y))

print('=' * 20)

z = 1
# Operator + and method __add__ refer to the same built-in code, they are equivalents
print(z + 2)
print(z.__add__(2))  # a, even declared as int, it's an object, and it has methods

print('=' * 20)


# CLASS INHERITANCE
class MyClass:
    pass


c = MyClass()
print('c is type:', type(c))

print('=' * 20)

# Type METACLASS
# Object is a class that inherits from its metaclass: type
print('type of object is:', type(object))

print('MyClass is type:', type(MyClass))

print('int/float/list... are type:', type(int))  # Absolutely all types of variables

print('type is type:', type(type))  # Circular reference, type instantiates itself

# SUMMARY: all objects inherit from object() class, and all classes (including object()) inherit
# from type() metaclass
