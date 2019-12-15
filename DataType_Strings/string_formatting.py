age = 24
print('My age is ' + str(age) + ' years')  # Concatenating strings as argument

# Replacement fields - Python version 3.0 and above
# {value : width}
print('My age is {0} years'.format(age))
print('There are {0} days in {1} and {2}'.format(31, 'Jan', 'March'))

# Index numbers are unnecessary, but then it's not possible to reuse them
# (assigned by order)
print('There are {} days in {} and {}'.format(31, 'Jan', 'March'))

print("""Jan: {2}
Feb: {0}
March: {2}
April: {1}
May: {2}
June: {1}""".format(28, 30, 31))

# It's also possible to refer arguments using named arguments
# good for nesting arguments if complex formatting is required
print('My name is {name} and I am a {species}!'.format(
    name='Max',
    species='Sapiens'
))

# and by index
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))

my_object = type('A', (), dict(attr=12))
# Referencing attributes from an instance of a class
print('My attribute is: {0.attr}'.format(my_object))

# From Python 3.6+, s = f'{x}' can be used in place of s = '{}'.format(x)
print(f'My age is {age}...')
print(f'Calc: {25 ** 2 - 7}; method: {len(str(age))}')

# Quotation can be used:
print('\n'.join(
    [f'{"*" * i:>10}*{"*" * i:10}' for i in range(10)]
))

# From Python 3.8+, a simpler way for debugging has been implemented
# Adding the '=' character, will print the variable name followed by its value
# print(f'{age=}...')  # Output is: 'age=24'

# If we wish to use curly braces inside the printing line while using format()
print('\n{{}} I am showing the curly braces! {}'.format(';)'))

print('=' * 30)

# spacing & figures - {0:n.m} - n is the total number of figures, m is the
# number of decimal figures
# .f for float type
print('\nPi is approximately {0:.10f}\n'.format(22 / 7))

print('=' * 30)

# Spacing with str
name = 'Edu'
print('{:15} BLDR'.format(name))
print('{:>15} BLDR'.format(name))  # justify to right
# curious fact: {:4} with numbers is right justified by default
# {:4} with str is left justified by default

print('=' * 30)

# Alignment: < for left alignment; > for right alignment (default);
# ^ for center alignment
# preceding the alignment character, we can set a filling character
# the + character indicates that we want to print '+' for positive numbers
# and '-' for negative
for i in range(-16, 30, 5):
    print('No. {0:+3} squared is {1:<6.1f} and cubed is {2:*^+12.2f}'.format(
        i, i ** 2, i ** 3)
    )

print('=' * 30)

# Converting to different numeral bases
print('int: {0:d}; hex: {0:x};HEX: {0:X}; oct: {0:o}; bin: {0:b}'.format(42))
# with 0x, 0o, or 0b as prefix:
print('int: {0:d}; hex: {0:#x};HEX: {0:#X}; oct: {0:#o}; bin: {0:#b}'.format(42))

print('=' * 30)

# Cool example
width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

print('=' * 30)

# Using the comma as a thousand separator
print('{:,}'.format(1234567890))

print('=' * 30)

# Conversion fields
"""
'Harold's a clever {0!s}'  # Calls str() on the argument first
'Bring out the holy {!r}'  # Calls repr() on the argument first
'More {!a}'  # Calls ascii() on the argument first
"""
