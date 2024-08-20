import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QGridLayout,QWidget,QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

application = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("python-test")
window.setMinimumSize(300,300)
centerWidget = QWidget()

parent_layout = QGridLayout()

label = QLabel("Login",alignment = Qt.AlignmentFlag.AlignCenter)
label.setMaximumHeight(100)
parent_layout.addWidget(label,0,0,1,4)

email_label = QLabel("Email:")
parent_layout.addWidget(email_label,1,0,1,1)
pass_label = QLabel("Password:")
parent_layout.addWidget(pass_label,2,0,1,1)

email_text = QLineEdit()
pass_text = QLineEdit()
pass_text.setEchoMode(QLineEdit.EchoMode.Password)
parent_layout.addWidget(email_text,1,1,1,3)
parent_layout.addWidget(pass_text,2,1,1,3)

submit_btn = QPushButton("Submit")
parent_layout.addWidget(submit_btn,3,0,1,4)

# parent_layout.setHorizontalSpacing(10)

centerWidget.setLayout(parent_layout)
window.setCentralWidget(centerWidget)
window.show()

sys.exit(application.exec())



