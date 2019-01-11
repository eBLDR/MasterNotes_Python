"""
turtle graphics module uses tkinter for underlying graphics and methods.
"""
import turtle

# SETTING SCREEN OBJECT
window = turtle.Screen()  # initialisation
window.setup(500, 500, 50, 50)  # the size of the screen (@width, @height, @startX, @startY)
window.bgcolor('black')  # background color
# window.colormode(255)         # 2 types: 1 for str color (default), 255 for RGB
# window.bgcolor(255, 255, 255) # to specify color, argument can also be like '#A7E30E', white by default
# window.bgpic("file.gif")      # picture on background, must be gif
window.title('Turtle Demo')  # screen title
# window.delay(5)               # in milliseconds - the time interval between two consecutive canvas updates
# the longer the drawing delay, the slower the animation
# will override turtle.speed() settings

# to retrieve screen size
print('Screen is {} x {}'.format(window.window_width(), window.window_height()))

# to change origin of coordinates
# (@lower_left_X, @lower_left_Y, @upper_right_X, @upper_right_Y)
window.setworldcoordinates(0, 0, window.window_width(), window.window_height())

# SETTING TURTLE OBJECT
atlas = turtle.Turtle()  # initialisation of turtle object, any valid name can be used
atlas.shape('turtle')  # [“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”, "blank"]
print(window.getshapes())  # to print the shapes list
atlas.speed('slowest')  # [“fastest”, “fast”, “normal”, “slow”, “slowest”] - can also be int, 0 is the maximum speed
atlas.color('red', 'blue')  # setting the color - it's a tuple (@pencolor, @fillcolor), both can be specified
# individually with turtle.pencolor() and turtle.fillcolor()
# arguments can also be RGB type - @(R, G, B), the we need to set Screen.colormode(255)
atlas.pensize(3)  # setting the thickness
atlas.shapesize(1, 2)  # resizing shape, perpendicular to orientation: @width stretch, @height stretch

# we can also create customised shapes
# new_shape_name = 'path_filename.gif'          # file must be .gif
# screen_object.register_shape(new_shape_name)  # registering shape
# turtle_object.shape(new_shape_name)           # assign the shape to the cursor


# DRAWING
atlas.penup()  # it won't draw on move
atlas.goto(150, 180)  # send the turtle to (x, y) - (0, 0) is the center of the screen - equivalent to setpos()
atlas.pendown()  # it will draw on move
atlas.forward(180)  # moves the cursor forward - equivalent to turtle.fd()
atlas.stamp()  # cursor stamps its shape
atlas.backward(30)  # moves the cursor backward - equivalent to turtle.bk()
atlas.right(250)  # turns right the @degrees - equivalent to turtle.rt()
# left() for left turning - equivalent to turtle.lt()
atlas.dot(10, 'white')  # draws a dot at the position - @size, @color
atlas.forward(150)
# atlas.home()          # will send the cursor to (0, 0) with heading of 0 degrees

atlas.setx(300)  # sending the cursor to a specific x coordinate
atlas.sety(200)  # sending the cursor to a specific y coordinate

# FILLINGS
atlas.begin_fill()  # will fill the shape drawn next
atlas.circle(60, 270)  # draws a circle of @radius, @degrees
atlas.end_fill()  # fills the shape drawn from last call of begin_fill()

# SHOW/HIDE SHAPE
atlas.hideturtle()  # won't show the cursor on screen, but nothing else is affected
# atlas.showturtle() to show cursor on screen again
atlas.home()  # turtle goes to origin (0, 0)
atlas.setheading(45)  # set the heading angle, 0 is towards right and increases counterclockwise - = to turtle.seth()
atlas.forward(150)

# WRITING TEXT
# font_style is a tuple with 3 arguments ('name_of_font', size, 'format')
font_style = ('Console', 40, 'bold')
atlas.write('TEST!', font=font_style)  # writing function, can take 3 arguments (text, font, align)
# align can be 'center', 'left, 'right'


# RETRIEVING
print(atlas.position())  # returns turtle's current position (x, y)
print(atlas.heading())  # returns turtle's current heading (degrees)
print(atlas.xcor())  # returns turtle's current x coordinate
print(atlas.ycor())  # returns turtle's current y coordinate

# RESETS
# turtle resetting
# legend = atlas.clone()    # creates a clone of atlas, with same setting values and position
# atlas.clear()     # delete the turtle's drawings from screen, does not affect its setting
# atlas.reset()     # delete the turtle's drawings from screen, returns setting values to default

# screen resetting
# window.clear()    # delete all drawings and all turtles from the screen, and reset it to its initial state -
# no background, no event bindings and tracing on
# window.reset()    # reset all turtles to their initial state


# ENDING CLAUSES
# window.bye()          # closes the window
# turtle.done()         # at the end, the window will stay until we manually close the screen
window.exitonclick()  # this will close the screen by clicking on it (anywhere)
# binds bye() method to screen click event - also calls mainloop() method for event collection
