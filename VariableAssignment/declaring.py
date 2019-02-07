# Declaring a new variable
v = 1  # v is the variable name

# Naming techniques
my_var = 0  # Snake case - name_of_this_technique
myVar = 0  # Camel case - nameOfThisTechnique

# Creating an object is much faster using literal syntax instead of using built-in function
a = set([1, 2, 3])  # Built-in function
a = {1, 2, 3}  # Literal syntax - also called "syntactic sugar"

# From Python 3.6+ variable annotations can be typed
# var_name: type = value
name: str = 'BLDR'

# Type list of int
numbers: list[int] = []

# Variable declaration without initial value
empty: str
