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
my_rect = pygame.draw.rect(screen, BLUE, (200, 150, 100, 50), 2)

# Draw calls return a Rect object
# collidepoint(), for instance, can be called
print(my_rect.collidepoint((200, 151)))

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
# Using system font (@font, @size, @bold=False, @italic=False)
sys_font = pygame.font.SysFont('Consolas', 32, bold=True, italic=True)

# Creating surface with text
# (@text, @anti-aliasing, @font_color, @background_color)
text = sys_font.render('Wasabi', True, BLACK)  # , WHITE)
screen.blit(text, (350, 220))

# Space needed for rendering the text
print(sys_font.size('Wasabi'))

# Using a font file (@file, @size)
font = pygame.font.Font('freesansbold.ttf', 16)
text_2 = font.render('Custom Font', True, BLACK)
screen.blit(text_2, (320, 100))

# Run the loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
