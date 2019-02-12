"""
This is a multi-line comment

'\' is the scape character, followed by control character
\a - ASCII bell (BEL)
\b - ASCII backspace (BS)
\f - ASCII formfeed (FF)
\n - ASCII linefeed (LF)
\r - ASCII carriage return (CR)
\t - ASCII horizontal tab (TAB)
\v - ASCII vertical tab (VT)
"""

# This is a single-line comment

text = 'Hello World'
print(text)

# One line
print('One'
      'line')

# Using triple quotation will respect the format as typed
formatted_string = """Split
   super
 formatted
string"""
print(formatted_string)

snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""
print(snek)

print('=' * 20)

# Scape character will take the next character and try to use an existing command, if exists
# In this case, will ignore the ' closing string
another_string = 'He said \'No, please\''
print(another_string)

# If we want to see the backslash
backslash_string = 'backslash \\followed by text'
print(backslash_string)

# New line
split_string = 'Split\nstring'
print(split_string)

# Tab
tabbed_string = '1\t2\t3\t4\t5'
print(tabbed_string)

# Backspace
more_string = 'Delete\b my last e'
print(more_string)

# r\ is a carriage return, returns to the left side and overwrites previous text
random_string = 'Remove half \rof me'
print(random_string)

extra_string = 'I don\'t \vknow what \ais \fthis.'
# \v is a vertical tab
# \f is a formfeed
# \a is a bell
print(extra_string)

strange_string = 'this ' \
                 'goes in ' \
                 'one line'
print(strange_string)

up_to = 10
for i in range(0, up_to + 1):
    if i < up_to:
        print(i, end=' - ')
    else:
        print(i)

print('=' * 20)

# Raw string literals, scape characters have no effect
raw_string = r'this is\na string split\t\tand tabbed'
print(raw_string)

# Raw literal string cannot end with a backslash
# error_string = r'this string ends with\'
