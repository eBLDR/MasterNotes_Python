"""
Camera will draw a portion of the game space (called camera view), according
to the screen size.
"""
import pygame

pygame.init()

# Screen
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Camera')

print('Screen size is:', screen.get_size())

# Background map
background_map = pygame.image.load('src/backgroundmap.jpg')

print('Map size is:', background_map.get_size())


class Camera:
    # For this example, 0, 0 coordinates are on top left corner
    # This can be changed
    def __init__(self, screen_size, background_size):
        self.x = 0
        self.y = 0

        self.screen_width, self.screen_height = screen_size
        self.background_width, self.background_height = background_size

        self.jump = 15

        self.camera_range_width, self.camera_range_height = \
            self.set_camera_range()

    def set_camera_range(self):
        return (
            range(0, self.background_width - self.screen_width + 1),
            range(0, self.background_height - self.screen_height + 1)
        )

    def get_blit_position(self, map_coordinates):
        map_x, map_y = map_coordinates
        return map_x - self.x, map_y - self.y

    def move_up(self):
        # Since when pressing "up" we want to scroll up and expand our camera
        # view to the north, it means that the background should move south
        # The same applies to left-right

        # Add boundaries
        if self.y - self.jump not in self.camera_range_height:
            self.y = min(self.camera_range_height)
        else:
            self.y -= self.jump

    def move_down(self):
        if self.y + self.jump not in self.camera_range_height:
            self.y = max(self.camera_range_height)
        else:
            self.y += self.jump

    def move_left(self):
        if self.x - self.jump not in self.camera_range_width:
            self.x = min(self.camera_range_width)
        else:
            self.x -= self.jump

    def move_right(self):
        if self.x + self.jump not in self.camera_range_width:
            self.x = max(self.camera_range_width)
        else:
            self.x += self.jump


camera = Camera(screen.get_size(), background_map.get_size())


# Object in map
class MySurface(pygame.Surface):
    def __init__(self, size, map_position):
        super().__init__(size)

        # New attribute to store position in map
        self.map_position = map_position


my_object = MySurface((35, 35), (300, 300))
my_object.fill((0, 0, 0))

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Camera motion
    if keys[pygame.K_UP]:
        camera.move_up()

    if keys[pygame.K_DOWN]:
        camera.move_down()

    if keys[pygame.K_LEFT]:
        camera.move_left()

    if keys[pygame.K_RIGHT]:
        camera.move_right()

    # Background map is at 0, 0
    screen.blit(background_map, camera.get_blit_position((0, 0)))

    # Draw objects
    screen.blit(my_object, camera.get_blit_position(my_object.map_position))

    pygame.display.update(screen.get_rect())

pygame.quit()
