from random import randint, uniform

import config

from entities.component import Component
from pyglet import image, sprite, resource


class Ball(Component):

    def __init__(self, *args, **kwargs):
        """
        Creates a sprite using a ball image.
        """
        super(Ball, self).__init__(**kwargs)
        self.speed = kwargs.get('speed', 5)

        # Loading image file
        self.ball_image = image.load(config.resources_path + 'ball.png')
        self.width = self.ball_image.width
        self.height = self.ball_image.height
        self.ball_sprite = sprite.Sprite(self.ball_image, self.x, self.y)

        self.ball_image.rotation = randint(0, 360)  # Rotates the sprite
        self.ball_image.scale = uniform(0.5, 2)

        self.x_direction = 1  # 1 for + axis direction
        self.y_direction = 1

    def update_self(self):
        """
        Increments x and y value and updates position.
        Also ensures that the ball does not leave the screen area by changing its axis direction.
        """
        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.ball_sprite.set_position(self.x, self.y)

        if self.x < 0 or (self.x + self.width) > config.window_width:
            self.x_direction *= -1

        if self.y < 0 or (self.y + self.height) > config.window_height:
            self.y_direction *= -1

    def draw_self(self):
        """
        Draws our ball sprite to screen.
        """
        self.ball_sprite.draw()
