"""
Since .py file are just plain text, we can create more .py files
with write() methods in 'w' mode.
"""

cats = [{'name': 'Nanu', 'color': 'orange'},
        {'name': 'Otto', 'color': 'grey'}]

print(str(cats))

with open('generated_python_file.py', 'w') as catFile:
    catFile.write('cats = ' + str(cats) + '\n')

import generatedpyfile

pet_name = generatedpyfile.cats[0]['name']
print(pet_name)
