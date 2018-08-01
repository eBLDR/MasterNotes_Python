# generating ranges

my_R = range(10)
print(my_R)
print(type(my_R))

# right use of ranges does not turn them into lists - waste of memory
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

decimals = range(0, 100)
print(type(decimals))
my_range = decimals[3:40:3]  # slicing ranges
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)
print(my_range == range(3, 40, 3))

print(range(0, 5, 2) == range(0, 6, 2))  # will return True
print(range(0, 100)[::-2] == range(99, 0, -2))  # slicing a range

o = range(0, 100, 4)
p = o[::5]  # 4*5 is what is happening
print(p)
for i in p:
    print(i)

print('=' * 40)
for i in p[::-1]:  # to reverse use a -1 slicing
    print(i)
