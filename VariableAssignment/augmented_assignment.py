# Augmented assignments
# Numbers - int or float
x = 11.1
print(x)

x += 1  # Equivalent to x = x + n
print(x)

x -= 4  # Equivalent to x = x - n
print(x)

x *= 2  # Equivalent to x = x * n
print(x)

x /= 4  # Equivalent to x = x / n
print(x)

x **= 3  # Equivalent to x = x ** n
print(x)

x %= 8  # Equivalent to x = x % n
print(x)

x //= 4  # Equivalent to x = x // n
print(x)

# Strings - str
word = 'kin'
word += 'g'
print(word)

word *= 5
print(word)

# Lists - list
my_list = [0]
print(my_list)

my_list += [9]
print(my_list)

my_list *= 2
print(my_list)

# example
number = '9,605,957,368,788,848,801'
cleaned_number = ''

# for i in range(0, len(number)):
for i in number:
    # if number[i] in '0123456789':
    if i in '0123456789':
        # cleaned_number += number[i]
        cleaned_number += i  # += is the augmented assignment

new_number = int(cleaned_number)
print('The number is {}'.format(new_number))
