"""
Long comment
'\' is the scape character, followed by control character
\n - new line
\t - tab
\b - backspace
\r - carriage return
"""

text = 'Hello World'
print(text)

# nice comment

# new line
splitString = "Split\nstring"
splitString2 = """Split
super
string"""
print(splitString)
print(splitString2)

# tabs
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# scape characters
anotherString = "He said \"No, please\""
print(anotherString)

# backspace
moreString = 'Delete\b my last e'
print(moreString)

# r\ is a carriage return, returns to the left side and overwrites previous text
randomString = 'Remove half \rof me'
print(randomString)

extraString = "I don't \vknow what \ais \fthis."
# \v is a vertical tab
# \f is a formfeed
# \a is a bell
print(extraString)

strangeString = "this " \
                "goes in " \
                "one line"
print(strangeString)

upTo = 10
for i in range(0, upTo + 1):
    if i < upTo:
        print(i, end=' - ')
    else:
        print(i)

print('=' * 20)

a_string = 'this is\na string split\t\tand tabbed'
print(a_string)

# raw string literals, scape characters have no effect
raw_string = r'this is\na string split\t\tand tabbed'
print(raw_string)

print('=' * 20)

# scape character will take the next character and try to use an existing command, if exists
backslash_string = 'backslash \followed by text'
print(backslash_string)

# if we want to see the backslash
backslash_string2 = 'backslash \\followed by text'
print(backslash_string2)

# raw literal string cannot end with a backslash
# error_string = r'this string ends with\'
