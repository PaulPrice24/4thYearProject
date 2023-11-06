import sys
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui

from maingui import Ui_mainGUI

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        self.mainUI = Ui_mainGUI()
        self.mainUI.setupUi(self)

        self.mainUI.pushButton.clicked.connect(self.connectLogin)
        self.mainUI.pushButton_2.clicked.connect(self.connectRegister)

        self.mainUI.movie = QtGui.QMovie("C:\\Users\\paulj\\OneDrive\\Desktop\\GUIimages\\ai.gif")
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

    def connectLogin(self):
        from subprocess import call
        self.close()
        call(["python", "login.py"])

    def connectRegister(self):
        from subprocess import call
        self.close()
        call(["python", "register.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())