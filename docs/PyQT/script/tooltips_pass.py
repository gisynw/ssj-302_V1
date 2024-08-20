import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QToolTip
from PyQt6.QtGui import QFont

class PasswordForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Form')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.email_label = QLabel('Email Address')
        layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password')
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)
        self.password_input.setToolTip(
            'Passwords should be at least 10 characters long and include 1 uppercase \nand 1 lowercase alpha character, '
            '1 number and 1 special character. Passwords are case sensitive.')

        self.confirm_password_label = QLabel('Confirm Password')
        layout.addWidget(self.confirm_password_label)
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.confirm_password_input)

        self.create_account_button = QPushButton('CREATE ACCOUNT')
        layout.addWidget(self.create_account_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('SansSerif', 10))
    form = PasswordForm()
    form.show()
    sys.exit(app.exec())
