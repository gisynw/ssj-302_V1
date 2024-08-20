import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog

class FileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Dialog Demo")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.open_file_btn = QPushButton("Open File")
        self.open_file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.open_file_btn)
        
        self.save_file_btn = QPushButton("Save File")
        self.save_file_btn.clicked.connect(self.save_file)
        layout.addWidget(self.save_file_btn)
        
        self.open_dir_btn = QPushButton("Open Directory")
        self.open_dir_btn.clicked.connect(self.open_directory)
        layout.addWidget(self.open_dir_btn)
        
        self.setLayout(layout)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            print(f"Selected File: {file_name}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            print(f"File to Save: {file_name}")

    def open_directory(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Open Directory", "")
        if dir_name:
            print(f"Selected Directory: {dir_name}")

app = QApplication(sys.argv)
window = FileDialogDemo()
window.show()
app.exec()
