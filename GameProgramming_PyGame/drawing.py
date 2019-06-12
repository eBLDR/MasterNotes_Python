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

# Drawing shapes - all have @width=0 argument at end, if width is 0, the
# shape will be filled with solid color
# Rectangle - @surface, @color_rgb, @rect
pygame.draw.rect(screen, BLUE, (200, 150, 100, 50), 2)

# Polygon - @surface, @color_rgb, @point_list
pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Line - @surface, @color_rgb, @start_position, @end_position
pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)

# Arc - @surface, @color_rgb, @rect, @start_angle, @end_angle
pygame.draw.arc(screen, BLACK, (150, 150, 20, 180), 0, 3)

# Circle - @surface, @color_rgb, @position, @radius
pygame.draw.circle(screen, RED, (300, 50), 25, 0)

# Ellipse - @surface, @color_rgb, @rect
pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)

# Draw single pixels
pix_obj = pygame.PixelArray(screen)  # Locks the surface while drawing pixels
# get_lock() will return True if it's locked
pix_obj[480][380] = BLACK
pix_obj[482][382] = BLACK
pix_obj[484][384] = BLACK
del pix_obj  # Unlocks the surface

# Write text - creating font object
font = pygame.font.Font('freesansbold.ttf', 32)
# Creating surface with text
# (@text, @anti-aliasing, @font color, @background color)
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
