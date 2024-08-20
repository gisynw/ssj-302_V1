import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialogButtonBox,QWidget

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Dialog")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Enter your details:")
        layout.addWidget(self.label)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(self.name_input)
        
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        layout.addWidget(self.age_input)
        
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)
        
        self.setLayout(layout)

    def accept(self):
        name = self.name_input.text()
        age = self.age_input.text()
        print(f"Name: {name}, Age: {age}")
        super().accept()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.custom_dialog_btn = QPushButton("Open Custom Dialog")
        self.custom_dialog_btn.clicked.connect(self.open_custom_dialog)
        layout.addWidget(self.custom_dialog_btn)
        
        self.setLayout(layout)

    def open_custom_dialog(self):
        dialog = CustomDialog()
        if dialog.exec():
            print("Dialog accepted!")
        else:
            print("Dialog rejected!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
