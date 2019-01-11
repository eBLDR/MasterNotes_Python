"""
The programmer specifies the position and the size of each widget in pixels. Limitations:
- The size and the position of a widget do not change if we resize a window
- Applications might look different on various platforms
- Changing fonts in our application might spoil the layout
- Changing the layout requires to redo the layout, which is tedious and time consuming
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Label are plain text
        lbl1 = QLabel('Hello', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('World', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Python!', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute Positioning')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())
