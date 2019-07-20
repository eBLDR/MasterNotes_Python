"""
A dictionary (also refer to as "mapper" or "mapping"
object consist of a key-value pairs - it's a "hash table".
Keys are immutable (keys must be "hashable"), whereas values are mutable.
The items inside a dictionary are ordered (from python version +3.6, before
were unordered).
If the dictionary must be ordered while using older versions, use:
from collections import OrderedDict
ordered_dict = OrderedDict()
"""

my_dict = {'alpha': 1,
           'beta': 2,
           'gamma': 3,
           'epsilon': 5}

print(my_dict['beta'])

# Add an entry
my_dict['delta'] = 'unknown'
print('delta is {}'.format(my_dict['delta']))
my_dict['delta'] = 4
print('delta is now {}'.format(my_dict['delta']))

# A dictionary can also be created using dict() method
d = dict(one=1, two=2, three=3)
print(d)

d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d2)

d3 = dict([('two', 2), ('one', 1), ('three', 3)])
print(d3)

print(d == d2 == d3)  # True

print('=' * 20)

# To delete a key-value pair
del my_dict['gamma']

# del myDict  # to delete the full dictionary

# key-value pairs are created in different order every time, and the
# order can be modified by changing the dictionary
ordered_keys = list(my_dict.keys())
ordered_keys.sort()  # sorts alphanumerically

# Equivalent to ordered_keys = sorted(list(myDict.keys()))

for key in ordered_keys:
    print(key + ' - ' + str(my_dict[key]))

# or even more concise
for key in sorted(my_dict.keys()):
    print(key + ' - ' + str(my_dict[key]))

my_dict_tuple = tuple(my_dict.items())  # Creating a tuple from a dict
print(my_dict_tuple)
print(type(my_dict_tuple))

# Useful for
for k, v in my_dict.items():
    print(k, v)

for i in my_dict_tuple:
    name, value = i
    print(name + ' = ' + str(value))

print(dict(my_dict_tuple))  # Creating a dict from a tuple

# Dictionaries can be nested
nested_dict = {'nest_1': {'A': 1, 'B': 2},
               'nest_2': {'A': 10}}

print(nested_dict['nest_1'], nested_dict['nest_2']['A'])

print('=' * 20)

# Merging dictionaries using the unpacked dictionary - **dict
my_dict_2 = {'omega': 0}
my_dict_3 = {**my_dict, **my_dict_2}
print(my_dict_3)

print('=' * 20)

# Filling a dictionary asking to the user
user_dict = {'a': 1}

asking_for = input('key: ')
searching_for = user_dict.get(asking_for, 'no')

if searching_for == 'no':
    new = input('value for {0}: '.format(asking_for))
    user_dict[asking_for] = new

print(user_dict)
