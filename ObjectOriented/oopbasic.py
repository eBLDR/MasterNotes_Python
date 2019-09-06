"""
Object Oriented Programming (OOP)

CLASS: template for creating objects of that specific type that will share the same characteristics.
OBJECT: an INSTANCE of a class.
INSTANTIATE: creating an instance of a class.
DATA ATTRIBUTE: a variable bound to an instance of a class.
METHOD: a function defined in a class that modifies the data attributes (it has the self parameter).
"""


# Example for class
class Kettle:  # By convention, start with capital letter and use camel case
    """ Class docstring. """
    # Kettle inherits form class 'object', a built-in class in Python 3 (new style class), there is no need to specify
    # i.e.: class Kettle:
    # in Python 2, class Kettle: will refer to the old style class, and class Kettle(object): to the new style

    # Class attributes (or static variable) that all the instances will share
    power_source = 'electric'

    # Constructor method
    def __init__(self, make, price):
        # Creating the data attributes (a variable bound to a class)
        # the self is a reference to the instance itself, called "attribute reference"
        self.make = make
        self.price = price
        self.on = False

        # Calling own functions: self.function_name()
        # self.switch_on()  # Will call a function when initialising

    # Defining a method
    def switch_on(self):
        """ Method docstring: switch on kettle. """
        self.on = True

    def __str__(self):
        # Specify what's the output when calling print(class_name)
        return 'I\'m an instance from class {}!'.format(Kettle.__name__)

    # def __doc__(self):
    # Will override the docstring specified on the class, if desired.

    def to_dict(self):
        # Returns a dictionary of the attributes and stored values (not
        # including method), so it's not necessary to access a protected
        # method from outside
        return self.__dict__


# Creating an instance of Kettle class
kenwood = Kettle('Kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75  # Reassigning the variable
print(kenwood.price)

# Creating another instance of Kettle
hamilton = Kettle('Hamilton', 14.55)

print('Models: {} = {}, {} = {}'.format(
    kenwood.make, kenwood.price, hamilton.make, hamilton.price)
)

# Replacement fields accept data attributes, pass the instance as a parameter
print('Models: {0.make} = {0.price}, {1.make} = {1.price}'.format(
    kenwood, hamilton)
)

print('hamilton is on: {}'.format(hamilton.on))

# Calling a method
hamilton.switch_on()
print('hamilton is on: {}'.format(hamilton.on))
print('kenwood is on: {}'.format(kenwood.on))

# We can also call the method of the class and pass an instance as parameter
Kettle.switch_on(kenwood)
print('kenwood is on: {}'.format(kenwood.on))

# Is also possible to create instance attributes dynamically (new attributes
# to one specific instance)
kenwood.power = 1.5

print('=' * 30)

# change the class attribute, all the instances are affected
Kettle.power_source = 'atomic'
print('Static variable "power_source"', Kettle.power_source)

# It tracks down to the class to replace the data attribute, it's not an
# attribute of the instance
print('hamilton power source: {}'.format(hamilton.power_source))

# by declaring this, new data attribute is created for this specific instance
kenwood.power_source = 'gas'
print('kenwood power source: {}'.format(kenwood.power_source))

print('=' * 30)

# Instance's base class
print('kenwood.__class__ is ', kenwood.__class__)

# Class' name
print('Kettle.__name__ is', Kettle.__name__)

print('=' * 30)

# Checking the namespaces
print('Kettle.__dict__ is\n\t', Kettle.__dict__)
print('kenwood.__dict__ is\n\t', kenwood.__dict__)
print('hamilton.to_dict() is\n\t', hamilton.to_dict())

print('=' * 30)

# Object's representation
print('Kettle.__str__ is\n\t', Kettle.__str__)
print(kenwood)

print('=' * 30)

print('Kettle.__bases__ is', Kettle.__bases__)

print('=' * 30)

# Displaying docstrings
# to print only the docstring of the class
print(Kettle.__doc__)

# to print only the docstring of a method of the class
print(Kettle.switch_on.__doc__)
