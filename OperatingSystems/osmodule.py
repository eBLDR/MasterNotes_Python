"""
When dealing with paths, ./file mean current directory, ../file means parent directory.
"""
import os

# os.system(command) - will run the command in the terminal
os.system("ls -a")  # sample command

# os.uname() - returns information about operating system and machine
print('os.uname(): {}'.format(os.uname()))

# os.getlogin() - returns the name of the user logged in
print('os.getlogin(): {}'.format(os.getlogin()))

# os.getpid() - returns the current process' id
print('os.getpid(): {}'.format(os.getpid()))

# os.getppid() - returns the parent's process' id
print('os.getppid(): {}'.format(os.getppid()))

# === ENVIRONMENT VARIABLES ===
"""
Are variables declared in the os, it's a dictionary like.
In Linux, we can see them with the command, 'export' in the terminal.
Are useful for avoiding having to write passwords on the scripts.
We can add them using a bash script, they will be erased after restart.
Or using os.environ['NEW_KEY'] = 'NEW_VALUE' in Python, they will be erased after killing the process.
In editors (like Pycharm), it's also possible to add them to the project's configuration.
"""
print('HOME is ', os.getenv('HOME', 'Not found'))

# === PATHS ===

# os.getcwd() - gets current working directory
current_path = os.getcwd()
print("Current path is: {}".format(current_path))

# We can change the cwd with chdir() method
os.chdir('CommandTest')
print("Changed to: {}".format(os.getcwd()))

# os.path.abspath(path) - will return the absolute path of the directory using proper separators depending
# on the OS used, directory must be in the working directory
absolute_path = os.path.abspath('./')
print("Absolute path is: {}".format(absolute_path))

# os.path.relpath(path, start) - relative path to start folder/file
print("Rel path to B is: {}".format(os.path.relpath('./', './01/B')))

print("=" * 20)

# os.path.split() - splits the last section of the path
print(os.path.split(absolute_path))

# os.path.join(path, path2) - join path2 to path
print(os.path.join(absolute_path, '01'))

# isabs(path) - return True if path is absolute

print("=" * 20)

# dir name and base name
my_path = os.path.join(os.getcwd(), 'hello.txt')
print("Dir name: " + os.path.dirname(my_path))      # name of path
print("Base name: " + os.path.basename(my_path))    # name of file or current folder

print("=" * 20)

# To get a list of separated directories from path
print(os.path.sep)  # a variable equal to the separator used in the current OS
print(my_path.split(os.path.sep))

print("=" * 20)

# Separting extension
print(os.path.splitext(my_path))

# Checking path validity
"""
os.path.exists(path) - return True if file or folder exists
os.path.isfile(path) - return True if path argument exists and is a file
os.path.isdir(path) - return True if path argument exists and is a directory
"""

# === DIRECTORIES AND FILES ===

print("=" * 20)

# os.listdir(path) - will generate the directories/files in the directory path
for item in os.listdir(absolute_path):
    print(item)

print("=" * 20)

# os.walk() - is a generator that iterates all the directories in the specified path (either relative to cwd or abs)
# each iteration returns a list [path, directories, files]
for path, directories, files in os.walk("./"):
    print("Path: {}".format(path))
    print("\tDirectories:")
    for dir_ in directories:
        print('\t\t{}'.format(dir_))
    print("\tFiles:")
    for file in files:
        print('\t\t{}'.format(file))


print("=" * 20)

# To get the size of a file
print("Size of hello.txt in bytes: ", os.path.getsize(my_path))

# Getting the size of all the contents in a folder
totalsize = 0
for filename in os.listdir('./'):
    totalsize += os.path.getsize(filename)
    print(filename)

print("Total size of (bytes) of cwd is :", totalsize)

# makedirs('path', exist_ok=False) - creates directory/ies
# If directory already exists, will raise an error, unless we set exist_ok=True
# it uses mkdir(), method that can only create one directory at the time
try:
    os.makedirs('./03/ABC')  # can create full path at once
except FileExistsError:
    print("Directory already exists.")

print("=" * 20)

# unlink() - permanently deletes file
file_name = 'tobedeleted.txt'
os.system('touch ./{}'.format(file_name))  # creating sample file to delete
os.unlink('./{}'.format(file_name))

# rmdir() - permanently deletes a single folder, folder must be empty
os.rmdir('./03/ABC')

# rmdirs() - applied to the same path above, will delete all ABC, 03 and ./, if both empt

print("./03/ABC deleted.")

print("=" * 20)

# rename(old_name, new_name) - rename a file/dir
try:
    os.rename('./02', './04')
except FileNotFoundError:
    pass
