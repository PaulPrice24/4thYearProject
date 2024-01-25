from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuGUI(object):
    def setupUi(self, menuGUI):
        menuGUI.setObjectName("menuGUI")
        menuGUI.resize(486, 524)
        menuGUI.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(menuGUI)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 200, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 170, 0);\n"
"font: 900 14pt \"Segoe UI Black\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(menuGUI)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 200, 200, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 900 14pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(menuGUI)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 290, 200, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("font: 900 14pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(menuGUI)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 380, 200, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("font: 900 14pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(menuGUI)
        QtCore.QMetaObject.connectSlotsByName(menuGUI)

    def retranslateUi(self, menuGUI):
        _translate = QtCore.QCoreApplication.translate
        menuGUI.setWindowTitle(_translate("menuGUI", "menuGUI"))
        self.pushButton.setText(_translate("menuGUI", "Text to Speech"))
        self.pushButton_2.setText(_translate("menuGUI", "Eye Mouse"))
        self.pushButton_3.setText(_translate("menuGUI", "Translator"))
        self.pushButton_4.setText(_translate("menuGUI", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuGUI = QtWidgets.QWidget()
    ui = Ui_menuGUI()
    ui.setupUi(menuGUI)
    menuGUI.show()
    sys.exit(app.exec_())
