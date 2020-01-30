import random

import pygame


class Square:
    def __init__(self):
        self.x = self.y = 50
        self.width = self.height = 20
        self.speed = 10
        self.color = (255, 0, 0)

    def change_color(self):
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )


pygame.init()

screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size))

pygame.display.set_caption('Events')

nemesis = Square()

run = True

while run:
    pygame.time.delay(50)

    # pygame.event.get() is a list of keyboard and mouse events, if no events,
    # it will be empty
    for event in pygame.event.get():

        # Clicking the close window button
        if event.type == pygame.QUIT:
            run = False

        # Mouse motion
        elif event.type == pygame.MOUSEMOTION:
            # event.pos is a tuple of coordinates (x, y)
            mouse_x, mouse_y = event.pos

        # On mouse click release
        elif event.type == pygame.MOUSEBUTTONUP:
            # Different mouse buttons
            if event.button == pygame.BUTTON_LEFT:
                print('Clicked with left button:', event.pos)
            elif event.button == pygame.BUTTON_MIDDLE:
                print('Clicked with wheel:', event.pos)
            elif event.button == pygame.BUTTON_RIGHT:
                print('Clicked with right button:', event.pos)

        # pygame.MOUSEBUTTONDWON for event in mouse button pressed
        # pygame.MOUSEWHEEL for wheel event

        # On releasing key
        elif event.type == pygame.KEYUP:

            # On releasing space
            if event.key == pygame.K_SPACE:
                nemesis.change_color()

        # pygame.KEYDOWN for event on key pressed

    # Dictionary, each key has a value of 1 if it's pressed and 0 otherwise
    key_state = pygame.key.get_pressed()

    # Equivalent for mouse buttons
    # pygame.mouse.get_pressed()
    # pygame.mouse.get_pos() to get mouse position

    # Checking if keys are being pressed
    if key_state[pygame.K_ESCAPE]:
        run = False

    # Add screen boundaries validation, so we don't move off the screen
    if key_state[pygame.K_LEFT] and nemesis.x >= nemesis.speed:
        # Screen boundaries validation could also be managed by class'
        # attribute's setter property
        nemesis.x -= nemesis.speed

    if key_state[pygame.K_RIGHT] and nemesis.x <= screen_size - nemesis.speed - nemesis.width:
        nemesis.x += nemesis.speed

    if key_state[pygame.K_UP] and nemesis.y >= nemesis.speed:
        nemesis.y -= nemesis.speed

    if key_state[pygame.K_DOWN] and nemesis.y <= screen_size - nemesis.speed - nemesis.height:
        nemesis.y += nemesis.speed

    # Fills the screen with black to remove previous rectangle
    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        nemesis.color,
        (nemesis.x, nemesis.y, nemesis.width, nemesis.height)
    )

    pygame.display.update()

# Closing the game
pygame.quit()
