"""
Each byte has 8 bits, the maximum integer number expressed in on byte is 255,
which is 1111 1111 in bin, and FF in hex.
The method .write(bytes()) writes one byte at the time in hex format,
so it cannot write numbers greater than 255.
The method .write(integer.to_bytes(#bytes, 'endian')) is able to write
any number, but we need to specify the number of bytes that corresponds
to each number.
"""
# 'b' mode for binary, followed by 'r' or 'w'
with open('binary', 'bw') as bin_file:  # 'binary' has no extension
    for i in range(17):  # range must be in (0, 256)
        bin_file.write(bytes([i]))  # function bytes() converts to kind of hex
    # equivalent to
    # binFile.write(bytes(range(17)))

with open('binary', 'br') as bin_file:
    for b in bin_file:
        print(b)

print('-' * 20)

a = 65534  # FF FE, it uses 2 bytes (16 bits)
b = 65535  # FF FF
c = 65536  # 00 01 00 00, it uses 4B (32 bits), the # of B used is even
x = 2998302  # 02 2D C0 1E

with open('binary2', 'bw') as bin_file2:
    bin_file2.write(a.to_bytes(2, 'big'))  # 2 is the length of the number in bytes
    bin_file2.write(b.to_bytes(2, 'big'))  # 'big' endian arranges the bytes from left to right
    bin_file2.write(c.to_bytes(4, 'big'))
    bin_file2.write(x.to_bytes(4, 'big'))
    bin_file2.write(x.to_bytes(4, 'little'))  # 'little' endian arranges the bytes from right to left

with open('binary2', 'br') as bin_file2:
    A = int.from_bytes(bin_file2.read(2), 'big')
    print(A)
    B = int.from_bytes(bin_file2.read(2), 'big')
    print(B)
    C = int.from_bytes(bin_file2.read(4), 'big')
    print(C)
    X = int.from_bytes(bin_file2.read(4), 'big')
    print(X)
    X2 = int.from_bytes(bin_file2.read(4), 'big')
    print(X2)
