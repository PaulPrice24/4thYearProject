import sys
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui
import subprocess

from translatorwindow import Ui_Translator  # Assuming you have a file named translatorwindow.py

class Translator(QWidget):
    def __init__(self):
        super(Translator, self).__init__()
        self.tran = Ui_Translator()
        self.tran.setupUi(self)

        self.tran.pushButton.clicked.connect(self.Translator)

        self.tran.pushButton_2.clicked.connect(self.Menu)

        self.tran.movie = QtGui.QMovie("C:\\Users\\paulj\\OneDrive\\Desktop\\GUIimages\\ai.gif")
        self.tran.label.setMovie(self.tran.movie)
        self.tran.movie.start()

        self.UiComponents()

        self.show()

    def UiComponents(self):
        combo_box = QComboBox(self)
        combo_box.setGeometry(185, 375, 120, 40)
        combo_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        combo_box.addItem("Select")
        combo_box.addItem("French")
        combo_box.addItem("Spanish")
        combo_box.addItem("German")
        combo_box.addItem("Dutch")
        combo_box.addItem("Polish")
        combo_box.addItem("Portuguese")
        combo_box.addItem("Russian")
        combo_box.addItem("Italian")

        combo_box.currentTextChanged.connect(self.set_current_language)
        self.current_language_text = ""

    def set_current_language(self, text):
        self.current_language_text = text

    def get_current_language_text(self):
        return self.current_language_text
    
    def Menu(self):
        from subprocess import call
        self.close()
        call(["python", "menu.py"])

    def Translator(self):
        if self.current_language_text and self.current_language_text != "Select":
            print(f"Selected language: {self.current_language_text}")

            # Run translator.py with the selected language
            subprocess.Popen(["python", "translator.py", self.current_language_text])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Translator()
    ui.show()
    sys.exit(app.exec_())