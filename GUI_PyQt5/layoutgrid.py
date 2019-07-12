# It divides the space into rows and columns
# It adjusts automatically to the screen size
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Instantiating the grid
        grid = QGridLayout()

        self.setLayout(grid)  # Setting the grid

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # List with the rows and columns
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)  # Unpacked tuple (row, column)
            # Also possible using, last argument is for aligning the widget
            # grid.addWidget(
            #     widgetName, row, column, row_span,
            #     column_span, Qt.AlignBottom
            # )

        # The size of the window will be adjusted automatically to the weight
        # of the elements inside
        self.move(300, 150)
        self.setWindowTitle('Grid Layout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
