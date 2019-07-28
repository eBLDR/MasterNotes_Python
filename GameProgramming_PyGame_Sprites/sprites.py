"""
A sprite is a 2D representation of something on the screen - a picture.
"""
import random

import pygame


# Inheriting from Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('src/wizard.png').convert()
        self.rect = self.image.get_rect(center=(300, 300))

        # If mask collision is intended
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = 10

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            # move_ip(@x, @y) method
            # move in place, moves the rectangle a given offset
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('src/missile.png').convert()

        # Setting white as transparent (our file .png has white background)
        # RLEACCEL renders faster on non-accelerated displays
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)

        self.rect = self.image.get_rect(center=(820, random.randint(0, 600)))

        # If mask collision is intended
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            # Sprite's method kill deletes the object from all the groups
            self.kill()


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sprites Class')

player = Player()

# Sprite groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Adding player sprite to sprite group
all_sprites.add(player)

# Checks if group contains sprites
print(all_sprites.has())

# Custom events
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

running = True

while running:
    pygame.time.delay(50)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    keys = pygame.key.get_pressed()

    player.update(keys)

    # This will call the specified method of all the sprites in the group
    enemies.update()

    # Iterate over the sprite group and render all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Equivalent to
    # all_sprites.draw(screen)

    # To clear all the sprites drawn on the last Group.draw() call
    # clear(@destination_surface, @background_surface)
    # @destination_surface is cleared with @background_surface
    # all_sprites.clear(screen, background_surface)

    # Checking sprite collision
    # spritecollideany(@sprite, @group)
    # True if @sprite collides with any in @group
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

    """
    pygame.sprite.spritecollide(@sprite, @group, @dokill, @collided=None)
    Return a list containing all Sprites in a Group that intersect with another
    Sprite. Intersection is determined by comparing the Sprite.rect attribute
    of each Sprite. The dokill argument is a bool. If set to True, all Sprites
    that collide will be removed from the Group.
    
    pygame.sprite.collide_rect(@sprite_1, @sprite_2)
    Collision detection between two sprites, using rects. Uses the pygame rect
    colliderect function to calculate the collision
    
    pygame.sprite.collide_circle(@sprite_1, @sprite_2)
    Collision detection between two sprites, using circles, by testing to see
    if two circles centered on the sprites overlap.
    
    pygame.sprite.collide_mask(@sprite_1, @sprite_2)
    Collision detection between two sprites, by testing if their bitmasks
    overlap. Returns first point on the mask where the masks collided, or None
    if there was no collision.
    """

    pygame.display.update()

pygame.quit()
