import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressDialog, QMessageBox
from PyQt5.QtCore import Qt,QThreadPool

from worker import task_decorator, WorkerSignals,Worker

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
        self.progressDialog.setAutoClose(False)
        self.progressDialog.setAutoReset(False)
        self.progressDialog.show()

        self.worker1 = self.create_worker(first_task)
        self.worker1.signals.error.connect(self.showError)
        self.worker1.signals.finished.connect(self.runSecondTask)
        
        self.btn.setEnabled(False)
        
    def runSecondTask(self, message):
        self.updateProgressDialog(message)
        self.worker2 = self.create_worker(second_task)
        self.worker2.signals.error.connect(self.showError)
        self.worker2.signals.finished.connect(self.taskFinished)

    def create_worker(self, func):
        worker = Worker(func)
        worker.signals.message.connect(self.updateProgressDialog)
        worker.signals.progress.connect(self.updateProgressValue)
        worker.signals.error.connect(self.showError)
        worker.signals.finished.connect(self.taskFinished)
        self.threadPool.start(worker)
        return worker

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

@task_decorator
def first_task(signals):
    for i in range(10):
        time.sleep(1)
        signals.progress.emit((i + 1) * 10)
        signals.message.emit(f"First Task: {i + 1} seconds passed")

@task_decorator
def second_task(signals):
    for i in range(4):
        time.sleep(1)
        signals.progress.emit(50 + (i + 1) * 10)
        signals.message.emit(f"Second Task: {i + 1} seconds passed")
    raise Exception("An error occurred in the second task")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    ex.show()
    sys.exit(app.exec_())
