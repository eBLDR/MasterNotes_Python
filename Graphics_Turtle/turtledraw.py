# A simple drawing program.
# Click on a color then click on the screen to draw lines of that color.
# The white color will allow you to move the turtle without drawing.

from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.title('Turtle Draw!')

screen_min_x = -screen.window_width() / 2
screen_min_y = -screen.window_height() / 2
screen_max_x = screen.window_width() / 2
screen_max_y = screen.window_height() / 2

# to adjust coordinates
screen.setworldcoordinates(screen_min_x, screen_min_y, screen_max_x, screen_max_y)

# brush cursor object
brush_turtle = Turtle()
brush_turtle.goto(0, 0)
brush_turtle.speed(10)


# Set up event handler to have the brush_turtle draw a line
# to the point that the user clicks on
def on_screen_click(x, y):
    if y < screen_max_y - 40:  # only draw if clicked below color squares
        brush_turtle.goto(x, y)


screen.onclick(on_screen_click)


class ColorPicker(Turtle):
    def __init__(self, color='red', num=0):
        Turtle.__init__(self)
        self.num = num
        self.color_name = color
        self.speed(0)
        self.shape('circle')
        self.color('black', color)  # @pen_color, @fill_color
        self.penup()

        # hack to register click handler to instance method
        self.onclick(self.handle_click)
        # self.onclick(lambda x, y: self.handle_click(x, y))

    def draw(self):
        self.setx(screen_min_x + 110 + self.num * 30)
        self.sety(screen_max_y - 20)

    def handle_click(self, x, y):
        if self.color_name == '#F9F9F9':
            brush_turtle.penup()
            brush_turtle.color('black')
        else:
            brush_turtle.pendown()
            brush_turtle.color(self.color_name)


# Suppress animations while interface is being drawn
screen.tracer(0)

# text cursor
ui_turtle = Turtle()
ui_turtle.ht()
ui_turtle.penup()
ui_turtle.goto(screen_min_x, screen_max_y - 23)
ui_turtle.write('TurtleDraw!', align='left', font=('Courier', 10, 'bold'))

# Create color choosing squares at the top of screen
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', '#F9F9F9']
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
    picker.draw()

# Resume animations now that main interface has been drawn
screen.tracer(1)

screen.mainloop()
