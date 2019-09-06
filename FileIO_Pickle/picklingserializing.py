"""
The module pickle allows to store any plain Python object in a file and then
get it back later.
This is called storing the object persistently.
"""

import pickle

a7x = ('Nightmare',
       'A7X',
       '2011',
       ((1, 'Critical Acclaim'),
        (2, 'Welcome to the family'),
        (3, 'Buried Alive'),
        (4, 'Eternal Rest')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# 'wb' writing binary mode
with open('a7x.pickle', 'wb') as a7x_file:
    pickle.dump(a7x, a7x_file)  # .dump() for writing the file
    # @1 is the variable, @2 is the file where is going to be written
    pickle.dump(even, a7x_file, protocol=0)
    pickle.dump(odd, a7x_file, protocol=pickle.DEFAULT_PROTOCOL)  # is possible to set different protocols on each code
    pickle.dump(1224, a7x_file, protocol=pickle.HIGHEST_PROTOCOL)  # is also possible to write values in the spot

"""
PROTOCOLS 5 @ the moment of writing
PROTOCOL 0, first version, easiest human readable
PROTOCOL 1, improvement of 0
PROTOCOL 2, in version 2 of python, was declare insecure, so only load trusted data
PROTOCOL 3, is the default, in version 3 of python, data pickled using python 3.x cannot be unpickled using python version 2.x
PROTOCOL 4, came with python version 3.4
"""
# reading binary mode
with open('a7x.pickle', 'rb') as a7x_file:
    new_a7x = pickle.load(a7x_file)  # reads the file and stores it into a variable
    even_list = pickle.load(a7x_file)
    odd_list = pickle.load(a7x_file)
    x = pickle.load(a7x_file)

print(new_a7x)
print(even_list)
print(odd_list)
print(x)

# loads() method, different code has to be typed depending on the os used
# del for delete, followed by the name of the file
# very easy to delete a file using pickle, spywares use techniques like this
# pickle.loads(b"cos\nsystem\n(S'del a7x.pickle'\ntR.")  # for Windows
