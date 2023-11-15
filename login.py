import sys
import typing
import bcrypt
import mysql.connector
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from tkinter import *
import tkinter.messagebox
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
        password = passwordInput.encode('utf-8')

        mycursor = mydb.cursor()
        sql = "SELECT password FROM userinfo WHERE email=%s"
        mycursor.execute(sql, (emailInput,))
        stored_hashed_password = mycursor.fetchone()

        if stored_hashed_password:
            if bcrypt.checkpw(password, stored_hashed_password[0].encode('utf-8')):
                from subprocess import call
                self.close()
                call(["python", "primary.py"])
            else:
                print("Invalid login")
                tkinter.messagebox.showinfo("Error", "Invalid Login")
        else:
            print("User not found")
            tkinter.messagebox.showinfo("Error", "User not found")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = login()
    ui.show()
    sys.exit(app.exec_())