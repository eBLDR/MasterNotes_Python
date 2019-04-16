"""
A descriptor is an object attribute with “binding behavior”,
one whose attribute access has been overridden by methods
in the descriptor protocol.
Those methods are __get__(), __set__(), and __delete__().
If any of those methods are defined for an object,
it is said to be a descriptor.

There are three ways to access an attribute:

To lookup its value, some_variable = obj.a - bound to __get__()
To change its value, obj.a = 'new value' - bound to __set__()
To delete it, del obj.a - bound to __delete__()
"""


# New protocol from Python v3.6+
# No need for __init__ & implementation of __set_name__()
class NonNegative:
    # Overriding __get__ descriptor
    def __get__(self, instance, owner):
        print('In NonNegative.__get__()')
        print('instance:', instance, ', owner :', owner)
        print('instance.__dict__:', instance.__dict__)
        return instance.__dict__[self.name]

    # Overriding __set__ descriptor
    def __set__(self, instance, value):
        print('In NonNegative.__set__()')
        print('instance:', instance, ', value :', value)
        print('self.name:', self.name)

        # value refers to the new value to be set
        if value < 0:
            raise ValueError('Cannot be negative.')

        # Update the instances' attr dictionary
        instance.__dict__[self.name] = value

    # Called at the time the owning class owner is created, the descriptor has been assigned to name
    def __set_name__(self, owner, name):
        print('In NonNegative.__set_name__()')
        print('owner:', owner, ', name :', name)
        self.name = name


class Order:
    # Binding the descriptors - the variable name will be set as descriptor's self.name
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    """
    # Use property to define the valid values of the attribute
    # If we want the same behaviour for several attributes, we have to
    # set one property for each attr leading to duplicated code.
    # In this case using a descriptor is much more efficient.
    @property
    def quantity(self):
        return self._quantity   

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        self._quantity = value
    """


apple_order = Order('apple', 1, 10)
apple_order.total()

# This will called the __get__() descriptor
print(apple_order.quantity)

# This will called the __set__() descriptor
apple_order.price = -10
apple_order.quantity = -10
