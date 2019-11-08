# GUI (Graphic User Interface)

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os  # only for the listbox sake

main_window = tkinter.Tk()
main_window.title('ProScreen')
main_window.geometry('640x480-8-200')

# adding padding
main_window['padx'] = 8

# a label
label = tkinter.Label(main_window, text='TkInter Grid Demo')
label.grid(row=0, column=0, columnspan=3)  # columnspan to set how many rows/columns is going to expand

# configuring rows and columns
# weight is the ratio that increases compared to each other when the screen is resize
main_window.columnconfigure(0, weight=100)
main_window.columnconfigure(1, weight=1)  # scroll bar doesn't need to grow nor shrink
main_window.columnconfigure(2, weight=1000)
main_window.columnconfigure(3, weight=600)
main_window.columnconfigure(4, weight=1000)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

# list box
file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    file_list.insert(tkinter.END, zone)  # .END insert at the end of the list, .0 at the beginning

# adding the scrollbar
list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_list.yview)  # yview for vertical scroll
# command=functionName, no parenthesis, we want to assign it to the command, not to call it when creating the button
list_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscroll'] = list_scroll.set  # this is for the scroll to remain in the position

# frame for the radio buttons, works as a relative coordinates too
option_frame = tkinter.LabelFrame(main_window, text='File Details')
option_frame.grid(row=1, column=2, sticky='ne')

rb_value = tkinter.IntVar()  # we need to create the variable that is going to be assigned using the radio buttons
rb_value.set(3)  # value of the default option
# radio buttons
radio1 = tkinter.Radiobutton(option_frame, text='Filename', value=1, variable=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text='Path', value=2, variable=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text='Timestamp', value=3, variable=rb_value)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
result_label = tkinter.Label(main_window, text='Result')
result_label.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
time_frame = tkinter.LabelFrame(main_window, text='Time')
time_frame.grid(row=3, column=0, sticky='new')
time_frame['padx'] = 36  # adding padding (space) on the x axis

# time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))  # either values or from/to
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=': ').grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=': ').grid(row=0, column=3)
second_spinner.grid(row=0, column=4)

# frame for the date spinners
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=4, column=0, sticky='new')

# date labels
day_label = tkinter.Label(date_frame, text='Day')
month_label = tkinter.Label(date_frame, text='Month')
year_label = tkinter.Label(date_frame, text='Year')
day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')
# date spinners
day_spin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spin = tkinter.Spinbox(date_frame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
year_spin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
day_spin.grid(row=1, column=0)
month_spin.grid(row=1, column=1)
year_spin.grid(row=1, column=2)

# buttons
ok_button = tkinter.Button(main_window, text='OK')
cancel_button = tkinter.Button(main_window, text='Cancel', command=main_window.destroy)
ok_button.grid(row=4, column=3, sticky='e')
cancel_button.grid(row=4, column=4, sticky='w')

main_window.mainloop()

# prints the value of the radio button chosen
print(rb_value.get())
