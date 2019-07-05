import os
import fnmatch  # Unix filename pattern matching - a module for matching names


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        # print('directories are: {}'.format(directories))
        # for artist in directories:

        # fnmatch(names, pattern) - return the subset of the list of names that match pattern
        # Using fnmatch to filter results
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            # print('subdir is: {}'.format(subdir))
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        # os.listdir will show all the files/directories in the directory
        for song in os.listdir(album[0]):  # [0] for the path
            yield song


album_list = find_albums('music', 'Aerosmith')
song_list = find_songs(album_list)  # passing a generator as an argument to another generator

for a in album_list:
    print(a)

for s in song_list:
    print(s)

# a simple example of fnmatch.filter()
lis = ['ZAS', 'B', 'zAX', 'hA', 'C']

for i in fnmatch.filter(lis, '*A*'):  # * is a wildcard
    print(i)
