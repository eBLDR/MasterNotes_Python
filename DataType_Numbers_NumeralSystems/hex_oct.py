# Hexadecimal and octal systems
for i in range(17):
    print(f"{i:>2} in hex is {i:>02x}")  # hexadecimal
    print(f"{i:>2} in oct is {i:>02o}")  # octal

# to declare variable
x = 0x10  # 16 in hex
y = 0x0a  # 10 in hex
z = 0o10  # 8 in oct

print(x, y, z)

print(f"\t{x}\t\t\t{hex(x)}\t\t\t{oct(x)}")
print(type(x), type(hex(x)))  # int, str
print(x * y, "=", hex(x * y))
