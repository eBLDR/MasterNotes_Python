import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QIcon


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.status_bar = None
        self.toolbar = None

        self.init_ui()

    def init_ui(self):
        # Instantiating the status bar
        self.status_bar = self.statusBar()
        # Displaying a message
        self.status_bar.showMessage('Ready')

        # Creating the options/actions to be added to the menu
        # @icon (optional), @name (& indicates key shortcut), @parent_widget
        exit_act = QAction('&Exit', self)
        # exit_act = QAction(QIcon('exit.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')  # Shortcut to action, if desired
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(sys.exit)  # Binding an action

        new_act = QAction('New', self)

        # Creating the menu bar
        menu_bar = self.menuBar()

        # Adding a menu to the menu bar, @name
        file_menu = menu_bar.addMenu('&File')

        # Adding actions to the menu - they are displayed by adding order
        file_menu.addAction(new_act)
        file_menu.addAction(exit_act)

        # Creating a submenu
        sub_menu = QMenu('Import', self)
        imp_act = QAction('Import &me', self)  # New action to be added to menu
        sub_menu.addAction(imp_act)
        file_menu.addMenu(sub_menu)  # Adding submenu to menu

        # Checkbox menu - checkable=True
        view_stat_act = QAction('View status bar', self, checkable=True)
        view_stat_act.setStatusTip('View status bar')
        view_stat_act.setChecked(True)  # Default value
        view_stat_act.triggered.connect(self.toggle_menu)  # It's passing a boolean to the function on click

        view_menu = menu_bar.addMenu('&View')  # New menu on menu bar
        view_menu.addAction(view_stat_act)

        # Adding a toolbar - it can be moved around the window by dragging it
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_act)

        self.setGeometry(10, 10, 300, 200)
        self.setWindowTitle('Message box')
        self.show()

    def toggle_menu(self, state):
        # State is passed by the menu, boolean
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()  # To hide status bar

    # Context menu, displayed with right click
    def context_menu_event(self, event):
        c_menu = QMenu(self)

        new_act = c_menu.addAction('New')
        opn_act = c_menu.addAction('Open')
        quit_act = c_menu.addAction('Quit')
        action = c_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_act:
            QApplication.close()  # Closes and quits the app


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())
