"""
Easy way of changing imaging file format.
.png and .gif support transparency mask, but not .jpeg.
"""
from PIL import Image

filename = 'BASIC_BG.png'
filename_no_extension = filename.split('.')[0]

"""
# normal conversion
im = Image.open(filename)
im.save('{}2.png'.format(filename_no_extension))
im.save('{}3.gif'.format(filename_no_extension))
"""
# mode conversion
im2 = Image.open(filename)
print(im2.mode)
# convert(@color_mode)
im3 = im2.convert('L')  # change to grey scale color mode
print(im3.mode)

# im3.save('{}2.gif'.format(filename_no_extension), 'GIF')
""" Converting to grey scale is the only way I've found to convert
.png to .gif and respect the transparent background. """
im3.save('{}2.gif'.format(filename_no_extension), transparency=0)  # save to .gif with transparent background
