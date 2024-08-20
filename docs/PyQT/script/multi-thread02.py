from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time

class Worker(QRunnable):
    @pyqtSlot()
    def run(self):
        print("Thread start")
        time.sleep(5)
        print("Thread complete")


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)

        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.show()

    def change_message(self):
        self.message = "OH NO"
        self.l.setText(self.message)

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)


app = QApplication([])
window = MainWindow()
app.exec()