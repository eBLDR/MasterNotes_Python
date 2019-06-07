"""
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

# Creates an image surface object
cat_img = pygame.image.load('catanimation_src/cat.png')

# Retrieving the rectangle object of a surface
# If @center is specified, it will set the center of the surface to
# specified position
img_rect = cat_img.get_rect(center=(200, 150))

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

    if random.random() > 0.9:
        cat_img_rotated = pygame.transform.rotate(cat_img, random.randint(1, 360))

    # Paste the surface object to main surface
    # (@surface, @position_tuple)
    screen.blit(text, (120, 300))

    # Rectangle object can also be used as a position
    screen.blit(cat_img_rotated, img_rect)

    pygame.display.update()

pygame.quit()
