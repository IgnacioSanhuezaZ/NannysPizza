# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Seleccion_promo_product_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import Controller.ControlModule


class Ui_sub_cathegory_promo_select(QDialog):
    def __int__(self):
        pass

    def setupUi(self, Ui_sub_cathegory_promo_select, nombre=["Tradicional"], por_categoria=True, cantidad=3):
        self.Ui_self = Ui_sub_cathegory_promo_select   # type: QDialog
        self.nombre = nombre
        self.por_categoria = por_categoria
        self.cantidad = cantidad
        Ui_sub_cathegory_promo_select.setObjectName("Ui_sub_cathegory_promo_select")
        Ui_sub_cathegory_promo_select.resize(545, 580)
        self.buttonBox = QtWidgets.QDialogButtonBox(Ui_sub_cathegory_promo_select)
        self.buttonBox.setGeometry(QtCore.QRect(10, 540, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listProductos = QtWidgets.QListWidget(Ui_sub_cathegory_promo_select)
        self.listProductos.setGeometry(QtCore.QRect(9, 40, 256, 471))
        self.listProductos.setObjectName("listProductos")
        self.listSeleccion = QtWidgets.QListWidget(Ui_sub_cathegory_promo_select)
        self.listSeleccion.setGeometry(QtCore.QRect(279, 40, 256, 471))
        self.listSeleccion.setObjectName("listSeleccion")

        self.retranslateUi(Ui_sub_cathegory_promo_select)
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(Ui_sub_cathegory_promo_select.reject)
        self.listProductos.doubleClicked.connect(self.On_product_list_double_click)
        self.listSeleccion.doubleClicked.connect(self.On_selection_list_double_click)
        QtCore.QMetaObject.connectSlotsByName(Ui_sub_cathegory_promo_select)

        self.get_product_data()

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)

    def retranslateUi(self, Ui_sub_cathegory_promo_select):
        _translate = QtCore.QCoreApplication.translate
        Ui_sub_cathegory_promo_select.setWindowTitle(_translate("Ui_sub_cathegory_promo_select", "Seleccione los componentes de la promoción"))

    def get_product_data(self):
        if self.por_categoria:
            data = Controller.ControlModule.get_Producto_by_Subcathegory(self.nombre[0])
            data = [elem['Nombre_producto'] for elem in data]
        else:
            data = self.nombre
        self.listProductos.addItems(data)

    def On_product_list_double_click(self, index: QtCore.QModelIndex):
        text = self.listProductos.currentItem().text()
        if self.listSeleccion.count() < self.cantidad:
            self.listSeleccion.addItem(text)
            if self.listSeleccion.count() == self.cantidad:
                self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
        else:
            QMessageBox.warning(self, "Aviso", "Ya está ingresada la cantidad suficiente de productos seleccionados")

    def On_selection_list_double_click(self, index: QtCore.QModelIndex):
        self.listSeleccion.takeItem(self.listSeleccion.currentIndex().row())

    def on_accept(self):
        if self.listSeleccion.count() == self.cantidad:
            self.nombre = []
            for i in range(0, self.listSeleccion.count()):
                self.nombre.append(self.listSeleccion.item(i).text())
            self.Ui_self.accept()
