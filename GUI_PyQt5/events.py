"""
The event source is the object whose state changes, It generates events.
The event object (event) encapsulates the state changes in the event source.
The event target is the object that wants to be notified.
Event source object delegates the task of handling an event to the event target.

The sender is an object that sends a signal. The receiver is the object that receives the signal.
The slot is the method that reacts to the signal.
"""
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QSlider, QLCDNumber
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Number LCD display
        lcd = QLCDNumber(self)
        # Slide bar
        sld = QSlider(Qt.Horizontal, self)

        # Connect a valueChanged signal of the slider to the display slot
        # of the lcd number
        sld.valueChanged.connect(lcd.display)

        grid.addWidget(lcd, 0, 0)
        grid.addWidget(sld, 1, 0)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Events - Signal and slot')
        self.show()

    def key_press_event(self, e):
        # Reimplementing event handler
        if e.key() == Qt.Key_Escape:
            # Managing the event Escape key pressed
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
