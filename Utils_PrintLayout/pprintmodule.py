# pretty print module

import pprint

message = 'I am a Python beast, yes man! 0 and 1 are my friends, keys are my family.'
count = {}  # we are going to count the number of times each character appears in the message

for char in message:
    count.setdefault(char, 0)  # check dictionaries notes for info about setdefault method
    count[char] += 1

print('Not cool printing . . .')
print(count)

print('\nCool printing . . .')
pprint.pprint(count)

print('=' * 10)
output = pprint.pformat(count)  # saves the cool printing into a object as str
print(output)
