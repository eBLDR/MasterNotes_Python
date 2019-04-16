try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

keys = [[('C', 1), ('CE', 1)],  # text, columnspan
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

main_window_padding = 8
main_window = tkinter.Tk()
main_window.title('CALCULATOR')
main_window.geometry('640x480+50+50')
main_window['padx'] = main_window_padding
main_window['pady'] = main_window_padding

result = tkinter.Entry(main_window)
result.grid(row=0, column=0, sticky='nsew')

key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=0, sticky='nsew')

row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(
            row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)  # tkinter.W = 'w'
        col += key[1]
    row += 1

main_window.update()  # to create the screen before running it
# to set the minimum size when resizing
main_window.minsize(key_pad.winfo_width() + main_window_padding * 2,
                    result.winfo_height() + key_pad.winfo_height() + main_window_padding * 2)
# to set the maximum size when resizing
main_window.maxsize(50 + key_pad.winfo_width() + main_window_padding * 2,
                    50 + result.winfo_height() + key_pad.winfo_height() + main_window_padding * 2)

main_window.mainloop()
