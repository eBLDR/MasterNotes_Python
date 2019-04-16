import tkinter
import math

number_of_items = 0  # this will be our example global variable


def parabola(area, size):
    global number_of_items
    number_of_items += 1
    for x in range(size + 1):
        y = x ** 2 / size  # / size to fit more values in the screen
        plot(area, x, y)
        plot(area, -x, y)  # because it's symmetric on Y axis, no need to calculate the whole range


def circle(page, radius, color='red'):
    global number_of_items
    number_of_items += 1
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


main_window = tkinter.Tk()
main_window.title('Parabola')
main_window.geometry('640x480')

canvas = tkinter.Canvas(main_window, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(main_window, width=320, height=480)
canvas2.grid(row=0, column=1)

print(type(canvas))
print(repr(canvas), repr(canvas2))  # representation, the number after the . is the location in memory of the object

draw_axis(canvas)
draw_axis(canvas2)

parabola(canvas, 100)
circle(canvas2, 100)
circle(canvas2, 80, color='blue')

print(number_of_items)

main_window.mainloop()
