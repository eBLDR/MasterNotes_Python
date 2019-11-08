import os

root = 'music'

# os.walk() is a generator, yields a tuple that contains a str (path) and 2 lists (directories and files)
for path, directories, files in os.walk(root, topdown=True):
    print('path is: {}'.format(path))
    # to split directories/files name from path
    t = path.count('/')

    for i in range(t):
        split = os.path.split(path)
        print(split)
        path = split[0]

    print('directories: {}'.format(directories))
    print('files: {}'.format(files))
    input()

    for f in files:
        print('\t{}'.format(f))
