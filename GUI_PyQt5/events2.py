"""
The event source is the object whose state changes, It generates events.
The event object (event) encapsulates the state changes in the event source.
The event target is the object that wants to be notified.
Event source object delegates the task of handling an event to the event
target.

The sender is an object that sends a signal. The receiver is the object that
receives the signal.
The slot is the method that reacts to the signal.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.text = ''
        self.label = None

        self.init_ui()

    def init_ui(self):
        x, y = 0, 0  # Init x and y
        self.text = 'x: {0},  y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(30, 30)

        # To receive mouse events when mouse moves, is False by default,
        # then it receives mouse events only on click
        self.setMouseTracking(True)

        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 100)
        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 100)

        # Binding methods to button clicked event
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouse_move_event(self, e):
        # e is the event object, with data about the event triggered
        # Methods with the coordinates of the pointer
        x = e.x()
        y = e.y()
        text = 'x: {0},  y: {1}'.format(x, y)  # Text formatting
        self.label.setText(text)

    def button_clicked(self):
        # Knowing who is the sender of the signal
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
