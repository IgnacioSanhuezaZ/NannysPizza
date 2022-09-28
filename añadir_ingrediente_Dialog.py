# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Añadir_ingrediente_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Controller import ControlModule


class Ui_Dialog(QtWidgets.QDialog):
    def __int__(self):
        pass

    def setupUi(self, Dialog, tamanio_precio):
        self.Dialog = Dialog
        self.data = None
        self.tamanio_precio = tamanio_precio
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 264)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 210, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cmb_nombre = QtWidgets.QComboBox(Dialog)
        self.cmb_nombre.setGeometry(QtCore.QRect(140, 80, 191, 20))
        self.cmb_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_precio = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_precio.setGeometry(QtCore.QRect(140, 165, 113, 20))
        self.lineEdit_precio.setObjectName("lineEdit_precio")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 40, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 140, 101, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        int_only = QtGui.QIntValidator(self.lineEdit_precio)
        int_only.setBottom(0)
        self.lineEdit_precio.setValidator(int_only)
        self.load_ingredients()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Añadir ingrediente"))
        self.label.setText(_translate("Dialog", "Nombre del ingrediente a ser agregado:"))
        self.label_2.setText(_translate("Dialog", "Monto a cobrar:"))

    def on_accept(self):
        if self.cmb_nombre.currentText() != "" and self.lineEdit_precio.text() != "":
            self.Dialog.accept()

    def on_index_change(self):
        if self.cmb_nombre.currentText() in self.data:
            precio = self.data[self.cmb_nombre.currentText()][self.tamanio_precio]
            self.lineEdit_precio.setText(str(precio))

    def load_ingredients(self):
        rec = ControlModule.get_Producto_by_Cathegory("Ingredientes")
        names = []
        data = {}
        for e in rec:
            names.append(e['Nombre_producto'])
            data[e['Nombre_producto']] = e
        self.cmb_nombre.addItems(names)
        self.cmb_nombre.setCurrentIndex(-1)
        self.cmb_nombre.currentIndexChanged.connect(self.on_index_change)
        self.data = data
