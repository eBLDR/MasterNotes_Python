"""
A set cannot contain duplicates and it's unordered.
It's hashable, that means that it can contain immutable objects but not
mutable.
Items in set can be of a different type.
"""
farm_animals = {'sheep', 'cow', 'hen'}  # create a set
empty_set = set()  # empty_set = {} will create and empty dictionary

print(type(farm_animals))

# sets are unordered and the can't contain duplicates
print(farm_animals)
# if we wish to print it sorted, notice that sorted ill return a list!
print(sorted(farm_animals))

for i in farm_animals:
    print(i)

sample_text = 'Python is as powerful as a giant python'
# will return a set out of a string, char by char, with no duplicates
print(set(sample_text))

# creating a set out of a list, a tuple will work also
wild_animals = set(['lion', 'tiger', 'panther'])

even = set(range(0, 30, 2))  # creating a set out of a range

squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)

print('-' * 30)

print(len(even), len(squares))

# - operations -
# union between 2 sets - a|b, items in either a or b - returns a new set - |
print('union')
print(even.union(squares))  # adding them both without repeated numbers
print(even | squares)  # equivalent operator
print(len(even.union(squares)))

# intersection between 2 sets - a&b, items in both a and b - returns a
# new set - &
print('intersection')
print(even.intersection(squares))  # numbers that are present in both sets
print(even & squares)  # equivalent operator

# difference between 2 sets - a-b, items in a but not in b - returns a
# new set - -
print('difference')
print('even minus squares')
print(sorted(even.difference(squares)))
print(sorted(even - squares))  # equivalent operator

print('squares minus even')
print(squares.difference(even))

# symmetric difference - a^b, items in a or b but not in both - returns a
# new set - ^
print('symmetric difference, returns the opposite of the intersection set')
print(sorted(even.symmetric_difference(squares)))
print(sorted(even ^ squares))  # equivalent operator

"""
print('difference_update() method')
# it does not return a new set, it modifies the current one
squares.difference_update(even)

print(squares)

intersection_update and symmetric_difference_update also exists
"""

print('-' * 30)

# subset and superset
if squares.issubset(even):  # all squares' items are found inside even
    print('squares is a subset of even')
# equivalent to if squares <= even

if even.issuperset(squares):  # even has all the items found in squares
    print('even is a superset of squares')
# equivalent to if even >= squares

# frozen set, immutable, they have no update methods (.add(), .discard()...)
odd = frozenset(range(1, 20, 2))
print(odd)
