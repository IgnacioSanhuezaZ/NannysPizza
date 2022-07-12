# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\inicio_session_dialogo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from Controller.ControlModule import control_acceso


class Ui_inicio_session(QtWidgets.QDialog):
    def setupUi(self, inicio_session):
        self.inicio_session = inicio_session
        inicio_session.setObjectName("inicio_session")
        inicio_session.resize(405, 397)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inicio_session.sizePolicy().hasHeightForWidth())
        inicio_session.setSizePolicy(sizePolicy)
        inicio_session.setMaximumSize(QtCore.QSize(405, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/pizza_slice_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inicio_session.setWindowIcon(icon)
        inicio_session.setStyleSheet("background-color: rgb(8, 185, 16);\n"
"alternate-background-color: rgb(255, 255, 255);")
        inicio_session.setSizeGripEnabled(True)
        self.Ingreso = QtWidgets.QDialogButtonBox(inicio_session)
        self.Ingreso.setGeometry(QtCore.QRect(40, 280, 341, 32))
        self.Ingreso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Ingreso.setOrientation(QtCore.Qt.Horizontal)
        self.Ingreso.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Ingreso.setObjectName("Ingreso")
        self.clave_input = QtWidgets.QLineEdit(inicio_session)
        self.clave_input.setGeometry(QtCore.QRect(230, 230, 151, 20))
        self.clave_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clave_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clave_input.setObjectName("clave_input")
        self.line_4 = QtWidgets.QFrame(inicio_session)
        self.line_4.setGeometry(QtCore.QRect(10, 310, 371, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.clave_label = QtWidgets.QLabel(inicio_session)
        self.clave_label.setGeometry(QtCore.QRect(150, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clave_label.setFont(font)
        self.clave_label.setObjectName("clave_label")
        self.label_2 = QtWidgets.QLabel(inicio_session)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 131, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\UI\\../Resources/pizza_PNG7143.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(inicio_session)
        self.line.setGeometry(QtCore.QRect(150, 210, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.usuario_label = QtWidgets.QLabel(inicio_session)
        self.usuario_label.setGeometry(QtCore.QRect(150, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usuario_label.setFont(font)
        self.usuario_label.setObjectName("usuario_label")
        self.label = QtWidgets.QLabel(inicio_session)
        self.label.setGeometry(QtCore.QRect(0, 0, 405, 151))
        self.label.setMaximumSize(QtCore.QSize(405, 16777215))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap(".\\UI\\../Resources/logooo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(inicio_session)
        self.line_2.setGeometry(QtCore.QRect(140, 260, 241, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(inicio_session)
        self.line_3.setGeometry(QtCore.QRect(70, 160, 311, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.usuario_input = QtWidgets.QLineEdit(inicio_session)
        self.usuario_input.setGeometry(QtCore.QRect(230, 180, 151, 20))
        self.usuario_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usuario_input.setObjectName("usuario_input")
        self.Error_label = QtWidgets.QLabel(inicio_session)
        self.Error_label.setGeometry(QtCore.QRect(130, 150, 181, 16))
        self.Error_label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_label.setText("")
        self.Error_label.setObjectName("Error_label")
        self.acces_token = False

        self.retranslateUi(inicio_session)
        self.Ingreso.accepted.connect(lambda: self.on_click_ingreso())
        self.Ingreso.rejected.connect(lambda: self.closeEvent())
        QtCore.QMetaObject.connectSlotsByName(inicio_session)

    @pyqtSlot()
    def on_click_ingreso(self):
        usuario = self.usuario_input.text()
        contrasena = self.clave_input.text()
        acceso = control_acceso(credenciales=[usuario, contrasena])
        if type(acceso) == list and acceso[-1] == "error":
            self.Error_label.setText(acceso[0])
        else:
            self.Error_label.setText("")
            self.acces_token = True
            self.inicio_session.accept()

    @pyqtSlot()
    def closeEvent(self, *event):
        close = QtWidgets.QMessageBox.question(self,
                                               "SALIR",
                                               "¿Está segura de querer salir?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            self.inicio_session.reject()

        else:
            pass

    def exec_(self):
        print("En ejecución")
        super(Ui_inicio_session, self).exec_()
        print("Fin ejecución")
        return self.acces_token

    def retranslateUi(self, inicio_session):
        _translate = QtCore.QCoreApplication.translate
        inicio_session.setWindowTitle(_translate("inicio_session", "Inicio de sesión"))
        self.clave_label.setText(_translate("inicio_session", "<html><head/><body><p><span style=\" font-size:12pt;\">Clave:</span></p></body></html>"))
        self.usuario_label.setText(_translate("inicio_session", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Usuario: </span></p></body></html>"))
