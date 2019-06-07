import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Music and Sounds')

# Background music
pygame.mixer.music.load('src/music.mp3')

# Start play bg music - (@time_of_loop (-1 = infinity), @seconds from beginning)
pygame.mixer.music.play(-1, 0.0)

# Creating sound object
sound_obj = pygame.mixer.Sound('src/badswap.wav')

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Hit any key!
        if event.type == pygame.KEYUP:
            # Play sound object
            sound_obj.play()

    pygame.display.update()

pygame.quit()
