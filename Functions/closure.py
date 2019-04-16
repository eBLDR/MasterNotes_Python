# Defining a closure function
def parent(num):
    def first_child():
        return 'Printing from the first_child() function.'

    def second_child():
        return 'Printing from the second_child() function.'

    # Returning functions
    if num == 10:
        return first_child
    else:
        return second_child


# Returned function is bound to variable
foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar())

print('=' * 30)


# Function generator
def make_multiplier_of(n):
    def multiplier(x):
        # Value for n is taken from enclosing scope
        return x * n

    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

print(times3(9))
print(times5(3))
print(times5(times3(2)))

# Accessing the cell objects of the closure function
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)
