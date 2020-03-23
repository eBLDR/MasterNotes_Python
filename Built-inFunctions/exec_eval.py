# eval() evaluates a expression, expression must be str
# when testing function, we can specify the namespaces
# eval(expression, globals=None, locals=None)

x = 3
y = 5

print(eval('x + y'))

# exec() supports dynamic execution of Python code
# argument must be str

z = 0
exec('z = 10')
print(z)

# Useful to create a set of variables with numbered names
list_of_var = []
for i in range(5):
    exec('var{0} = {0}'.format(i))
    exec('list_of_var.append(var{})'.format(i))

print(list_of_var)
print(var4)  # despite the warning, var4 exists
