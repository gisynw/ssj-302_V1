import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

application = QApplication(sys.argv)

window = QMainWindow()
window.setMinimumSize(500,500)
centerWidget = QWidget()


parent_layout = QVBoxLayout()

label = QLabel("This is a example!")
parent_layout.addWidget(label)

button_layout = QHBoxLayout()
btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
button_layout.addWidget(btn1)
button_layout.addSpacing(80)
button_layout.addWidget(btn2)
parent_layout.addLayout(button_layout)



centerWidget.setLayout(parent_layout)

window.setCentralWidget(centerWidget)
window.show()

sys.exit(application.exec())



