import sys

from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    # If we close a QtGui.QWidget, a QtGui.QCloseEvent is generated.
    # To modify the widget behaviour we
    # need to overwrite the closeEvent() event handler.
    def close_event(self, event):

        # (@widget, @title, @message, @option1 | @option2, @default_option
        reply = QtGui.QMessageBox.question(self,
                                           'Message',
                                           'Are you sure to quit?',
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
