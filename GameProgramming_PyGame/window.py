"""
Top left corner of the screen is (0, 0) coordinate,
bottom right corner is (width, height)
"""
import pygame

# Initialising pygame
pygame.init()

# Window's size ((@width, @height), @flags=0, depth=0)
screen = pygame.display.set_mode((500, 500))  # , flags=pygame.FULLSCREEN)
# Fullscreen - use flag for full screen

# Window's title
pygame.display.set_caption('My First Pygame Window!')

# Window's icon
# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)

run = True

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Drawing a rectangle - (@window_obj, @RGB_tuple, @rect_tuple)
    # @rect_tuple = (@x_coordinate, @y_coordinate, @width, @height)
    # coordinates of rectangle's top left corner
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # Fills the screen with color (@RGB_tuple)
    # screen.fill((0, 0, 0))

    # Updating the screen - @rectangle can be passed, it allows to only update
    # a portion of the screen
    pygame.display.update()

# Closing the game
pygame.quit()
