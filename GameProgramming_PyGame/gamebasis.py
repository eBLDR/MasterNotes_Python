# Created and developed by
# BLDR, 2015

import pygame
import sys
from pygame.locals import *

pygame.init()

# --- CONSTANTS

MOUSE_LEFT = 1

FPS = 24

SCREEN_SIZE = (800, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 155)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
fps_clock = pygame.time.Clock()
pygame.display.set_caption('Game')


def draw_screen():
    screen.fill(WHITE)


def exit_game():
    pygame.quit()
    sys.exit()


def main():
    while True:
        mouse_x, mouse_y = 0, 0

        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()

            elif event.type == MOUSEBUTTONUP and event.button == MOUSE_LEFT:
                mouse_x, mouse_y = event.pos

        draw_screen()
        pygame.display.update()
        fps_clock.tick(FPS)


# --- EXECUTE
if __name__ == '__main__':
    main()
