"""
The scope of a variable is where it can be seen or used.
LOCAL (local namespace) scope variables are the ones declared inside the function, they cannot be seen from outside
of the function.

GLOBAL (global namespace) scope variables are the ones declared in the main body, outside all functions, they can be
seen (and used as a comparision) from anywhere, and modified only if the object is mutable,
if trying to change a immutable object, Python will create a new local variable instead.
Shadowing a variable means the we are using the same name for a local variable and for a global variable simultaneously,
it's a bad idea.

OUTER scope refers to looking variables declared in the global namespace. ENCLOSING scope refers to the NONLOCAL ones.
A function should be self-contained, should not make changes to global variables, ideally. If it's necessary, just
type 'global variableName' in the first line of the function when defining it. When a function changes the value of
a global variable (or appends/removes items from a list), it's called side effect

--- LEGB Scope Rule, order of namespaces used when searching for variable names ---

L, Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
E, Enclosing-function locals — Names in the local scope of any and all statically enclosing functions (def or lambda),
from inner to outer.
G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def
within the file.
B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...
"""
import tkinter
import math

numberOfItems = 0  # this will be our example global variable


def parabola(area, size):
    global numberOfItems
    numberOfItems += 1
    for x in range(size + 1):
        y = x ** 2 / size  # / size to fit more values in the screen
        plot(area, x, y)
        plot(area, -x, y)  # because it's symmetric on Y axis, no need to calculate the whole range


def circle(page, radius, color='red'):
    global numberOfItems
    numberOfItems += 1
    accuracy = 10  # to plot more points, more defined circle, more time for the CPU. Can be done with a generator
    for x in range((radius * accuracy) + 1):
        x /= accuracy
        y = math.sqrt(radius ** 2 - (x ** 2))
        plot(page, x, y, color=color)
        plot(page, x, -y, color=color)
        plot(page, -x, y, color=color)
        plot(page, -x, -y, color=color)


def draw_axis(area):
    area.update()
    x_origin = area.winfo_width() / 2
    y_origin = area.winfo_height() / 2
    # moving the origin from -x,-y to x,y (still referred to the original origin
    area.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    area.create_line(-x_origin, 0, x_origin, 0, fill='black')
    area.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())  # to print the local variables, takes no arguments


def plot(area, x, y, color='red'):
    y = -y  # -y because tk has positive y axis pointing bottom
    area.create_line(x, y, x + 1, y + 1, fill=color)


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480)
canvas2.grid(row=0, column=1)

print(type(canvas))
print(repr(canvas), repr(canvas2))  # representation, the number after the . is the location in memory of the object

draw_axis(canvas)
draw_axis(canvas2)

parabola(canvas, 100)
circle(canvas2, 100)
circle(canvas2, 80, color='blue')

print(numberOfItems)

mainWindow.mainloop()
