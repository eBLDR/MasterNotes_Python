# zipfile module - creates, reads and unzips folders
import os
import zipfile

os.chdir('Lab')

# Create a zip file - works similar to open()
new_zip = zipfile.ZipFile('./poems.zip', 'w', compression=zipfile.ZIP_DEFLATED)
# write (w) mode to overwrite/create the file
# append (a) mode to add content to the zip file
# ZIP_DEFLATED is a compressing algorithm that works well on all types of data,
# is the one by default

# Adding/overwriting content to the zip file
# write(@filename, @arcname=archive_filename, @compress_type=None)
# @arcname is the destination path inside the archive,
# ff no @arcname is specified, it will take @filename value
new_zip.write('poem.txt')

new_zip.write('SUBFOLDER')  # Adding a sub folder

new_zip.write('poem2.txt', arcname='SUBFOLDER/poem2.txt')

new_zip.close()  # It needs to be closed

# Reading a zip file
with zipfile.ZipFile('poems.zip') as read_zip:
    print(read_zip.namelist())  # show a list of dir/files inside the zip

    info = read_zip.getinfo('poem.txt')  # to get info of a specific file
    file_size = info.file_size
    compressed_size = info.compress_size

    print('File size: {}B\nCompressed size: {}B'.format(
        file_size, compressed_size)
    )

    print('Compressed is {}x smaller!'.format(
        round(file_size / compressed_size, 2))
    )

# Extracting a zip file
with zipfile.ZipFile('poems.zip') as extract_zip:
    # this will extract all the file in the zip in the (argument) folder,
    # will create it if it doesn't exist
    extract_zip.extractall('./poems_extracted/')

    # to extract a single file
    # extract_zip.extract('path/filename.ext', 'destination_folder')
