"""
A metaclass (sometime referred to as 'class factories') is a class whose
instances are classes.
type is the metaclass where int, float, list, etc. inherit from.
Classes are objects too.
"""

# Defining a class dynamically using type(@name, @bases, @dct)
# @name is class' name, __name__
# @base tuple of the base classes which the class inherits, __bases__
# @dct is the namespace dict containint attributes, __dict__

# Simplest example, empty class - equivalen to class Foo: pass
Foo = type('Foo', (), {})
print(Foo.__name__, Foo.__bases__, Foo.__dict__)

print()

# Adding inheritance and data attributes
Bar = type('Bar', (Foo,), dict(attr=100))
print(Bar.__name__, Bar.__bases__, Bar.__dict__)

print()

# Adding inheritance, data attributes and methods
Bar = type(
    'Bar',
    (Foo,),
    {'attr': 100,
     'attr_val': lambda x: x.attr})

print(Bar.__name__, Bar.__bases__, Bar.__dict__)

print()


# Methods can also be assigned using a defined function
def f(obj):
    print('attr =', obj.attr)


Bar = type(
    'Bar',
    (Foo,),
    {'attr': 100,
     'attr_val': f})

print(Bar.__name__, Bar.__bases__, Bar.__dict__)

print()

# Customising metaclasses
z = Bar()
z.attr_val()
# The object creation line calls __call__() method, which invokes __new__()
# and __init__()
# If those methods are not specified, will be inherited from object's ancestry.
# Overriding them allows for customized behaviour when instantiating classes.

print()


def new(cls):
    x = object.__new__(cls)
    x.attr = 101
    return x


Bar.__new__ = new  # Overriding __new__ method
y = Bar()
print(y.attr)

# type.__new__ = new will raise an Error, python does not allow modification
# of type metaclass

print()


# Creating own's metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 101
        return x


# Equivalent to
class Meta2(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 101


# Inheritance using metaclass keyword argument - Python 3 syntax
# By default, metaclass = type
class Bar(metaclass=Meta):
    pass


print(Bar.attr)
