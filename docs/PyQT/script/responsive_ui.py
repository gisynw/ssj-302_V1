import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ResponsiveUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle('Responsive UI Example')
        self.setGeometry(100, 100, 800, 600)

        # Create a vertical layout
        vbox = QVBoxLayout()

        # Add a label
        self.label = QLabel('Enter your name:', self)
        vbox.addWidget(self.label)

        # Add a line edit
        self.line_edit = QLineEdit(self)
        vbox.addWidget(self.line_edit)

        # Add buttons in a horizontal layout
        hbox = QHBoxLayout()
        self.ok_button = QPushButton('OK', self)
        self.cancel_button = QPushButton('Cancel', self)

        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)

        # Add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)

        # Set the main layout
        self.setLayout(vbox)

        # Connect signals and slots
        self.ok_button.clicked.connect(self.on_ok)
        self.cancel_button.clicked.connect(self.on_cancel)

        # Set initial font size
        self.update_font_size()

    def on_ok(self):
        name = self.line_edit.text()
        self.label.setText(f'Hello, {name}!')

    def on_cancel(self):
        self.line_edit.clear()
        self.label.setText('Enter your name:')

    def resizeEvent(self, event):
        self.update_font_size()
        super().resizeEvent(event)

    def update_font_size(self):
        # Calculate font size based on the window size
        base_size = min(self.width(), self.height()) // 30
        font = QFont()
        font.setPointSize(base_size)

        # Set font size for the label, line edit, and buttons
        self.apply_font_size(font, [self.label, self.line_edit, self.ok_button, self.cancel_button])

        # Adjust line edit height
        self.line_edit.setFixedHeight(base_size * 3)

    def apply_font_size(self, font, widgets):
        for widget in widgets:
            widget.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResponsiveUI()
    window.show()
    sys.exit(app.exec_())
