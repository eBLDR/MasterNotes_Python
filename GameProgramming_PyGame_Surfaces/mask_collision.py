"""
Mask - pixel collision detection
A mask uses 1 bit per pixel to store which pixel is transparent or no
"""
import pygame


class MyObject:
    def __init__(self):
        self.image = pygame.image.load('src/cat.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(150, 150)

        """
        A mask makes the transparent parts of the Surface not set, and the
        opaque parts set.
        The alpha of each pixel is checked to see if it is greater than the
        given threshold.
        If the Surface is color-keyed, then threshold is not used.
        Mask can be used for mask collision.
        """
        self.mask = pygame.mask.from_surface(self.image)  # , threshold=127)
        self.w, self.h = self.image.get_size()

    def draw(self, screen_):
        screen_.blit(self.image, self.rect)

    def is_over(self, x, y):
        x = int(x)
        y = int(y)

        x -= self.rect.x
        y -= self.rect.y

        if 0 <= x < self.w and 0 <= y < self.h:
            # Returns nonzero if the bit at (x, y) is set
            return self.mask.get_at((x, y))

        # This function could be re-written using:
        # if self.rect.collidepoint(x, y):
        #     x -= self.rect.x
        #     y -= self.rect.y
        #     return self.mask.get_at((x, y))


screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Mask collision')

clock = pygame.time.Clock()
quit_ = False
my_object = MyObject()

while not quit_:
    mouse_x = mouse_y = None

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_ = True

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    screen.fill((255, 255, 255))

    my_object.draw(screen)

    if mouse_x and mouse_y and my_object.is_over(mouse_x, mouse_y):
        print('Mouse is over me!')

    """
    pygame.sprite.collide_mask(@sprite_1, @sprite_2)
    Collision detection between two sprites, by testing if their bitmasks
    overlap. Returns first point on the mask where the masks collided, or None
    if there was no collision.
    """

    pygame.display.flip()

pygame.quit()
