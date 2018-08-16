# functions that work with sequence/iterable type data (str, list, tuple, range...)

string_sample = 'I am a sample, yes'            # immutable
list_sample = ['A', 'ch', 12, True, 'X', 36]    # mutable
tuple_sample = 4, 12, 0, 100, 1                 # immutable
set_sample = {1, 5, 45, 55}                     # mutable, not indexed

# in keyword - membership - returns True or False to the question: is value-x in seq?
print(5 in tuple_sample)
print(1 in tuple_sample)
print('z' not in string_sample)

print('=' * 20)

# indexes
print(list_sample[1])       # index must be in range
print(tuple_sample[-1])     # negative indexes also work
print(string_sample[-5])

print('=' * 20)

# slicing technique - breaks the sequence into slice [start:stop:step]
print(string_sample[1:12])
print(list_sample[:5])
print(tuple_sample[1:300:2])  # the stop number can be out of index, will stop on last
print(string_sample[::3])

print(string_sample[::-1])  # backwards
print(tuple_sample[::-2])

print('=' * 20)

# multiple assignment
a, b, c, d, e, f = list_sample
print(c, e)
a, b, c, d, e = tuple_sample
print(d, a)
a, b, c, d, e, f, g, h, i, j, k, m, l, n, p, q, o, t = string_sample
print(k, i, o)

print('=' * 20)

# len() - tells the number of items in the seq
print("len is: {}".format(len(string_sample)))

print('=' * 20)

# min() & max ()
print(min(tuple_sample))  # returns the minimum value
print(max(tuple_sample))  # returns the maximum value

print('=' * 20)

# sum()
print(sum(tuple_sample))  # returns the sum of all the values

print('=' * 20)

# sorted(key=function, reverse=False) - returns a sorted list, cannot mix digits with alphabetical characters
# @key will sort by the value returned from passing the item to the function (i.e.: key=len will sort using len())
sor = sorted(tuple_sample, reverse=False)
print(sor)

print('=' * 20)

# reversed() - returns a reversed iterator of sequence
for i in reversed(tuple_sample):
    print(i)

print('=' * 20)

# count() - to count the number of times a certain object is found in a sequence
print(string_sample.count("a"))

print('=' * 20)

# index() - to find certain value - the first one found
index_char_e = string_sample.index('e')  # returns index of desired character/value
print(index_char_e)
print(list_sample.index(True))

print('=' * 20)

# any() & all()
# any(seq) return True if any of the value in the sequence is True, False otherwise
# it does OR between each item, e.g.: bool(seq[0]) or bool(seq[1]) or ... bool(seq[n])
print('any():', any(tuple_sample))

# all(seq) return True all the value in the sequence are True, False otherwise
# it does AND between each item, e.g.: bool(seq[0]) and bool(seq[1]) and ... bool(seq[n])
print('all():', all(tuple_sample))

print('=' * 20)

# join(seq) - for joining list/tuple into a string
str_from_list = "-|-".join(list_sample[:2])  # 'delimiter'.join(list/tuple) - sequence must be made of str
print(str_from_list)

print('=' * 20)

# split() - opposite to join, split method will split the string into a list of strings
split_string = string_sample.split()    # breaks every word, all feed characters (\t, ,\n...) are the default delimiters
print(split_string)                     # it's now a list made of strings
print(string_sample.split(","))         # breaks using a given character

print('=' * 20)

# zip(seq1, seq2) - returns a zip iterable object, it's a list containing pairs of tuples correspoding
# to the same indices of the two sequences, len is equal to the minimum len of both
zip_tuple = zip(string_sample, list_sample)
for i in zip_tuple:
    print(i)

print('=' * 20)

# enumerate(seq) - return an enumerate object, iterable, a tuple containing a count (from start which
# defaults to 0) and the values obtained from iterating over the sequence
for i,j in enumerate(list_sample, start=1):
    print(i, j)

# direct conversion to list/tuple/dict...
enum_tuple = tuple(enumerate(list_sample, start=1))
print(enum_tuple)
