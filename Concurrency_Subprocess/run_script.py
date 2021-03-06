"""
Running another python script from the main execution.
"""
import subprocess

# Launching a python script as an independent process - variables won't be shared
# Popen can accept stdout, stdin, stderr as a communication pipe
py_script = subprocess.Popen(
    ['python', 'launched_script.py'], stdout=subprocess.PIPE
)  # shell=True), it opens a new python shell

# communicate() return the stdout and stderr pipes from the launched script
# as bytes type
# It will halt the main process until the launched process has finished
out, err = py_script.communicate()

print(type(out))
print(out)
print(err)

# Convert bytes into str
result = out.decode('utf-8')

print(result)
