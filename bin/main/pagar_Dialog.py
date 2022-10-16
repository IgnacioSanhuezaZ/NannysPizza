# -*- coding: utf-8 -*-
import numpy as np
# Form implementation generated from reading ui file '.\UI\Pagar_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtPrintSupport import QPrintDialog

from Controller.ControlModule import set_boleta

from tabulate import tabulate


class Ui_Pagar_Dialog(QtWidgets.QDialog):
    def __int__(self):
        pass

    def setupUi(self, Pagar_Dialog, nombre_usuario, info_cliente, datos_despacho, id_sesion, items_boleta):
        self.Pagar_Dialog = Pagar_Dialog
        self.nombre_usuario = nombre_usuario
        self.nombre_cliente = info_cliente['nombre']
        self.direccion_cliente = info_cliente['direccion']
        self.telefono_cliente = info_cliente['telefono']
        self.is_desacho = datos_despacho['despacho']
        self.is_pedidos_ya = datos_despacho['pedidos_ya']
        self.zona_despacho = datos_despacho['zona']
        self.precio_despacho = datos_despacho['precio']
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

        self.lineEdit_vuelto.setReadOnly(True)
        int_only = QtGui.QIntValidator(self.lineEdit_vuelto)
        int_only.setBottom(0)
        self.lineEdit_vuelto.setValidator(int_only)
        int_only2 = QtGui.QIntValidator(self.lineEdit_efectivo)
        int_only2.setBottom(0)
        self.lineEdit_efectivo.setValidator(int_only2)
        self.tree_to_text()
        self.lineEdit_efectivo.textChanged.connect(self.on_text_change)

    def retranslateUi(self, Pagar_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Pagar_Dialog.setWindowTitle(_translate("Pagar_Dialog", "Verificación de pago"))
        self.radioButton_tarjetas.setText(_translate("Pagar_Dialog", "Débito / Crédito"))
        self.radioButton_efectivo.setText(_translate("Pagar_Dialog", "Efectivo"))
        self.label.setText(_translate("Pagar_Dialog", "Ingreso en efectivo:"))
        self.label_2.setText(_translate("Pagar_Dialog", "Vuelto:"))

    def on_accept(self):
        def select_data_from_item(key, item=None):
            data = []
            if 'Promoción' in key:
                nombre_promo = key
                nombre_producto = None
            else:
                nombre_promo = None
                nombre_producto = key
                if len(key.split(" - ")) > 1:
                    nombre_producto = key.split(" - ")[0]
            if not item:
                tamanio = self.items_boleta[key]['tamanio']
                cantidad = self.items_boleta[key]['cantidad']
                values_to_insert = [nombre_producto, cantidad, tamanio, nombre_promo]
                data.append(values_to_insert)
                for children in self.items_boleta[key]['sub_items']:
                    if children['tipo'] == "Agregado":
                        nombre_producto = children['datos'][0].split(": ")[1]
                        nombre_promo = None
                        cantidad = 1
                        values_to_insert = [nombre_producto, cantidad, tamanio, nombre_promo]
                        data.append(values_to_insert)
            else:
                tamanio = item['tamanio']
                cantidad = item['cantidad']
                values_to_insert = [nombre_producto, cantidad, tamanio, nombre_promo]
                data.append(values_to_insert)
                for children in item['sub_items']:
                    if children['tipo'] == "Agregado":
                        nombre_producto = children['datos'][0].split(": ")[1]
                        nombre_promo = None
                        cantidad = 1
                        values_to_insert = [nombre_producto, cantidad, tamanio, nombre_promo]
                        data.append(values_to_insert)
            return data
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
        """
        key order venta: (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo ,)

        key order boleta: (Nombre_producto, Cantidad, Tamano, Nombre_promocion,)
        """
        for item in self.items_boleta:
            parcial = int(self.items_boleta[item]['precio'])
            total += int(self.items_boleta[item]['precio'])
            values_to_insert = select_data_from_item(item)
            data_boleta += values_to_insert
            for children in self.items_boleta[item]['sub_items']:
                if children['tipo'] == "Agregado":
                    total += int(children['datos'][1])
                    parcial += int(children['datos'][1])
            for other in self.items_boleta[item]['otros']:
                parcial = int(other['precio'])
                total += int(other['precio'])
                values_to_insert = select_data_from_item(item, other)
                data_boleta += values_to_insert
                for children in self.items_boleta[item]['sub_items']:
                    if children['tipo'] == "Agregado":
                        total += int(children['datos'][1])
                        parcial += int(children['datos'][1])
        # data_raw_text = self.editor.document().toPlainText().split("\n")
        # i = 0
        # n = 0
        # data_grouped = []
        # row = []
        # while i < len(data_raw_text):
        #     if data_raw_text[i] == "" and i != 0:
        #         data = ""
        #     elif i != 0:
        #         data = data_raw_text[i]
        #     else:
        #         i += 1
        #         continue
        #     row.append(data)
        #     i += 1
        #     if n >= 2:
        #         n = 0
        #         data_grouped.append(row)
        #         row = []
        #     else:
        #         n += 1
        # data_text = np.array(data_grouped)
        # for item in data_text:
        #     print(item)
        #     nombre = item[0]
        #     tamano = item[3]
        #     if nombre != '' and nombre.split(":")[0] != 'Comentario':
        #         if tamano == "Precio_unitario":
        #             tamano = 1
        #         elif tamano == "Precio_mediana":
        #             tamano = 2
        #         elif tamano == "Precio_familiar":
        #             tamano = 3
        #         adicional = 0
        #         for j in range(0, item.childCount()):
        #             sub_item = item.child(j)
        #             if sub_item.text(2) != "" and "Adicional: " in sub_item.text(1):
        #                 adicional += int(sub_item.text(2))
        #         if len(nombre.split(":")) == 2:
        #             data_boleta.append([None, count_equal_items(self.editor.topLevelItem(i),
        #                                                         tamano, nombre.split(": ")[1], adicional)])
        #         else:
        #             data_boleta.append([nombre, count_equal_items(self.editor.topLevelItem(i),
        #                                                           tamano, None, adicional)])
        if (self.radioButton_efectivo.isChecked() and int(self.lineEdit_efectivo.text()) >= total) or \
                self.radioButton_tarjetas.isChecked():
            if self.is_desacho:
                data_boleta.append([self.zona_despacho, 1, 'Precio_unitario', None])
            data_venta = [nombre_usuario, nombre_cliente, direccion, id_sesion, efectivo]
            set_boleta(data_venta=data_venta, data_boleta=data_boleta)
            self.handlePrint()
            self.Pagar_Dialog.accept()

    def handlePrint(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def tree_to_text(self):
        def item_to_text(item, key):
            data_list = []
            data_list.append(["Nombre: ", self.nombre_cliente, ""])
            data_list.append(["Dirección: ", self.direccion_cliente, ""])
            data_list.append(["Teléfono: ", self.telefono_cliente, ""])
            total = 0
            data_list.append([key, "", item['precio']])
            temp = [[key, "", item['precio']]]
            temp_total = int(item['precio'])
            total += int(item['precio'])
            for e in item['sub_items']:
                if len(e['datos']) > 1:
                    data_list.append(["", e['datos'][0], e['datos'][1]])
                    temp.append(["", e['datos'][0], e['datos'][1]])
                    if e['datos'][1] != '':
                        total += int(e['datos'][1])
                        temp_total += int(e['datos'][1])
                else:
                    data_list.append(["", e['datos'][0], ""])
                    temp.append(["", e['datos'][0], ""])
            if item['cantidad'] > 1:
                data_list += temp * (item['cantidad'] - 1)
                total += temp_total * (item['cantidad'] - 1)
            return data_list, total
        data_list = []
        total = 0
        for key in self.items_boleta.keys():
            values, num_val = item_to_text(self.items_boleta[key], key)
            data_list += values
            total += num_val
            # item = QtWidgets.QTreeWidgetItem(self.editor)
            # item.setText(0, key)
            # item.setText(1, self.items_boleta[key]['precio'])
            # data_list.append([key, "", self.items_boleta[key]['precio']])
            # temp = [[key, "", self.items_boleta[key]['precio']]]
            # temp_total = int(self.items_boleta[key]['precio'])
            # total += int(self.items_boleta[key]['precio'])
            # for e in self.items_boleta[key]['sub_items']:
                # sub_item = QtWidgets.QTreeWidgetItem(item)
                # sub_item.setText(1, self.items_boleta[key]['sub_items']['data'][0])
                # sub_item.setText(2, self.items_boleta[key]['sub_items']['data'][1])
                # sub_item.setText(3, self.items_boleta[key]['sub_items']['data'][2])
                # if len(e['datos']) > 1:
                #     data_list.append(["", e['datos'][0], e['datos'][1]])
                #     temp.append(["", e['datos'][0], e['datos'][1]])
                #     if e['datos'][1] != '':
                #         total += int(e['datos'][1])
                #         temp_total += int(e['datos'][1])
                # else:
                #     data_list.append(["", e['datos'][0], ""])
                #     temp.append(["", e['datos'][0], ""])
            for e in self.items_boleta[key]['otros']:
                values, num_val = item_to_text(e, key)
                data_list += values
                total += num_val
            # if self.items_boleta[key]['cantidad'] > 1:
            #     data_list += temp * (self.items_boleta[key]['cantidad'] - 1)
            #     total += temp_total * (self.items_boleta[key]['cantidad'] - 1)
        self.total = total
        data_list.append(["", "", ""])
        if self.is_desacho or self.is_pedidos_ya:
            if self.is_pedidos_ya:
                data_list.append("Despacho: Pedidos ya! ", "", "")
            else:
                data_list.append("Despacho: " + self.zona_despacho, self.precio_despacho, "")
                total += int(self.precio_despacho)
                self.total = total
        data_list.append(["", "", ""])
        data_list.append(["", "Total", str(total)])
            #     item.addChild(sub_item)
            # self.editor.addTopLevelItem(item)
        # self.editor.setAcceptRichText(True)
        # self.editor.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        string_formated = tabulate(tabular_data=data_list,
                                     headers=["Producto", "Detalle", "Monto"],
                                     tablefmt="html",
                                     colalign=("center","stralign",),
                                     numalign="center")
        # length_margins = string_formated.find("╕")
        print(string_formated)
        # print(length_margins)
        # self.editor.document().setPageSize(QSizeF(0.0, float(length_margins+1)))
        self.editor.document().setDocumentMargin(1)
        self.editor.setHtml(string_formated)
        # self.editor.setText(string_formated)

    def on_text_change(self):
        if self.lineEdit_efectivo.text() != "":
            num = int(self.lineEdit_efectivo.text())
            if num < self.total:
                if self.lineEdit_vuelto.text() != "":
                    self.lineEdit_vuelto.setText("")
            else:
                self.lineEdit_vuelto.setText(str(num - self.total))
