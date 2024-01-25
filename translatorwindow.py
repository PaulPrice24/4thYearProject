from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Translator(object):
    def setupUi(self, Translator):
        Translator.setObjectName("Translator")
        Translator.resize(483, 518)
        Translator.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Translator)
        self.label.setGeometry(QtCore.QRect(-10, -10, 481, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\paulj\\OneDrive\\Desktop\\GUIimages\\ai.gif"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Translator)
        self.pushButton.setGeometry(QtCore.QRect(200, 430, 81, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(C:/Users/paulj/OneDrive/Desktop/GUIimages/899261-200.png);\n"
"background-color: rgb(203, 203, 203);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Translator)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.pushButton_2.setStyleSheet("border-image: url(C:/Users/paulj/OneDrive/Desktop/GUIimages/menu.png);")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Translator)
        QtCore.QMetaObject.connectSlotsByName(Translator)

    def retranslateUi(self, Translator):
        _translate = QtCore.QCoreApplication.translate
        Translator.setWindowTitle(_translate("Translator", "Translator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Translator = QtWidgets.QWidget()
    ui = Ui_Translator()
    ui.setupUi(Translator)
    Translator.show()
    sys.exit(app.exec_())
