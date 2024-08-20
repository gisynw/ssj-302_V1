from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QApplication, QLineEdit, QComboBox, QMenu
from PyQt6.QtGui import QIcon, QAction

class Window(QMainWindow):    
    def __init__(self) -> None:
        super().__init__()
        self.clicked_times = 0
        
        self.setMinimumSize(300,300)
        
        grid_layout = QGridLayout()
        self.label = QLabel("This is a label", alignment=Qt.AlignmentFlag.AlignCenter)
        self.btn = QPushButton("Click Me!")
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Please Enter your last name")
        self.comboBox = QComboBox()
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Green")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem(QIcon("./asset/utd.jpg"), "UTD")
             
        self.btn.clicked.connect(self.clickHandler)
        self.lineEdit.textChanged.connect(self.textChangeHandler)
        self.lineEdit.setMaxLength(10)
        self.comboBox.currentTextChanged.connect(self.comboChange)          
        
        grid_layout.addWidget(self.label, 0, 0)
        grid_layout.addWidget(self.comboBox, 1, 0)
        grid_layout.addWidget(self.lineEdit, 2, 0)
        grid_layout.addWidget(self.btn, 3, 0)
        centerWidget = QWidget()
        centerWidget.setLayout(grid_layout)
        
        self.setCentralWidget(centerWidget)
        
    def clickHandler(self):
        print("Button clicked!")
        self.clicked_times += 1 
        self.label.setText(f"Button has Been Clicked {self.clicked_times} times!")
        
    def textChangeHandler(self):
        self.label.setText(f"Your last name is {self.lineEdit.text()}")
        
    def comboChange(self):
        self.label.setText(f"Current Combo Box text is {self.comboBox.currentText()}")
        
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
            
    def contextMenuEvent(self, e):
        context = QMenu(self)
        
        action1 = QAction("test 1", self)
        action2 = QAction("test 2", self)
        action3 = QAction("test 3", self)
        
        context.addAction(action1)
        context.addAction(action2)
        context.addAction(action3)
        
        action1.triggered.connect(lambda: self.setLabelText("test 1 from context menu"))
        action2.triggered.connect(lambda: self.setLabelText("test 2 from context menu"))
        action3.triggered.connect(lambda: self.setLabelText("test 3 from context menu"))
        
        context.exec(e.globalPos())
    
    def setLabelText(self, text):
        self.label.setText(text)

app = QApplication([])

window = Window()

window.show()

app.exec()
