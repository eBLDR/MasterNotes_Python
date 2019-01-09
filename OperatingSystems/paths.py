"""
When dealing with paths, . mean current directory, .. means parent directory.
"""
import os

# os.getcwd() - gets current working directory
current_path = os.getcwd()
print('Current path is: {}'.format(current_path))

# We can change the cwd with chdir() method
os.chdir('CommandTest')
print('Changed to: {}'.format(os.getcwd()))

# os.path.abspath(path) - will return the absolute path of the directory using proper separators depending
# on the OS used, directory must be in the working directory
absolute_path = os.path.abspath('./')
print('Absolute path is: {}'.format(absolute_path))

# os.path.relpath(path, start) - relative path to start folder/file
print('Rel path to B is: {}'.format(os.path.relpath('./', './01/B')))

print('=' * 20)

# os.path.split() - splits the last section of the path
print(os.path.split(absolute_path))

# os.path.join(path, path2) - join path2 to path
print(os.path.join(absolute_path, '01'))

# isabs(path) - return True if path is absolute

print('=' * 20)

# dir name and base name
my_path = os.path.join(os.getcwd(), 'hello.txt')
print('Dir name: ' + os.path.dirname(my_path))  # Name of path
print('Base name: ' + os.path.basename(my_path))  # Name of file or current folder

print('=' * 20)

# To get a list of separated directories from path
print(os.path.sep)  # A variable equal to the separator used in the current OS
print(my_path.split(os.path.sep))

print('=' * 20)

# Separating extension
print(os.path.splitext(my_path))
