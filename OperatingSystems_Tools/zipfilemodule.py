# zipfile module - creates, reads and unzips folders

import zipfile
import os

os.chdir('Lab')

# create a zip file - works similar to open()
newZip = zipfile.ZipFile('./poems.zip', 'w')  # in write (w) mode to overwrite/create the file
# append (a) mode to add content to the zip file

# adding/overwriting content to the zip file
newZip.write('poem.txt', compress_type=zipfile.ZIP_DEFLATED)
# ZIP_DEFLATED is a compressing algorithm that works well on all types of data, is the one by default

newZip.write('poem2.txt')

newZip.write('SUBFOLDER')  # is also possible to add sub folder

newZip.close()  # need to be closed

# reading a zip file
with zipfile.ZipFile('poems.zip') as readZip:  # with method to open also works, like a normal file
    print(readZip.namelist())  # show a list of dir/files inside the zip
    info = readZip.getinfo('poem.txt')  # to get info of a specific file
    fileSize = info.file_size
    compressedSize = info.compress_size
    print("File size: {}B\nCompressed size: {}B".format(fileSize, compressedSize))
    print("Compressed is {}x smaller!".format(round(fileSize / compressedSize, 2)))

# extracting a zip file
with zipfile.ZipFile('poems.zip') as extractZip:
    extractZip.extractall('./poems/')  # this will extract all the file in the zip
    # in the (argument) folder, will create it if it doesn't exist

    # to extract a single file
    # extractZip.extract('path/filename.ext', 'destination_folder')
