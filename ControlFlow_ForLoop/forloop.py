# The for loop on each iteration is actually calling the next() function in the iterable object.

for i in range(1, 11):
    print('i is now {:2}'.format(i))

number = '123,456,789'
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

for char in number:
    if char in '0123456789':
        print(char)

for state in ['monster', 'monkey']:
    print('You are a ' + state)

for i in range(0, 30, 5):
    print('i is {}'.format(i))

for i in range(1, 6):
    for j in range(1, 6):
        print('{1} times {0} is {2:2}'.format(i, j, i * j))
    print('===========')

print('=' * 30)

# multiple assignments
dots = [(0, 1, 0), (3, 6, 1), (4, 2, 0)]
for x, y, z in dots:
    print(x, y, z)

print('=' * 30)

X = list(range(1, 11))
Y = list(range(10, 101, 10))
# print(len(X), len(Y))

if len(X) == len(Y):
    for x, y in zip(X, Y):  # zip() method to match two iterable objects, there is no need to have the same number
        # of items, whichever finishes first, will stop the for loop
        print('{} x {} = {}'.format(x, y, x * y))

print('=' * 30)

# unpacking tuples
T = ((0, 1), (5, -1), (6, -2), (1, 1))
for (x, y) in T:
    print(x, y)

print('=' * 30)

for i in range(5):
    letter = input('{} - Give a letter: '.format(i)).lower()
    if letter:  # to check if letter is not NoneType
        if letter in 'aeiou':
            print('I hate vowels!')
            break
        elif letter in 'bcdfghjklmnpqrstvwxyz':
            print('I love consonants!')
        else:
            print('I ignore everything but not single letters')
            continue  # continue will move the iterator to the next value immediately
    else:
        print('You input nothing!')
    # continue is executed here at the background

else:  # else is executed when the for loop is finished normally, not because of a break
    print('Finish successfully')  # also if the for was never started
