# using a generator to generate a Fibonacci sequence


def gen_fibonacci():
    # starting numbers
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = gen_fibonacci()
print(type(fib))

# number of values of Fibonacci sequence to be shown
numbers = 21

for i in range(numbers):
    print(next(fib))
