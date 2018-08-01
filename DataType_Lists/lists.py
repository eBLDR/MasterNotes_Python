# a list can contain items of different types, though is recommended to
# keep the list homogeneous (all items are of the same type)

# create empty list
list_1 = []
list_2 = list()  # constructor, creates new list
print(list("Constructing a list"))

even = []
odd = []

for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)  # appends an object to the end of the list
    else:
        odd.append(i)

print(even[3])   # to call specific index
print(even[-1])  # to call the last item, negative indexes also work

# lists can be concatenated
numbers = even + odd + [100]
# and multiplied
numbers2 = numbers * 2
print(numbers2)

del numbers[1]  # deletes specific index from list
print(numbers)

# lists can be nested
nested_list = [[0, 1], [10, 11], [100, 111]]
print(nested_list)
print(nested_list[0], nested_list[1][1])  # use multiple index to refer a specific item

# copy lists
another_even_1 = even  # dependent, refers to the same ID - pointing to the same memory location
print('even is {}'.format(even))
print('another_even_1 is {}'.format(another_even_1))
print(id(another_even_1))
print(id(even))

another_even_1.append(0)  # changing one of the list will cause both to change - applies also to nested lists
print('even is {}'.format(even))
print('another_even_1 is {}'.format(another_even_1))

another_even_2 = list(even)   # independent copy - pointing to a new memory location
another_even_3 = even.copy()  # also independent copy
another_even_2.append(10)
print("Even is now {0} and another_even_2 is {1}".format(even, another_even_2))
print(id(another_even_2))
print(id(even))
print(id(another_even_3))

print(another_even_1 is even)  # check the identity, returns True or False
