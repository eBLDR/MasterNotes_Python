import os
import time

# Checking path validity
"""
os.path.exists(path) - return True if file or folder exists
os.path.isfile(path) - return True if path argument exists and is a file
os.path.isdir(path) - return True if path argument exists and is a directory
"""

# os.listdir(path=working_directory) - will generate the directories/files in the directory path
for item in os.listdir(os.path.abspath('./')):
    print(item)

print('=' * 20)

# os.walk() - is a generator that iterates all the directories in the specified path (either relative to cwd or abs)
# each iteration returns a list [path, directories, files]
for path, directories, files in os.walk('./'):
    print('Path: {}'.format(path))
    print('\tDirectories:')
    for dir_ in directories:
        print('\t\t{}'.format(dir_))
    print('\tFiles:')
    for file in files:
        print('\t\t{}'.format(file))

print('=' * 20)

# File properties
# To get the size of a file
file_name = 'CommandTest/hello.txt'
print('Size of {} in bytes: '.format(file_name), os.path.getsize(os.path.join(os.getcwd(), file_name)))

# Getting creation date of file in Windows, last metadata change in Unix
print('{} was created on'.format(file_name), time.ctime(os.path.getctime(file_name)))

# Getting last modification date of file
print('{} was last modified on'.format(file_name), time.ctime(os.path.getmtime(file_name)))

# Getting creation date of file in Windows, last metadata change in Unix
print('{} was last accessed on'.format(file_name), time.ctime(os.path.getatime(file_name)))

# Getting the size of all the contents in a folder
total_size = 0
for filename in os.listdir('./'):
    total_size += os.path.getsize(filename)
    print(filename)
print('Total size of (bytes) of cwd is :', total_size)

print('=' * 20)

# File manipulation
# makedirs('path', exist_ok=False) - creates directory/ies
# If directory already exists, will raise an error, unless we set exist_ok=True
# it uses mkdir(), method that can only create one directory at the time
try:
    os.makedirs('./03/ABC')  # can create full path at once
except FileExistsError:
    print('Directory already exists.')

print('=' * 20)

# unlink() - permanently deletes file
file_name = 'tobedeleted.txt'
os.system('touch ./{}'.format(file_name))  # creating sample file to delete
os.unlink('./{}'.format(file_name))

# rmdir() - permanently deletes a single folder, folder must be empty
os.rmdir('./03/ABC')

# rmdirs() - applied to the same path above, will delete all ABC, 03 and ./, if both empty
print('./03/ABC deleted.')

print('=' * 20)

# rename(old_name, new_name) - rename a file/dir
try:
    os.rename('./02', './04')
except FileNotFoundError:
    pass
