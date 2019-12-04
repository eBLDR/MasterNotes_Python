"""
Different random size and color faces, in different random positions,
with different random noses.
"""
import math as math
import random as random
import turtle as turtle


def eyes(cursor, x, y, scale_):
    # draws the 2 eyes
    rad = 10
    cursor.penup()
    cursor.goto(x - (5 * scale_), y)
    cursor.setheading(90)
    cursor.pendown()
    cursor.circle(rad * scale_, 360)
    cursor.penup()
    cursor.goto(x + (5 * scale_), y)
    cursor.setheading(270)
    cursor.pendown()
    cursor.circle(rad * scale_, 360)


def nose_rounded(cursor, x, y, scale_):
    # draws rounded nose
    cursor.penup()
    cursor.goto(x - (7.5 * scale_), (y - (math.tan(30 * 2 * math.pi / 360) * 7.5 * scale_)))
    cursor.setheading(0)
    cursor.pendown()
    cursor.forward(15 * scale_)
    cursor.setheading(120)
    cursor.forward(15 * scale_)
    cursor.setheading(240)
    cursor.forward(15 * scale_)


def nose_squared(cursor, x, y, scale_):
    # draws squared nose
    cursor.penup()
    cursor.goto(x - (7.5 * scale_), y - (7.5 * scale_))
    cursor.setheading(0)
    cursor.pendown()
    cursor.forward(15 * scale_)
    cursor.setheading(90)
    cursor.forward(15 * scale_)
    cursor.setheading(180)
    cursor.forward(15 * scale_)
    cursor.setheading(270)
    cursor.forward(15 * scale_)


def mouth(cursor, x, y, scale_):
    # draws mouth
    rad = 25
    cursor.penup()
    cursor.goto(x - (rad * scale_), (y + (4 / 3 * rad * scale_ / math.pi)))
    cursor.setheading(270)
    cursor.pendown()
    cursor.circle(rad * scale_, 180)


def contour(cursor, x, y, scale_):
    # draws contour of the face
    rad = 50
    cursor.penup()
    cursor.goto(x, y - (rad * scale_))
    cursor.setheading(0)
    cursor.pendown()
    cursor.circle(rad * scale_, 360)


def draw_face(cursor, x, y, scale_):
    # calls functions for each face component
    contour(cursor, x, y, scale_)
    eyes(cursor, x, (y + (20 * scale_)), scale_)
    mouth(cursor, x, (y - (20 * scale_)), scale_)
    # randomizing nose type
    if random.randint(1, 2) == 1:
        nose_rounded(cursor, x, (y - (5 * scale_)), scale_)
    else:
        nose_squared(cursor, x, (y - (5 * scale_)), scale_)


# setting up the screen
window = turtle.Screen()
window.setup(500, 500)
window.bgcolor('white')
window.title('Random Faces')

# instantiating turtle object
atlas = turtle.Turtle()
atlas.speed('fastest')

num_faces = 10

while num_faces > 0:
    # random position and scale
    pos_x = random.randint(-210, 210)
    pos_y = random.randint(-210, 210)
    scale = 1.5 * random.random() + 0.5

    # setting random color
    face_color = ('blue', 'black', 'red', 'green', 'yellow', 'orange')
    atlas.pencolor(random.choice(face_color))

    # setting random thickness
    atlas.pensize(str(random.randint(1, 5)))

    # calling drawing function
    draw_face(atlas, pos_x, pos_y, scale)

    # updating counter
    num_faces -= 1

window.exitonclick()
