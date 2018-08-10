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
calcProc = subprocess.Popen('/usr/bin/gnome-calculator')

print(type(calcProc))

# poll() method serves as a run check - will return None if the process is still
# running at the time poll() is called, if the process has terminated, it will return
# the process's integer exit code
print(calcProc.poll())

# wait() method will block main process until the launched process has terminated
# the return value of wait() is the process's exit code
print('\tWaiting for the process to be terminated')
calcProc.wait()

print('Launched process terminated with exit code: {}'.format(calcProc.poll()))
