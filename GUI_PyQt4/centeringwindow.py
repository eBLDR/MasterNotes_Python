import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.center()           #code that will center
        
        self.setWindowTitle('Center')    
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry() #rectangle specifying geometry of main window
        cp = QtGui.QDesktopWidget().availableGeometry().center() #centre
        qr.moveCenter(cp)
        self.move(qr.topLeft()) #move the top-left point of the application
        #window to the top-left point of the qr rectangle,
        #thus centering the window on our screen
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  
