"""
Creates an image from a .csv file that contains grey-scale values (integers from 0 to 255).
"""

from PIL import Image, ImageDraw
import csv


def gen_array(file_name):
    # generates an array given a .csv file
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for r in reader:
            row = []
            for pixel in r:
                row.append(int(pixel))  # value must be an integer

            data.append(row)

    return data


array_img = gen_array('IMG_Lenna.csv')

W = len(array_img[0])
H = len(array_img)

image = Image.new('L', (W, H))

for y in range(len(array_img)):
    for x in range(len(array_img[y])):
        image.putpixel((x, y), array_img[y][x])

image.save('imgfromarray.jpeg', 'JPEG')

print(image)

image.show()
