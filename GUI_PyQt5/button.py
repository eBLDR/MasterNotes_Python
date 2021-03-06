import sys

from PyQt5.QtGui import QFont  # Customized fonts
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QWidget


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Custom font for tooltip, (@font_name, @pixel_size)
        QToolTip.setFont(QFont('SansSerif', 10))

        # Text accept rich formatting
        # Setting tooltip for widget
        self.setToolTip('This is a <b>QWidget</b> widget')
        # Tooltips will be displayed after 1 second of hovering on top of the
        # element

        # Button
        btn = QPushButton('Button', self)  # (@name, @parent_widget)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())  # Default size based on text length
        btn.move(50, 50)  # Position from top left corner

        # Binding a method to the button click event
        btn.clicked.connect(App.sample_function)

        self.setGeometry(10, 10, 300, 200)
        self.setWindowTitle('Push Button')
        self.show()

    @staticmethod
    def sample_function():
        print('You pushed me!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())
