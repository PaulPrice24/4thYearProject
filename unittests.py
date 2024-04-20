import unittest
import register
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
import mysql.connector
from unittest.mock import MagicMock, patch
from login import login

app = QApplication([])

class TestRegister(unittest.TestCase):

    def setUp(self):

        self.app = QApplication([])

        self.register_instance = register.register()

    def tearDown(self):

        self.app.quit()

    def test_register(self):

        self.register_instance.registerUI.lineEdit.setText('Jake')
        self.register_instance.registerUI.lineEdit_2.setText('jake@example.com')
        self.register_instance.registerUI.dateEdit.setDate(QDate.fromString('2000-01-01', 'yyyy-MM-dd'))
        self.register_instance.registerUI.lineEdit_4.setText('password')

        self.register_instance.Registered()

        db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="password",
        database="userinfodb"
    )
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM userinfo WHERE name = 'Jake' AND email = 'jake@example.com'")
        result = db_cursor.fetchone()
        db_connection.close()

        self.assertIsNotNone(result, "Data was not inserted into the database.")

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        login_instance = login()
        login_instance.loginUI.email.setText("jake@example.com")
        login_instance.loginUI.password.setText("password")

        with patch('mysql.connector.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = ("$2b$12$R7IcIj8t1Z4Nf17Z6Nk6ZeG8Reb6OzoCrjwCf3RGoFtZvXxR3cIz2",)
            mock_connect.return_value.cursor.return_value = mock_cursor

            with patch('subprocess.call') as mock_call:
                login_instance.ValidateLogin()

                mock_call.assert_called_once_with(["python", "primary.py", "Jake", "01/01/2000"])

    def test_invalid_login(self):
        login_instance = login()
        login_instance.loginUI.email.setText("jake@example.com")
        login_instance.loginUI.password.setText("wrongpassword")

        with patch('mysql.connector.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = ("$2b$12$R7IcIj8t1Z4Nf17Z6Nk6ZeG8Reb6OzoCrjwCf3RGoFtZvXxR3cIz2",)
            mock_connect.return_value.cursor.return_value = mock_cursor

            with patch('tkinter.messagebox.showinfo') as mock_showinfo:
                login_instance.ValidateLogin()

                mock_showinfo.assert_called_once_with("Error", "Invalid Login")

    def test_user_not_found(self):
        login_instance = login()
        login_instance.loginUI.email.setText("nonexistent@example.com")
        login_instance.loginUI.password.setText("password")

        with patch('mysql.connector.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = None
            mock_connect.return_value.cursor.return_value = mock_cursor

            with patch('tkinter.messagebox.showinfo') as mock_showinfo:
                login_instance.ValidateLogin()

                mock_showinfo.assert_called_once_with("Error", "User not found")

if __name__ == '__main__':
    with open('unit_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)