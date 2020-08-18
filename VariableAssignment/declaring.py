# Declaring a new variable
v = 1  # v is the variable name

# Naming techniques
my_var = 0  # Snake case - name_of_this_technique
myVar = 0  # Camel case - nameOfThisTechnique

# Creating an object is much faster using literal syntax instead of using built-in function
a = set([1, 2, 3])  # Built-in function
a2 = {1, 2, 3}  # Literal syntax - also called "syntactic sugar"

# From Python 3.6+ variable annotations can be typed, this will show warnings
# var_name: type = value
name: str = 'BLDR'

# Multiple types can be specified
age: (int, None) = None

# Type list of int
# numbers: list[int] = []

# Variable declaration without initial value
empty: str

# From Python 3.8+, "walrus" notation can be used
# It will create new variable and assign the value to it
print(walrus := True)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)

"""
# Current usage
env_base = os.environ.get("PYTHONUSERBASE", None)
if env_base:
    return env_base

# Using "walrus"
if env_base := os.environ.get("PYTHONUSERBASE", None):
    return env_base
"""
