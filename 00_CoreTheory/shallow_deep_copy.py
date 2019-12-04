"""
Two kinds of copies:
- SHALLOW copy creates a new variable name with a new reference referring to the same object.
- DEEP copy creates a new variable name with a new reference referring to new object with equal value.

There are 2 kinds of objects:
- MUTABLE objects can change its value during the program execution, without loosing its identity.
- IMMUTABLE objects cannot change its value after they've been created. They do not accept in-place methods,
methods that modify the value keeping the identity.
"""
# Immutable objects
a = 1
b = a  # shallow copy
print('a = {}, b = {}'.format(a, b))
print('id(a) is {}, id(b) is {}'.format(id(a), id(b)))

# When trying to change the value of the object, a new object is created with the new value
b += 1
print('b = {}'.format(b))
print('id(b) is {}'.format(id(b)))  # new id

# When creating a new variable name with a value that already exists, only a new reference is created,
# not a new object
c = 1
print('a = {}, c = {}'.format(a, c))
print('a is c: {}'.format(a is c))

print('=' * 20)

# Mutable objects
l_1 = [0, 1, 2]
l_2 = l_1  # shallow copy
l_3 = l_1[:]  # deep copy
print('L1 = {}, L2 = {}, L3 = {}'.format(l_1, l_2, l_3))
print('id(L1) is {}, id(L2) is {}, id(L3) is {}'.format(id(l_1), id(l_2), id(l_3)))

# When trying to change the value of the object, the content is change without creating a new object
l_1[0] = -1
print('L1 = {}, L2 = {}'.format(l_1, l_2))
print('id(L1) is {}, id(L2) is {}'.format(id(l_1), id(l_2)))  # id remains the same

# is keyword for assessing if variable reference to same object
print('L1 is L2: {}'.format(l_1 is l_2))

# equivalent to
print('id(L1) == id(L2): {}'.format(id(l_1) == id(l_2)))

print('L1 is L3: {}'.format(l_1 is l_3))
print('id(L1) == id(L3) {}'.format(id(l_1) == id(l_3)))

print('=' * 20)

# Use of copy module
import copy

my_l = [1, 0]

# deepcopy() for a deep copy
deep_copy_of_my_l = copy.deepcopy(my_l)

print(my_l is deep_copy_of_my_l)
