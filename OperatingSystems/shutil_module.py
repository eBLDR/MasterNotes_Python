"""
shutil module - shell utilities
for copying and moving/renaming stuff and complex deleting
to create/delete/rename simple dir/files see os module
"""
import os
import shutil

os.chdir('./CommandTest')

# copy(source, destination) - to copy a SINGLE file
shutil.copy('./magic.txt', './01/moremagic.txt')
# if we don't specify the name, the file will be copied with the same name:
# shutil.copy('./magic.txt', './01')

# copytree(source, destination) - copies the entire folder with all the
# folders and files in it
try:
    shutil.copytree('./01', './01Copy')
except FileExistsError:
    pass

# move(source, destination) - to move files or folders
try:
    shutil.move('./01/A', './02')
except FileNotFoundError:
    pass

# to move a folder shutil.move('./file.txt', './newDir/')
# CAUTION: if newDir doesn't exist, file.txt will be renamed to newDir and
# extension will be lost
# CAUTION2: path must exist, is not going to be created
# move() can also be used just for renaming the file:
# shutil.move('./hello.txt', './renamedhello.txt')

# rmtree() - permanently removes the folder with all the folders/files in it
shutil.rmtree('./01Copy')
