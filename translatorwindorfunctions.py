import sys
import typing
import pyttsx3
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QProcess, QTextCodec
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import * 

from translatorwindow import Ui_Translator

class Translator(QWidget):
    def __init__(self):
        super(Translator, self).__init__()
        self.tran = Ui_Translator()
        self.tran.setupUi(self)

        self.tran.pushButton.clicked.connect(self.Translator)

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
        combo_box.addItem("Chinese") 
        combo_box.addItem("Polish") 
        combo_box.addItem("Russian")
        combo_box.addItem("Irish") 
        combo_box.addItem("Japanese") 

        

        combo_box.currentTextChanged.connect(self.set_current_language)
        self.current_language_text = ""

    def set_current_language(self, text):
        self.current_language_text = text

    def get_current_language_text(self):
        return self.current_language_text

    def Translator(self):
        if self.current_language_text:
                print(f"Selected language: {self.current_language_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Translator()
    ui.show()
    sys.exit(app.exec_())