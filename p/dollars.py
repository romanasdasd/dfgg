from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()

win.resize(500,500)

win.setWindowTitle("Dollars")

enter_Dollars=QLineEdit()

enter_Dollars.setPlaceholderText("Введіть в доларах")

message_disable=QMessageBox()

message_disable.show()
message_disable.exec_()
    

login_button=QPushButton("Перевести")

row=QHBoxLayout()

col=QVBoxLayout()

row.addWidget(enter_Dollars)


col.addLayout(row)
col.addWidget(login_button)
win.setLayout(col)


win.show()

app.exec_()