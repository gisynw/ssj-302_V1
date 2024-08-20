import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressDialog
from PyQt6.QtCore import QThread, QObject, pyqtSignal, Qt

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(list)

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.progress.emit([f"Working on step {i + 1}",(i + 1) * 10])  # Emit progress as percentage
        self.finished.emit()

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt6 Button Click Example')
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        
        self.btn = QPushButton('Click me', self)
        self.btn.clicked.connect(self.showDialog)
        layout.addWidget(self.btn)
        
        self.setLayout(layout)

    def showDialog(self):
        self.progressDialog = QProgressDialog("Task in progress...", "Cancel", 0, 100, self)
        self.progressDialog.setWindowTitle("Task Progress")
        self.progressDialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progressDialog.setMinimumDuration(0)
        
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.updateProgressDialog)
        self.thread.start()
        
        self.btn.setEnabled(False)
        self.thread.finished.connect(lambda: self.btn.setEnabled(True))
        self.thread.finished.connect(self.progressDialog.close)

    def updateProgressDialog(self, value):
        self.progressDialog.setLabelText(value[0])
        self.progressDialog.setValue(value[1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    ex.show()
    sys.exit(app.exec())
