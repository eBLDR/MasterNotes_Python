import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# Set up the colors - RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)  # Fill screen with color

# Drawing polygons
pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.circle(screen, RED, (300, 50), 25, 0)
pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))

# Draw single pixels
pix_obj = pygame.PixelArray(screen)  # Locks the surface while drawing pixels
# get_lock() will return True if it's locked
pix_obj[480][380] = BLACK
pix_obj[482][382] = BLACK
pix_obj[484][384] = BLACK
del pix_obj  # Unlocks the surface

# Write text - creating font object
font = pygame.font.Font('freesansbold.ttf', 32)
# Creating surface with text - (@text, @anti-aliasing, @font color, @background color)
text = font.render('Wasabi', True, BLACK)  # , WHITE)

screen.blit(text, (350, 220))

# Run the loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
