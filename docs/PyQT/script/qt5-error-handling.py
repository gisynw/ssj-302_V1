import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressDialog, QMessageBox
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, Qt

class WorkerSignals(QObject):
    progress = pyqtSignal(int)
    message = pyqtSignal(str)
    finished = pyqtSignal(str)
    result = pyqtSignal()
    error = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self, func, name, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func 
        self.name = name 
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
    
    def run(self):
        try:
            self.signals.message.emit(f"{self.name} start")
            self.func(self.signals, *self.args, **self.kwargs)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit(f"{self.name} has finished")

def first_task(signals):
    # Simulate a task that takes 10 seconds
    for i in range(10):
        time.sleep(1)
        signals.progress.emit((i + 1) * 10)
        signals.message.emit(f"First Task: {i + 1} seconds passed")
    signals.progress.emit(50)

def second_task(signals):
    # Simulate a task that takes 5 seconds and raises an error
    for i in range(4):
        time.sleep(1)
        signals.progress.emit(50 + (i + 1) * 10)
        signals.message.emit(f"Second Task: {i + 1} seconds passed")
    signals.progress.emit(100)
    raise Exception("An error occurred in the second task")

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Button Click Example')
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        
        self.btn = QPushButton('Click me', self)
        self.btn.clicked.connect(self.runTasks)
        layout.addWidget(self.btn)
        
        self.setLayout(layout)
        self.threadPool = QThreadPool()

    def runTasks(self):
        self.progressDialog = QProgressDialog("Task in progress...", "Cancel", 0, 100, self)
        self.progressDialog.setWindowTitle("Task Progress")
        self.progressDialog.setWindowModality(Qt.WindowModal)
        self.progressDialog.setMinimumDuration(0)
        self.progressDialog.show()

        self.worker1 = Worker(first_task, "First Task")
        self.worker1.signals.message.connect(self.updateProgressDialog)
        self.worker1.signals.progress.connect(self.updateProgressValue)
        self.worker2 = Worker(second_task, "Second Task")
        self.worker1.signals.error.connect(self.showError)
        self.worker1.signals.finished.connect(lambda x: self.threadPool.start(self.worker2))
        
        self.worker2.signals.message.connect(self.updateProgressDialog)
        self.worker2.signals.progress.connect(self.updateProgressValue)
        self.worker2.signals.error.connect(self.showError)
        self.worker2.signals.finished.connect(self.taskFinished)
        
        self.btn.setEnabled(False)
        self.threadPool.start(self.worker1)
        
    def updateProgressDialog(self, message):
        self.progressDialog.setLabelText(message)
    
    def updateProgressValue(self, value):
        self.progressDialog.setValue(value)

    def taskFinished(self, message):
        self.updateProgressDialog(message)
        self.btn.setEnabled(True)
        self.progressDialog.close()

    def showError(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("An error occurred")
        msgBox.setInformativeText(message)
        msgBox.setWindowTitle("Error")
        msgBox.exec()
        self.btn.setEnabled(True)
        self.progressDialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    ex.show()
    sys.exit(app.exec_())
