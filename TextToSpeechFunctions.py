import sys
import typing
import pyttsx3
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QProcess, QTextCodec
from PyQt5 import QtCore, QtGui

from texttospeech import Ui_TextToSpeech

class TextToSpeech(QWidget):
    def __init__(self):
        super(TextToSpeech, self).__init__()
        self.tts = Ui_TextToSpeech()
        self.tts.setupUi(self)

        self.tts.pushButton.clicked.connect(self.TextToSpeech)

        self.tts.pushButton_2.clicked.connect(self.Menu)

    def TextToSpeech(self):
        text = self.tts.plainTextEdit.toPlainText()

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def Menu(self):
        from subprocess import call
        self.close()
        call(["python", "menu.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TextToSpeech()
    ui.show()
    sys.exit(app.exec_())