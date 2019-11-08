# It divides the space into rows and columns
# It adjusts automatically to the screen size
import sys

from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QPushButton, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.btn = None
        self.le = None

        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        # Line edit
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def show_dialog(self):
        # Returns the text input, and True if something was input
        text, ok = QInputDialog.getText(
            self, 'Input Dialog', 'Enter your name:'
        )

        if ok:
            # Binds to the line edit, could be anything
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
