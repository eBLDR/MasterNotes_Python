# -*- encoding: utf-8 -*-
# 
# Ejercicios sugeridos:
#
# 1 - Realice que los copos tengan colores aleatorios, siempre en un escala de
#     grises.
#
# 2 - Evite que los copos desaparezcan, busque la forma de hacer que queden
#     visibles en el suelo.
#
# 3 - El rendimiento del ejemplo podría mejorar, busque la forma de eliminar
#     las partículas que ya no están en movimiento (pero que se sigan viendo
#     en pantalla). Consejo: puede alterar la superficie 'image' del arbol
#     para pintar los copos.

import pygame
from random import randint


class Ejemplo:
    """Representa el ejemplo completo.

    Contiene un bucle y todos los recursos que debe actualizar.
    """

    def __init__(self):
        # contruye la pantalla principal.
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
        quit = False
        tree = Tree()

        while not quit:

            self.create_a_random_particle()

            # procesa los eventos de entrada, si
            # el usuario pulsa ESCAPE o Q el programa
            # termina inmediatamente.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                        quit = True

            # aplica una pausa para mantener el rendimiento
            # del juego en 60 cuados por segundo (si es posible).
            #
            # la variable 'dt' indica el tiempo que ha transcurrido
            # desde la anterior llamada, esto se usa en el metodo
            # update del objeto 'Particle' para mantener la velocidad
            # constante.
            dt = clock.tick(60)

            # como dt se indica en milisegundos se convierte
            # a unidad de segundos. Esto significa que dt
            # crece en 1 cada un segundo.
            dt = dt / 1000.0


            # limpia la pantalla
            self.screen.fill((100, 100, 100))

            # dibuja al protagonista
            tree.draw(self.screen)

            # actualiza y dibuja todos los particles sobre la
            # pantalla.

            # como cada particle pinta directamente sobre la
            # pantalla se gana rendimiento bloqueando la
            # superficie primero.
            self.screen.lock()
            
            for particle in self.particles:
                particle.update(dt, tree)
                particle.draw(self.screen)


            # elimia toda particula que este por debajo
            # de la linea horizontal y=320
            self.particles = [particle for particle in self.particles
                                if particle.y < 320]

            self.screen.unlock()

            # muestra los cambios en la pantalla.
            pygame.display.flip()

            # muestra el rendimiento del programa en
            # el titulo de la ventana.
            pygame.display.set_caption("FPS: %d" %(clock.get_fps()))


            
class Tree:

    def __init__(self):
        self.image = pygame.image.load('tree.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(110, 120)
        self.mask = pygame.mask.from_surface(self.image)
        self.w, self.h = self.image.get_size()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def do_collide(self, x, y):
        """Consulta si es colisionable el pixel (x, y).

        tanto 'x' como 'y' son coordenadas de pantalla y no
        relativas al personaje."""
        x = int(x)
        y = int(y)

        x -= self.rect.x
        y -= self.rect.y

        if 0 <= x < self.w and 0 <= y < self.h:
            return self.mask.get_at((x, y))


class Particle:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

        # indica si la particula debe moverse hacia abajo
        self.do_motion = True

    def update(self, dt, tree):
        if self.do_motion:
            self.y += dt * self.speed
            
            # se detiene si colisiona con los pixels
            # del arbol:
            if tree.do_collide(self.x, self.y):
                self.stop()

    def stop(self):
        "Detiene la particula en donde se encuentre."
        self.do_motion = False

    def draw(self, screen):
        position = int(self.x), int(self.y)
        white = (255, 255, 255)
        screen.set_at(position, white)


if __name__ == "__main__":
    ejemplo = Ejemplo()
    ejemplo.loop()
