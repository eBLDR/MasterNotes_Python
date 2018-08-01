"""
cmath module - for complex numbers operations.
For logarithmic and trigonometric functions see math module,
cmath has the same ones applied to complex numbers.
"""

import cmath

# CONSTANTS
# complex with zero real part and + infinity imaginary part
# print(cmath.infj)   # new in version 3.6

# complex with zero real part and NaN imaginary part
# print(cmath.nanj)   # new in version 3.6

# COORDINATES CONVERSION
# phase - argument of x
print(cmath.phase(complex(-1.0, 0.0)))

# modulus - use abs() built-in function
print(abs(complex(3, 4)))

# complex to polar coordinates - returns a pair equivalent to (abs(x), phase(x))
print(cmath.polar(complex(3, 4)))

# polar coordinates to complex
print(cmath.rect(5, cmath.pi))
