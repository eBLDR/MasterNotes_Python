from time import time
from functools import wraps


def timing_function(some_function):
    """
    Outputs the time a function takes to execute.
    :param some_function: function to be timed.
    :return: wrapper function.
    """

    @wraps(some_function)
    def wrapper(*args, **kwargs):
        t0 = time()
        some_function(*args, **kwargs)
        t = time() - t0
        return '\nTime it took to run the function (sec): ' + str(t)

    return wrapper


@timing_function
def my_function(n):
    """
    Sample function to be timed.
    """
    num_list = []
    for num in range(1, n):
        num_list.append(num)

    print('\nSum of all the numbers from 1 to {} = {}'.format(n, sum(num_list)))


print(my_function(10000))
print(my_function(100000))
