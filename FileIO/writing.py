cities = ['BCN', 'TGN', 'Reus', 'Girona', 'Lleida']

# 'w' mode for writing
with open('writing_cities.txt', 'w') as city_file:  # The file will be overwritten if already exists
    for city in cities:
        print(city, file=city_file)  # This is the actual writing, is printing in the file
        # is equivalent to
        city_file.write(city + '\n')

new_cities = []
with open('writing_cities.txt', 'r') as city_file:
    for city in city_file:
        new_cities.append(city.strip('\n'))  # .strip(char) deletes the char from and
        # only from the beginning or the end of the string, and can be partially
        # i.e.: 'adelaide'.strip('del') = 'adelai'
print(new_cities)

# Using the eval() function to recover the original variable type
a7x = 'Nightmare', 'A7X', '2011', (  # a tuple
    (1, 'Critical Acclaim'), (2, 'Welcome to the family'))

# Writing a tuple to a .txt
with open('writing_a7x.txt', 'w') as a7x_file:
    print(a7x, file=a7x_file)

# Reading a .txt, returns a str
with open('writing_a7x.txt', 'r') as a7x_file:
    contents = a7x_file.readline().strip('\n')

print(contents)
print(type(contents))  # str
# eval() evaluates the string and asses which variable was originally formatted
new_a7x = eval(contents)
print(new_a7x)
print(type(new_a7x))  # tuple
title, artist, year, tracks = new_a7x
print(artist)
print(tracks[0][1])
