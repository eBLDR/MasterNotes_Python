"""
Surfaces and Rects and the basic building blocks in PyGame.
All font / image objects are surfaces.
Each surface has a rectangle, which represents the space occupied by that
surface. It can be retrieved using get_rect() method.
By default, position is taken from top left corner of that rectangle.
"""
import random

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Surfaces')

# Create basic surface - @rectangle
my_surface = pygame.Surface((75, 25))

# Changes surface color - @rgb_color
my_surface.fill((255, 180, 180))

# Surface information
print('Surface size:', my_surface.get_size())

# Retrieving the rectangle object of a surface
# If @center is specified, it will set the center of the surface to
# specified position - default is @topleft
my_rectangle = my_surface.get_rect(center=(50, 50))
print('Surface rectangle is:', my_rectangle)
print(my_rectangle.top, my_rectangle.bottom,
      my_rectangle.left, my_rectangle.right)

# Creates an image surface object
cat_img = pygame.image.load('src/cat.png')

# .convert_alpha() method can be used to change the pixel format of an image
# including per pixel alphas

cat_rectangle = cat_img.get_rect(center=(200, 150))

# Rotates the image
cat_img_rotated = pygame.transform.rotate(cat_img, 180)

# Creating font object
font = pygame.font.Font('freesansbold.ttf', 24)

# Creating font surface - (@text, @anti-aliasing, @font color, @background color)
text = font.render('Spinning Cat', True, (255, 0, 0))  # , (255, 255, 255)))

run = True

while run:
    pygame.time.delay(100)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if random.random() > 0.8:
        cat_img_rotated = pygame.transform.rotate(cat_img, random.randint(1, 360))

    # Paste the surface object to another surface
    # (@surface, @position_tuple)
    screen.blit(my_surface, (50, 50))

    screen.blit(text, (120, 300))

    # Rectangle object can also be used as a "blitting" position
    screen.blit(cat_img_rotated, cat_rectangle)

    pygame.display.update()

pygame.quit()
