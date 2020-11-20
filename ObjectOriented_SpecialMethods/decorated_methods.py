class Simple:
    def method(self):
        return 'Calling instance method:', self

    @classmethod
    def classmethod(cls):
        return 'Calling class method:', cls

    @staticmethod
    def staticmethod():
        return 'Calling static method'


s = Simple()
print(s.method())
print(s.classmethod())
print(s.staticmethod())

print('#' * 30)


class BaseClass:
    """ Simple account class with balance. """

    def __init__(self, name):
        self.name = name
        self.counter = 0

    # @item are called DECORATORS
    # static methods don't have access to the attributes of an instance of a
    # class nor to the attributes of the class
    @staticmethod
    def add_1(n):
        # Doesn't take self argument
        return n + 1

    # Class attribute
    status = 0

    # Class methods have access to the class attributes, not to the instance
    # attributes.
    # The changes made by a class method will affect all the instances of the
    # class and of the instances of the subclasses, if any
    @classmethod
    def upgrade_status(cls):
        # Takes cls instead of self
        cls.status += 1

    def do_something(self):
        self.counter = self.add_1(self.counter)
        # Equivalent to
        # self.counter = BaseClass.add_1(self.counter)


# See inheritance.py
class SubClass(BaseClass):

    def __init__(self, name):
        super().__init__(name)


parent = BaseClass('parent')
child_1 = SubClass('child_1')
child_2 = SubClass('child_2')

print('parent.status:', parent.status)
print('child_1.status:', child_1.status)
print('child_2.status:', child_2.status)

# Calling a @classmethod through an instance will affect all other instances
# of the class and subclasses
parent.upgrade_status()
print('Calling class method parent.upgrade_status()...')

print('parent.status:', parent.status)
print('child_1.status:', child_1.status)
print('child_2.status:', child_2.status)

# Calling a @classmethod through the class itself will produce the same result
BaseClass.upgrade_status()
print('Calling class method BaseClass.upgrade_status()...')

print('parent.status:', parent.status)
print('child_1.status:', child_1.status)
print('child_2.status:', child_2.status)

print('=' * 30)

print('child_1.counter:', child_1.counter)

child_1.do_something()
print('Calling static method child_1.do_something()...')

print('child_1.counter:', child_1.counter)

# Calling a @staticmethod through the instance
print('Calling static method child_1.add_1(3):', child_1.add_1(3))

# Calling a @staticmethod through the class
print('Calling static method BaseClass.add_1(4):', BaseClass.add_1(4))
