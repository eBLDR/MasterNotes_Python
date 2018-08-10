"""
A generator works like an iterator. The difference is that the value is only calculated when requested.
Yield returns a 'sleeping' value, the function that returns a yielded value
is actually being called only when iterating, and the function 'remembers' which was the last value sent.
The values inside the generator are 'consumed' when used. There is no need to consume the range fully.
A range, contrary, isn't consumed when used.
Essentially, the list is not created upfront, only one item is created when requested.
"""
import sys


def my_range(n: int):  # Creating a generator
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


print(my_range)
print(type(my_range))  # Type function

# big_range = range(5)  # 48 bytes
big_range = my_range(5)  # 88 bytes
print(type(big_range))  # Type generator

print(next(big_range))  # Calling the next value (in this case the first) of the generator

# sys.getsizeof(object) shows the size in bytes of the object
print("big_range is {} bytes".format(sys.getsizeof(big_range)))
print(big_range)

big_list = []

_ = input("line 36 - press <enter>")  # Using _ as a unnecessary variable name (placeholder)
for val in big_range:  # what 'for' is actually doing is calling next()
    _ = input("line 38 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print("looping again... or not")  # once the iterator is used, it's empty
for i in big_range:
    print("i is {}".format(i))
    print("big_range is already used")

print("Starting a new range")
for i in my_range(5):  # creating another generator
    print("i is {}".format(i))

print('=' * 20)

# yield from iterator


def my_gen(n):
    # for i in range(n):
    #     yield i
    
    # Equivalent to
    r = range(n)
    yield from r


generator = my_gen(5)
for i in generator:
    print(i)
