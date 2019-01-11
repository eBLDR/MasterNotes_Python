class BaseClass:
    """ Simple account class with balance. """

    # @item are called DECORATORS
    # static methods don't have access to the attributes of an instance of a class nor to the attributes of the class
    @staticmethod
    def add_1(n):
        # Doesn't take self argument
        return n + 1

    status = 0

    # Class methods have access to the class attributes, not to the instance attributes.
    # The changes made by a class method will affect all the instances of the class and of the
    # instances of the subclasses, if any
    @classmethod
    def activate_status(cls):
        # Takes cls instead of self
        cls.status = 1

    def __init__(self, name):
        self.name = name
        self.counter = 0

    def do_something(self):
        self.counter = BaseClass.add_1(self.counter)


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

parent.activate_status()
print('Calling class method parent.activate_status()...')

print('parent.status:', parent.status)
print('child_1.status:', child_1.status)
print('child_2.status:', child_2.status)

print('=' * 30)

print('child_1.counter:', child_1.counter)

child_1.do_something()
print('Calling static method child_1.do_something()...')

print('child_1.counter:', child_1.counter)

print('Calling static method child_1.add_1(3):', child_1.add_1(3))
