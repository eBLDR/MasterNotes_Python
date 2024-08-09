"""
map() and filter() work usually together with lambda functions.

lambda was considered to be dropped from when migrating to
Python 3, but it finally remained.


All functions created with lambda operator can also be created using the
normal way of defining a function.
"""

# lambda operator is a way to create anonymous functions
# syntax is - lambda argument_lit: expression
add = lambda x, y: x + y

print(add(3, 4))

print('=' * 20)

# lambda with map()
C = [39.2, 36.5, 37.0, 38.1, 40.3]  # A list with degrees Celsius

# Creating a list with degrees Fahrenheit
F = list(map(lambda x: x * 9 / 5 + 32, C))
print(F)


# Equivalence creating a function and using list comprehension
def converter(n):
    return n * 9 / 5 + 32


F_comp = [converter(x) for x in C]
print(F_comp)

print('=' * 20)

# lambda with filter()
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_fib = list(filter(lambda x: x % 2, fibonacci))
# Remember that bool(int!=0) is True
print('bool(2) is {}'.format(bool(2)))  # only bool(0) is False
print(odd_fib)

# equivalence using list comprehension
odd_fib_comp = [x for x in fibonacci if x % 2 != 0]
print(odd_fib_comp)

print('=' * 20)

# lambda with reduce()
from functools import reduce

# Returns the largest value
f = lambda a, b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102, 13]))

# Returns the sum of all numbers
print(reduce(lambda x, y: x + y, range(1, 101)))

print('=' * 20)


class StringConversionMethod:
    """Class for defining string conversion methods."""

    def __init__(self, name, execute_func):
        self.name = name
        self.execute_func = execute_func

    def __str__(self):
        return self.name

    def apply(self, string_to_convert):
        converted_string = ''

        try:
            converted_string = self.execute_func(string_to_convert)
        except Exception as exc:
            print('Failed to apply conversion: ' + self.name)
            print(exc)

        return converted_string


my_rules = [
    StringConversionMethod(
        'Strip everything after 30 characters',
        (lambda x: x[:30])
    ),
    StringConversionMethod(
        'Add 10 whitespaces before last character',
        (lambda x: x[:-1] + ' ' * 10 + x[-1])
    )
]

my_string = 'This is a test string for conversion purposes. Feel free to ' \
            'update me if you wish to.'

print('Before conversion: ' + my_string)

for rule in my_rules:
    print('Applying rule: ' + rule.name + ' ...')
    my_string = rule.apply(my_string)

print('After conversion: ' + my_string)
