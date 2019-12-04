"""
Creates a matrix which contains the grey-scale values of the pixels
of an image and saves it into .csv file.
"""
import csv

from PIL import Image


def save_array(name, array):
    # writes a .csv file given an array
    path = '{}.csv'.format(name)
    with open(path, 'w') as ex:
        writer = csv.writer(ex, delimiter=';')
        for w in range(len(array)):
            writer.writerow(array[w])


img = Image.open('Lenna.jpg')

pixels = img.load()  # this is not a list, nor is it list'able
width, height = img.size
print(type(pixels))

all_pixels = []

for y in range(height):
    row = []
    for x in range(width):
        c_pixel = pixels[x, y]
        row.append(c_pixel)
    all_pixels.append(row)

# some data control
print(all_pixels[0][0], ',', all_pixels[511][511])
print(len(all_pixels))

# saving the array
save_array('array_from_img', all_pixels)
