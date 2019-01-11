# NUMBERS, immutable variables
# Can be: integer (subset of float), float, complex

a = 12  # Integer - equivalent to int(12)
a2 = 0  # zero integer
print(a, type(a))
print(a2, type(a2))

print('=' * 20)

b = 3.6  # Float - equivalent to float(3.6)
b2 = 0.0  # zero float
b_exp = 3.45e-5  # 3.45*10**(-5), also float
print(b, type(b))
print(b2, type(b))
print(b_exp, type(b))

c = 5 + 3j  # Complex - equivalent to complex(5, 3)
c2 = 0j  # zero complex
print(c, type(c))
print(c2, type(c2))

print('=' * 20)

# Operators + - * ** / // %
# Expressions: variable_1 + operator + variable_2
print('a + b = {}'.format(a + b))  # sum
print('a - b = {}'.format(a - b))  # subtraction
print('a * b = {}'.format(a * b))  # multiplication
print('a ** b = {}'.format(a ** b))  # a to the power b
print('a / b = {}'.format(a / b))  # division
print('a // b = {}'.format(a // b))  # floor division (quotient, no decimals)
print('a % b = {}'.format(a % b))  # remainder of a/b

# Operator precedence, default precedence can be overridden by explicit parentheses
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
print(float(i))

f = 1.95
print(int(f))  # Deletes the decimal part
