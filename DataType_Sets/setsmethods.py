numbers = {1, 5, 12, 201}
print(numbers)

# adding and removing
numbers.add(24)  # adding an item
print(numbers)

numbers.discard(9)  # discards an existing item, if exists
print(numbers)

numbers.discard(8)  # no error, does nothing

numbers.remove(5)   # removes an existing item, must exist
print(numbers)
# numbers.remove(7)  # will give an error, useful when Try Except

n = numbers.pop()  # remove and return an arbitrary element from the set
print(numbers, n)

# a.update(b) - adds all elements from b to a
numbers2 = {7, 9, 11}
numbers.update(numbers2)
print(numbers)

# copy() - makes a copy of the set
numbers3 = numbers.copy()
print(numbers3)

# set.clear() - remove all elements from the set
numbers.clear()
print(numbers)
