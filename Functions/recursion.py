"""
A recursion function is the one that calls itself.
"""


def fact(n):
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n*(n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
        # call factorial(n-1), then call factorial(n-2),...,then call factorial(n-(n+1)),
        # then return from the last


def fib(n):
    # Fibonacci series
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)  # non efficient way, we recalculate n-2 on each recursion


for i in range(13):
    print('{:2}! is {} = {}'.format(i, fact(i), factorial(i)))

for i in range(11):
    print('{:2} {}'.format(i, fib(i)))
