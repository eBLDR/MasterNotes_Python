import sys
from PyQt4 import QtGui


"""
tooltip = descripcio en pantalleta al deixar el ratoli a sobre
"""


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10)) #font and size
        
        self.setToolTip('This is a <b>QWidget</b> widget') #crear tooltip per la finestra
        
        btn = QtGui.QPushButton('Button', self) #creem boto
        btn.setToolTip('This is a <b>QPushButton</b> widget') #tooltip al boto
        btn.resize(btn.sizeHint()) #tamany recomanat buto
        btn.move(50, 50) #posicio respecto widget       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
