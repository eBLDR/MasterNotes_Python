import pygame
import sys

pygame.init()

FPS = 30
fps_clock = pygame.time.Clock()  # clock object

screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Cat Animation')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

cat_img = pygame.image.load('catanimation_src/cat.png')  # creates another surface object
cat_x = 10
cat_y = 10
direction = 'right'

# Creating font object
font_obj = pygame.font.Font('freesansbold.ttf', 32)
# Creating surface with text - (@text, @anti-aliasing, @font color, @background color)
text_surface_obj = font_obj.render('Epic Cat', True, RED)  # , WHITE)

text_rect_obj = text_surface_obj.get_rect()  # text rectangle, will be automatically adjusted to long text
text_rect_obj.center = (200, 150)  # reposition of text rectangle

"""
# background music
pygame.mixer.music.load('catanimation_src/tetrisc.mid')
# start play bg music; @time of loop (-1 = infinity); @second from beginning
pygame.mixer.music.play(-1, 0.0)
"""

# Creating sound object
sound_obj = pygame.mixer.Sound('catanimation_src/badswap.wav')


while True:
    screen.fill(BLACK)

    if direction == 'right':
        cat_x += 5
        # Boundary collision
        if cat_x == 280:
            # Play sound object
            sound_obj.play()
            # The delay is because of silent time in sound the file
            direction = 'down'

    elif direction == 'down':
        cat_y += 5
        if cat_y == 220:
            sound_obj.play()
            direction = 'left'

    elif direction == 'left':
        cat_x -= 5
        if cat_x == 10:
            sound_obj.play()
            direction = 'up'

    elif direction == 'up':
        cat_y -= 5
        if cat_y == 10:
            sound_obj.play()
            direction = 'right'

    screen.blit(cat_img, (cat_x, cat_y))  # paste the surface object to main surface
    screen.blit(text_surface_obj, text_rect_obj)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fps_clock.tick(FPS)  # calculates time pause needed based on last call of this method
    # for accomplish assigned frames per second
    # in this case (FPS = 30), each loop runs for at least 33.3ms, that means the
    # program will stop for the rest of time, waiting to accomplish 33.3ms per loop
