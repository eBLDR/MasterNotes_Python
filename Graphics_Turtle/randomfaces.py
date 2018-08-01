""" Different random size and color faces, in different random positions,
with different random noses. """

import turtle as turtle
import math as math
import random as random


def eyes(cursor, x, y, scale):
    # draws the 2 eyes
    rad = 10
    cursor.penup()
    cursor.goto(x - (5 * scale), y)
    cursor.setheading(90)
    cursor.pendown()
    cursor.circle(rad * scale, 360)
    cursor.penup()
    cursor.goto(x + (5 * scale), y)
    cursor.setheading(270)
    cursor.pendown()
    cursor.circle(rad * scale, 360)


def nose_rounded(cursor, x, y, scale):
    # draws rounded nose
    cursor.penup()
    cursor.goto(x - (7.5 * scale), (y - (math.tan(30 * 2 * math.pi / 360) * 7.5 * scale)))
    cursor.setheading(0)
    cursor.pendown()
    cursor.forward(15 * scale)
    cursor.setheading(120)
    cursor.forward(15 * scale)
    cursor.setheading(240)
    cursor.forward(15 * scale)


def nose_squared(cursor, x, y, scale):
    # draws squared nose
    cursor.penup()
    cursor.goto(x - (7.5 * scale), y - (7.5 * scale))
    cursor.setheading(0)
    cursor.pendown()
    cursor.forward(15 * scale)
    cursor.setheading(90)
    cursor.forward(15 * scale)
    cursor.setheading(180)
    cursor.forward(15 * scale)
    cursor.setheading(270)
    cursor.forward(15 * scale)


def mouth(cursor, x, y, scale):
    # draws mouth
    rad = 25
    cursor.penup()
    cursor.goto(x - (rad * scale), (y + (4 / 3 * rad * scale / math.pi)))
    cursor.setheading(270)
    cursor.pendown()
    cursor.circle(rad * scale, 180)


def contour(cursor, x, y, scale):
    # draws contour of the face
    rad = 50
    cursor.penup()
    cursor.goto(x, y - (rad * scale))
    cursor.setheading(0)
    cursor.pendown()
    cursor.circle(rad * scale, 360)


def draw_face(cursor, x, y, scale):
    # calls functions for each face component
    contour(cursor, x, y, scale)
    eyes(cursor, x, (y + (20 * scale)), scale)
    mouth(cursor, x, (y - (20 * scale)), scale)
    # randomizing nose type
    if random.randint(1, 2) == 1:
        nose_rounded(cursor, x, (y - (5 * scale)), scale)
    else:
        nose_squared(cursor, x, (y - (5 * scale)), scale)


# setting up the screen
window = turtle.Screen()
window.setup(500, 500)
window.bgcolor("white")
window.title("Random Faces")

# instantiating turtle object
atlas = turtle.Turtle()
atlas.speed("fastest")

num_faces = 10

while num_faces > 0:
    # random position and scale
    posX = random.randint(-210, 210)
    posY = random.randint(-210, 210)
    scale = 1.5 * random.random() + 0.5

    # setting random color
    face_color = ("blue", "black", "red", "green", "yellow", "orange")
    atlas.pencolor(random.choice(face_color))

    # setting random thickness
    atlas.pensize(str(random.randint(1, 5)))

    # calling drawing function
    draw_face(atlas, posX, posY, scale)

    # updating counter
    num_faces -= 1

window.exitonclick()
