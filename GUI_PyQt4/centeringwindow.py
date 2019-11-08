import sys

from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(250, 150)
        self.center()  # code that will center

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # rectangle specifying geometry of main window
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()  # centre
        qr.moveCenter(cp)
        self.move(qr.topLeft())  # move the top-left point of the application
        # window to the top-left point of the qr rectangle,
        # thus centering the window on our screen


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
