a_dict = {'A': 1, 'B': 3, 'C': -2}
b_dict = {'A': 0, 'D': 11}

# to clear the dictionary and leave it empty
# b_dict.clear()

# get(key, None) - to try if the key is in the dictionary, will return value if key exists,
# print None (by default) if it doesn't
value = a_dict.get('Z', 'Wrong key')
print(value)

print('=' * 30)

# view object are connected to the source (dynamic), they will change accordingly to the changes
# produced in the object that they refer to
# keys() - returns the keys of the dictionary
my_keys = a_dict.keys()  # this is a view object (is iterable)
print(my_keys)
print(type(my_keys))

a_dict['Z'] = 99  # adding a new key
print(my_keys)  # the view object has changed accordingly

print('=' * 30)
# values() - returns the values of the dictionary
my_values = a_dict.values()  # also a view object
print(my_values)
print(type(my_values))

print('=' * 30)
# items() - returns a view object of the key-value pairs - can be converted into a tuple
my_items = a_dict.items()
print(my_items)
print(type(my_items))

print('=' * 30)
# pop(key, default) - removes and returns key's value or default if there isn't
p = a_dict.pop('H', 'Not here')
print(p, a_dict)

print('=' * 30)
# popitem() - removes and returns an arbitrary key-value pair
arb = a_dict.popitem()
print(arb, a_dict)

print('=' * 30)
# update([other]) - updates the dict with the key-value pairs from other, creating new items
# or overwriting existing ones
a_dict.update(b_dict)
print(a_dict)

print('=' * 30)
# copy() - makes a shallow copy
c_dict = a_dict.copy()
print(c_dict)

print('=' * 30)
# setdefault(key[default]) - if key in dict, return its value, if not, inserts key
# with a value of default and return default
message = 'I am a Python beast, yes man!'
count = {}  # we are going to count the number of times each character appears in the message
for char in message:
    count.setdefault(char, 0)  # set = 0 if key 'char' doesn't exist
    count[char] += 1
print(count)

print('=' * 30)
# fromkeys(seq, value) - creates a new dictionary with keys from seq and values set to value
n_keys = 'B'
d_dict = a_dict.fromkeys(n_keys, 0)
print(d_dict)
