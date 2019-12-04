import turtle

file_name_turtle = 'spiral_turtle.eps'
file_name_canvas = 'spiral_canvas.eps'

window = turtle.Screen()
window.setup(500, 500, 50, 50)
window.bgcolor('yellow')  # screen attr are not saved in image

cursor = turtle.Turtle()
cursor.color('black')
cursor.speed(0)

x = 121
y = 1
scale = 200

size = 0
for i in range(scale):
    size += y
    cursor.left(x)
    cursor.forward(size)

# Return the TurtleScreen object the turtle is drawing on. TurtleScreen methods can then be called for that object.
# It can used to save it as a file
turtle_screen = cursor.getscreen()
print(type(turtle_screen))

# It's a screen object, but does not seem to work
turtle_screen.bgcolor('yellow')

turtle_screen.getcanvas().postscript(file=file_name_turtle)

# Equivalent to
canvas = window.getcanvas()
print(type(canvas))

# canvas.postscript(file=file_name_canvas)
