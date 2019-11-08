try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()  # opens a sample window

main_window = tkinter.Tk()  # creating a master window
main_window.title('BLDR')  # setting the title
main_window.geometry('640x480')  # setting the size

label = tkinter.Label(main_window, text='Plump')
# there are 3 geometry managers in TkInter
# pack() method places the stuff into the window
label.pack(side='top')

# non-visual frames
left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='n', expand=False)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=2)
canvas.pack(side='left', fill=tkinter.X, expand=True)

button1 = tkinter.Button(right_frame, text='button1')
button2 = tkinter.Button(right_frame, text='button2')
button3 = tkinter.Button(right_frame, text='button3')
button1.pack(side='left', anchor='n')  # anchoring stuff to north, south, east, west
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')

main_window.mainloop()  # gives control to Tk
