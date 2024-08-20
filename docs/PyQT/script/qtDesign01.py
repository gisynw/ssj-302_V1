from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton
import design 

# class MyWindow(QMainWindow,design.Ui_MainWindow):
#     def __init__(self) -> None:
#         super().__init__()
#         self.setupUi(self)
        
#         self.pushButton.clicked.connect(self.pushBtnHandler)
        
#     def pushBtnHandler(self):
#         self.listWidget.addItem(self.lineEdit.text())
#         self.lineEdit.setText("")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

    
app = QApplication([])
window = MainWindow()
window.show()
app.exec()