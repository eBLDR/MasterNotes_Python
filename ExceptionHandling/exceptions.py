"""
There are 2 types of errors we can get:
    - Syntax Error, for example a typo or wrong placement of special characters
    - Exception Error, all the rest

The order of the exceptions matters. Except1 will be assessed before Except2 in case of error.
Exceptions are (as everything else in Python) objects, all inherit from class called BaseExceptions.
We can use this to trap all the exceptions that are raised by using: "except BaseExceptions:", which is equivalent
to: "except:". Is always better to be more specific.

Force the errors to find out the name of the exception
"""


def factorial(n):
    # n! can also be defined as n * (n-1)
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    # all the code will be executed, if an exception is raised, will skip the rest and jump to 'except'
    print(factorial(99))
    # force maximum recursion depth by passing a parameter > 998

except RecursionError:  # we need to specify the error's name
    # if no exception is raised in 'try', this block won't be executed
    print('This program cannot calculate factorials that large')

# try can have as many except clause as needed
except OverflowError:
    print('This computer cannot work with numbers that large')
    # note: Python is extremely powerful when dealing with huge integers, so Over Flowing is almost impossible

# is also possible to combine both exceptions into one except clause
# except (RecursionError, OverflowError):

# after all except clauses but before finally
else:  # will be executed if no exceptions were raised and the program was not terminated inside the try clause
    print('Everything worked fine')

finally:  # finally is executed regardless an exception was raised or not, even if it was raised by force (raise Exception)
    # even if user tries to crash using Ctrl+D (see eoferror.py)!
    # very useful for tidying tasks before closing
    print('The finally clause always executes')

print('Program terminating')
