import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QTextEdit
from PyQt6.QtGui import QKeySequence,QAction


class MenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menus")
        self.setGeometry(100, 100, 600, 400)
        
        # Create a central widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create a menu bar
        menubar = self.menuBar()

        # Add File menu
        file_menu = menubar.addMenu('File')

        # Add Edit menu
        edit_menu = menubar.addMenu('Edit')

        # Add Help menu
        help_menu = menubar.addMenu('Help')

        # Add actions to the Edit menu
        undo_action = QAction('Undo', self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction('Redo', self)
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction('Cut', self)
        cut_action.setShortcut(QKeySequence.StandardKey.Cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self)
        copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction('Paste', self)
        paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        edit_menu.addAction(paste_action)

        # Add Format submenu to Edit menu
        format_menu = QMenu('Format', self)
        edit_menu.addMenu(format_menu)

        bold_action = QAction('Bold', self)
        bold_action.setShortcut('Ctrl+B')
        format_menu.addAction(bold_action)

        italic_action = QAction('Italic', self)
        italic_action.setShortcut('Ctrl+I')
        format_menu.addAction(italic_action)

        format_menu.addSeparator()

        left_align_action = QAction('Left Align', self)
        left_align_action.setShortcut('Ctrl+L')
        left_align_action.setCheckable(True)
        left_align_action.setChecked(True)
        format_menu.addAction(left_align_action)

        right_align_action = QAction('Right Align', self)
        right_align_action.setShortcut('Ctrl+R')
        right_align_action.setCheckable(True)
        format_menu.addAction(right_align_action)

        justify_action = QAction('Justify', self)
        justify_action.setShortcut('Ctrl+J')
        justify_action.setCheckable(True)
        format_menu.addAction(justify_action)

        center_action = QAction('Center', self)
        center_action.setShortcut('Ctrl+E')
        center_action.setCheckable(True)
        format_menu.addAction(center_action)

        format_menu.addSeparator()

        line_spacing_action = QAction('Set Line Spacing...', self)
        format_menu.addAction(line_spacing_action)

        paragraph_spacing_action = QAction('Set Paragraph Spacing...', self)
        format_menu.addAction(paragraph_spacing_action)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuDemo()
    sys.exit(app.exec())
