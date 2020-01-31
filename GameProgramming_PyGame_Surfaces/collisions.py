import pygame


class SpaceShip:
    img = pygame.image.load('src/spaceship.png')

    def __init__(self, position, color):
        self.x = self.y = position
        self.speed = 10
        self.color = color

    def get_hit_box(self):
        # Space in which our object is
        return self.img.get_rect(center=(self.x, self.y))

    def draw(self, window):
        # Draw hit box
        pygame.draw.rect(
            window,
            self.color,
            self.get_hit_box(),
            1
        )

        # Draw image
        window.blit(self.img, self.get_hit_box())


def check_surface_collision(rectangle_1, rectangle_2):
    # Checks collision between 2 rectangles
    # Tests if 2 rectangles overlap
    return rectangle_1.colliderect(rectangle_2)


def check_mouse_collide(rectangle, mouse_position, name):
    # Checks if point is inside a rectangle
    if rectangle.collidepoint(mouse_position):
        print('{}: Mouse on top!'.format(name.upper()))


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Collisions')

clock = pygame.time.Clock()

falcon = SpaceShip(150, (0, 0, 255))
hawk = SpaceShip(300, (255, 0, 0))

run = True

while run:
    clock.tick(30)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            check_mouse_collide(hawk.get_hit_box(), (mouse_x, mouse_y), 'hawk')
            check_mouse_collide(falcon.get_hit_box(), (mouse_x, mouse_y), 'falcon')

    key_state = pygame.key.get_pressed()

    # Move space ship 1
    if key_state[pygame.K_LEFT]:
        falcon.x -= falcon.speed
    if key_state[pygame.K_RIGHT]:
        falcon.x += falcon.speed
    if key_state[pygame.K_UP]:
        falcon.y -= falcon.speed
    if key_state[pygame.K_DOWN]:
        falcon.y += falcon.speed

    falcon.draw(screen)
    hawk.draw(screen)

    # Surface collision
    if check_surface_collision(falcon.get_hit_box(), hawk.get_hit_box()):
        print('COLLISION!')

    pygame.display.update()

pygame.quit()
