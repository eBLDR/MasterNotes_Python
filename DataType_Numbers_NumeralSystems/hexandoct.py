# hexadecimal and octal systems
for i in range(17):
    print("{0:>2} in hex is {0:>02x}".format(i))  # hexadecimal
    print("{0:>2} in oct is {0:>02o}".format(i))  # octal

# to declare variable
x = 0x10  # 16 in hex
y = 0x0a  # 10
z = 0o10  # 8 in oct

print(x, y, z)

print('\t{}\t\t\t{}\t\t\t{}'.format(x, hex(x), oct(x)))
print(type(x), type(hex(x)))  # type are int, str
print(x * y, "=", hex(x * y))
