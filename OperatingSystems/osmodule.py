import os

# os.system(command) - will run the command in the terminal
os.system('ls -a')  # Sample command

# os.uname() - returns information about operating system and machine
print('os.uname(): {}'.format(os.uname()))

# os.getlogin() - returns the name of the user logged in
print('os.getlogin(): {}'.format(os.getlogin()))

# os.getpid() - returns the current process' id
print('os.getpid(): {}'.format(os.getpid()))

# os.getppid() - returns the parent's process' id
print('os.getppid(): {}'.format(os.getppid()))
