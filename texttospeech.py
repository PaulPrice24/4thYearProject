from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextToSpeech(object):
    def setupUi(self, TextToSpeech):
        TextToSpeech.setObjectName("TextToSpeech")
        TextToSpeech.resize(483, 518)
        TextToSpeech.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(TextToSpeech)
        self.plainTextEdit.setGeometry(QtCore.QRect(33, 69, 421, 351))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(TextToSpeech)
        self.pushButton.setGeometry(QtCore.QRect(200, 430, 81, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(C:/Users/paulj/OneDrive/Desktop/GUIimages/899261-200.png);\n"
"background-color: rgb(203, 203, 203);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TextToSpeech)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.pushButton_2.setStyleSheet("border-image: url(C:/Users/paulj/OneDrive/Desktop/GUIimages/menu.png);")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(TextToSpeech)
        QtCore.QMetaObject.connectSlotsByName(TextToSpeech)

    def retranslateUi(self, TextToSpeech):
        _translate = QtCore.QCoreApplication.translate
        TextToSpeech.setWindowTitle(_translate("TextToSpeech", "TextToSpeech"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TextToSpeech = QtWidgets.QWidget()
    ui = Ui_TextToSpeech()
    ui.setupUi(TextToSpeech)
    TextToSpeech.show()
    sys.exit(app.exec_())
