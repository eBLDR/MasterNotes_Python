# formatting operators - old method for Python 2 - still works in python +3
# %d - integer
# %s - string
# %f - float
age = 24

print('My age is %d years' % age)
print('My age is %d %s, %d months' % (age, 'years', 6))

for i in range(1, 12):
    print('No. %2d squared is %3d and cubed is %4d' % (i, i ** 2, i ** 3))

print('Pi is approximately %.10f' % (22 / 7))
