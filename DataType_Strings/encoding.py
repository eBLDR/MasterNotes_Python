# -*- coding: utf-8 -*-
"""
The above line is the encoding magic line (see magic_lines.txt).
"""
# ASCII (American Standard Code for Information Interchange) Character
# Encoding - direct equivalent of utf-8
# all the characters of the string are saved in binary
print('\nASCII')

for i in range(0, 256):
    end_char = '\t'
    if i % 10 == 0:
        end_char = '\n'

    # chr() returns the ASCII character corresponding to the integer
    print('{0:3} {1}'.format(i, chr(i)), end=end_char)
    # chr() ranges from 0 to 1,114,111

# Opposite to chr() is ord() function, takes one character and returns the
# UNICODE reference number
# UNICODE is a superset of ASCII
print('\n\n\t', ord('o'))

print('=' * 30)

# Using ASCII codes, 10 is new line, 9 is tab
b_string = 'this is' + chr(10) + 'a string split' + chr(9) + chr(9) + 'and tabbed'

# Unicode strings, we can store characters using its unicode hexadecimal key
# Python 3 treats all the strings as unicode, whereas in python 2 u' needs to
# be specified
# u'' will encode the string using the encoding declared in the magic line,
# default encoding is ASCII
uni = u'äöü\xe4\xf6\xfc'
print(uni)

# Bytes object - the string will be saved with it's corresponding encoding
# values
byte_string = b'I like bytes'
print(byte_string, type(byte_string))

for byte in byte_string:
    print(hex(byte))

# Encoding
my_str = 'I want to be encoded'
enc_str = my_str.encode('utf-16')  # Returns a byte string

print(enc_str)
print(type(enc_str))

# Decoding
dec_str = enc_str.decode('utf-16')
print(dec_str)
print(type(dec_str))
