# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Edicion_producto_boleta_dialogo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog, name, price):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 253)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 190, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 60, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(86, 122, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineNombre_producto = QtWidgets.QLineEdit(Dialog)
        self.lineNombre_producto.setGeometry(QtCore.QRect(140, 60, 291, 20))
        self.lineNombre_producto.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineNombre_producto.setObjectName("lineNombre_producto")
        self.linePrecio = QtWidgets.QLineEdit(Dialog)
        self.linePrecio.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.linePrecio.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.linePrecio.setObjectName("linePrecio")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        int_only = QtGui.QIntValidator(self.linePrecio)
        int_only.setBottom(0)
        self.linePrecio.setValidator(int_only)
        self.lineNombre_producto.setText(name)
        self.linePrecio.setText(price)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nombre del producto:"))
        self.label_2.setText(_translate("Dialog", "Precio:"))
