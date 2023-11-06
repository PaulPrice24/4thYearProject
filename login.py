import sys
import typing
import mysql.connector
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui

from loginWindow import Ui_Form

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="password",
    database="userinfodb"
)

class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.loginUI = Ui_Form()
        self.loginUI.setupUi(self)

        self.loginUI.pushButton.clicked.connect(self.ValidateLogin)
        self.loginUI.password.setEchoMode(QLineEdit.Password)

    def ValidateLogin(self):
        emailInput = self.loginUI.email.text()
        passwordInput = self.loginUI.password.text()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM userinfo WHERE email=%s and password=%s"
        mycursor.execute(sql, (emailInput, passwordInput))
        myresult = mycursor.fetchone()
        if myresult==None:
            print("Invalid login")
        else:
            from subprocess import call
            self.close()
            call(["python", "primary.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = login()
    ui.show()
    sys.exit(app.exec_())