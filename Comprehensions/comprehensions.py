# Comprehension are faster and more concise.
# All the following code can be applied to both lists and sets
# Comprehension structure:
# expression - iterator (any iterable type) - 0 or more filter/s

numbers = [1, 2, 3, 4, 5, 6, 6]

# Control variables in a for loop overwrite any existing variable with the same name
number = 0
print('Number is {}'.format(number))
squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

# Control variables in a list comprehension won't
print('Number is {}'.format(number))
number = 0
print('Number is {}'.format(number))

# Using comprehension
squares_comp = [number ** 2 for number in range(1, 7)]
print(squares_comp)

print('Number is {}'.format(number))

print('=' * 30)

# set comprehension - useful if we don't want duplicates
squares_set_comp = {number ** 2 for number in numbers}
print(squares_set_comp)

print('=' * 30)

# dictionary comprehensions are also possible
dict_comp = {n: n ** 3 for n in range(1, 11)}
print(dict_comp)

print('=' * 30)

# Conditional comprehensions
# When using filters, the value will be added to the list if the condition of the filter returns True
odd_numbers = [i for i in range(1, 20) if i % 2 != 0]  # cannot have and else clause
print(odd_numbers)

# Adding complexity - each filter starts with if and can have multiple and/or
even_numbers_no_squares = [i for i in range(1, 30) if i % 2 == 0 or i == 5 if i not in squares]
print(even_numbers_no_squares)

print('=' * 30)

# Using conditional expressions with comprehensions
fizzbuzz = ['fibbuz' if n % 3 == 0 and n % 5 == 0 else 'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else str(n) for n in range(21)]

print(fizzbuzz)

print('=' * 30)

# Creating a list of tuples
dots = [(i, i ** 2) for i in even_numbers_no_squares]
print(dots)

print('=' * 30)

# Nested comprehensions - or comprehension with multiple iterators
doubled = ['i={} j={}'.format(i, j) for i in range(3) for j in range(5)]
print(doubled)

doubled_2 = [['i={} j={}'.format(i, j) for i in range(3)] for j in range(5)]
print(doubled_2)

print('=' * 30)

# Combinations
combs = []
for x in [1, 2, 3]:
    for y in [1, 3, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

# Equivalent to - notice how the for/for/if are in the same order as above
combs_comp = [(x, y) for x in [1, 2, 3] for y in [1, 3, 4] if x != y]
print(combs_comp)

print('=' * 30)

# Creating a matrix
row = range(3)
column = range(5)
matrix = [[0 for c in column] for r in row]
print(matrix)
