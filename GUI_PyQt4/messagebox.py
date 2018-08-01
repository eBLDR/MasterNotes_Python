import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()

    #If we close a QtGui.QWidget, a QtGui.QCloseEvent is generated.
    #To modify the widget behaviour we
    #need to reimplement the closeEvent() event handler.
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message', #title bar
            "Are you sure to quit?", QtGui.QMessageBox.Yes | #text displayed
            #third arg is combination of buttons
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            #last parameter is the default button
        
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
