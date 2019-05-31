"""
When having multiple instances of an application open,
each of those instances is a separate process of the same program.
Every process can have multiple threads. Unlike threads,
a process cannot directly read and write another process’s variables.
"""

# subprocess module allows us to use this functionality
import subprocess

# starting a new process with the Popen() (Process open) method
# @path (str) to the executable file, can also be a command (i.e.: 'ls')
calc_process = subprocess.Popen('/usr/bin/gnome-calculator')

print(type(calc_process))

# poll() method serves as a run check - will return None if the process is still
# running at the time poll() is called, if the process has terminated, it will return
# the process's integer exit code
print(calc_process.poll())

# wait() method will block main process until the launched process has terminated
# the return value of wait() is the process's exit code
print('\tWaiting for the process to be terminated')
calc_process.wait()

print('Launched process terminated with exit code: {}'.format(calc_process.poll()))

"""
It is possible to pass command line arguments to processes launched with Popen().
To do so, pass a list as the sole argument, the first str in the list will be the executable filename
of the program to be launched; all the subsequent str will be the command line arguments,
in fact, this list will be the value of sys.argv.
"""

# Opening the file with the corresponding program
text = subprocess.Popen(['gedit', 'sample.txt'])

# Opening files with the default application
# Programs in charge of searching for default application corresponding to file's extension
# Windows - 'start'
# OS X - 'open'
# Ubuntu Linux - 'see'
# subprocess.Popen(['see', 'sample.txt'])  # , shell=True) - needed only in Windows
