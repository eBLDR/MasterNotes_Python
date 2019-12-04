"""
The following effect is due to binary conversion when dealing with floats.
To fix it, we can use the module 'decimal' from Python Standard Library:
import decimal
"""

x = 10.10
print('x = {}'.format(x))

x += 0.10
print('+0.10... x: {}'.format(x))

x += 0.10
print('+0.10... x: {}'.format(x))

x -= 0.30
print('-0.30... x: {}'.format(x))

print('\n0.2 + 0.1 = {}'.format(0.2 + 0.1))

print('\n25.45 - 22.5 = {}'.format(25.45 - 22.5))
