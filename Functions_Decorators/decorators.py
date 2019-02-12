"""
Decorators wrap a function, modifying its behaviour.
Decorators take a function as an argument, and return also
a function, the wrapping one.
"""


# Half decorator, can only add extra behaviour before decorated function is called
def half_decorator(f):
    print('I am half_decorator.')
    return f  # Must return a callable


# Pie syntax
# @half_decorator is equivalent of saying:
# decorated = @half_decorator(decorated)
@half_decorator
def decorated():
    print('I am decorated.')


decorated()

print('=' * 30)


# Full decorator, can add behaviour both before and after decorated function is called
def my_decorator(some_function):
    def wrapper():
        print('Before some_function() is executed.')

        some_function()

        print('After some_function() is executed.')

    return wrapper


def just_some_function():
    print('I am just_some_function!')


just_some_function = my_decorator(just_some_function)

# Call
just_some_function()

print(type(just_some_function))
print(type(my_decorator))

print(just_some_function)
print(my_decorator)

print('=' * 30)


@my_decorator
def just_some_function_2():
    """Docstring test."""
    print('I am just_some_function_2!')


just_some_function_2()

# Information is lost
print('just_some_function_2.__name__ is:', just_some_function_2.__name__)
print(just_some_function_2.__doc__)

print('=' * 30)

# To keep the information, use wraps from functools
from functools import wraps


def my_decorator_2(some_function):
    # wraps call as a decorator
    @wraps(some_function)
    def wrapper(*args, **kwargs):  # It is a good practise to always pass arguments, should they exist
        print('Before some_function() is executed.')

        some_function(*args, **kwargs)
        print(*args)

        print('After some_function() is executed.')

    return wrapper


@my_decorator_2
def just_some_function_3(*args):
    """Docstring test."""
    print('I am just_some_function_3 with args: ', *args)


print(just_some_function_3.__name__)
print(just_some_function_3.__doc__)
# Passing arguments
just_some_function_3('1', '2')

print('=' * 30)


def tool(*numbers):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('Arguments passed to @decorator:', *numbers)

            f(*args, **kwargs)

        return wrapper

    return decorator


@tool('First', 'Second', 'Last')
def motivate(*names):
    print('Arguments passed to decorated function:', *names)
    for n in names:
        print('Go', n)


motivate('Me', 'You', 'All')
