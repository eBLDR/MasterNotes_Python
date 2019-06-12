import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Music and Sounds')

# Background music
pygame.mixer.music.load('src/music.mp3')

# Start play bg music - (@time_of_loop (-1 = looping), @seconds from beginning)
pygame.mixer.music.play(-1, 0.0)

# Queuing songs - start playing the song after the previous is finished
# pygame.mixer.music.queue('src/music2.mp3')

# Pausing music
# pygame.mixer.music.pause()
# pygame.mixer.music.unpause()

# Rewinding - restart current song
# pygame.mixer.music.rewind()

# Creating sound object
sound_obj = pygame.mixer.Sound('src/badswap.wav')

# Setting the volume of the sound object @[0.0 - 1.0] - also works for music
sound_obj.set_volume(0.6)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            run = False

        # Hit any key!
        if event.type == pygame.KEYUP:
            # Play sound object
            # The delay is because of silent time in sound the file
            # play(@loops=0, maxtime=0, fade_ms=0)
            sound_obj.play()

            # Stopping the sound
            # sound_obj.stop()

    pygame.display.update()

pygame.quit()
