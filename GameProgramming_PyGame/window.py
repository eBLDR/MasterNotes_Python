import pygame
import sys
from pygame.locals import *

pygame.init()  # at the start of the program
DISPLAY_SURF = pygame.display.set_mode((400, 300))      # size window
pygame.display.set_caption("My First Pygame Window!")   # title window

while True:  # main loop
    # pygame.event.get() adds events to a list, any event is an object, and it can be callable with
    # pygame.event.Event. If no events happened since last loop, it will return a blank list
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
