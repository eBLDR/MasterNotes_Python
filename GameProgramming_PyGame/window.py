"""
Top left corner of the screen is (0, 0) coordinate,
bottom right corner is (width, height)
"""

import pygame

# Initialising pygame
pygame.init()

# window's size (@width, @height)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Pygame Window!')  # window's title

run = True

# Main loop
while run:
    # Delaying the game the given amount of @milliseconds
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Drawing a rectangle - (@window_obj, @RGB_tuple, @rect_tuple)
    # @rect_tuple = (@x_coordinate, @y_coordinate, @width, @height)
    # coordinates of rectangle's top left corner
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # Fills the screen with color (@RGB_tuple)
    # screen.fill((0, 0, 0))

    # Updating the screen
    pygame.display.update()

# Closing the game
pygame.quit()
