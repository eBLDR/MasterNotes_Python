a = 3
li = [1, 5]
li2 = li  # shallow copy
dc = {'C': 0}
s = 'string'

# type() - returns the class type of the object
print(type(a))
print(type(li))

# id() - shows the object's id - memory location
print(id(dc), id(li), id(li2))

# is equivalent to using the 'is' keyword, both refer to the memory location of an object
print(a is 3, a is li, li is li2)

# repr() - return a string containing a printable representation of an object
print(repr(dc))

# help() - prints out the help of the object's class
help(str)  # Help for data type
help(s.upper)  # equivalent to help(str.upper)

# dir() - return the list of names in the current local scope. With an object as argument,
# return a list of valid attributes for that object
print(dir(s))

# globals() - return a dictionary representing the current global symbol table
print(globals())

# locals() - update and return a dictionary representing the current local symbol table
print(locals())

# hash() - return the hash value of the object (if it has one)
print(hash(a))
