import tkinter

main_window = tkinter.Tk()

main_window.title('SuperGrid')
main_window.geometry('640x480+50+100')  # +x axis from left +y axis from top

label = tkinter.Label(main_window, text='Asomao')
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)
right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky='n')  # north, south, etc

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

button1 = tkinter.Button(right_frame, text='Button1')
button2 = tkinter.Button(right_frame, text='Button2')
button3 = tkinter.Button(right_frame, text='Button3')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

right_frame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

main_window.mainloop()
