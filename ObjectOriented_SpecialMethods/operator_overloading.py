"""
Operator overloading allows the same operator to
behave differently according to the context.
It can be overwritten.

OPERATOR            EXPRESSION	    INTERNALLY

Addition	        p1 + p2	        p1.__add__(p2)
Subtraction	        p1 - p2	        p1.__sub__(p2)
Multiplication	    p1 * p2	        p1.__mul__(p2)
Power	            p1 ** p2	    p1.__pow__(p2)
Division	        p1 / p2	        p1.__truediv__(p2)
Floor Division	    p1 // p2	    p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	        p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	    p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	    p1.__rshift__(p2)
Bitwise AND	        p1 & p2	        p1.__and__(p2)
Bitwise OR	        p1 | p2	        p1.__or__(p2)
Bitwise XOR	        p1 ^ p2	        p1.__xor__(p2)
Bitwise NOT	        ~p1	            p1.__invert__()
Less than	        p1 < p2	        p1.__lt__(p2)
Less than or
    equal to        p1 <= p2	    p1.__le__(p2)
Equal to            p1 == p2	    p1.__eq__(p2)
Not equal to	    p1 != p2	    p1.__ne__(p2)
Greater than	    p1 > p2	        p1.__gt__(p2)
Greater than or
    equal to	    p1 >= p2	    p1.__ge__(p2)

"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x},{y})'.format(x=self.x, y=self.y)

    # Overriding the method being called with the "+" operator
    def __add__(self, other):
        # self refers to the object on the left of the +, and other to the
        # one on the right
        x = self.x + other.x
        y = self.y + other.y

        # Returns a new instance of itself
        return Point(x, y)

    # Overriding the method being called with the "-" operator
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)


p1 = Point(2, 3)
p2 = Point(-1, 5)

print(p1 + p2)
print(p1 - p2)

"""
Overloading methods are used in other languages (such as Java or C++) to use
different versions of the method depending on the number and type of arguments
that are passed to it.
Python doesn't have such a thing, the arguments are assigned by order, by
named parameters, or set to default if not specified. (See functions.)
"""
