""" Using the string.py module for ASCII characters. """

import string

# all the ascii letter including both lowercase and uppercase
ascii_all = string.ascii_letters

# only the lowercase ascii letters
ascii_lower = string.ascii_lowercase

# only the uppercase ascii letters
ascii_upper = string.ascii_uppercase

# the decimal digits
digits = string.digits

# hexadecimal digits
hex_digits = string.hexdigits

# octal digits
oct_digits = string.octdigits

# punctuation characters
punctuation = string.punctuation

# whitespace, includes space, tab, return, linefeed, form feed, vertical tab
whitespace = string.whitespace

# all the printable characters, combination of digits, ascii_letters, punctuation and whitespace
all_chars = string.printable

print(ascii_lower)
print(ascii_upper)
print(ascii_all)
print(digits, hex_digits, oct_digits)
print(punctuation)
print(whitespace)
print(all_chars)
