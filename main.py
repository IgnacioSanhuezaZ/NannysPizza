import sys

from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox

)

from PyQt5.uic import loadUi

from MainWindow import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        pass

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()


class FindReplaceDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("UI/Main.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
