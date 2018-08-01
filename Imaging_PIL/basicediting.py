"""
Pillow module for image editing.
Pillow creates PNG images that are 72 pixels per inch by default,
a point is 1/72 of an inch.
"""
from PIL import Image
# module that contains a list of equivalences string color name (i.e.: 'red') to RGBA values
from PIL import ImageColor

# create a new image object - new(@color_mode, @(width, height), @background_color)
# if bg color isn't specified, will be invisible black (0, 0, 0, 0)(transparent) by default
myImg2 = Image.new('RGBA', (100, 200))

# saving image - save(@filename, @format) - if format isn't specified, will take the extension from @filename
myImg2.save('transparentImage.png', 'PNG')  # transparency=0 can be used when dealing with .gif files

# to see the RGBA values of a string name color
print(ImageColor.getcolor('chocolate', 'RGBA'))


# to open a image - open(path)
myImg = Image.open('Lenna.jpeg')

# data attributes
print('Size is: {}'.format(myImg.size))         # get size - (width, height)
print('Name is: {}'.format(myImg.filename))     # get filename
print('Format is: {}'.format(myImg.format))     # get file's extension
print(myImg.format_description)                 # get expanded file's extension
print('Color mode is: {}'.format(myImg.mode))   # get color mode

print('=' * 20)

# image editing - original image object is left untouched, all editing tools (if applies) return a new object
# @boxed_tuple = begin_X, begin_Y, end_X, end_Y - includes begin pixel but not end pixel
myImgCropped = myImg.crop((220, 220, 360, 360))

myImgCropped.show()  # displays the image using default image app
print('Cropped image size is {}'.format(myImgCropped.size))

# create a copy of the image object
myImgCopy = myImg.copy()

# to paste and image onto another one
# image_where_to_paste.paste(@img_to_be_pasted, @top_left_corner_position, @mask)
# mask arg is optional, if the img has transparent pixels, pass the image again in the place of @mask
myImgCopy.paste(myImgCropped, (10, 10))

# cool tiled image
baseWidth, baseHeight = myImg.size
tileWidth, tileHeight = myImgCropped.size

for left in range(0, baseWidth, tileWidth):
    for top in range(0, baseHeight, tileHeight):
        print(left, top)
        myImgCopy.paste(myImgCropped, (left, top))

myImgCopy.save('tiled.png')

# resize(@(width, height)) - to resize an image
myImgQuarterSized = myImg.resize((int(baseWidth / 2), int(baseHeight / 2)))
myImgQuarterSized.save('quartersized.png')

# rotate(@degrees, expand=False) - rotates the image counterclockwise by @degrees
# if expand=False (default) size will be respected, if expand=True image will be expanded to fit the rotation
myImg.rotate(12, expand=True).save('rotated12.png')

# mirror flip - transpose(@) - @ must be either Image.FLIP_LEFT_RIGHT (horizontal flip)
# or Image.FLIP_TOP_BOTTOM (vertical flip)
myImg.transpose(Image.FLIP_LEFT_RIGHT).save('horizontalflip.png')

# changing individual pixels
width = 100
height = 100
myImg3 = Image.new('RGBA', (width, height))

# getpixel(@(x, y)) - returns the RGBA tuple of the color of that specific pixel
print(myImg3.getpixel((0, 0)))

# putpixel(@(x, y), @RGB_or_RGBA_color_tuple)
for x in range(width):
    for y in range(int(height / 2)):
        # if alpha is not specified, will take default value of 255 (maximum opacity)
        myImg3.putpixel((x, y), (210, 210, 210))

    for y in range(int(height / 2), height):
        myImg3.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

print('Pixel (0, 0) has color {}'.format(myImg3.getpixel((0, 0))))
print('Pixel (0, 50) has color {}'.format(myImg3.getpixel((0, 50))))

myImg3.save('putpixel.png')
