# Written in same format as list-set comprehension, but using () instead
# increases performance a lot, if we are not interested in reusing the list.
my_gen = ((i, i * j) for j in range(5) for i in range(3))
print(my_gen)
print(type(my_gen))

for v in range(10):
    print(next(my_gen))

print('=' * 20)

# Very useful with sum(), min() and max() functions
my_sum = sum(x * x for x in range(10))
print(my_sum)
