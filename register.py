import sys
import typing
import mysql.connector
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui

from registerGUI import Ui_Form

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="password",
    database="userinfodb"
)

class register(QWidget):
    def __init__(self):
        super(register, self).__init__()
        self.registerUI = Ui_Form()
        self.registerUI.setupUi(self)

        self.registerUI.pushButton.clicked.connect(self.Registered)
        self.registerUI.lineEdit_4.setEchoMode(QLineEdit.Password)

    def Registered(self):
        nameInput = self.registerUI.lineEdit.text()
        emailInput = self.registerUI.lineEdit_2.text()
        dateInput = self.registerUI.dateEdit.text()
        passwordInput = self.registerUI.lineEdit_4.text()
        if nameInput == '':
            print("Please fill in all fields!")
        elif emailInput == '':
            print("Please fill in all fields!")
        elif passwordInput == '':
            print("Please fill in all fields!")
        else:
            mycursor = mydb.cursor()
            sqlFormula = "INSERT INTO userinfo (name, email, dob, password) VALUES (%s, %s, %s, %s)"
            user = (nameInput, emailInput, dateInput, passwordInput)
            mycursor.execute(sqlFormula, user)
            mydb.commit()

            from subprocess import call
            self.close()
            call(["python", "mainPage.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = register()
    ui.show()
    sys.exit(app.exec_())