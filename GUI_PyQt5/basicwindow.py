import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget  # QDesktopWidget only for centering
# For small windows, QWidget is enough, for bigger structures, use QMainWindow
from PyQt5.QtGui import QIcon  # If we want to display an icon

"""
The QWidget widget is the base class of all user interface objects in PyQt5.
We provide the default constructor for QWidget. The default constructor has no parent.
A widget with no parent is called a window.
"""
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Simple Window'
        self.left = 10  # Margin from left
        self.top = 10  # Margin from top
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        # self.setWindowIcon(QIcon('path/to/img.png')  # Setting the icon

        self.center()
        
        self.show()  # To display the window

    # To center the window on the screen
    def center(self):
        qr = self.frameGeometry()  # Rectangle specifying the geometry of the main window
        cp = QDesktopWidget().availableGeometry().center()  # Screen resolution and center point
        qr.moveCenter(cp)  # Moving rectangle to center
        self.move(qr.topLeft())  # Moving widget to rectangle

 
if __name__ == '__main__':
    # Creating application object
    app = QApplication(sys.argv)  # Passing command line arguments, if not, pass an empty list
    example = App()
    # example.resize(250, 250)  # Resizes the window
    # example.move(300, 300)  # Moves the window
    sys.exit(app.exec_())  # Mainloop - waiting for click event on the screen's closing button to exit
