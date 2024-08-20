from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time

from PyQt6.QtWidgets import QWidget

class MianWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel("Start")
        self.button = QPushButton("Do not click")
        self.button.pressed.connect(self.btnPressed)
        self.counter = 0
        
        layout = QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(self.button,1,0)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.show()
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        
    def btnPressed(self):
        time.sleep(5)
        
    def recurring_timer(self):
        self.counter +=1
        self.label.setText("Counter: %d" % self.counter)
        
app = QApplication([])
window = MianWindow()
app.exec()
    
    