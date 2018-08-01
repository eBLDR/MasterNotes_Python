cities = ['BCN', 'TGN', 'Reus', 'Girona', 'Lleida']

# 'w' mode for writing
with open('cities.txt', 'w') as cityFile:  # the file will be overwritten if already exists
    for city in cities:
        print(city, file=cityFile)  # this is the actual writing, is printing in the file
        # is equivalent to
        cityFile.write(city + '\n')

newCities = []
with open('cities.txt', 'r') as cityFile:
    for city in cityFile:
        newCities.append(city.strip('\n'))  # .strip(char) deletes the char from and
        # only from the beginning or the end of the string, and can be partially
        # i.e.: 'adelaide'.strip('del') = 'adelai'
print(newCities)

# using the eval() function to recover the original variable type
a7x = 'Nightmare', 'A7X', '2011', (  # a tuple
    (1, 'Critical Acclaim'), (2, 'Welcome to the family'))

# writing a tuple to a .txt
with open('a7x.txt', 'w') as a7xFile:
    print(a7x, file=a7xFile)

# reading a .txt, returns a str
with open('a7x.txt', 'r') as a7xFile:
    contents = a7xFile.readline().strip('\n')

print(contents)
print(type(contents))  # str
# eval() evaluates the string and asses which variable was originally
newA7x = eval(contents)
print(newA7x)
print(type(newA7x))  # tuple
title, artist, year, tracks = newA7x
print(artist)
print(tracks[0][1])
