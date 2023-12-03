import sys
import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QProcess, QTextCodec
from PyQt5 import QtCore, QtGui

from primaryPage import Ui_Form

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        self.mainUI = Ui_Form()
        self.mainUI.setupUi(self)

        self.mainUI.pushButton_2.clicked.connect(self.Logout)
        self.mainUI.pushButton_3.clicked.connect(self.VoiceAssistant)

        self.mainUI.movie = QtGui.QMovie("C:\\Users\\paulj\\OneDrive\\Desktop\\GUIimages\\ai.gif")
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

    def Logout(self):
        from subprocess import call
        self.close()
        call(["python", "mainPage.py"])

    def VoiceAssistant(self):
        self.voice_process = QProcess()
        self.voice_process.readyReadStandardOutput.connect(self.read_output)
        self.voice_process.readyReadStandardError.connect(self.read_error)
        self.voice_process.start("python", ["main.py"])

    def read_output(self):
        codec = QTextCodec.codecForLocale()
        data = self.voice_process.readAllStandardOutput().data()
        output = codec.toUnicode(data)
        print(output, end='')

    def read_error(self):
        codec = QTextCodec.codecForLocale()
        data = self.voice_process.readAllStandardError().data()
        error = codec.toUnicode(data)
        print(error, end='')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())