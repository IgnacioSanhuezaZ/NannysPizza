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

global access_token
global user_name
global is_admin


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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        globals()['user_name'] = "test"
        globals()['is_admin'] = False
        self.loginForm()
        self.setupUi(self, user_name=globals()['user_name'], is_admin=globals()['is_admin'])
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
        dialog.exec()
        globals()['access_token'] = dialog.ui.acces_token
        globals()['user_name'] = dialog.ui.user_name
        globals()['is_admin'] = dialog.ui.user_admin
        print(globals().values())


class FindReplaceDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("UI/Main_loged.ui", self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow, globals()['user_name'], globals()['is_admin'])
    MainWindow.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    #
    # sys.exit(app.exec())
