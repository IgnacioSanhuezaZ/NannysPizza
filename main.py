import signal
import sys

# import PyQt5.uic.Compiler.compiler
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox

)
from PyQt5.uic import loadUi

from inicio_session_dialogo import Ui_inicio_session

from MainWindow_loged import Ui_MainWindow

global acces_token

class Window(QMainWindow, Ui_inicio_session):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        pass

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    @pyqtSlot()
    def closeEvent(self):
        close = QtWidgets.QMessageBox.question(self,
                                               "SALIR",
                                               "¿Está segura de querer salir?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        acces_token = self.acces_token
        if close == QtWidgets.QMessageBox.Yes:
            acces_token = self.acces_token
            self.close()

        else:
            pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loginForm()
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        pass

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def loginForm(self):
        dialog = QDialog()
        dialog.ui = Window()
        dialog.ui.setupUi(dialog)
        print("A punto...")
        dialog.exec()
        acces_token = dialog.ui.acces_token
        print("Pasó...")
        if not acces_token:
            self.close()

        else:
            pass


class FindReplaceDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("UI/Main_loged.ui", self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    #
    # sys.exit(app.exec())
