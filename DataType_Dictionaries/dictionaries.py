"""
A dictionary object consist of a key-value pairs - it's a "hash table".
Keys are immutable (keys must be "hashable"), whereas values are mutable.
The items inside a dictionary are ordered (from python 3.6, before were unordered).
"""

myDict = {'alpha': 1,
          'beta': 2,
          'gamma': 3,
          'epsilon': 5}

print(myDict["beta"])

# to add entry
myDict['delta'] = 'unknown'
print('delta is {}'.format(myDict['delta']))
myDict['delta'] = 4
print('delta is now {}'.format(myDict['delta']))

# a dictionary can also be created using dict()
d = dict(one=1, two=2, three=3)
print(d)

d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d2)

d3 = dict([('two', 2), ('one', 1), ('three', 3)])
print(d3)

print(d == d2 == d3)  # True

print('=' * 20)

# to delete a key-value pair
del myDict['gamma']

# del myDict  # to delete the full dictionary

# key-value pairs are created in different order every time, and the
# order can be modified by changing the dictionary
ordered_keys = list(myDict.keys())
ordered_keys.sort()  # sort by alphanumerical

# equivalent to ordered_keys = sorted(list(myDict.keys()))

for key in ordered_keys:
    print(key + ' - ' + str(myDict[key]))
# or even more concise
for key in sorted(myDict.keys()):
    print(key + ' - ' + str(myDict[key]))

myDict_tuple = tuple(myDict.items())  # creating a tuple from a dict
print(myDict_tuple)
print(type(myDict_tuple))

# useful for
for k, v in myDict.items():
    print(k, v)

for i in myDict_tuple:
    name, value = i
    print(name + ' = ' + str(value))

print(dict(myDict_tuple))  # creating a dict from a tuple

# dictionaries can be nested
nested_dict = {'nest_1': {'A': 1, 'B': 2},
               'nest_2': {'A': 10}}

print(nested_dict['nest_1'], nested_dict['nest_2']['A'])

print('=' * 20)

# merging dictionaries using the unpacked dictionary - **dict
myDict2 = {'omega': 0}
myDict3 = {**myDict, **myDict2}
print(myDict3)

print('=' * 20)

# filling a dictionary asking to the user
userDict = {'a': 1}

askingFor = input('key: ')
searchingFor = userDict.get(askingFor, 'no')

if searchingFor == 'no':
    new = input('value for {0}: '.format(askingFor))
    userDict[askingFor] = new

print(userDict)

