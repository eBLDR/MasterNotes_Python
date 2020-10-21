# Declaring a new variable
v = 1  # v is the variable name

# Naming techniques
my_var = 0  # Snake case - name_of_this_technique
myVar = 0  # Camel case - nameOfThisTechnique

"""
Variables' names cannot:
    - Start with number.
    - Be just a number.
    - Contain special characters (except for `_`).
    - Replace special keywords (def, for, while...)
"""

# Creating an object is much faster using literal syntax instead of using built-in function
a = set([1, 2, 3])  # Built-in function
a2 = {1, 2, 3}  # Literal syntax - also called "syntactic sugar"

print(type(a) == type(a2))

print('=' * 20)

# From Python 3.8+, "walrus" notation can be used
# It will create new variable and assign the value to it
print(walrus := False)
print(walrus)

print('=' * 20)

# Standard no "walrus" usage
import os

env_base = os.environ.get("HOME", None)
if env_base:
    print(env_base)

# Using "walrus"
if env_base := os.environ.get("HOME", None):
    print(env_base)

print('=' * 20)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
