""" Multiple modes example. """
# type full path ("C:\User\BLDR\Desktop\...") or relative path using \\
# sometimes we need to use the scape backslash (\\) to avoid unexpected formatting (\n, \t, ...)
# in UNIX, use / instead, or ./ for parent folder

# WRITE - Create file if not found, truncates the file
myFile = open('myFile.txt', 'w', encoding='utf-8')
# Encoding can specify the file's character encoding

myFile.write('Aloha!\n')  # Adding some text
myFile.close()

# APPEND - Appending data at the end of the file, will create the file if not found
myFile = open('myFile.txt', 'a')
myFile.write('Do you love ukelele?')  # Appending more text
myFile.close()

# READ - 'r' is also default mode
myFile = open('myFile.txt', 'r')
content = myFile.read()
myFile.close()

print(content)
