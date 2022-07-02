# Python can work with binary, octal, decimal, hexadecimal

# Numbers are in base 10 by default (type: int)
n = 12

print(f"n: {n}, bin(n): {bin(n)}, oct(n): {oct(n)}, hex(n): {hex(n)}")

print(type(bin(n)))  # str

# Number of bits necessary to represent the number in binary
print(f"n' bit length: {n.bit_length()}")

# Declared variables are auto converted to decimal
x = 0b1010  # 10 in binary
y = 0o12  # 10 in oct
z = 0x0a  # 10 in hex

print(x, y, z)
print(x == y == z)

print(type(x), type(bin(x)))  # int, str
print(x * y, "=", hex(x * y))

print("#" * 30)

# Printing in different systems
for i in range(17):
    print(f"{i:>2} in binary is {i:>05b}")  # binary
    print(f"{i:>2} in oct is {i:>02o}")  # octal
    print(f"{i:>2} in hex is {i:>02x}")  # hexadecimal
