# casing format
myString = 'I am a machine.'
print(myString.upper())         # all chars in uppercase
print(myString.lower())         # all chars in lowercase
print(myString.title())         # all first chars of words in uppercase
print(myString.capitalize())    # only first letter of the str in uppercase
print(myString.swapcase())      # inverts casing

print("=" * 30)

# Data type check
anotherString = input('Enter a string: ')

print('Is digit = {}'.format(anotherString.isdigit()))  # true if str is number (int)
print('Is alpha = {}'.format(anotherString.isalpha()))  # true if str is alphabetic
print('Is alnum = {}'.format(anotherString.isalnum()))  # true if str is alphanumeric
print('Startswith \'a\' = {}'.format(anotherString.startswith('a')))  # true if str starts whit 'char'
print('Endswith \'a\' = {}'.format(anotherString.endswith('a')))  # true if str ends with 'char'

print("=" * 30)

# Stripping - default value for stripping is \n
file_name = "image.png"
print(file_name.strip('pg.n'))      # will strip from both sides if matching, order doesn't matter
print(file_name.rstrip('.png'))     # will strip only from right side if matching
print(file_name.lstrip('ma'))       # will strip only from left side if matching

print("=" * 30)

# str.replace(@old, @new, @count) - replaces @old with @new a maximum of @count times
name = 'Epsylon'
new_name = name.replace('E', 'I')
print(new_name)

print("=" * 30)

# str.find(@char, @start, @end) - return the lowest index in the str where @char is found
# return -1 if it is not found
print(name.find('sy'))
print(name.find('p', 3, 6))

print("=" * 30)

# Justifying text - @num_of_spaces, @filling_character, it returns a new string
name = 'Edu'

print(name.ljust(15) + ' BLDR')         # left justification
print(name.rjust(15, '-') + ' BLDR')    # right justification
print(name.center(20, '+'))             # center justification

print("=" * 30)

# str.zfill() - pads a numeric string on the left with zeros
for j in range(5):
    n = -0.2 * j
    print('{}'.format(str(n).zfill(6)))

print("=" * 30)


# Nice printing example
def print_inventory(inventory_dict, left_width, right_width, cool_char='-'):
    print(' INVENTORY '.center(left_width + right_width, cool_char))
    for k, v in inventory_dict.items():
        print((k + ' ').ljust(left_width, '.') + str(v).rjust(right_width))


inventory = {'gold': 12, 'ropes': 1, 'dagger': 3, 'arrows': 7}
print_inventory(inventory, 18, 4)
print_inventory(inventory, 15, 5, cool_char='+')

print("=" * 30)

# Encoding
test = 'encoding'
print(test.encode(encoding='utf-32'))  # utf-8 is the default
