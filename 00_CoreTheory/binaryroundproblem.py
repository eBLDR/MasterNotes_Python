"""
The following effect is due to binary conversion when dealing with floats.
To fix it, we can use the module 'decimal' from Python Standard Library:
import decimal
"""

x = 10.10
print(x)
x += 0.10
print(x)
x += 0.10
print(x)
x -= 0.30
print(x)
