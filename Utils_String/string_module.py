# Using the string.py module for ASCII characters
import string

# All the ascii letter including both lowercase and uppercase
ascii_all = string.ascii_letters

# Only the lowercase ascii letters
ascii_lower = string.ascii_lowercase

# Only the uppercase ascii letters
ascii_upper = string.ascii_uppercase

# Decimal digits
digits = string.digits

# Hexadecimal digits
hex_digits = string.hexdigits

# Octal digits
oct_digits = string.octdigits

# Punctuation characters
punctuation = string.punctuation

# Whitespace - includes space, tab, return, linefeed, form feed, vertical tab
whitespace = string.whitespace

# All the printable characters, combination of digits, ascii_letters, punctuation and whitespace
all_chars = string.printable

print(ascii_lower)
print(ascii_upper)
print(ascii_all)
print(digits, hex_digits, oct_digits)
print(punctuation)
print(whitespace)
print(all_chars)
