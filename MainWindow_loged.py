# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Main_loged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog

from inicio_session_dialogo import Ui_inicio_session
from Controller import ControlModule

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_name, is_admin):
        self.user_name = user_name
        self.is_admin = is_admin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 815)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 761, 181))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 551, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_Nombre = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_Nombre.setEditable(True)
        self.comboBox_Nombre.setMaxVisibleItems(30)
        self.comboBox_Nombre.setObjectName("comboBox_Nombre")
        self.horizontalLayout.addWidget(self.comboBox_Nombre)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_Direcion = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Direcion.setObjectName("lineEdit_Direcion")
        self.horizontalLayout_3.addWidget(self.lineEdit_Direcion)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_Telefono = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Telefono.setObjectName("lineEdit_Telefono")
        self.horizontalLayout_4.addWidget(self.lineEdit_Telefono)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 20, 180, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Buscar_cliente = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_Buscar_cliente.setObjectName("pushButton_Buscar_cliente")
        self.horizontalLayout_2.addWidget(self.pushButton_Buscar_cliente)
        self.pushButton_Crear_cliente = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_Crear_cliente.setObjectName("pushButton_Crear_cliente")
        self.horizontalLayout_2.addWidget(self.pushButton_Crear_cliente)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.cmb_zona_cliente = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmb_zona_cliente.setEnabled(True)
        self.cmb_zona_cliente.setObjectName("cmb_zona_cliente")
        self.cmb_zona_cliente.addItem("")
        self.cmb_zona_cliente.addItem("")
        self.cmb_zona_cliente.addItem("")
        self.horizontalLayout_8.addWidget(self.cmb_zona_cliente)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioBtn_Pedidos_Ya = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioBtn_Pedidos_Ya.setEnabled(False)
        self.radioBtn_Pedidos_Ya.setObjectName("radioBtn_Pedidos_Ya")
        self.horizontalLayout_7.addWidget(self.radioBtn_Pedidos_Ya)
        self.radioBtn_Despacho = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioBtn_Despacho.setEnabled(False)
        self.radioBtn_Despacho.setObjectName("radioBtn_Despacho")
        self.horizontalLayout_7.addWidget(self.radioBtn_Despacho)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(30, 260, 761, 461))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Pizzas = QtWidgets.QWidget()
        self.tab_Pizzas.setEnabled(True)
        self.tab_Pizzas.setAutoFillBackground(False)
        self.tab_Pizzas.setObjectName("tab_Pizzas")
        self.listPizzas = QtWidgets.QListWidget(self.tab_Pizzas)
        self.listPizzas.setGeometry(QtCore.QRect(0, 20, 751, 411))
        self.listPizzas.setUniformItemSizes(True)
        self.listPizzas.setItemAlignment(QtCore.Qt.AlignLeading)
        self.listPizzas.setObjectName("listPizzas")
        self.radioButton_individual = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_individual.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.radioButton_individual.setObjectName("radioButton_individual")
        self.radioButton_Mediana = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_Mediana.setGeometry(QtCore.QRect(110, 0, 82, 17))
        self.radioButton_Mediana.setObjectName("radioButton_Mediana")
        self.radioButton_Familiar = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_Familiar.setGeometry(QtCore.QRect(210, 0, 82, 17))
        self.radioButton_Familiar.setObjectName("radioButton_Familiar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/pizza_PNG7143.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Pizzas, icon, "")
        self.tab_Empnadas = QtWidgets.QWidget()
        self.tab_Empnadas.setObjectName("tab_Empnadas")
        self.listEmpanadas = QtWidgets.QListWidget(self.tab_Empnadas)
        self.listEmpanadas.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listEmpanadas.setObjectName("listEmpanadas")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/chicken_quesadilla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Empnadas, icon1, "")
        self.tab_Agregados = QtWidgets.QWidget()
        self.tab_Agregados.setObjectName("tab_Agregados")
        self.listAgregados = QtWidgets.QListWidget(self.tab_Agregados)
        self.listAgregados.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listAgregados.setObjectName("listAgregados")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/bbq-ribs-clipart-17336204-an-image-of-barbecue-spare-ribs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Agregados, icon2, "")
        self.tab_Bebidas = QtWidgets.QWidget()
        self.tab_Bebidas.setObjectName("tab_Bebidas")
        self.listBebidas = QtWidgets.QListWidget(self.tab_Bebidas)
        self.listBebidas.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listBebidas.setObjectName("listBebidas")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/3-bebidas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Bebidas, icon3, "")
        self.tab_Promociones = QtWidgets.QWidget()
        self.tab_Promociones.setObjectName("tab_Promociones")
        self.listPromociones = QtWidgets.QListWidget(self.tab_Promociones)
        self.listPromociones.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listPromociones.setObjectName("listPromociones")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/estrella.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Promociones, icon4, "")
        self.pushButton_Pagar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pagar.setGeometry(QtCore.QRect(1080, 732, 81, 31))
        self.pushButton_Pagar.setObjectName("pushButton_Pagar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 1200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\UI\\../Resources/fondo_SDM.jpg"))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 30, 391, 691))
        self.groupBox_2.setObjectName("groupBox_2")
        self.treeView_Venta = QtWidgets.QTreeView(self.groupBox_2)
        self.treeView_Venta.setGeometry(QtCore.QRect(10, 20, 371, 661))
        self.treeView_Venta.setMouseTracking(True)
        self.treeView_Venta.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView_Venta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeView_Venta.setObjectName("treeView_Venta")
        self.label.raise_()
        self.groupBox.raise_()
        self.tabWidget.raise_()
        self.pushButton_Pagar.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdministrar_Sesion = QtWidgets.QMenu(self.menubar)
        self.menuAdministrar_Sesion.setObjectName("menuAdministrar_Sesion")
        self.menuAdministrar_usuarios = QtWidgets.QMenu(self.menubar)
        self.menuAdministrar_usuarios.setObjectName("menuAdministrar_usuarios")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIniciar_Sesion = QtWidgets.QAction(MainWindow)
        self.actionIniciar_Sesion.setObjectName("actionIniciar_Sesion")
        self.actionCerrar_caja = QtWidgets.QAction(MainWindow)
        self.actionCerrar_caja.setObjectName("actionCerrar_caja")
        self.actionCerrar_sesion = QtWidgets.QAction(MainWindow)
        self.actionCerrar_sesion.setObjectName("actionCerrar_sesion")
        self.actionAdministrar_usuarios = QtWidgets.QAction(MainWindow)
        self.actionAdministrar_usuarios.setObjectName("actionAdministrar_usuarios")
        self.actionCrear_usuario = QtWidgets.QAction(MainWindow)
        self.actionCrear_usuario.setObjectName("actionCrear_usuario")
        self.actionModificar_usuario = QtWidgets.QAction(MainWindow)
        self.actionModificar_usuario.setObjectName("actionModificar_usuario")
        self.actionEliminar_usuario = QtWidgets.QAction(MainWindow)
        self.actionEliminar_usuario.setObjectName("actionEliminar_usuario")
        self.actionEditar_productos = QtWidgets.QAction(MainWindow)
        self.actionEditar_productos.setObjectName("actionEditar_productos")
        self.actionEditar_promociones = QtWidgets.QAction(MainWindow)
        self.actionEditar_promociones.setObjectName("actionEditar_promociones")
        self.actionAbrir_caja = QtWidgets.QAction(MainWindow)
        self.actionAbrir_caja.setObjectName("actionAbrir_caja")
        self.menuAdministrar_Sesion.addAction(self.actionIniciar_Sesion)
        self.menuAdministrar_Sesion.addAction(self.actionCerrar_sesion)
        self.menuAdministrar_Sesion.addSeparator()
        self.menuAdministrar_Sesion.addAction(self.actionAbrir_caja)
        self.menuAdministrar_Sesion.addAction(self.actionCerrar_caja)
        self.menuAdministrar_usuarios.addAction(self.actionCrear_usuario)
        self.menuAdministrar_usuarios.addAction(self.actionModificar_usuario)
        self.menuAdministrar_usuarios.addAction(self.actionEliminar_usuario)
        self.menuEditar.addAction(self.actionEditar_productos)
        self.menuEditar.addAction(self.actionEditar_promociones)
        self.menubar.addAction(self.menuAdministrar_Sesion.menuAction())
        self.menubar.addAction(self.menuAdministrar_usuarios.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tabs = {
            "Pizzas": self.tab_Pizzas,
            "Empanadas": self.tab_Empnadas,
            "Agregados": self.tab_Agregados,
            "Bebidas": self.tab_Bebidas,
            "Promociones": self.tab_Promociones
        }

        self.actionIniciar_Sesion.triggered.connect(self.inicio_sesion)
        self.radioBtn_Despacho.clicked.connect(self.on_click_Despacho_RButton)
        self.radioBtn_Pedidos_Ya.clicked.connect(self.on_click_PedidosYa_RButton)
        self.radioBtn_ClearSelection = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioBtn_ClearSelection.setVisible(False)
        self.radioBtn_ClearSelection.setObjectName("radioBtn_ClearSelection")
        self.radioBtn_ClearSelection.setText("")
        self.load_buttons()
        self.tabWidget.setCurrentIndex(0)
        self.is_despacho = False
        self.is_pedidos_ya = False
        self.configure_enabling()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nanny\'s Pizza"))
        self.groupBox.setTitle(_translate("MainWindow", "Cliente"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_3.setText(_translate("MainWindow", "Dirección:"))
        self.label_4.setText(_translate("MainWindow", "Teléfono"))
        self.pushButton_Buscar_cliente.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_Crear_cliente.setText(_translate("MainWindow", "Crear"))
        self.label_7.setText(_translate("MainWindow", "Zona"))
        self.cmb_zona_cliente.setItemText(0, _translate("MainWindow", "1: Cuidad Satélite"))
        self.cmb_zona_cliente.setItemText(1, _translate("MainWindow", "2: Padre Hurtado y otros"))
        self.cmb_zona_cliente.setItemText(2, _translate("MainWindow", "3: Más allá"))
        self.radioBtn_Pedidos_Ya.setText(_translate("MainWindow", "Pedidos Ya!"))
        self.radioBtn_Despacho.setText(_translate("MainWindow", "Despacho"))
        self.radioButton_individual.setText(_translate("MainWindow", "Individual"))
        self.radioButton_Mediana.setText(_translate("MainWindow", "Mediana"))
        self.radioButton_Familiar.setText(_translate("MainWindow", "Familiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Pizzas), _translate("MainWindow", "Pizzas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Empnadas), _translate("MainWindow", "Empanadas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Agregados), _translate("MainWindow", "Agregados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Bebidas), _translate("MainWindow", "Bebidas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Promociones), _translate("MainWindow", "Promociones"))
        self.pushButton_Pagar.setText(_translate("MainWindow", "Pagar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Venta"))
        self.menuAdministrar_Sesion.setTitle(_translate("MainWindow", "Administrar Sesión"))
        self.menuAdministrar_usuarios.setTitle(_translate("MainWindow", "Administrar usuarios"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.actionIniciar_Sesion.setText(_translate("MainWindow", "Iniciar sesión"))
        self.actionCerrar_caja.setText(_translate("MainWindow", "Cerrar caja"))
        self.actionCerrar_sesion.setText(_translate("MainWindow", "Cerrar sesión"))
        self.actionAdministrar_usuarios.setText(_translate("MainWindow", "Administrar usuarios"))
        self.actionCrear_usuario.setText(_translate("MainWindow", "Crear usuario"))
        self.actionModificar_usuario.setText(_translate("MainWindow", "Modificar usuario"))
        self.actionEliminar_usuario.setText(_translate("MainWindow", "Eliminar usuario"))
        self.actionEditar_productos.setText(_translate("MainWindow", "Editar productos"))
        self.actionEditar_promociones.setText(_translate("MainWindow", "Editar promociones"))
        self.actionAbrir_caja.setText(_translate("MainWindow", "Abrir caja"))






    def block_unblock_all(self, operation):
        self.centralwidget.setEnabled(operation)
        self.groupBox.setEnabled(operation)
        self.verticalLayoutWidget.setEnabled(operation)
        self.verticalLayout_2.setEnabled(operation)
        self.horizontalLayout.setEnabled(operation)
        self.label_2.setEnabled(operation)
        self.comboBox_Nombre.setEnabled(operation)
        self.horizontalLayout_3.setEnabled(operation)
        self.label_3.setEnabled(operation)
        self.lineEdit_Direcion.setEnabled(operation)
        self.horizontalLayout_4.setEnabled(operation)
        self.label_4.setEnabled(operation)
        self.lineEdit_Telefono.setEnabled(operation)
        self.verticalLayoutWidget_2.setEnabled(operation)
        self.verticalLayout.setEnabled(operation)
        self.horizontalLayout_2.setEnabled(operation)
        self.pushButton_Buscar_cliente.setEnabled(operation)
        self.pushButton_Crear_cliente.setEnabled(operation)
        self.horizontalLayout_8.setEnabled(operation)
        self.label_7.setEnabled(operation)
        self.cmb_zona_cliente.setEnabled(operation)
        self.horizontalLayout_7.setEnabled(operation)
        self.radioBtn_Pedidos_Ya.setEnabled(operation)
        self.radioBtn_Despacho.setEnabled(operation)
        self.tabWidget.setEnabled(operation)
        self.tab_Pizzas.setEnabled(operation)
        self.tab_Empnadas.setEnabled(operation)
        self.tab_Agregados.setEnabled(operation)
        self.tab_Bebidas.setEnabled(operation)
        self.tab_Promociones.setEnabled(operation)
        self.pushButton_Pagar.setEnabled(operation)
        self.label.setEnabled(operation)
        self.groupBox_2.setEnabled(operation)
        self.treeView_Venta.setEnabled(operation)
        self.menubar.setEnabled(operation)
        self.menuAdministrar_Sesion.setEnabled(operation)
        self.statusbar.setEnabled(operation)
        self.actionIniciar_Sesion.setEnabled(operation)
        self.actionCerrar_caja.setEnabled(operation)
        self.actionCerrar_sesion.setEnabled(operation)
        self.menuAdministrar_usuarios.setEnabled(operation)
        self.menuEditar.setEnabled(operation)

    def configure_enabling(self):
        if self.user_name is None or self.user_name == "":
            self.block_unblock_all(False)
            self.menubar.setEnabled(True)
            self.menuAdministrar_Sesion.setEnabled(True)
            self.actionIniciar_Sesion.setEnabled(True)
        else:
            self.block_unblock_all(True)
            self.actionIniciar_Sesion.setEnabled(False)
            if self.is_admin is False:
                self.menuEditar.setEnabled(False)
                self.menuAdministrar_usuarios.setEnabled(False)

    def inicio_sesion(self):
        if self.user_name is None or self.user_name == "":
            dialog = QDialog()
            dialog.ui = Window()
            dialog.ui.setupUi(dialog)
            dialog.exec()
            globals()['access_token'] = dialog.ui.acces_token
            globals()['user_name'] = dialog.ui.user_name
            globals()['is_admin'] = dialog.ui.user_admin
            self.user_name = globals()['user_name']
            self.is_admin = globals()['is_admin']
            self.configure_enabling()

    def on_click_Despacho_RButton(self):
        print("despacho", self.is_despacho)
        if self.is_despacho:
            if self.radioBtn_Despacho.isChecked():
                self.is_despacho = False
                self.radioBtn_Despacho.setChecked(False)
                self.radioBtn_ClearSelection.setChecked(True)
            else:
                self.is_despacho = True
                self.radioBtn_Despacho.setChecked(True)
                self.radioBtn_Despacho.setFocus(True)
        else:
            self.is_despacho = True
            self.radioBtn_Despacho.setChecked(True)
            self.radioBtn_Despacho.setFocus(True)
        self.radioBtn_Pedidos_Ya.setChecked(False)
        self.radioBtn_Pedidos_Ya.clearMask()
        self.is_pedidos_ya = False
        # self.radioBtn_Despacho.setChecked(self.is_despacho)
        # self.radioBtn_Despacho.setFocus(self.is_despacho)
        print(self.is_despacho)

    def on_click_PedidosYa_RButton(self):
        print("pedidos ya", self.is_pedidos_ya)
        if self.is_pedidos_ya:
            if self.radioBtn_Pedidos_Ya.isChecked():
                self.is_pedidos_ya = False
                self.radioBtn_Pedidos_Ya.setChecked(False)
                self.radioBtn_ClearSelection.setChecked(True)
            else:
                self.is_pedidos_ya = True
                self.radioBtn_Pedidos_Ya.setChecked(True)
                self.radioBtn_Pedidos_Ya.setFocus(True)
        else:
            self.is_pedidos_ya = True
            self.radioBtn_Pedidos_Ya.setChecked(True)
            self.radioBtn_Pedidos_Ya.setFocus(True)
        self.radioBtn_Despacho.setChecked(False)
        self.is_despacho = False
        self.radioBtn_Despacho.clearMask()
        # self.radioBtn_Pedidos_Ya.setFocus(self.is_pedidos_ya)
        print(self.is_pedidos_ya)

    def load_buttons(self):
        """
        """
        productos = ControlModule.get_Productos()
        for producto in productos:
            categoria = producto['Categoria']
            if categoria == 'Pizzas':
                self.listPizzas.addItem(producto['Nombre_producto'])
            elif categoria == 'Empanadas':
                self.listEmpanadas.addItem(producto['Nombre_producto'])
            elif categoria == 'Agregados':
                self.listAgregados.addItem(producto['Nombre_producto'])
            elif categoria == 'Bebidas':
                self.listBebidas.addItem(producto['Nombre_producto'])


class Window(QMainWindow, Ui_inicio_session):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

