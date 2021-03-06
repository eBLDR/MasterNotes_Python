"""
Top left corner of the screen is (0, 0) coordinate,
bottom right corner is (width, height)
"""
import pygame

# Initialising pygame
pygame.init()

# Window's size ((@width, @height), @flags=0, depth=0)
screen = pygame.display.set_mode((500, 500))  # , flags=pygame.FULLSCREEN)
# If @size is not passed, screen adjusts to monitor size (?)
# Fullscreen - use flag for full screen

# Screen rectangle
print('Size:', screen.get_size())
# get_width(), get_height() methods also available

print('Rectangle:', screen.get_rect())

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

    # Makes a copy of the current state of the screen, useful to set
    # background screen, to improve performance and avoiding redrawing it
    # screen_copy = screen.copy()

    # Updating the display - @rectangle can be passed, it allows to only update
    # a portion of the screen
    pygame.display.update()

# Closing the game
pygame.quit()
