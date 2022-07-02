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
a = 0b1001
b = 0b0111

print(f"a: {a}, b: {b}")

# Operators
print(f"NOT a: {bin(~ a)}")  # ~x is equivalent to -(x-1)
print(f"a AND b: {bin(a & b)}")
print(f"a OR b: {bin(a | b)}")
print(f"a XOR b: {bin(a ^ b)}")

# Bit shifts
# Left shift, moves the bits to the left and places new 0 on the right
print(f"Left shift: {bin(a << 1)}")  # x << y is equivalent to x * 2**y

# Right shift, moves the bits to the right
print(f"Right shift: {bin(a >> 1)}")  # x >> y is equivalent to x // 2**y
