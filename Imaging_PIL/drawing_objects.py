"""
ImageDraw module has several methods for drawing shapes.
"""
from PIL import Image, ImageDraw

img = Image.new('RGBA', (200, 200), 'white')

# DRAWING SHAPES
# creating the Draw object, @ is the Image object
draw = ImageDraw.Draw(img)

# draws specific point - @ is a list with the coordinates tuples, @fill is the color
draw.point([(10, 10), (12, 12), (15, 15)], fill='black')

# draws a series of lines - connects the points passed as @ in a a list
draw.line([(5, 5), (194, 5), (194, 194), (5, 194), (5, 5)], fill='black', width=3)

# draws a rectangle - @((box_tuple), fill=filling_color, outline=outline_color)
draw.rectangle((20, 30, 60, 60), fill='blue')

# draws an ellipse - @((box_tuple_that_contains_the_ellipse), fill=filling_color, outline=outline_color)
draw.ellipse((120, 30, 160, 60), fill='red')

# draws an arbitrary polygon - @(list_of_connecting_points_of_polygon_sides, fill=...)
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='orange')

# cool line grip
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

# DRAWING TEXT
# @(top_left_corner_tuple, 'text', fill=font_color)
draw.text((20, 150), 'I am a TEXT!', fill='purple')

# to use a different font style
"""
import os
from PIL import ImageFont

fontsFolder = '/usr/share/fonts/truetype'  # in Linux
# in Windows is C:\Windows\Fonts

# truetype(@path_of_font_file, @size_of_font)
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

draw.text((100, 150), 'Cool Arial', fill='gray', font=arialFont)
"""

img.save('drawingshapes.png')
img.show()
