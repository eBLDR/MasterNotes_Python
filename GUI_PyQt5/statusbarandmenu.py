import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Instantiating the status bar
        self.statusbar = self.statusBar()
        # Displaying a message
        self.statusbar.showMessage('Ready')

        # Creating the options/actions to be added to the menu
        # @icon (optional), @name (& indictes key shortcut), @parent_widget
        exitAct = QAction('&Exit', self)
        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')  # Shortcut to action, if desired
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(sys.exit)  # Binding an action

        newAct = QAction('New', self)

        # Creating the menu bar
        menuBar = self.menuBar()

        # Adding a menu to the menu bar, @name
        fileMenu = menuBar.addMenu('&File')

        # Adding actions to the menu - they are displayed by adding order
        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)
        
        # Creating a submenu
        subMenu = QMenu('Import', self)
        impAct = QAction('Import &me', self)  # New action to be added to menu
        subMenu.addAction(impAct)
        fileMenu.addMenu(subMenu)  # Adding submenu to menu

        # Checkbox menu - checkable=True
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)  # Default value
        viewStatAct.triggered.connect(self.toggleMenu)  # It's passing a boolean to the function on click

        viewMenu = menuBar.addMenu('&View')  # New menu on menu bar
        viewMenu.addAction(viewStatAct)

        # Adding a toolbar - it can be moved around the window by dragging it
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(10, 10, 300, 200)        
        self.setWindowTitle('Message box')    
        self.show()

    def toggleMenu(self, state):
        # State is passed by the menu, boolean
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()  # To hide status bar

    # Context menu, displayed with right click
    def contextMenuEvent(self, event):
           cmenu = QMenu(self)
           
           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))
           
           if action == quitAct:
               QApplication.close()  # Closes and quits the app
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())
