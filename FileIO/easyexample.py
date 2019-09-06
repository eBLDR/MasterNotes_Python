""" Multiple modes example.
Three broad types of files exist:
    - Plain text files
    - Binary files
    - Raw files, AKA "unbuffered"
"""
# type full path ('C:\User\BLDR\Desktop\...') or relative path using \\
# sometimes we need to use the scape backslash (\\) to avoid unexpected formatting (\n, \t, ...)
# in UNIX, use / instead, or ./ for parent folder

filename = 'easyexample.txt'

# WRITE - Create file if not found, truncates the file
# @buffering=0, disable buffering for dealing with raw streams
my_file = open(filename, 'w', encoding='utf-8')  # , buffering=0)
# Encoding can specify the file's character encoding

my_file.write('Aloha!\n')  # Adding some text
my_file.close()

# APPEND - Appending data at the end of the file, will create the file if not found
my_file = open(filename, 'a')
my_file.write('Do you love ukelele?\n')  # Appending more text
my_file.close()

# READ - 'r' is also default mode
my_file = open(filename, 'r')
content = my_file.read()
my_file.close()

print(content)

# Copy file, read and then write
with open(filename, 'r') as read_file, open(filename.rsplit('.', 1)[0] + 'copy.txt', 'w') as write_file:
    write_file.write(read_file.read())
