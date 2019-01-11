string = '1234567890'

for char in string:
    print(char)

# equivalent to
for char in iter(string):  # iter function creates an iterator at the background
    print(char)

print('-----')

my_iterator = iter(string)
print(type(my_iterator))
print(next(my_iterator))  # values are consumed when used
print(next(my_iterator))

print('starting the for loop')

# for just calls the next() function on the iterator passed
for i in my_iterator:  # because the first two values are already consumed, this loop will start at the third (next)
    print(i)

print('-----')

my_list = ['A', 'B', 'C', 'D', 'E']
my_iterator_2 = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator_2)
    print(next_item)

# equivalent to
for i in my_list:
    print(i)
