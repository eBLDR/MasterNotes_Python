"""
OR : True if only one of the conditions is True.
AND : True only if all of the conditions are True.
"""

# All the following are False
f = False  # bool
f2 = not True
n = None  # NoneType
v = 0  # int
s = ''  # str
l = []  # list
t = ()  # tuple
d = {}  # dictionary
st = set()  # set

print("""False:\t\t{0}
not True:\t{7}
None:\t\t{1}
0.0:\t\t{2}
'':\t\t{3}
[]:\t\t{4}
():\t\t{5}
{{}}:\t\t{6}
set():\t\t{8}""".format(
    bool(f), bool(n), bool(v), bool(s), bool(l), bool(t),
    bool(d), bool(f2), bool(st))
)

print('=' * 25)

# comparators - assess the value, not the identity (id()) - return a boolean
a = -1
b = 5
print('{} == {}:\t{}'.format(a, b, a == b))
print('{} != {}:\t{}'.format(a, b, a != b))
print('{} < {}:\t\t{}'.format(a, b, a < b))
print('{} > {}:\t\t{}'.format(a, b, a > b))
print('{} <= {}:\t{}'.format(a, b, a <= b))
print('{} >= {}:\t{}'.format(a, b, a >= b))

# multiple line
print('{} < {} < {}:\t{}'.format(a, 0, b, a < 0 < b))

print('=' * 25)

# is/is not comparator - does not asses the value, assesses the identity (id())
# return a boolean
a = [2, 3]
b = [2, 3]
print('{} == {} : {}'.format(a, b, a == b))
print('{} is {} : {}'.format(a, b, a is b))
print('{} is not {} : {}'.format(a, b, a is not b))

print('=' * 25)

# OR
print('- OR -')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# AND
print('- AND -')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('=' * 25)

print(' or 1:\t\t{}'.format(bool(0 or 1)))
print('[2] and {{}}:\t{}'.format(bool([2] and {})))

print(' < 5 and 7 > 0:\t{}'.format(2 < 5 and 7 > 0))

# The next expression will raise an error when comparing 7 to a str,
# but because the first condition is False, using the AND operator
# will stop the comparisons as soon as one False is found.
print('\nAvoided error:')
print('2 > 5 and 7 > \'string\':\t{}'.format(2 > 5 and 7 > 'string'))

print('=' * 25)

# in keyword, checks item's existence in a sequence
char1 = 'a'
char2 = 'z'
s = 'abc'
print('{} in {}:\t{}'.format(char1, s, char1 in s))
print('{} in {}:\t{}'.format(char2, s, char2 in s))

print('=' * 25)

first_name = ''
last_name = 'Me'

# Booleans can also be used for variable assignment
name = first_name or last_name  # It will take the first non-empty value
print(name)
