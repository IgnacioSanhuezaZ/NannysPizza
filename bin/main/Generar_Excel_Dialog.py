# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Guardar_Boletin_Fechar_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from Controller import ControlModule
import xlsxwriter


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateEdit_inicio = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_inicio.setGeometry(QtCore.QRect(150, 60, 110, 22))
        self.dateEdit_inicio.setObjectName("dateEdit")
        self.dateEdit_final = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_final.setGeometry(QtCore.QRect(150, 110, 110, 22))
        self.dateEdit_final.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 113, 91, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fecha de inicio:"))
        self.label_2.setText(_translate("Dialog", "Fecha de término:"))

    def on_accept(self):
        rec = ControlModule.db.GetVentasPerDates(self.dateEdit_inicio, self.dateEdit_final)
