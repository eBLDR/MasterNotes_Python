# 'r' for reading mode
sonnet = open("sample.txt", 'r')

print("jabber type is: ", type(sonnet))

print("=" * 30)

sonnet_content = sonnet.read()  # Can only be used once, it's consumed when called
print(type(sonnet_content))
print(sonnet_content)

sonnet.close()  # Always closing the file at the end of use

print("=" * 30)

sonnet = open("./sample.txt", 'r')

# equivalent to
# for line in jabber:  # in 'file.txt' identifies the lines
#    print(line, end='')

# equivalent to
for line in sonnet.read().splitlines():  # Returns a list of str separated by '\n' char, eq to split('\n')
    print(line)

sonnet.close()  # Always closing the file at the end of use

print("=" * 30)

# with (context manager), a more efficient way to open a file
# with will close the file at the end automatically and will also trap errors
with open("sample.txt", 'r') as sonnet:
    for line in sonnet:  # line type = str
        if 'AND' in line.upper():
            print(line, end='')

print("\n", "=" * 30)

# The next example prints in the same way, but specifying the reading manually
with open('sample.txt', 'r') as sonnet:
    line = sonnet.readline()  # This will return a string
    while line:
        print(line, end='')
        line = sonnet.readline()

print("\n", "=" * 30)

# Saving as a list of strings
with open('sample.txt', 'r') as sonnet:
    lines = sonnet.readlines()  # This will return a list of strings, corresponding to each line
print(lines)

print("=" * 30)

# Saving the whole file as a single string
with open('sample.txt', 'r') as sonnet:
    lines = sonnet.read()
    print(type(lines))

for char in lines[::-1]:
    print(char, end='')
