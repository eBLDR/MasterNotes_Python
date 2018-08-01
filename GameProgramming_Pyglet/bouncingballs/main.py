import sys

import pyglet
import config

from entities.ball import Ball
from entities.component import Component

from random import randint

# Creating a window object
window = pyglet.window.Window(height=config.window_height,
                              width=config.window_width)

# Window's origin coordinates (0, 0) start at the bottom left

# Ball container
ball_objects = []


@window.event
def on_draw():
    """
    Overriding the method, renders the window.
    """
    # Clears the screen
    window.clear()

    # Label object, @anchor_x/y is the center point
    level_label = pyglet.text.Label(text="Balls in Game: {}".format(len(ball_objects)), x=10, y=10)  # , anchor_x='center')
    level_label.draw()

    for ball in ball_objects:
        if isinstance(ball, Component):
            ball.draw_self()


def update(time):
    """
    Updates our list of ball objects.
    :param time: passed by schedule_interval
    """
    for ball in ball_objects:
        if isinstance(ball, Component):
            ball.update_self()


# window.event decorator for capture window events
# Click events have 4 arguments @x, @y, @button (1, 2...), @modifiers (such as Alt, Shift, etc.)
@window.event
def on_mouse_press(x, y, button, modifiers):
    """ Control mouse click events. """
    print('Pressed button {}, with modifiers {}, at x: {}, y: {}'.format(button, modifiers, x, y))
    ball_objects.append(Ball(x=x, y=y, speed=randint(3, 12)))


# Key events have 2 arguments @symbol (key pressed), @modifiers
@window.event
def on_key_press(symbol, modifiers):
    """ Control key press events. """
    print('Pressed key {}, with modifiers {}'.format(symbol, modifiers))


@window.event
def on_key_release(symbol, modifiers):
    """ Control key release events. """
    print('Released key {}, with modifiers {}'.format(symbol, modifiers))

    # Setting behaviour for certain key
    if symbol == pyglet.window.key.ESCAPE:
        sys.exit()


def main():
    """ Main method, it contains an embedded method. """
    # @window.event
    # def on_draw():
    #     draw()

    # schedule_interval(@f, @seconds) - periodic task, calls @f every @seconds
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    # Run main loop
    pyglet.app.run()


if __name__ == '__main__':
    main()
