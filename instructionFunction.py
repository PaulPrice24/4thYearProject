import sys
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui

from instruction import Ui_Instructions

class menuFile(QWidget):
    def __init__(self):
        super(menuFile, self).__init__()
        self.mainUI = Ui_Instructions()
        self.mainUI.setupUi(self)

        self.mainUI.pushButton.clicked.connect(self.connectHome)

    def connectHome(self):
        from subprocess import call
        self.close()
        call(["python", "primary.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = menuFile()
    ui.show()
    sys.exit(app.exec_())