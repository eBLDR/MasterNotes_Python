"""
reduce() was dropped from Python 2 when migrating to Python 3.
It is now found in the functools module.
map() and filter() were also considered to be dropped,
but they finally remained.

The reason:
All lists returned by map() and filter() can be also created using list comprehension.
"""
# map() - map() is in alternative to list comprehensions, being comprehensions faster
text = 'what have the romans ever done for us'

words = [word.upper() for word in text.split(' ')]
print(words)

# Equivalence using map()
# map(@function, @iterable) - applies the @function to all the items in the @iterable
map_words = map(str.upper, text.split(' '))  # Returns a map object, it's an iterable
print(type(map_words))

map_words = list(map_words)
print(map_words)

print(words == map_words)

print('#' * 30)

# filter() - it can also be replaced by comprehensions, and comprehensions is way faster
menu = [
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon'],
    ['egg', 'spam'],
    ['egg']
]

meals = [meal for meal in menu if 'spam' not in meal]
print(meals)


def not_spam(meal_list):
    return 'spam' not in meal_list


# Equivalence using filter()
# filter(@function, @iterable) - applies @function to all the items in @iterable
# filter() applies a bool() over the return value of @function - so @function must return a boolean to be useful
# if the result is True, it's added to the filter list, discarded otherwise
meals_filter = filter(not_spam, menu)  # Returns a filter object, it's an iterable
print(type(meals_filter))

meals_filter = list(meals_filter)
print(meals_filter)

print(meals == meals_filter)

print('#' * 30)

# reduce()
from functools import reduce


def calc(x, y):
    return x + y


numbers = [2, 3, 5, 8, 13]

# reduce(@function, @sequence) - continually applies the function to the sequence,
# it returns a single value - i.e.: if list has 4 items: func(func(func(i1, i2), i3), i4)
reduced_value = reduce(calc, numbers)
print(reduced_value)
