import sys
from PyQt6.QtWidgets import QWidget,QApplication,QMainWindow,QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setMinimumSize(200,200)
        self.setCentralWidget(self.label)
        
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()