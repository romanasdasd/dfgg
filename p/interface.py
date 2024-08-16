from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()

win.resize(500,500)

win.setWindowTitle("Python")

enter_login=QLineEdit()

enter_login.setPlaceholderText("Enter Login")

enter_password=QLineEdit()
enter_password.setPlaceholderText("Enter password")

login_button=QPushButton("Login")

row=QHBoxLayout()

col=QVBoxLayout()

row.addWidget(enter_login)
row.addWidget(enter_password)

col.addLayout(row)
col.addWidget(login_button)

win.setLayout(col)

def check_password():
    password=enter_password.text()
    if len(password)< 6:
        message_disable=QMessageBox()
        message_disable.setText("Please enter loger password than 6 characters")
        message_disable.show()
        message_disable.exec_()
    else:
        message_abled=QMessageBox()
        message_abled.setText("Password correct")
        message_abled.show()
        message_abled.exec_()



win.show()

app.exec_()