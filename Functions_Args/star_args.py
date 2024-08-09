"""
Both *args and **kwargs must be the only or the last of the parameters of
their type. Example:
def blabla(word, *args, keyW=None, keyX=False, **kwargs):
In this case, *args and **kwargs will absorb all the remaining positional
arguments/key word arguments respectively.
"""
# print has a *args (see builtins.py)
print('Hello', 'planet', 'Earth')


# *args can get any number of positional arguments, from 0 to n
# args can be replaced by any valid name (i.e. *sgra), conventionally use args
# the function expects an unpacked tuple in place of args
def average(*args):
    # *tuple is an unpacked tuple
    print(type(args))
    print('args is {}: '.format(args))
    print('*args is: ', *args)
    mean = 0

    # To use the arguments, we iterate over args (unpacking)
    for arg in args:
        mean += arg

    return mean / len(args)


print(average(1, 2, 3, 4))

# Unpacking can also be used when calling functions
numbers = [1, 2, 3, 4]
print(average(*numbers))

print('=' * 30)


def happy_text(*texts, sep=' :) '):
    text = ''
    for arg in texts:
        text += str(arg) + sep
    return text


print(happy_text('I', 'am', 'damn', 'happy', sep=' :( '))
print(happy_text('Assigning', 'returned', 'values'))

print('=' * 30)


# *args can take any number of arguments, passed to the function in a tuple
def centre_text(*texts, sep_char=' ', end_char='\n', file=None):
    text = ''
    for arg in texts:
        text += str(arg) + sep_char
    left_margin = (50 - len(text)) // 2
    print(' ' * left_margin, text, end=end_char, file=file)


# Saving to a file
with open('centred.txt', mode='w') as centredFile:
    centre_text('Twelve', file=centredFile)
    centre_text('in binary is', file=centredFile)
    centre_text(1100, file=centredFile)
    centre_text('or 0000 1100 in 1 byte', file=centredFile)
    centre_text('or C in hex', file=centredFile)
    centre_text('it can', 'also take', 'several number of', 'arguments', sep_char='-sep-', file=centredFile)

# From Python 3.8+, positional-only and keyword-only argument notation is implemented
# Failing to call the function in the correct way when specified will raise
# a TypeError
# Use of "/" denote that all arguments before it must be specified by position
def increment(x, /):
    return x + 1


print(increment(5))
# print(increment(x=5))  # TypeError


# Use of "*" denote that all arguments after it must be specified by keyword
def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5


print(to_fahrenheit(celsius=40))
print(to_fahrenheit(40))  # TypeError


# A combination of both is possible
# In this example, @border can be specified both w/ or w/o keyword
def headline(text, /, border="♦", *, width=50):
    return f' {text} '.center(width, border)
