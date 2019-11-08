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

# Prints the binary representation of an integer
print(bin(integer))

# Prints the number of bits necessary to print the int in binary
print(integer.bit_length())

for i in range(17):
    print('{0:>2} in binary is {0:>05b}'.format(i))

# To declare variables in binary
a = 0b1001
b = 0b0111
print('\t{}\t\t{}'.format(a, bin(a)))
print('\t{}\t\t{}'.format(b, bin(b)))
print(type(a), type(bin(a)))  # types are int, str

# not operator - equivalent -(x-1)
not_a = ~ a

# and operator
a_and_b = a & b

# or operator
a_or_b = a | b

# or exclusive operator
a_xor_b = a ^ b

print('NOT a is {}'.format(bin(not_a)))
print('a AND b is {}'.format(bin(a_and_b)))
print('a OR b is {}'.format(bin(a_or_b)))
print('a XOR b is {}'.format(bin(a_xor_b)))

# Bit shifts
# Left shift, moves the bits to the left and places new 0 on the right
print(bin(a << 1))
# x << y is equivalent to x * 2**y

# Right shift, moves the bits to the right
print(bin(a >> 1))
# x >> y is equivalent to x // 2**y
