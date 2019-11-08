import random

import pygame


def draw_random_rect(surface):
    pygame.draw.rect(
        surface,
        (0, 255, 0),
        (random.randint(10, 390), random.randint(10, 390), 15, 15)
    )


pygame.init()

# Frames per second
FPS = 30

# Clock object
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Timers')

# Custom event - all event are integers, constant
# All the values less than USEREVENT are already taken by built-in events
ADDRECT = pygame.USEREVENT + 1

# set_timer(@event, @milliseconds)
# Will insert the event into the event queue every lapse of time
pygame.time.set_timer(ADDRECT, 250)

run = True

while run:
    # Update screen method # 1
    # Delaying the game the given amount of @milliseconds
    # pygame.time.delay(100)

    # Similar to delay, but will share the processor with other programs
    # instead of holding it, resulting in being slightly less accurate
    # pygame.time.wait(100)

    # Update screen method # 2 - using Clock()
    fps_clock.tick(FPS)
    # Calculates time pause needed based on last call of this method, in oder
    # to accomplish assigned frames per second. In this case (FPS = 30), each
    # loop runs for at least 33.3ms, this means that the program will stop for
    # the rest of time, waiting to reach 33.3ms per loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == ADDRECT:
            draw_random_rect(screen)

    # Returns the numbers of fps at the current moment
    print(fps_clock.get_fps())

    pygame.display.update()

pygame.quit()
