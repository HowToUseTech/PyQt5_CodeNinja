from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class example(QMainWindow):
    def __init__(self):
        super(example, self).__init__()
        loadUi("Example.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = example()
    widget = QStackedWidget()
    widget.addWidget(run)
    widget.setWindowTitle("Example")
    widget.setFixedWidth(324)
    widget.setFixedHeight(474)

    widget.show()

    sys.exit(app.exec())