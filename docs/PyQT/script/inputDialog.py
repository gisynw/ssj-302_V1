import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Dialog Demo")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.text_btn = QPushButton("Get Text")
        self.text_btn.clicked.connect(self.get_text)
        layout.addWidget(self.text_btn)
        
        self.int_btn = QPushButton("Get Integer")
        self.int_btn.clicked.connect(self.get_integer)
        layout.addWidget(self.int_btn)
        
        self.double_btn = QPushButton("Get Double")
        self.double_btn.clicked.connect(self.get_double)
        layout.addWidget(self.double_btn)
        
        self.combo_btn = QPushButton("Get Combo Box Selection")
        self.combo_btn.clicked.connect(self.get_combobox_selection)
        layout.addWidget(self.combo_btn)
        
        self.setLayout(layout)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "Input Text", "Enter your name:")
        if ok:
            print(f"Name: {text}")

    def get_integer(self):
        number, ok = QInputDialog.getInt(self, "Input Integer", "Enter your age:", 25, 0, 100, 1)
        if ok:
            print(f"Age: {number}")

    def get_double(self):
        number, ok = QInputDialog.getDouble(self, "Input Double", "Enter your salary:", 50000.0, 0, 1000000, 2)
        if ok:
            print(f"Salary: {number}")

    def get_combobox_selection(self):
        items = ["Option 1", "Option 2", "Option 3", "Option 4"]
        item, ok = QInputDialog.getItem(self, "Select an Option", "Options:", items, 0, False)
        if ok and item:
            print(f"Selected: {item}")

app = QApplication(sys.argv)
window = InputDialogDemo()
window.show()
app.exec()
