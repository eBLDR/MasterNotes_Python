"""
math module.
"""

import math

# factorial
print(math.factorial(5))

# CONSTANTS
# euler number
print("e =", math.e)

# pi number
print("pi =", math.pi)

# tau number = 2pi
# print(math.tau)  # new in version 3.6

# floating-point positive infinity - use -math.inf for negative infinity
print(math.inf)     # equivalent to float('inf')

# floating-point 'not a number' (NaN)
print(math.nan)     # equivalent to float('nan')

# POWER AND LOGARITHMIC
# square root
print(math.sqrt(144))

# to the power of - equivalent to 2**5
print(math.pow(2, 5))   # returns float
print(2 ** 5)           # returns int

# e**x
print(math.exp(2))

# logarithm of x to base (e is default base)
print(math.log(101, 3))

# base-2 logarithm of x
print(math.log2(512))

# base-10 logarithm of x
print(math.log10(1000))

# ANGULAR CONVERSION
# angle x from radians to degrees
print(math.degrees(math.pi))

# angle x from degrees to radians
print(math.radians(90))

# TRIGONOMETRY
# sine of x radians
print(math.sin(math.pi * 0.5))

# cosine of x radians
print(math.cos(math.pi))

# tan of x radians
print(math.tan(math.pi * 0.25))

# asin() - acos() - atan() for arcs of x in radians

# hypotenuse - euclidean norm - sqrt(x*x + y*y)
print(math.hypot(3, 4))
