import os
import fnmatch


def find_extension(root, extension):
    for path, directories, files in os.walk(root):
        for file in fnmatch.filter(files, "*.{}".format(extension)):
            # to find the absolute path
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


for f in find_extension('music', 'emp3'):
    print(f)
