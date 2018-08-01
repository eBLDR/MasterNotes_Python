import random
import turtle


def random_drawing(cursor):
    cursor.setheading(random.randint(0, 360))
    cursor.forward(random.randint(10, 50))


# creating screen
window = turtle.Screen()
window.title('Turtle Threads')
window.setup(600, 600)
window.colormode(255)

# creating cursors
n_of_cursors = 8
cursors = []  # cursor container
for i in range(n_of_cursors):
    c = turtle.Turtle()
    c.speed(0)
    c.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    cursors.append(c)

# start the motion
for j in range(30):
    for c in cursors:
        random_drawing(c)
