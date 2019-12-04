"""
pdb - Python DeBugger module
Simple debugger included in the standard library.

pdb can also be invoked as a script:
python3 -m pdb <script.py>

Python version 3.7+ can use the breakpoint() built-in function instead of
import pdb; pdf.set_trace()

Both are equivalent, since breakpoint() is actually calling the import pdb and pdb.set_trace()

We can set the environment variable PYTHONBREAKPOINT=0 to disable breakpoint() calls, thus disabling debugging.
"""


def func(x):
    return x + 1


test = True
filename = __file__

# Next call will enter the debugger in following line - equivalent to breakpoint()
import pdb

pdb.set_trace()

print('filename is: {}'.format(filename))

y = func(4)
print('y is: {}'.format(y))
