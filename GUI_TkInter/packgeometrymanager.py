# GUI (Graphic User Interface)

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()  # opens a sample window

mainWindow = tkinter.Tk()  # creating a master window
mainWindow.title('BLDR')  # setting the title
mainWindow.geometry('640x480')  # setting the size

label = tkinter.Label(mainWindow, text='Plump')
# there are 3 geometry managers in TkInter
# pack() method places the stuff into the window
label.pack(side='top')

# non-visual frames
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=2)
canvas.pack(side='left', fill=tkinter.X, expand=True)

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button1.pack(side='left', anchor='n')  # anchoring stuff to north, south, east, west
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')

mainWindow.mainloop()  # gives control to Tk
