# List is also called array.
# A list can contain items of different types, though is recommended to
# keep the list homogeneous (all items are of the same type)

# Create empty list
list_1 = []
list_2 = list()  # Constructor, creates new list
print(list('Constructing a list'))

list_1 += [1, 2]  # Adding items to the end of the list
print(list_1)

even = []
odd = []

for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)  # Appends an object to the end of the list
    else:
        odd.append(i)

print(even[3])  # To call specific index
print(even[-1])  # To call the last item, negative indexes also work

# Lists can be concatenated
numbers = even + odd + [100]
# And multiplied
numbers2 = numbers * 2
print(numbers2)

del numbers[1]  # Deletes specific index from list
print(numbers)

# Copying lists
# Shallow copy, refers to the same ID - pointing to the same memory location
another_even_1 = even  # This is called "aliasing"
print('even is {}'.format(even))
print('another_even_1 is {}'.format(another_even_1))
print(id(another_even_1))
print(id(even))

# Changing one of the list will cause both to change - applies also to nested
# lists
another_even_1.append(0)
print('even is {}'.format(even))
print('another_even_1 is {}'.format(another_even_1))

# Deep copy - pointing to a new memory location
another_even_2 = list(even)
another_even_3 = even.copy()  # Also deep copy
another_even_2.append(10)
print('Even is now {0} and another_even_2 is {1}'.format(even, another_even_2))
print(id(another_even_2))
print(id(even))
print(id(another_even_3))

print(another_even_1 is even)  # Check the identity, returns True or False
