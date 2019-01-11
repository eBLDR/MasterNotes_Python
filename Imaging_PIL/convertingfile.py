""" Easy way of changing imaging file format.
.png and .gif support transparency mask, but not .jpeg. """

from PIL import Image

"""
# normal conversion
im = Image.open('Lenna.jpeg')
im.save('Lenna2.png')
im.save('Lenna3.gif')
"""
# mode conversion
im2 = Image.open('saturn.png')
print(im2.mode)
# convert(@color_mode)
im3 = im2.convert('L')  # change to grey scale color mode
print(im3.mode)

# im3.save('saturn2.gif', 'GIF')
""" Converting to grey scale is the only way I've found to convert
.png to .gif and respect the transparent background. """
im3.save('saturn2.gif', transparency=0)  # save to .gif with transparent background
