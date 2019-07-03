"""
A string is a sequence of characters.
Strings are immutable: str[0] = new_value will raise en exception.
"""

# Can contain any character
s = 'ParRot &8-8*lfj@$sdk'
print(s)
print(type(s))

# Either 'str', "str" or """str""" can be used
s2 = 'OPP!'
print(s2)

s2_b = "OOP!"
print(s2_b)

# Explicit line join - if line is too long
s_long = 'This is a very very very very very very very very very very \
very very very very very very very very very very long line.'
print(s_long)

# For multi-line string
s2_c = """OOP! First line...
OPP! Second line.
OOP! Third line!
"""
print(s2_c)

# Calling characters by index
print(s[0])
print(s[5])

# Can be concatenated
s3 = s + s2 + '==='
print(s3)

# Can be multiplied by int
s4 = s2 * 5
print(s4)
