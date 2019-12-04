# kwargs, key word arguments
# kwargs is a dictionary with all the key word parameters (if any) with
# its default values


def dad(n, name='', mode='', cool=True):
    print('This is dad().')
    print('n is: {}; name is: {}; mode is: {}'.format(n, name, mode))
    if cool:
        print('Dad is cool.')


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
    # Since it's a dictionary we are free to manipulate it
    kwargs.pop('end', None)
    for word in args[::-1]:
        # print(word[::-1], end=' ', file=file) turns into:
        # When using kwargs there is no need to unpack them
        print(word[::-1], end=' ', **kwargs)


with open('backwards.txt', 'w') as backwards:
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to',
                    'your', 'leader', end=' ', file=backwards)
