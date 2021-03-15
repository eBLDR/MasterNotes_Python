"""
Ellipsis notation is tripe consecutive dots: `...`
"""
e = ...

print(e)
print(type(e))


def todo():
    # Used as a placeholder
    ...


todo()

# Notation to represent circular references
x = [0, 1]
x[0] = x
print(x)
