# We can pass snippets to timeit by converting them into str or as a reference to a callable
import timeit


def odds_func():
    odds = []
    for i in range(100):
        if i % 2 != 0:
            odds.append(i)


odds_str = """\
odds = []
for i in range(100):
    if i % 2 != 0:
        odds.append(i)
"""

# When passing functions to timeit this way, functions can't take arguments
result_func = timeit.timeit(odds_func, number=1000)
result_str = timeit.timeit(odds_str, number=1000)

# there isn't performance difference
print('In function:\t{} sec'.format(result_func))
print('In string:\t\t{} sec'.format(result_str))


# using arguments in functions
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print('#' * 30)

# import the desired function in the setup parameter and use the called in the snippet
if __name__ == '__main__':
    print(timeit.timeit('x = factorial(100)', setup='from __main__ import factorial', number=1000))
