from random import randint

import pygame


class Example:
    def __init__(self):
        self.screen = pygame.display.set_mode((320, 240))
        self.particles = []

    def create_a_random_particle(self):
        x = randint(0, 320)
        y = randint(-30, 0)
        speed = randint(50, 100)
        self.add_particle(x, y, speed)

    def add_particle(self, x, y, speed):
        self.particles.append(Particle(x, y, speed))

    def loop(self):
        clock = pygame.time.Clock()
        quit_ = False
        tree = Tree()

        while not quit_:

            self.create_a_random_particle()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_ = True
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                        quit_ = True

            dt = clock.tick(60)
            dt = dt / 1000.0

            self.screen.fill((60, 60, 60))

            tree.draw(self.screen)

            self.screen.lock()

            for particle in self.particles:
                particle.update(dt, tree)
                particle.draw(self.screen)

            self.particles = [particle for particle in self.particles if particle.y < 320]

            self.screen.unlock()

            pygame.display.flip()

            pygame.display.set_caption('FPS: {:2}'.format(round(clock.get_fps())))


class Tree:
    def __init__(self):
        self.image = pygame.image.load('src/tree.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(110, 120)

        self.mask = pygame.mask.from_surface(self.image)
        self.w, self.h = self.image.get_size()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def do_collide(self, x, y):
        x = int(x)
        y = int(y)

        if self.rect.collidepoint(x, y):
            x -= self.rect.x
            y -= self.rect.y
            return self.mask.get_at((x, y))


class Particle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

        self.do_motion = True

    def update(self, dt, tree):
        if self.do_motion:
            self.y += dt * self.speed

            if tree.do_collide(self.x, self.y):
                self.stop()

    def stop(self):
        self.do_motion = False

    def draw(self, screen):
        position = int(self.x), int(self.y)
        white = (255, 255, 255)
        screen.set_at(position, white)


if __name__ == '__main__':
    example = Example()
    example.loop()
