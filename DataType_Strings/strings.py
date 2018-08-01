# Strings are immutable: str[0] = new_value will raise en exception.

# Can contain any character
s = 'ParRot &8-8*lfj@$sdk'
s2 = 'OPP!'

print(s)
print(type(s))
print(s[0])
print(s[5])  # Calling characters by index

s3 = s + s2 + '==='  # Can be concatenated
print(s3)

s4 = s2 * 5  # Can be multiplied by int
print(s4)
