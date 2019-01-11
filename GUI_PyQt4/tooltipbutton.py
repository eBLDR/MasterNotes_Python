import sys
from PyQt4 import QtGui

"""
tooltip = description on mouse hover
"""


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))  # font and size

        self.setToolTip('This is a <b>QWidget</b> widget')  # Create tooltip

        btn = QtGui.QPushButton('Button', self)  # Create button
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())  # Recommended size
        btn.move(50, 50)  # Position

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
