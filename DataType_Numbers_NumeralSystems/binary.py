# Python can work with decimal, binary, hexadecimal, octal
"""
- Bitwise operators-

|   NOT  |   |    AND    |  |    OR     |  |    XOR    |
 --------      ---------      ---------      ---------
  ~ 0 = 1  ||  0 & 0 = 0  ||  0 | 0 = 0  ||  0 ^ 0 = 0
  ~ 1 = 0  ||  0 & 1 = 0  ||  0 | 1 = 1  ||  0 ^ 1 = 1
           ||  1 & 0 = 0  ||  1 | 0 = 1  ||  1 ^ 0 = 1
           ||  1 & 1 = 1  ||  1 | 1 = 1  ||  1 ^ 1 = 0

* NOT is also called "ones' complement"
"""

integer = 12
print(bin(integer))  # prints the binary representation of an integer
print(integer.bit_length())  # prints the number of bits necessary to print the int in binary

for i in range(17):
    print('{0:>2} in binary is {0:>05b}'.format(i))

# To declare variables in binary
a = 0b1001
b = 0b0111
print('\t{}\t\t{}'.format(a, bin(a)))
print('\t{}\t\t{}'.format(b, bin(b)))
print(type(a), type(bin(a)))  # types are int, str

not_a = ~ a  # not operator - returns -x -1
a_and_b = a & b  # and operator
a_or_b = a | b  # or operator
a_xor_b = a ^ b  # or exclusive operator

print('NOT a is {}'.format(bin(not_a)))
print('a AND b is {}'.format(bin(a_and_b)))
print('a OR b is {}'.format(bin(a_or_b)))
print('a XOR b is {}'.format(bin(a_xor_b)))

# Bit shifts
print(bin(a << 1))  # left shift, moves the bits to the left and places new 0 on the right
# x << y is equivalent to x * 2**y
print(bin(a >> 1))  # right shift, moves the bits to the right
# x >> y is equivalent to x // 2**y
