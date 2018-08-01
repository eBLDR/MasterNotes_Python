import turtle as t
from random import randint

screen = t.Screen()             # to create the screen object, is optional but recommended
screen.title('Turtle Race')     # to change the title
screen.setup(500, 400)          # setting the size x, y
screen.bgcolor('grey')

builder = t.Turtle()        # creating the turtle to draw the map
builder.speed(10)           # to set the speed of the motion, 0 is the maximum speed
builder.penup()             # for not drawing
builder.goto(-140, 140)     # move to a specific position (x=0,y=0 is the centre of the screen)

race_distance = 300
num_of_lines = 11

for step in range(num_of_lines):
    # writing text
    builder.write(step, align='center')  # to align text
    builder.right(90)  # turning in degrees
    builder.forward(10)
    builder.pendown()  # to start drawing again
    builder.forward(150)
    builder.penup()
    builder.backward(160)
    builder.left(90)
    builder.forward(race_distance/num_of_lines)

# drawing map
builder.goto(-100, -120)
# ('font name', size, 'format')
style = ('Console', 40, 'bold')  # specifying font style
builder.write('RACE!', font=style, align='center')
builder.hideturtle()  # will make the turtle disappear

racers = []  # racers container

ada = t.Turtle()  # to create a turtle object
ada.color('red')  # changing color
racers.append(ada)
bob = t.Turtle()
bob.color('blue')
racers.append(bob)
eli = t.Turtle()
eli.color('green')
racers.append(eli)
ark = t.Turtle()
ark.color('orange')
ark.turtlesize(0.8)  # setting the size of the turtle
racers.append(ark)

# put them in place
init_y = 100
for racer in racers:
    racer.shape('turtle')  # different shapes are built-in
    racer.penup()
    racer.goto(-160, init_y)
    racer.pendown()
    init_y -= 30

# create counter for meters
for racer in racers:
    racer.meters_covered = 0  # create new attribute for each

# the race
racing = True
while racing:
    for racer in racers:
        meters_in_turn = randint(1, 5)
        racer.forward(meters_in_turn)
        racer.meters_covered += meters_in_turn
        if racer.meters_covered > race_distance:
            racing = False
            winner = str(racer)

t.done()  # to wait until manually close the screen
