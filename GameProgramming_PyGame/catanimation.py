import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()  # clock object

DISPLAY_SURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Cat Animation')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

catImg = pygame.image.load('catanimation_src/cat.png')  # creates another surface object
catx = 10
caty = 10
direction = 'right'

fontObj = pygame.font.Font('freesansbold.ttf', 32)  # creates a font object
# creates a surface with text - (@text, @anti-aliasing, @font color, @background color)
textSurfaceObj = fontObj.render('Epic Cat', True, RED)  # , WHITE)
textRectObj = textSurfaceObj.get_rect()  # text rectangle, will be automatically adjusted to long text
textRectObj.center = (200, 150)  # reposition of text rectangle

"""
# background music
pygame.mixer.music.load('catanimation_src/tetrisc.mid')
# start play bg music; @time of loop (-1 = infinity); @second from beginning
pygame.mixer.music.play(-1, 0.0)

# creates sound object
soundObj = pygame.mixer.Sound('catanimation_src/badswap.wav')
"""

while True:
    DISPLAY_SURF.fill(BLACK)
    if direction == 'right':
        catx += 5
        if catx == 280:
            # soundObj.play()  # plays sound object
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            # soundObj.play()
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            # soundObj.play()
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            # soundObj.play()
            direction = 'right'

    DISPLAY_SURF.blit(catImg, (catx, caty))  # paste the surface object to main surface
    DISPLAY_SURF.blit(textSurfaceObj, textRectObj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            # pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS) # calculates time pause needed based on last call of this method
    # for accomplish asigned frames per second
    # in this case (FPS = 30), each loop runs for at least 33.3ms, that means the
    # program will stop for the rest of time, waitting to accomplish 33.3ms per loop
    
