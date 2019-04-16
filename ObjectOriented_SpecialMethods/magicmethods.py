"""
Magic methods are class methods of the kind __method__.
They are also called 'dunder methods'.

Are methods that are not invoked directly. The invoking is realized behind
the scenes.
"""


class Alpha:

    # __init__ is a magic method, it's invoked at the moment of the instantiation
    def __init__(self, x):
        self.x = x


# At the moment of creating the object, the magic method __new__(cls) of Alpha is called,
# __new__ takes the class and the arguments that pass along to __init__.
# Then, __init__ is called, it is the primary constructor.
my_alpha = Alpha(1)


# Objects can also have the __del__ magic method, which can handle the garbage collection
# at the moment of deleting the object.

# The __call__ method turns the instances into callable
class Poly:

    def __init__(self, *factors):
        self.factors = factors[::-1]

    # Overriding the method
    def __call__(self, f):
        r = 0
        for n, factor in enumerate(self.factors):
            r += factor * f ** n

        return r


p1 = Poly(12)
p2 = Poly(1, 0.5, -2.25)

for i in range(5):
    # Invoking __call__ as if the instances were functions
    print(i, p1(i), p2(i))

print('=' * 20)

# Each built-in class has it's own set of magic methods.
# For example all int and float have __add__, __sub__, __mul__, etc.
# This methods are linked to certain characters (operators)
x = 1
y = 3

# The operator '+' ...
print('x + y: ', x + y)

# ... is calling
print('x.__add__(y): ', x.__add__(y))
