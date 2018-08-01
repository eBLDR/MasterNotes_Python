import pygame
import sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAY_SURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

# set up the colors - RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY_SURF.fill(WHITE) # fill screen with color
pygame.draw.polygon(DISPLAY_SURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAY_SURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.circle(DISPLAY_SURF, RED, (300, 50), 25, 0)
pygame.draw.ellipse(DISPLAY_SURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAY_SURF, BLUE, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAY_SURF) # this locks the surface while drawing pixels
pixObj[480][380] = BLACK # get_lock() will return True if it's locked
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
del pixObj # this unlocks the surface

# run the loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
