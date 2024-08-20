import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

class MessageBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message Box Demo")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.info_btn = QPushButton("Show Information")
        self.info_btn.clicked.connect(self.show_information)
        layout.addWidget(self.info_btn)
        
        self.warning_btn = QPushButton("Show Warning")
        self.warning_btn.clicked.connect(self.show_warning)
        layout.addWidget(self.warning_btn)
        
        self.error_btn = QPushButton("Show Error")
        self.error_btn.clicked.connect(self.show_error)
        layout.addWidget(self.error_btn)
        
        self.question_btn = QPushButton("Show Question")
        self.question_btn.clicked.connect(self.show_question)
        layout.addWidget(self.question_btn)
        
        self.setLayout(layout)

    def show_information(self):
        QMessageBox.information(self, "Information", "This is an information message.")

    def show_warning(self):
        QMessageBox.warning(self, "Warning", "This is a warning message.")

    def show_error(self):
        QMessageBox.critical(self, "Error", "This is an error message.")

    def show_question(self):
        reply = QMessageBox.question(self, "Question", "Do you like PyQt6?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            print("User likes PyQt6!")
        else:
            print("User doesn't like PyQt6!")

app = QApplication(sys.argv)
window = MessageBoxDemo()
window.show()
app.exec()
