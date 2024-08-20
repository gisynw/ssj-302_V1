import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressDialog, QMessageBox
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, Qt

class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    error = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def run(self):
        try:
            for i in range(10):
                if i == 9:
                    raise IndexError("Index out of range error at step 9")
                time.sleep(1)
                self.signals.progress.emit((i + 1) * 10)  # Emit progress as percentage
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()

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
        self.threadPool = QThreadPool()

    def showDialog(self):
        self.progressDialog = QProgressDialog("Task in progress...", "Cancel", 0, 100, self)
        self.progressDialog.setWindowTitle("Task Progress")
        self.progressDialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progressDialog.setMinimumDuration(0)
        
        self.worker = Worker()
        self.worker.signals.progress.connect(self.updateProgressDialog)
        self.worker.signals.finished.connect(self.taskFinished)
        self.worker.signals.error.connect(self.showError)
        
        self.btn.setEnabled(False)
        self.threadPool.start(self.worker)

    def updateProgressDialog(self, value):
        self.progressDialog.setLabelText(f"Working on {value}...")
        self.progressDialog.setValue(value)

    def taskFinished(self):
        self.btn.setEnabled(True)
        self.progressDialog.close()

    def showError(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Critical)
        msgBox.setText("An error occurred")
        msgBox.setInformativeText(message)
        msgBox.setWindowTitle("Error")
        msgBox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    ex.show()
    sys.exit(app.exec())
