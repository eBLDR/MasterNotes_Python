import pygame


class Character:
    def __init__(self):
        self.x = 200
        self.y = 350
        self.speed = 5

        # Character moving direction
        self.left = False
        self.right = False

        # Standing image
        self.img_standing = pygame.image.load('src/standing.png')

        # Animation counter
        self.walk_count = 0

        # Array of sprite images
        self.img_walk_right = [
            pygame.image.load('src/R1.png'), pygame.image.load('src/R2.png'),
            pygame.image.load('src/R3.png'), pygame.image.load('src/R4.png'),
            pygame.image.load('src/R5.png'), pygame.image.load('src/R6.png'),
            pygame.image.load('src/R7.png'), pygame.image.load('src/R8.png'),
            pygame.image.load('src/R9.png')
        ]
        self.img_walk_left = [
            pygame.image.load('src/L1.png'), pygame.image.load('src/L2.png'),
            pygame.image.load('src/L3.png'), pygame.image.load('src/L4.png'),
            pygame.image.load('src/L5.png'), pygame.image.load('src/L6.png'),
            pygame.image.load('src/L7.png'), pygame.image.load('src/L8.png'),
            pygame.image.load('src/L9.png')
        ]

    def draw(self):
        # Sprite animation, displaying the same image for 3 frames
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        # Character is facing left
        if self.left:
            screen.blit(self.img_walk_left[self.walk_count // 3],
                        (self.x, self.y))
            self.walk_count += 1

        # Character is facing right
        elif self.right:
            screen.blit(self.img_walk_right[self.walk_count // 3],
                        (self.x, self.y))
            self.walk_count += 1

        # Character is standing still
        else:
            screen.blit(self.img_standing, (self.x, self.y))


def redraw_window():
    # Function that draws all the screen on every frame
    # blit(@img, @position) paste the image to screen at position
    screen.blit(img_bg, (0, 0))

    character.draw()

    pygame.display.update()


pygame.init()

screen = pygame.display.set_mode((500, 480))
pygame.display.set_caption('Sprite Animation')

# Clock object, manages the frames per second
clock = pygame.time.Clock()

FPS = 27

img_bg = pygame.image.load('src/bg.jpg')

character = Character()

run = True

while run:
    # Instead of delay method, clock can be used
    # clock.tick(@int) will update the screen the specified frames per second
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Character is moving left
    if keys[pygame.K_LEFT]:
        character.x -= character.speed
        character.left = True
        character.right = False

    # Character is moving right
    elif keys[pygame.K_RIGHT]:
        character.x += character.speed
        character.left = False
        character.right = True

    # Character is not moving, reset the animation counter
    else:
        character.left = False
        character.right = False
        walkCount = 0

    redraw_window()

pygame.quit()
