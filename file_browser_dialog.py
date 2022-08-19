import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon


class Ui_file_browser_Dialog(QFileDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Seleccione archivo'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.files = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                     "All Files (*);;Python Files (*.py)", options=options)



#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Ui_file_browser_Dialog()
#     sys.exit(app.exec_())