t = ('a', 'b', 'c')  # Declaring a tuple
t_2 = 'a', 'b', 'c'  # Packing a tuple, enclosing brackets are optional

print(t == t_2)

test = ('abc')
print(type(test))  # type str

test2 = ('abc',)  # For creating a tuple with only one item
test3 = tuple('abc')  # or using the tuple function
print(type(test2))  # type tuple
print(type(test3))

# tuples can't be changed, immutable
# t[0] = 'Random' will give an error

# tuples can be multiplied
test2b = test2 * 2
print(test2b)

# and added
test2c = test2 + ('de',)
print(test2c)

# tuples can be nested
nested_tuple = ((0, 1), (10, 11), (100, 111))
print(nested_tuple)
print(nested_tuple[0], nested_tuple[1][1])

print('=' * 20)

metallica = 'Master', 'Metallica', 1984  # Can contain items of different types
imelda = 'Mayhem', 'Emilda May', 2011
print(metallica)
print(metallica[0])

print(imelda)
print(id(imelda))
imelda = imelda[0], 'Imelda May', imelda[2]  # We're reassigning the values by creating a new list with same name
print(imelda)
print(type(imelda))
print(id(imelda))

# Unpacking the tuple, number of items in tuple have to match with numbers of variables
title, artist, year = metallica
print(title)
print(artist)
print(year)

# *tuple also unpacks the tuple
print(*metallica)

print('=' * 20)

a7x = 'Nightmare', 'Avenged Sevenfold', 2011, [
    (1, 'Nightmare'), (2, 'Critical Acclaim'), (3, 'Buried Alive')
]

# It is possible to change a list inside a tuple
a7x[3].append((4, 'Second Heartbeat'))

title, artist, year, tracks = a7x
tracks.append((5, 'Unholy confessions'))
print(title, artist, year)
print(type(tracks))  # tracks is a list inside a tuple
for song in tracks:
    track, title = song
    print('\tTrack #{}, Title: {}'.format(track, title))

# tuples only hold 2 methods
print(test3.count('b'))
print(test3.index('a'))
