import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv) #must create an application obejct

    w = QtGui.QWidget()         #window
    w.resize(250, 150)          #tamany
    w.move(400, 300)            #posicio respecte la pantalla
    w.setWindowTitle('Simple')  #titol
    w.show()                    #mostrar
    
    sys.exit(app.exec_())       #mainloop a la espera de exit() (activa
                                #clicant a la creu)


if __name__ == '__main__':
    main()
