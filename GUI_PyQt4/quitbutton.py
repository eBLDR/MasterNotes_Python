import sys

from PyQt4 import QtCore, QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        q_btn = QtGui.QPushButton('Quit', self)
        q_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # clicked.connect calls another function when clicking
        q_btn.resize(q_btn.sizeHint())
        q_btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
