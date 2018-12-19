"""
map() and filter() work usually together with lambda functions.
reduce() was dropped from Python 2 when migrating to Python 3.
Is now found in the functools module.
Lambda, map() and filter() were also considered to be dropped,
but they finally remained.

The reason:
All functions created with lambda operator can also be created using the normal way of defining a function.
All lists returned by map() and filter() can be also created using list comprehension.
"""

# lambda operator is a way to create anonymous functions
# syntax is - lambda argument_lit: expression
add = lambda x, y: x + y

print(add(3, 4))

# map(@function, @sequence) - map() applies the @func to all the elements in the @seq
# @seq can be any iterable (list, tuple, range...) returns an iterator
C = [39.2, 36.5, 37.0, 38.1, 40.3]  # a list with degrees Celsius
F = list(map(lambda x: x * 9 / 5 + 32, C))  # creating a list with degrees Fahrenheit
print(F)


# equivalence creating a function and using list comprehension
def converter(n):
    return n * 9 / 5 + 32


F_comp = [converter(x) for x in C]
print(F_comp)

print('=' * 20)

# filter(@function, @sequence) - filters the elements of the @sequence, passing them to the
# @function and adding them to the list only if the bool(return_value) is True
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_fib = list(filter(lambda x: x % 2, fibonacci))
# remember that bool(int!=0) is True
print('bool(2) is {}'.format(bool(2)))  # only bool(0) is False
print(odd_fib)

# equivalence using list comprehension
odd_fib_comp = [x for x in fibonacci if x % 2 != 0]
print(odd_fib_comp)

print('=' * 20)

# reduce(@function, @sequence) - continually applies the function to the sequence,
# it returns a single value - i.e.: if list has 4 items: func(func(func(i1, i2), i3), i4)
from functools import reduce

# returns the largest value
f = lambda a, b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102, 13]))

# returns the sum of all numbers
print(reduce(lambda x, y: x + y, range(1, 101)))
