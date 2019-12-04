"""
Shelve files work similar to a dictionary, most of the methods for dict will work on a shelve item
Important to notice, while dictionaries accept any kind of immutable variable as a key,
shelve will only accept a string.
Shelve files are also pickled (serialised)
When creating the file, will create several database files.
"""
import shelve

# Creating the file, no need to specify any mode
with shelve.open('shelf_test') as alphabet:
    alphabet['A'] = 'alpha'
    alphabet['B'] = 'beta'
    alphabet['C'] = 'charlie'
    alphabet['D'] = 'delta'
    alphabet['E'] = 'echo'
    print(alphabet['C'])

print(alphabet)
# print(alphabet['C'])  # will return an error
print('-' * 30)

# shelve is persistent to a file
with shelve.open('bike') as bike:
    bike['make'] = 'Honda'
    bike['model'] = '250 dream'
    bike['engineSize'] = 250
    # bike['enginSize'] = 249  # once is created it remains there

    for key in bike:
        print(key)
    # the solution is using del command to delete wrong keys
    # del bike['enginSize']
    print(bike['engineSize'])
    print(bike['enginSize'])

print('-' * 30)

# opening an existing file, also possible to use with statement
alphabet = shelve.open('shelf_test')
print(alphabet)
while True:
    letter = input('Enter a letter: ')
    letter = letter.upper()
    if letter == 'QUIT':
        break
    # method 1, .get() method
    radio = alphabet.get(letter)

    # method 2
    """
    if letter in alphabet:
        radio = alphabet[letter]
    else:
        print('None')
    """
    print(radio)

alphabet.close()
