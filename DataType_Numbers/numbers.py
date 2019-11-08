"""
Numbers are immutable. They can be:
    - Integer numbers (subset of float).
    - Floating point numbers (or float for short).
    - Complex numbers.
"""
# Integer - equivalent to int(12)
a = 12
a2 = 0  # zero integer
print(a, type(a))
print(a2, type(a2))

print('=' * 20)

# Float - equivalent to float(3.6)
b = 3.6
b2 = 0.0  # zero float

# Scientific notation
b_exp = 3.45e-5  # 3.45*10**(-5), also float
print(b, type(b))
print(b2, type(b))
print(b_exp, type(b))

# Complex - equivalent to complex(5, 3)
c = 5 + 3j
c2 = 0j  # zero complex
print(c, type(c))
print(c2, type(c2))

print('=' * 20)

# Operators + - * ** / // %
# Expressions: variable_1 + operator + variable_2
# Sum
print('a + b = {}'.format(a + b))

# Subtraction
print('a - b = {}'.format(a - b))

# Multiplication
print('a * b = {}'.format(a * b))

# Power - a to the power b
print('a ** b = {}'.format(a ** b))

# Division
print('a / b = {}'.format(a / b))

# Floor division (quotient, no decimals)
print('a // b = {}'.format(a // b))

# Modulo, remainder of a/b
print('a % b = {}'.format(a % b))

# Operator precedence, default precedence can be overridden by explicit
# parentheses
print('a + b * a = {}'.format(a + b * a))
print('(a + b) * a = {}'.format((a + b) * a))

print('=' * 20)

# Functions
z = -12.93578

# abs() function returns the absolute value
print(abs(z))

# round() returns the rounded number, specifying the number of decimals
print(round(z, 2))

# Data conversion
i = 5

# Convert to float
print(float(i))

f = 1.95

# Convert to integer
print(int(f))  # Deletes the decimal part

# int(@value, @base=10)
# We can specify the base, by default decimal
# In this case we use binary, base 2
print(int('11', 2))
