# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Pagar_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSizeF

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QTextEdit

from Controller.ControlModule import set_boleta

from tabulate import tabulate


class Ui_Pagar_Dialog(QtWidgets.QDialog):
    def __int__(self):
        pass

    def setupUi(self, Pagar_Dialog, nombre_usuario, nombre_cliente, direccion_cliente, id_sesion, items_boleta):
        self.Pagar_Dialog = Pagar_Dialog
        self.nombre_usuario = nombre_usuario
        self.nombre_cliente = nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.id_sesion = id_sesion
        self.total = 0
        self.items_boleta = items_boleta   # type: dict
        Pagar_Dialog.setObjectName("Pagar_Dialog")
        Pagar_Dialog.resize(549, 661)
        self.buttonBox = QtWidgets.QDialogButtonBox(Pagar_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 600, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.editor = QtWidgets.QTextEdit(Pagar_Dialog)
        self.editor.setGeometry(QtCore.QRect(190, 10, 341, 571))
        self.editor.setObjectName("treeView")
        self.radioButton_tarjetas = QtWidgets.QRadioButton(Pagar_Dialog)
        self.radioButton_tarjetas.setGeometry(QtCore.QRect(20, 200, 101, 17))
        self.radioButton_tarjetas.setObjectName("radioButton_tarjetas")
        self.radioButton_efectivo = QtWidgets.QRadioButton(Pagar_Dialog)
        self.radioButton_efectivo.setGeometry(QtCore.QRect(20, 240, 82, 17))
        self.radioButton_efectivo.setObjectName("radioButton_efectivo")
        self.label = QtWidgets.QLabel(Pagar_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit_efectivo = QtWidgets.QLineEdit(Pagar_Dialog)
        self.lineEdit_efectivo.setGeometry(QtCore.QRect(10, 330, 113, 20))
        self.lineEdit_efectivo.setObjectName("lineEdit_efectivo")
        self.lineEdit_vuelto = QtWidgets.QLineEdit(Pagar_Dialog)
        self.lineEdit_vuelto.setGeometry(QtCore.QRect(10, 400, 113, 20))
        self.lineEdit_vuelto.setText("")
        self.lineEdit_vuelto.setObjectName("lineEdit_vuelto")
        self.label_2 = QtWidgets.QLabel(Pagar_Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 370, 101, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Pagar_Dialog)
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(Pagar_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Pagar_Dialog)

        self.editor.setReadOnly(True)
        # tabulate.PRESERVE_WHITESPACE = True

        int_only = QtGui.QIntValidator(self.lineEdit_vuelto)
        int_only.setBottom(0)
        self.lineEdit_vuelto.setValidator(int_only)
        int_only2 = QtGui.QIntValidator(self.lineEdit_efectivo)
        int_only2.setBottom(0)
        self.lineEdit_efectivo.setValidator(int_only2)
        self.tree_to_text()

    def retranslateUi(self, Pagar_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Pagar_Dialog.setWindowTitle(_translate("Pagar_Dialog", "Verificación de pago"))
        self.radioButton_tarjetas.setText(_translate("Pagar_Dialog", "Débito / Crédito"))
        self.radioButton_efectivo.setText(_translate("Pagar_Dialog", "Efectivo"))
        self.label.setText(_translate("Pagar_Dialog", "Ingreso en efectivo:"))
        self.label_2.setText(_translate("Pagar_Dialog", "Vuelto:"))

    def on_accept(self):
        def count_equal_items(item_to_compare: QtWidgets.QTreeWidgetItem, index_to_exlude):
            counter = 0
            to_delete = []
            for item, i in zip(self.items_boleta, range(len(self.items_boleta))):
                if i != index_to_exlude:
                    item = item   # type: QtWidgets.QTreeWidgetItem
                    if item_to_compare.text(0) == item.text(0):
                        if item_to_compare.text(1) == item.text(1):
                            counter += 1
                            to_delete.append(i)
            for i in to_delete.reverse():
                self.items_boleta.pop(i)
            return counter
        if not self.radioButton_efectivo.isChecked() and not int(self.lineEdit_efectivo) >= self.total:
            return None
        nombre_usuario = self.nombre_usuario
        nombre_cliente = self.nombre_cliente
        direccion = self.direccion_cliente
        id_sesion = self.id_sesion
        if self.radioButton_efectivo.isChecked():
            efectivo = 1
        else:
            efectivo = 0
        data_boleta = []
        total = 0
        for item in self.items_boleta:
            total += int(self.items_boleta[item]['precio'])
            for children in self.items_boleta[item]['sub_items']:
                total += int(children['datos'][2])

        for i in range(0, self.editor.topLevelItemCount()):
            item = self.editor.topLevelItem(i)
            nombre = item.text(0)
            tamano = item.text(3)
            if tamano == "Precio_unitario":
                tamano = 1
            elif tamano == "Precio_mediana":
                tamano = 2
            elif tamano == "Precio_familiar":
                tamano = 3
            adicional = 0
            for j in range(0, item.childCount()):
                sub_item = item.child(j)
                if sub_item.text(2) != "" and "Adicional: " in sub_item.text(1):
                    adicional += int(sub_item.text(2))
            if len(nombre.split(":")) == 2:
                data_boleta.append([None, count_equal_items(self.editor.topLevelItem(i),
                                                            tamano, nombre.split(": ")[1], adicional)])
            else:
                data_boleta.append([nombre, count_equal_items(self.editor.topLevelItem(i),
                                                              tamano, None, adicional)])
        if (self.radioButton_efectivo.isChecked() and int(self.lineEdit_efectivo.text()) >= total) or \
                self.radioButton_tarjetas.isChecked():

            data_venta = [nombre_usuario, nombre_cliente, direccion, id_sesion, adicional, efectivo]
            set_boleta(data_venta=data_venta, data_boleta=data_boleta)
            self.handlePrint()
            self.Pagar_Dialog.accept()

    def handlePrint(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def tree_to_text(self):
        data_list = []
        total = 0
        for key in self.items_boleta.keys():
            # item = QtWidgets.QTreeWidgetItem(self.editor)
            # item.setText(0, key)
            # item.setText(1, self.items_boleta[key]['precio'])
            data_list.append([key, self.items_boleta[key]['precio'], ""])
            total += int(self.items_boleta[key]['precio'])
            for e in self.items_boleta[key]['sub_items']:
                # sub_item = QtWidgets.QTreeWidgetItem(item)
                # sub_item.setText(1, self.items_boleta[key]['sub_items']['data'][0])
                # sub_item.setText(2, self.items_boleta[key]['sub_items']['data'][1])
                # sub_item.setText(3, self.items_boleta[key]['sub_items']['data'][2])
                if len(e['datos']) > 1:
                    data_list.append(["", e['datos'][0], e['datos'][1]])
                    total += int(e['datos'][1])
                else:
                    data_list.append(["", e['datos'][0], ""])
        self.total = total
            #     item.addChild(sub_item)
            # self.editor.addTopLevelItem(item)
        # self.editor.setAcceptRichText(True)
        # self.editor.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        string_formated = tabulate(tabular_data=data_list,
                                     headers=["Producto", "Detalle", "Cobros extra"],
                                     tablefmt="html",
                                     colalign=("center",),
                                     numalign="center")
        # length_margins = string_formated.find("╕")
        print(string_formated)
        # print(length_margins)
        # self.editor.document().setPageSize(QSizeF(0.0, float(length_margins+1)))
        self.editor.document().setDocumentMargin(1)
        self.editor.setHtml(string_formated)
        # self.editor.setText(string_formated)
