import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QToolTip
from PyQt6.QtGui import QFont

class CustomTooltipDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Tooltip Demo")
        self.setGeometry(100, 100, 300, 200)
        
        # Set global font for tooltips
        QToolTip.setFont(QFont('SansSerif', 10))
        
        layout = QVBoxLayout()
        
        self.button = QPushButton("Hover over me")
        self.button.setToolTip("<b style='color:blue;'>This is a blue tooltip</b>")
        layout.addWidget(self.button)
        
        self.setLayout(layout)

app = QApplication(sys.argv)
window = CustomTooltipDemo()
window.show()
app.exec()
