import sys
import random
from PyQt4 import QtGui


def clicked():
    print('Hello! You clicked me!')


def random_number():
    global button_2
    button_2.setText(str(random.randint(0, 100)))


app = QtGui.QApplication(sys.argv)

screen = QtGui.QWidget()
screen.setWindowTitle('Screen')

button_1 = QtGui.QPushButton('Btn 1', screen)
button_1.move(50, 50)
button_1.clicked.connect(clicked)

button_2 = QtGui.QPushButton('Btn 2', screen)
button_2.move(150, 150)
button_2.clicked.connect(random_number)

screen.show()

sys.exit(app.exec_())
