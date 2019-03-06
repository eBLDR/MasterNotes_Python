"""
Both *args and **kwargs must be the only or the last of the parameters of their type. Example:
def blabla(word, *args, keyW=None, keyX=False, **kwargs):
In this case, *args and **kwargs will absorb all the remaining positional arguments/key word
arguments respectively.
"""
# print has a *args (see builtins.py)
print('Hello', 'planet', 'Earth')


# *args can get any number of positional arguments
# args could be replaced by any valid name (i.e. *sgra), but by convention args is used
# the function assumes that args is going to be an unpacked tuple
def average(*args):
    # *tuple is an UNPACKED tuple
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


# kwargs, key word arguments
# kwargs is a dictionary with all the key word parameters (if any) with its default values
def dad(n, name='', mode=''):
    print('This is dad().')
    print('n is: {}; name is: {}; mode is: {}'.format(n, name, mode))


def child(n, **mykwargs):
    print('child(), calling dad()...')
    # **dict is an UNPACKED dictionary
    print(type(mykwargs))  # Dictionary type
    print('mykwargs are: {}'.format(mykwargs))
    mykwargs['mode'] = 'OP'  # Kwargs can be updated like a normal dictionary
    print('mykwargs are: {}'.format(mykwargs))
    dad(n, **mykwargs)


# Named argument passed in call must exist in the top level function
print('Calling child()...')
child(5, name='myName')

# Unpacking can also be used when calling functions
values = {'name': 'myName', 'cool': False}
print(child(2, **values))

print('=' * 30)


# def print_backwards(*args, file=None): turns into:
def print_backwards(*args, **kwargs):
    print('kwargs is {}: '.format(kwargs))

    # The next line is to avoid a potential kwarg duplicate
    kwargs.pop('end', None)  # Since it's a dictionary we are free to manipulate it
    for word in args[::-1]:
        # print(word[::-1], end=' ', file=file) turns into:
        # When using kwargs there is no need to unpack them
        print(word[::-1], end=' ', **kwargs)


with open('backwards.txt', 'w') as backwards:
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end=' ', file=backwards)
