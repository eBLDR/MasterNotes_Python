import turtle


class MyTurtle(turtle.Turtle):
    # inheriting from Turtle constructor to add more functions
    # x, y arguments are passed by onclick and onrelease functions
    def glow(self, x, y):
        self.fillcolor('blue')  # setting the fill color, if empty will be transparent

    def unglow(self, x, y):
        self.fillcolor('black')


def exit_():
    window.bye()


def details():
    window.textinput('NAME', 'Enter your name: ')  # pops up a dialog for text input and returns it
    window.numinput('AGE', 'Enter your age: ', 1, 0, 99)  # pops up a dialog for number input - @default, @min, @max
    # is necessary to return the focus back to the screen
    window.listen()


def change_color(x, y):
    if window.bgcolor() == 'white':
        window.bgcolor('red')
    elif window.bgcolor() == 'red':
        window.bgcolor('white')


def move():
    cursor.fd(50)


def right():
    cursor.right(45)


def left():
    cursor.left(45)


def time_over():
    window.clear()
    window.bgcolor('black')
    end = turtle.Turtle()
    end.color('white')
    end.write('TIME OVER')


window = turtle.Screen()
window.setup(600, 600)
window.title('Turtle Events')

cursor = MyTurtle()
cursor.color('black')
cursor.speed(0)
cursor.pensize('5')
cursor.shapesize(5, 5)  # resizing shape, width stretch, height stretch

# action starts
cursor.write('Use the arrows to move Me!\nOr click on Me!\nOr press "n"\nOr click the screen!')

# binding functions to turtle (clicking on it)
cursor.onclick(cursor.glow, btn=1)  # binding to click - @function, @btn=1 default, button 1 is the mouse left button
cursor.onrelease(cursor.unglow)  # binding to release
# cursor.ondrag() will bind to click dragging

# binding functions to screen (keys and click) - for keys, exact key symbol must be used, case sensitive (n != N)
window.onkey(exit_, 'Escape')  # binds to key release - @function, @key_symbol
# for binding to key press use onkeypress() - it will allow to send multiple event while pressing
window.onkey(details, 'n')
window.onkey(move, 'Up')
window.onkey(right, 'Right')
window.onkey(left, 'Left')
window.onclick(change_color, btn=1)  # binding to click

# bind to time, at the moment of the statement, timer starts
window.ontimer(time_over, 10000)  # @function, @milliseconds to event

# @screen_updates - if 0, immediate drawing
window.tracer(0)
window.tracer(1)  # go back to normal rate

window.listen()  # sets focus on screen in order to collect key-events
window.mainloop()  # start the event loop, halts the code, must be the last statement of the code
# activates tkinter mainloop - collects click-events
# mainloop() is equivalent to turtle.done()

print('END')  # this will show after the mainloop finishes, that means once turtleScreen is closed
