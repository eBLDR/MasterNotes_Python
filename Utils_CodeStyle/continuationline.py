"""
Based on PEP8, code lines should be 79 characters length max
Docstring or comments should be 72 characters length max
"""

a = 6
b = 1

# Continuation line on implicit line join
if (a == 5 or
        b == 1 or
        a != b):
    print('True')

# Explicit line join when implicit continuation cannot be used
if a == 5 or \
        b == 1 or \
        a != b:
    print('True')

# Aligned with opening delimiter
foo = '{hour}:{minute}:{second}.{ms}'.format(hour='08', minute='12',
                                             second='24', ms='001')


# Used by adding an extra level of indentation after the '('
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    return locals()


# Hanging indents add a level of indentation
bar = long_function_name(
    a, b,
    b, a
)

# Multi-line constructs
mu_list = [
    1, 2, 3,
    6, 9, 12
]

# Line break with operators, operator should be at the start of line
income = (1000
          + 121
          + 10 - 2
          - 78)
