try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os  # only for the listbox sake

mainWindow = tkinter.Tk()
mainWindow.title('ProScreen')
mainWindow.geometry('640x480-8-200')

# adding padding
mainWindow['padx'] = 8

# a label
label = tkinter.Label(mainWindow, text='TkInter Grid Demo')
label.grid(row=0, column=0, columnspan=3)  # columnspan to set how many rows/columns is going to expand

# configuring rows and columns
# weight is the ratio that increases compared to each other when the screen is resized
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)  # scroll bar doesn't need to grow nor shrink
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# list box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)  # .END insert at the end of the list, .0 at the beginning

# adding the scrollbar
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)  # yview for vertical scroll
# command=functionName, no parenthesis, we want to assign it to the command, not to call it when creating the button
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscroll'] = listScroll.set  # this is for the scroll to remain in the position

# frame for the radio buttons, works as a relative coordinates too
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()  # we need to create the variable that is going to be assigned using the radio buttons
rbValue.set(3)  # value of the default option
# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
timeFrame['padx'] = 36  # adding padding (space) on the x axis
# time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))  # either values or from/to
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=': ').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=': ').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

# frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# buttons
okButton = tkinter.Button(mainWindow, text='OK')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')





mainWindow.mainloop()

# prints the value of the radio button chosen
print(rbValue.get())
