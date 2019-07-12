import sys
from PyQt4 import QtGui


def main():
    app = QtGui.QApplication(sys.argv)  # must create an application object

    w = QtGui.QWidget()  # window
    w.resize(250, 150)  # size
    w.move(400, 300)  # position
    w.setWindowTitle('Simple')  # title
    w.show()

    sys.exit(app.exec_())  # mainloop


if __name__ == '__main__':
    main()
