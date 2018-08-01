try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

keys = [[('C', 1), ('CE', 1)],  # text, columnspan
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

mainWindowPadding = 8
mainWindow = tkinter.Tk()
mainWindow.title('CALCULATOR')
mainWindow.geometry('640x480+50+50')
mainWindow['padx'] = mainWindowPadding
mainWindow['pady'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(
            row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)  # tkinter.W = 'w'
        col += key[1]
    row += 1

mainWindow.update()  # to create the screen before running it
# to set the minimum size when resizing
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding * 2,
                   result.winfo_height() + keyPad.winfo_height() + mainWindowPadding * 2)
# to set the maximum size when resizing
mainWindow.maxsize(50 + keyPad.winfo_width() + mainWindowPadding * 2,
                   50 + result.winfo_height() + keyPad.winfo_height() + mainWindowPadding * 2)

mainWindow.mainloop()
