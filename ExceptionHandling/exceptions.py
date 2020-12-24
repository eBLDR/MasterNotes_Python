"""
There are 2 types of errors we can get:
    - Syntax Error, for example a typo or wrong placement of special characters
    - Exception Error, all the rest

The order of the exceptions matters. Except1 will be assessed before Except2
in case of error.
Exceptions are (as everything else in Python) objects, all inherit from class
called BaseException.
We can use this to trap all the exceptions that are raised by using:
"except BaseException:", which is equivalent to: "except:".
Is always better to be more specific.

Force the errors to find out the name of the exception.

Scripts finished with an exception being raised (either accidentally or not)
will exit with exit code 1 instead of the usual 0.
"""


def factorial(n):
    # n! can also be defined as n * (n-1)
    """ Calculates n! recursively """
    # a = 'op' + 9
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    # All the code will be executed, if an exception is raised, will skip the
    # rest and jump to `except` clause
    print(factorial(99))
    # Force maximum recursion depth by passing a great number as a parameter

# Specify the error's name
# If no exception is raised in `try`, this code block won't be executed
except RecursionError:
    print('This program cannot calculate factorials that large')

# try can have as many except clause as needed
except OverflowError:
    print('This computer cannot work with numbers that large')
    # note: Python is powerful when dealing with huge integers,
    # so Over Flowing is difficult to reproduce in some computers

# General exception to catch any error, storing Exception object as <name>
except Exception as e:
    print(type(e))  # type <exception>
    print(e.args)  # Attribute containing the message (tuple)


# It is also possible to combine both exceptions into one `except` clause
# except (RecursionError, OverflowError):

# After all `except` clauses but before `finally` - will be executed if no
# exceptions were raised and the program was not terminated inside the `try`
# clause
else:
    print('Everything worked fine')

# `finally` is executed regardless an exception was raised or not, even if it
# was raised by force (raise Exception) or user tries to crash using Ctrl+D
# (see eoferror.py). Useful for tidying tasks before closing
finally:
    print('The finally clause always executes')

print('Program terminating')
