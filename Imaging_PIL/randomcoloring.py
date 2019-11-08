from random import randint

from PIL import Image


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


W = 800
H = 600

# creating the image file - @mode, @size
image = Image.new('RGB', (W, H))

for i in range(W):
    for j in range(H):
        # putpixel() method places at (x, y) position the color value
        image.putpixel((i, j), random_color())

# saving image
image.save('randomcoloring.jpeg', 'jpeg')

print(image)
print(type(image))

# to show the image after creation
image.show()
