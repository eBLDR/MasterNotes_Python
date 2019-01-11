import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(10, 10, 300, 200)
        self.setWindowTitle('Message box')
        self.show()

    # Overriding closeEvent method
    def close_event(self, event):

        # (@widget, @title, @message, @option1 | @option2, @default_option
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
