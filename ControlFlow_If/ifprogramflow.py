"""
The expression following the 'if' keyword is being assessed by the bool() function.
'if expr:' is actually calling 'if bool(expr):'.
"""

name = input('Name: ')
age = int(input('Your age, {0}? '.format(name)))
print(age)

# Starting with a if statement
# all equivalent
# if age >= 18 and age <= 65:
# if 18 <= age <= 65:
if 17 < age < 66:
    print('Welcome to work!')

# Followed by 0 or more elif clauses
# elif age > 99:
elif not (age < 99):
    print('Black screen')
elif age == 24:
    print('Special case, 24yo cannot join!')

# Can have 0 or 1 else clause, will happen always if none of the above if/elif is True
else:
    print('Come back in {0} years'.format(18 - age))

x = input('Enter some text: ')

# Will return True if the variable is not 0, nor None nor empty srt, list, dict, tuple...
if x:  # equivalent to if x is not None:
    print('You entered \'{}\''.format(x))
else:
    print('You did not enter anything.')

# in keyword
parrot = 'Norwegian Blue'
letter = input('Enter a character: ')

if letter in parrot:
    print('Give me an {}!'.format(letter))
else:
    print('I don\'t need that letter.')
