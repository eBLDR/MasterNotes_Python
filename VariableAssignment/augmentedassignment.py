my_var = 0  # snake case is the name_of_this_technique
myVar = 0  # camel case is the nameOfThisTechnique

# int or float
x = 11.1
print(x)

x += 1
print(x)

x -= 4
print(x)

x *= 2
print(x)

x /= 4
print(x)

x **= 3
print(x)

x %= 8
print(x)

# str
word = 'kin'
word += 'g'
print(word)

word *= 5
print(word)

# list
my_list = [0]
print(my_list)

my_list += [9]
print(my_list)

my_list *= 2
print(my_list)

# example
number = '9,605,957,368,788,848,801'
cleanedNumber = ''  # camel case is the nameOfThisTechnique

# for i in range(0, len(number)):
for i in number:
    # if number[i] in '0123456789':
    if i in '0123456789':
        # cleanedNumber += number[i]
        cleanedNumber += i  # += is the augmented assignment

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
