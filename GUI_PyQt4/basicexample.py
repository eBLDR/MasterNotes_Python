import sys
import random
from PyQt4 import QtGui

def has_fet_click(): #funci\u00f3 a realitzar en fer click
    print("Hola! Has fet Click!")

def aleatori(): #funci\u00f3 a realitzar en fer click
    global boto2
    boto2.setText(str(random.randint(0,100)))

#aqu\u00ed comen\u00e7a el programa amb interf\u00edcie gr\u00e0fica

app = QtGui.QApplication(sys.argv)  #1: creem objecte aplicaci\u00f3

finestra = QtGui.QWidget()          #2: creem objecte finestra
finestra.setWindowTitle('Finestra')

boto1 = QtGui.QPushButton('Boto 1', finestra) #3: creem objecte de control: un boto
boto1.move(50, 50)
boto1.clicked.connect(has_fet_click) #4: definim l'event que aten el click de boto

boto2 = QtGui.QPushButton('Boto 2', finestra) #5: altres objectes de control
boto2.move(150, 150)
boto2.clicked.connect(aleatori)

finestra.show()         #6: mostrem finestra

sys.exit(app.exec_())   #7: deixem programa a l'espera de que tanquem finstra
