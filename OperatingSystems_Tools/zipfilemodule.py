# zipfile module - creates, reads and unzips folders
import zipfile
import os

os.chdir('Lab')

# create a zip file - works similar to open()
new_zip = zipfile.ZipFile('./poems.zip', 'w')  # in write (w) mode to overwrite/create the file
# append (a) mode to add content to the zip file

# adding/overwriting content to the zip file
new_zip.write('poem.txt', compress_type=zipfile.ZIP_DEFLATED)
# ZIP_DEFLATED is a compressing algorithm that works well on all types of data, is the one by default

new_zip.write('poem2.txt')

new_zip.write('SUBFOLDER')  # is also possible to add sub folder

new_zip.close()  # need to be closed

# reading a zip file
with zipfile.ZipFile('poems.zip') as read_zip:  # with method to open also works, like a normal file
    print(read_zip.namelist())  # show a list of dir/files inside the zip
    info = read_zip.getinfo('poem.txt')  # to get info of a specific file
    file_size = info.file_size
    compressed_size = info.compress_size
    print('File size: {}B\nCompressed size: {}B'.format(file_size, compressed_size))
    print('Compressed is {}x smaller!'.format(round(file_size / compressed_size, 2)))

# extracting a zip file
with zipfile.ZipFile('poems.zip') as extract_zip:
    extract_zip.extractall('./poems/')  # this will extract all the file in the zip
    # in the (argument) folder, will create it if it doesn't exist

    # to extract a single file
    # extract_zip.extract('path/filename.ext', 'destination_folder')
