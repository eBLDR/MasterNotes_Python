"""
Running another python script from the main execution.
"""

import subprocess

# Launching a python script as an independent process - variables won't be shared
# Popen can accept stdout, stdin, stderr as a communication pipe
pyScript = subprocess.Popen(['python', 'launchedscript.py'], stdout=subprocess.PIPE)  # shell=True), it opens a new python shell

# communicate() return the stdout and stderr pipes from the launched script as bytes type
# It will halt the main process until the launched process has finished
out, err = pyScript.communicate()

print(type(out))
print(out)
print(err)

# Convert bytes into str
result = out.decode('utf-8')

print(result)
