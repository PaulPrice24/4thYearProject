import sys
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui

from menugui import Ui_menuGUI

class menuFile(QWidget):
    def __init__(self):
        super(menuFile, self).__init__()
        self.mainUI = Ui_menuGUI()
        self.mainUI.setupUi(self)

        self.mainUI.pushButton.clicked.connect(self.connectTextToSpeech)
        self.mainUI.pushButton_2.clicked.connect(self.connectEyeMouse)
        self.mainUI.pushButton_3.clicked.connect(self.connectTranslator)
        self.mainUI.pushButton_4.clicked.connect(self.connectMain)

    def connectTextToSpeech(self):
        from subprocess import call
        self.close()
        call(["python", "TextToSpeechFunctions.py"])

    def connectEyeMouse(self):
        from subprocess import call
        self.close()
        call(["python", "eyemouse.py"])

    def connectTranslator(self):
        from subprocess import call
        self.close()
        call(["python", "translatorwindorfunctions.py"])

    def connectMain(self):
        from subprocess import call
        self.close()
        call(["python", "primary.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = menuFile()
    ui.show()
    sys.exit(app.exec_())