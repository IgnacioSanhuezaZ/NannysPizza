# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '.\UI\Main_loged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox

from inicio_session_dialogo import Ui_inicio_session
from edicion_producto_boleta_dialogo import Ui_Dialog as Ui_edicion_producto_boleta
from file_browser_dialog import Ui_file_browser_Dialog
from seleccion_promo_prduct_Dialog import Ui_sub_cathegory_promo_select
from pagar_Dialog import Ui_Pagar_Dialog
from Aniadir_usuario_Dialog import Ui_Dialog as Ui_Aniadir_Usuario_Dialog
from Modificar_usuario_Dialog import Ui_Dialog as Ui_Modificar_Usuario_Dialog
from Eliminar_usuario_Dialog import Ui_Dialog as Ui_Eliminar_Usuario_Dialog
from añadir_comentario_Dialog import Ui_Dialog as Ui_añadir_comentario
from añadir_ingrediente_Dialog import Ui_Dialog as Ui_añadir_ingrediente
from Aniadir_retiro_Dialog import Ui_Dialog as Ui_Aniadir_Retiro_Dialog
from Export_boletin_fechas_Dialog import Ui_Dialog as UI_Export_Boletin_Fechas_Dialog
from Controller import ControlModule

from numpy import genfromtxt
import datetime


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, user_name, is_admin):
        self.MainWindow = MainWindow
        self.user_name = user_name
        self.is_admin = is_admin
        self.caja_abierta = False
        self.id_session = None
        self.boleta = None
        self.promociones = None
        self.nombre_cliente = None
        self.is_despacho = False
        self.is_pedidos_ya = False
        self.clientes_en_memoria = {}
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
        self.comboBox_Nombre = CustomCombo(self.verticalLayoutWidget)
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
        self.radioButton_individual = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_individual.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.radioButton_individual.setObjectName("radioButton_individual")
        self.radioButton_Mediana = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_Mediana.setGeometry(QtCore.QRect(110, 0, 82, 17))
        self.radioButton_Mediana.setObjectName("radioButton_Mediana")
        self.radioButton_Familiar = QtWidgets.QRadioButton(self.tab_Pizzas)
        self.radioButton_Familiar.setGeometry(QtCore.QRect(210, 0, 82, 17))
        self.radioButton_Familiar.setObjectName("radioButton_Familiar")
        self.listPizzas = QtWidgets.QListWidget(self.tab_Pizzas)
        self.listPizzas.setGeometry(QtCore.QRect(0, 20, 761, 411))
        self.listPizzas.setObjectName("listPizzas")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/pizza_PNG7143.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Pizzas, icon, "")
        self.tab_Empnadas = QtWidgets.QWidget()
        self.tab_Empnadas.setObjectName("tab_Empnadas")
        self.listEmpanadas = QtWidgets.QListWidget(self.tab_Empnadas)
        self.listEmpanadas.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listEmpanadas.setObjectName("listEmpanadas")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/chicken_quesadilla.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Empnadas, icon1, "")
        self.tab_Agregados = QtWidgets.QWidget()
        self.tab_Agregados.setObjectName("tab_Agregados")
        self.listAgregados = QtWidgets.QListWidget(self.tab_Agregados)
        self.listAgregados.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.listAgregados.setObjectName("listAgregados")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(".\\UI\\../Resources/bbq-ribs-clipart-17336204-an-image-of-barbecue-spare-ribs.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.listPromociones.setGeometry(QtCore.QRect(0, -1, 761, 431))
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
        self.treeView_Venta = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeView_Venta.setGeometry(QtCore.QRect(10, 20, 371, 631))
        self.treeView_Venta.setMouseTracking(True)
        self.treeView_Venta.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView_Venta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeView_Venta.setObjectName("treeView_Venta")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_Venta.sizePolicy().hasHeightForWidth())
        self.treeView_Venta.setSizePolicy(sizePolicy)
        self.treeView_Venta.setColumnCount(3)
        self.treeView_Venta.header().setMinimumSectionSize(100)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 660, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_Total = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Total.setGeometry(QtCore.QRect(80, 660, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Total.setFont(font)
        self.lineEdit_Total.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_Total.setReadOnly(True)
        self.lineEdit_Total.setObjectName("lineEdit_Total")
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
        self.menuEditar_productos = QtWidgets.QMenu(self.menuEditar)
        self.menuEditar_productos.setObjectName("menuEditar_productos")
        self.menuEditar_promociones = QtWidgets.QMenu(self.menuEditar)
        self.menuEditar_promociones.setObjectName("menuEditar_promociones")
        self.menuBolet_n = QtWidgets.QMenu(self.menubar)
        self.menuBolet_n.setObjectName("menuBolet_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIniciar_Sesion = QtWidgets.QAction(MainWindow)
        self.actionIniciar_Sesion.setObjectName("actionIniciar_Sesion")
        self.actionIngresarRetiro = QtWidgets.QAction(MainWindow)
        self.actionIngresarRetiro.setObjectName("actionIngresarRetiro")
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
        self.actionAbrir_caja = QtWidgets.QAction(MainWindow)
        self.actionAbrir_caja.setObjectName("actionAbrir_caja")
        self.actionEditar_un_producto = QtWidgets.QAction(MainWindow)
        self.actionEditar_un_producto.setObjectName("actionEditar_un_producto")
        self.actionSubir_CSV_con_lista_de_productos = QtWidgets.QAction(MainWindow)
        self.actionSubir_CSV_con_lista_de_productos.setObjectName("actionSubir_CSV_con_lista_de_productos")
        self.actionSubir_CSV_con_lista_de_promociones = QtWidgets.QAction(MainWindow)
        self.actionSubir_CSV_con_lista_de_promociones.setObjectName("actionSubir_CSV_con_lista_de_promociones")
        self.actionAgregar_promoci_n = QtWidgets.QAction(MainWindow)
        self.actionAgregar_promoci_n.setObjectName("actionAgregar_promoci_n")
        self.actionEditar_promoci_n = QtWidgets.QAction(MainWindow)
        self.actionEditar_promoci_n.setObjectName("actionEditar_promoci_n")
        self.actionEliminar_promoci_n = QtWidgets.QAction(MainWindow)
        self.actionEliminar_promoci_n.setObjectName("actionEliminar_promoci_n")
        self.actionA_adir_un_producto = QtWidgets.QAction(MainWindow)
        self.actionA_adir_un_producto.setObjectName("actionA_adir_un_producto")
        self.actionEliminar_un_producto = QtWidgets.QAction(MainWindow)
        self.actionEliminar_un_producto.setObjectName("actionEliminar_un_producto")
        self.actionGenerar_bolet_n_de_ventas_del_d_a = QtWidgets.QAction(MainWindow)
        self.actionGenerar_bolet_n_de_ventas_del_d_a.setObjectName("actionGenerar_bolet_n_de_ventas_del_d_a")
        self.actionGenerar_bolet_n_de_ventas_del_mes = QtWidgets.QAction(MainWindow)
        self.actionGenerar_bolet_n_de_ventas_del_mes.setObjectName("actionGenerar_bolet_n_de_ventas_del_mes")
        self.actionGenerar_bolet_n_de_ventas_del_total = QtWidgets.QAction(MainWindow)
        self.actionGenerar_bolet_n_de_ventas_del_total.setObjectName("actionGenerar_bolet_n_de_ventas_del_total")
        self.menuAdministrar_Sesion.addAction(self.actionIniciar_Sesion)
        self.menuAdministrar_Sesion.addAction(self.actionCerrar_sesion)
        self.menuAdministrar_Sesion.addSeparator()
        self.menuAdministrar_Sesion.addAction(self.actionAbrir_caja)
        self.menuAdministrar_Sesion.addAction(self.actionCerrar_caja)
        self.menuAdministrar_Sesion.addSeparator()
        self.menuAdministrar_Sesion.addAction(self.actionIngresarRetiro)
        self.menuAdministrar_usuarios.addAction(self.actionCrear_usuario)
        self.menuAdministrar_usuarios.addAction(self.actionModificar_usuario)
        self.menuAdministrar_usuarios.addAction(self.actionEliminar_usuario)
        self.menuEditar_productos.addAction(self.actionA_adir_un_producto)
        self.menuEditar_productos.addAction(self.actionSubir_CSV_con_lista_de_productos)
        self.menuEditar_productos.addAction(self.actionEditar_un_producto)
        self.menuEditar_productos.addAction(self.actionEliminar_un_producto)
        self.menuEditar_promociones.addAction(self.actionAgregar_promoci_n)
        self.menuEditar_promociones.addAction(self.actionSubir_CSV_con_lista_de_promociones)
        self.menuEditar_promociones.addAction(self.actionEditar_promoci_n)
        self.menuEditar_promociones.addAction(self.actionEliminar_promoci_n)
        self.menuEditar.addAction(self.menuEditar_productos.menuAction())
        self.menuEditar.addAction(self.menuEditar_promociones.menuAction())
        self.menuBolet_n.addAction(self.actionGenerar_bolet_n_de_ventas_del_d_a)
        self.menuBolet_n.addAction(self.actionGenerar_bolet_n_de_ventas_del_mes)
        self.menuBolet_n.addAction(self.actionGenerar_bolet_n_de_ventas_del_total)
        self.menubar.addAction(self.menuAdministrar_Sesion.menuAction())
        self.menubar.addAction(self.menuAdministrar_usuarios.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuBolet_n.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tabs = {
            "Pizzas": self.tab_Pizzas,
            "Empanadas": self.tab_Empnadas,
            "Agregados": self.tab_Agregados,
            "Bebidas": self.tab_Bebidas,
            "Promociones": self.tab_Promociones
        }

        int_only = QtGui.QIntValidator(self.lineEdit_Telefono)
        int_only.setBottom(0)
        self.lineEdit_Telefono.setValidator(int_only)
        int_only2 = QtGui.QIntValidator(self.lineEdit_Total)
        int_only2.setBottom(0)
        self.lineEdit_Total.setValidator(int_only2)

        self.accion_editar = QtWidgets.QAction("Editar producto", self.treeView_Venta)
        self.accion_ingrediente = QtWidgets.QAction("Agregar ingrediente", self.treeView_Venta)
        self.accion_comentario = QtWidgets.QAction("Agregar comentario", self.treeView_Venta)

        self.actionSubir_CSV_con_lista_de_productos.triggered.connect(self.on_click_action_agregar_productos_CSV)
        self.actionSubir_CSV_con_lista_de_promociones.triggered.connect(self.on_click_action_agregar_promociones_CSV)
        self.accion_editar.triggered.connect(self.on_click_action_editar)
        self.accion_ingrediente.triggered.connect(self.on_click_action_ingrediente)
        self.accion_comentario.triggered.connect(self.on_click_action_comentario)
        self.actionIniciar_Sesion.triggered.connect(self.inicio_sesion)
        self.actionCerrar_sesion.triggered.connect(self.cierre_sesion)
        self.actionCerrar_caja.triggered.connect(self.cerrar_caja)
        self.actionAbrir_caja.triggered.connect(self.abrir_caja)
        self.actionCrear_usuario.triggered.connect(self.crear_usuario)
        self.actionModificar_usuario.triggered.connect(self.modificar_usuario)
        self.actionEliminar_usuario.triggered.connect(self.eliminar_usuario)
        self.actionIngresarRetiro.triggered.connect(self.registrar_Retiro)
        self.actionGenerar_bolet_n_de_ventas_del_total.triggered.connect(self.on_click_action_boletin_fechas)
        self.radioBtn_Despacho.clicked.connect(self.on_click_Despacho_RButton)
        self.radioBtn_Pedidos_Ya.clicked.connect(self.on_click_PedidosYa_RButton)
        self.listPizzas.doubleClicked.connect(self.on_double_click_Pizzas)
        self.listAgregados.doubleClicked.connect(self.on_double_click_Agregados)
        self.listEmpanadas.doubleClicked.connect(self.on_double_click_Empanadas)
        self.listBebidas.doubleClicked.connect(self.on_double_click_Bebidas)
        self.listPromociones.doubleClicked.connect(self.on_double_click_Promociones)
        self.treeView_Venta.doubleClicked.connect(self.On_ventas_tree_double_click)
        self.pushButton_Buscar_cliente.clicked.connect(self.on_click_buscar)
        self.comboBox_Nombre.enter_pressed.connect(self.on_click_buscar)
        self.comboBox_Nombre.currentIndexChanged.connect(self.on_index_change_nombre)
        self.cmb_zona_cliente.currentIndexChanged.connect(self.on_zone_change)
        self.pushButton_Crear_cliente.clicked.connect(self.on_click_crear)
        self.pushButton_Pagar.clicked.connect(self.on_click_pagar)
        self.radioBtn_ClearSelection = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioBtn_ClearSelection.setVisible(False)
        self.radioBtn_ClearSelection.setObjectName("radioBtn_ClearSelection")
        self.radioBtn_ClearSelection.setText("")
        self.load_buttons()
        self.load_tree()
        self.tabWidget.setCurrentIndex(0)
        self.radioButton_individual.setChecked(True)
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
        self.treeView_Venta.headerItem().setText(0, _translate("MainWindow", "Producto"))
        self.treeView_Venta.headerItem().setText(1, _translate("MainWindow", "Detalle"))
        self.treeView_Venta.headerItem().setText(2, _translate("MainWindow", "Cobros extra"))
        self.label_5.setText(_translate("MainWindow", "Total:"))
        self.lineEdit_Total.setText(_translate("MainWindow", "0"))
        self.menuAdministrar_Sesion.setTitle(_translate("MainWindow", "Administrar Sesión"))
        self.menuAdministrar_usuarios.setTitle(_translate("MainWindow", "Administrar usuarios"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuEditar_productos.setTitle(_translate("MainWindow", "Editar productos"))
        self.menuEditar_promociones.setTitle(_translate("MainWindow", "Editar promociones"))
        self.menuBolet_n.setTitle(_translate("MainWindow", "Administrar finanzas"))
        self.actionIniciar_Sesion.setText(_translate("MainWindow", "Iniciar sesión"))
        self.actionCerrar_caja.setText(_translate("MainWindow", "Cerrar caja"))
        self.actionCerrar_sesion.setText(_translate("MainWindow", "Cerrar sesión"))
        self.actionAdministrar_usuarios.setText(_translate("MainWindow", "Administrar usuarios"))
        self.actionCrear_usuario.setText(_translate("MainWindow", "Crear usuario"))
        self.actionModificar_usuario.setText(_translate("MainWindow", "Modificar usuario"))
        self.actionEliminar_usuario.setText(_translate("MainWindow", "Eliminar usuario"))
        self.actionAbrir_caja.setText(_translate("MainWindow", "Abrir caja"))
        self.actionEditar_un_producto.setText(_translate("MainWindow", "Editar un producto"))
        self.actionSubir_CSV_con_lista_de_productos.setText(
            _translate("MainWindow", "Subir CSV con lista de productos"))
        self.actionSubir_CSV_con_lista_de_promociones.setText(
            _translate("MainWindow", "Subir CSV con lista de promociones"))
        self.actionAgregar_promoci_n.setText(_translate("MainWindow", "Agregar promoción"))
        self.actionEditar_promoci_n.setText(_translate("MainWindow", "Editar promoción"))
        self.actionEliminar_promoci_n.setText(_translate("MainWindow", "Eliminar promoción"))
        self.actionA_adir_un_producto.setText(_translate("MainWindow", "Añadir un producto"))
        self.actionEliminar_un_producto.setText(_translate("MainWindow", "Eliminar un producto"))
        self.actionGenerar_bolet_n_de_ventas_del_d_a.setText(
            _translate("MainWindow", "Generar boletín de ventas del día"))
        self.actionGenerar_bolet_n_de_ventas_del_mes.setText(
            _translate("MainWindow", "Generar boletín de ventas del mes"))
        self.actionGenerar_bolet_n_de_ventas_del_total.setText(
            _translate("MainWindow", "Generar boletín de ventas por fechas"))
        self.actionIngresarRetiro.setText(
            _translate("MainWindow", "Ingresar retiro"))

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
        self.menuBolet_n.setEnabled(operation)
        self.actionIngresarRetiro.setEnabled(operation)

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
                self.menuBolet_n.setEnabled(False)
            if self.caja_abierta:
                self.actionAbrir_caja.setEnabled(False)
            else:
                self.actionCerrar_caja.setEnabled(False)

    def inicio_sesion(self):
        if self.user_name is None or self.user_name == "":
            dialog = QDialog()
            dialog.ui = Inicio_session_Dialog()
            dialog.ui.setupUi(dialog)
            ret = dialog.exec()
            if ret == dialog.Accepted:
                globals()['access_token'] = True
                globals()['user_name'] = dialog.ui.user_name
                globals()['is_admin'] = dialog.ui.user_admin
                self.user_name = globals()['user_name']
                self.is_admin = globals()['is_admin']
                self.get_info_last_sesion()
                if not self.caja_abierta:
                    self.abrir_caja()
                self.configure_enabling()
            else:
                globals()['access_token'] = False

    def cierre_sesion(self):
        dialog = QtWidgets.QMessageBox
        ret = dialog.question(self, '¿Estás segura de querer cerrar sesión?', "Cierre de sesión", dialog.Ok | dialog.No)
        if ret == dialog.Ok:
            if self.caja_abierta:
                ret = dialog.question(self, '¿Estás segura de querer cerrar sesión sin cerrar la caja antes?',
                                      "Cierre de sesión",
                                      dialog.Ok | dialog.No)
                if ret == dialog.Ok:
                    self.cerrar_caja()
            globals()['access_token'] = False
            globals()['user_name'] = None
            globals()['is_admin'] = False
            self.user_name = None
            self.is_admin = False
            self.configure_enabling()

    def buscar_archivo(self, titulo=""):
        dialog = QDialog()
        dialog.ui = Buscador_archvos()
        files = dialog.ui.setupUi(titulo)
        return files

    def crear_usuario(self):
        dialog = QDialog()
        dialog.ui = Crear_Usuario_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.show()
        return

    def modificar_usuario(self):
        dialog = QDialog()
        dialog.ui = Modificar_Usuario_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.show()
        return

    def eliminar_usuario(self):
        dialog = QDialog()
        dialog.ui = Eliminar_Usuario_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.show()
        return

    def abrir_caja(self):
        last_session = ControlModule.getLastSession()
        if last_session:
            id = last_session['Id_sesion']
            if last_session['Cerrado'] == 1:
                """Nombre_usuario (fk_Usuarios), Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre"""
                nombre = globals()['user_name']
                cerrado = 0
                fecha_apertura = datetime.datetime.now().date().isoformat().split("-")
                fecha_apertura = fecha_apertura[0] + fecha_apertura[1] + fecha_apertura[2]
                fecha_apertura = int(fecha_apertura)
                apertura_caja = last_session['monto_cierre']
                values = [nombre, cerrado, fecha_apertura, None, apertura_caja, None]
                ControlModule.set_session(values)
                id += 1
                """Keys: Id_sesion (fk_Sesiones), Nombre_usuario (fk_Usuarios)"""
                values = [id, nombre]
                ControlModule.set_turno(values)
            else:
                nombre = globals()['user_name']
                values = [id, nombre]
                ControlModule.set_turno(values)
            self.id_session = id
            self.caja_abierta = True
            self.actionCerrar_caja.setEnabled(True)
            self.actionAbrir_caja.setEnabled(False)
        else:
            if 'user_name' not in globals():
                self.inicio_sesion()
                if 'user_name' not in globals():
                    self.MainWindow.close()
                    sys.exit(0)
            nombre = globals()['user_name']
            cerrado = 0
            fecha_apertura = datetime.datetime.now().date().isoformat().split("-")
            fecha_apertura = fecha_apertura[0] + fecha_apertura[1] + fecha_apertura[2]
            fecha_apertura = int(fecha_apertura)
            apertura_caja = 0
            values = [nombre, cerrado, fecha_apertura, None, apertura_caja, None]
            ControlModule.set_session(values)
    def registrar_Retiro(self):
        dialog = QDialog()
        dialog.ui = Aniadir_Retiro_Dialog()
        dialog.ui.setupUi(dialog)
        rec = dialog.exec()

    def cerrar_caja(self):
        last_session = ControlModule.getLastSession()
        if last_session:
            id = last_session['Id_sesion']
            dialog = QtWidgets.QMessageBox
            ret = dialog.question(self, "Cierre de caja", '¿Desea ingresar retiros de efectivo?',
                                  dialog.Ok | dialog.No)
            if ret == dialog.Ok:
                self.registrar_Retiro()
            if last_session['Cerrado'] == 0:
                """tuple(Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre, Id_sesion)"""
                nombre = globals()['user_name']
                cerrado = 1
                fecha_apertura = last_session['Fecha_apertura']
                fecha_cierre = datetime.datetime.now().date().isoformat().split("-")
                fecha_cierre = fecha_cierre[0] + fecha_cierre[1] + fecha_cierre[2]
                fecha_cierre = int(fecha_cierre)
                apertura_caja = last_session['Apertura_caja']
                rec, ret, total, efectivo = ControlModule.Calculate_end_session(id)
                monto_cierre = apertura_caja + efectivo
                """tuple(Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre, Id_sesion)"""
                values = [nombre, cerrado, fecha_apertura, fecha_cierre, apertura_caja, monto_cierre, id]
                ControlModule.update_session(values)
                self.id_session = None
                self.caja_abierta = False
                self.user_name = None
                self.is_admin = False
                self.configure_enabling()
                self.actionAbrir_caja.setEnabled(True)
            else:
                self.caja_abierta = False
                self.cierre_sesion()
                self.actionAbrir_caja.setEnabled(True)
                self.actionCerrar_caja.setEnabled(False)

    def get_info_last_sesion(self):
        last_session = ControlModule.getLastSession()  # type: list
        if last_session and 'Fecha_cierre' in last_session:
            if last_session['Fecha_cierre'] is None:
                self.caja_abierta = True
            else:
                self.caja_abierta = False
            self.id_session = last_session['Id_sesion']

    def on_change_tree(self):
        total = 0
        for i in range(self.treeView_Venta.topLevelItemCount()):
            total += int(self.treeView_Venta.topLevelItem(i).text(1))
            if self.treeView_Venta.topLevelItem(i).childCount() > 0:
                for j in range(self.treeView_Venta.topLevelItem(i).childCount()):
                    if "Agregado: " in self.treeView_Venta.topLevelItem(i).child(j).text(1):
                        total += int(self.treeView_Venta.topLevelItem(i).child(j).text(2))
                    elif self.treeView_Venta.topLevelItem(i).child(j).childCount() > 0:
                        for k in range(self.treeView_Venta.topLevelItem(i).child(j).childCount()):
                            if "Agregado: " in self.treeView_Venta.topLevelItem(i).child(j).child(k).text(1):
                                total += int(self.treeView_Venta.topLevelItem(i).child(j).child(k).text(2))
        self.lineEdit_Total.setText(str(total))

    def on_double_click_Pizzas(self, index: QModelIndex):
        nombre_producto = self.listPizzas.item(index.row()).text()
        prod = ControlModule.get_Producto(nombre_producto)
        if prod:
            precio = None
            if self.radioButton_individual.isChecked():
                precio = prod[0]['Precio_unitario']
                tamano = "Precio_unitario"
                tamano_str = " Individual"
            elif self.radioButton_Mediana.isChecked():
                precio = prod[0]['Precio_mediana']
                tamano = "Precio_mediana"
                tamano_str = " Mediana"
            elif self.radioButton_Familiar.isChecked():
                precio = prod[0]['Precio_familiar']
                tamano = "Precio_familiar"
                tamano_str = " Familiar"
            es_cuatro_estaciones = False
            if nombre_producto == 'Cuatro Estaciones':
                es_cuatro_estaciones = True
                rec, nombres_a_agregar = self.cuatro_estaciones()
            if (es_cuatro_estaciones and rec == 1) or not es_cuatro_estaciones:
                if self.is_despacho or self.is_pedidos_ya:
                    despacho_item = self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
                else:
                    despacho_item = None
                item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                if es_cuatro_estaciones:
                    for e in nombres_a_agregar:
                        new_item = QtWidgets.QTreeWidgetItem(item)
                        new_item.setText(1, e)
                        item.addChild(new_item)
                item.setText(0, nombre_producto + " - " + tamano_str)
                if precio is None:
                    precio = 0
                item.setText(1, str(precio))
                item.setText(3, tamano)
                self.treeView_Venta.addTopLevelItem(item)
                if despacho_item:
                    item_despacho = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                    item_despacho.setText(0, despacho_item.text(0))
                    item_despacho.setText(1, despacho_item.text(1))
                    self.treeView_Venta.addTopLevelItem(item_despacho)
                    del despacho_item
                self.treeView_Venta.expandAll()
                self.on_change_tree()

    def cuatro_estaciones(self):
        nombres = ['Champiñon', 'Jardinera', 'Española', 'Italiana']
        dialog = QDialog()
        dialog.ui = Select_promo_component()
        dialog.ui.setupUi(dialog, nombre=nombres, cantidad=4, por_categoria=False)
        dialog.setWindowTitle("Escoja el producto de la promoción")
        rec = dialog.exec()
        out = []
        if rec == 1:
            for i in range(dialog.ui.listSeleccion.count()):
                name_item = dialog.ui.listSeleccion.item(i)
                out.append(name_item.text())
        return rec, out

    def on_double_click_Agregados(self, index: QModelIndex):
        nombre_producto = self.listAgregados.item(index.row()).text()
        prod = ControlModule.get_Producto(nombre_producto)
        if prod:
            precio = prod[0]['Precio_unitario']
            if self.is_despacho or self.is_pedidos_ya:
                despacho_item = self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
            else:
                despacho_item = None
            item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
            item.setText(0, nombre_producto)
            if precio is None:
                precio = 0
            item.setText(1, str(precio))
            item.setText(3, "Precio_unitario")
            self.treeView_Venta.addTopLevelItem(item)
            if despacho_item:
                item_despacho = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item_despacho.setText(0, despacho_item.text(0))
                item_despacho.setText(1, despacho_item.text(1))
                self.treeView_Venta.addTopLevelItem(item_despacho)
                del despacho_item
            self.treeView_Venta.expandAll()
            self.on_change_tree()

    def on_double_click_Empanadas(self, index: QModelIndex):
        nombre_producto = self.listEmpanadas.item(index.row()).text()
        prod = ControlModule.get_Producto(nombre_producto)
        if prod:
            precio = prod[0]['Precio_unitario']
            if self.is_despacho or self.is_pedidos_ya:
                despacho_item = self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
            else:
                despacho_item = None
            item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
            item.setText(0, nombre_producto)
            if precio is None:
                precio = 0
            item.setText(1, str(precio))
            item.setText(3, "Precio_unitario")
            self.treeView_Venta.addTopLevelItem(item)
            if despacho_item:
                item_despacho = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item_despacho.setText(0, despacho_item.text(0))
                item_despacho.setText(1, despacho_item.text(1))
                self.treeView_Venta.addTopLevelItem(item_despacho)
                del despacho_item
            self.treeView_Venta.expandAll()
            self.on_change_tree()

    def on_double_click_Bebidas(self, index: QModelIndex):
        nombre_producto = self.listBebidas.item(index.row()).text()
        prod = ControlModule.get_Producto(nombre_producto)
        if prod:
            precio = prod[0]['Precio_unitario']
            if self.is_despacho or self.is_pedidos_ya:
                despacho_item = self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
            else:
                despacho_item = None
            item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
            item.setText(0, nombre_producto)
            if precio is None:
                precio = 0
            item.setText(1, str(precio))
            item.setText(3, "Precio_unitario")
            self.treeView_Venta.addTopLevelItem(item)
            if despacho_item:
                item_despacho = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item_despacho.setText(0, despacho_item.text(0))
                item_despacho.setText(1, despacho_item.text(1))
                self.treeView_Venta.addTopLevelItem(item_despacho)
                del despacho_item
            self.treeView_Venta.expandAll()
            self.on_change_tree()

    def on_double_click_Promociones(self, index: QModelIndex):
        nombre_promocion = self.listPromociones.item(index.row()).text()
        prod = ControlModule.get_Promocion(nombre_promocion)
        items_a_ingresar = []
        if prod:
            precio = prod[0]['precio']
            tamano = prod[0]['Tamano']
            componentes = prod[0]['Componentes']
            # cantidad = np.array([dictio['Cantidad'] for dictio in componentes]).sum()
            for componente in componentes:
                cantidad = componente['Cantidad']
                if componente['Sub_categoria']:
                    nombres = componente['Sub_categoria']
                else:
                    nombres = componente['Nombre_Producto']
                por_categoria = componente['Sub_categoria'] is not None and componente['Sub_categoria'] != ""
                dialog = QDialog()
                dialog.ui = Select_promo_component()
                dialog.ui.setupUi(dialog, nombre=[nombres], cantidad=cantidad, por_categoria=por_categoria)
                dialog.setWindowTitle("Escoja el producto de la promoción")
                rec = dialog.exec()
                if rec == 1:
                    if componente['Nombre_Producto'] is not None:
                        nombre_categoria = ControlModule.get_Producto(componente['Nombre_Producto'])[0]['Categoria']
                    else:
                        nombre_categoria = ""
                    if (por_categoria and componente['Sub_categoria'] != 'Bebidas 1 1/2') or \
                            (nombre_categoria != "" and nombre_categoria == "Pizzas"):
                        if tamano == 1:
                            tamano_str = " Individual"
                        elif tamano == 2:
                            tamano_str = " Mediana"
                        elif tamano == 3:
                            tamano_str = " Familiar"
                    else:
                        tamano_str = ""
                    items_a_ingresar += [e + tamano_str for e in dialog.ui.nombre]

            if self.is_despacho or self.is_pedidos_ya:
                despacho_item = self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
            else:
                despacho_item = None
            item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
            item.setText(0, "Promoción: " + nombre_promocion)
            if precio is None:
                precio = 0
            item.setText(1, str(precio))
            item.setText(3, str(tamano))
            for nombre in items_a_ingresar:
                sub_item = QtWidgets.QTreeWidgetItem(item)
                sub_item.setText(1, nombre)
                item.addChild(sub_item)
            self.treeView_Venta.addTopLevelItem(item)
            if despacho_item:
                item_despacho = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item_despacho.setText(0, despacho_item.text(0))
                item_despacho.setText(1, despacho_item.text(1))
                self.treeView_Venta.addTopLevelItem(item_despacho)
                del despacho_item
            self.treeView_Venta.expandAll()
            self.on_change_tree()

    def On_ventas_tree_double_click(self, index: QtCore.QModelIndex):
        if self.is_despacho or self.is_pedidos_ya:
            if index.row() == self.treeView_Venta.topLevelItemCount()-1:
                return
        self.treeView_Venta.takeTopLevelItem(index.row())
        self.on_change_tree()

    def on_zone_change(self):
        new_zone = self.cmb_zona_cliente.currentText()
        despachos = ControlModule.get_Producto(new_zone)
        if self.is_despacho:
            precio = despachos[0]['Precio_unitario']
            self.treeView_Venta.topLevelItem(self.treeView_Venta.topLevelItemCount()-1).setText(0, "Despacho: " + new_zone)
            self.treeView_Venta.topLevelItem(self.treeView_Venta.topLevelItemCount()-1).setText(1, str(precio))
            self.on_change_tree()

    def on_click_Despacho_RButton(self):
        if self.is_despacho:
            if self.radioBtn_Despacho.isChecked():
                self.is_despacho = False
                self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
                self.on_change_tree()
                self.radioBtn_Despacho.setChecked(False)
                self.radioBtn_ClearSelection.setChecked(True)
            else:
                self.is_despacho = True
                nombre_zona = self.cmb_zona_cliente.currentText()
                zona = ControlModule.get_Producto(nombre_zona)
                if zona:
                    precio_despacho = zona[0]['Precio_unitario']
                    if self.is_pedidos_ya:
                        self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount() - 1)
                    item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                    item.setText(0, "Despacho: " + nombre_zona)
                    item.setText(1, str(precio_despacho))
                    self.treeView_Venta.addTopLevelItem(item)
                    self.on_change_tree()
                self.radioBtn_Despacho.setChecked(True)
        else:
            self.is_despacho = True
            nombre_zona = self.cmb_zona_cliente.currentText()
            zona = ControlModule.get_Producto(nombre_zona)
            if zona:
                precio_despacho = zona[0]['Precio_unitario']
                if self.is_pedidos_ya:
                    self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount() - 1)
                item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item.setText(0, "Despacho: " + nombre_zona)
                item.setText(1, str(precio_despacho))
                self.treeView_Venta.addTopLevelItem(item)
                self.on_change_tree()
            self.radioBtn_Despacho.setChecked(True)
        self.radioBtn_Pedidos_Ya.setChecked(False)
        self.radioBtn_Pedidos_Ya.clearMask()
        self.is_pedidos_ya = False

    def on_click_PedidosYa_RButton(self):
        if self.is_pedidos_ya:
            if self.radioBtn_Pedidos_Ya.isChecked():
                self.is_pedidos_ya = False
                self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount()-1)
                self.on_change_tree()
                self.radioBtn_Pedidos_Ya.setChecked(False)
                self.radioBtn_ClearSelection.setChecked(True)
            else:
                self.is_pedidos_ya = True
                if self.is_despacho:
                    self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount() - 1)
                item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
                item.setText(0, "Despacho: Pedidos Ya!")
                item.setText(1, "0")
                self.treeView_Venta.addTopLevelItem(item)
                self.on_change_tree()
                self.radioBtn_Pedidos_Ya.setChecked(True)
        else:
            self.is_pedidos_ya = True
            if self.is_despacho:
                self.treeView_Venta.takeTopLevelItem(self.treeView_Venta.topLevelItemCount() - 1)
            item = QtWidgets.QTreeWidgetItem(self.treeView_Venta)
            item.setText(0, "Despacho: Pedidos Ya!")
            item.setText(1, "0")
            self.treeView_Venta.addTopLevelItem(item)
            self.on_change_tree()
            self.radioBtn_Pedidos_Ya.setChecked(True)
        self.radioBtn_Despacho.setChecked(False)
        self.is_despacho = False
        self.radioBtn_Despacho.clearMask()

    # def on_nombre_change(self, value):
    #     print(value)
    #     QInputMethodQueryEvent(QtCore.Qt.InputMethodQuery.ImEnterKeyType, QVariant(value))
    #     key_event = QKeyEvent(QEvent(7), , "\n", False, 0)
    #     self.comboBox_Nombre.keyReleaseEvent(key_event)
    #     if value != self.nombre_cliente:
    #         self.nombre_cliente = value
    #     else:
    #         self.on_click_buscar()

    def on_index_change_nombre(self):
        text = self.comboBox_Nombre.itemText(self.comboBox_Nombre.currentIndex()).split(" - ")
        if len(text) >= 2:
            nombre = text[0]
            direccion = text[1]
            if nombre in self.clientes_en_memoria:
                telefono = self.clientes_en_memoria[nombre]['Telefono']
                sector = self.clientes_en_memoria[nombre]['Sector']
            else:
                telefono = self.clientes_en_memoria[text]['Telefono']
                sector = self.clientes_en_memoria[text]['Sector']
            self.lineEdit_Direcion.setText(direccion)
            self.lineEdit_Telefono.setText(str(telefono))
            self.cmb_zona_cliente.setCurrentIndex(sector - 1)
            self.comboBox_Nombre.currentIndexChanged.disconnect()
            self.comboBox_Nombre.clear()
            self.comboBox_Nombre.setCurrentText(nombre)
            self.comboBox_Nombre.currentIndexChanged.connect(self.on_index_change_nombre)

    def on_click_buscar(self):
        if self.comboBox_Nombre.currentText() != "" and self.comboBox_Nombre.count() == 0:
            clientes = ControlModule.get_Clientes_by_name(self.comboBox_Nombre.currentText())
            for cliente in clientes:
                nombre = cliente['Nombre_cliente']
                direccion = cliente['Direccion']
                sector = cliente['Sector']
                telefono = cliente['Telefono']
                self.clientes_en_memoria[nombre] = {'Direccion': direccion, 'Sector': sector, 'Telefono': telefono}
            if len(self.clientes_en_memoria) == 0:
                QMessageBox.warning(self, "Error!", "Cliente no existe en base de datos, creelo antes de continuar.")
            elif len(self.clientes_en_memoria) == 1:
                self.comboBox_Nombre.setCurrentText(nombre)
                self.lineEdit_Direcion.setText(direccion)
                self.lineEdit_Telefono.setText(str(telefono))
                self.cmb_zona_cliente.setCurrentIndex(sector - 1)
                self.clientes_en_memoria[nombre] = {'Direccion': direccion, 'Sector': sector, 'Telefono': telefono}
            else:
                self.comboBox_Nombre.currentIndexChanged.disconnect()
                for name in self.clientes_en_memoria.keys():
                    self.clientes_en_memoria[name] = {'Direccion': direccion, 'Sector': sector, 'Telefono': telefono}
                    self.comboBox_Nombre.addItem(name + " - " + self.clientes_en_memoria[name]['Direccion'])
                self.comboBox_Nombre.setCurrentIndex(-1)
                self.comboBox_Nombre.currentIndexChanged.connect(self.on_index_change_nombre)
                self.comboBox_Nombre.showPopup()
        # elif self.comboBox_Nombre.currentText() == "":
        #     self.clientes_en_memoria = {}

    def on_click_crear(self):
        if self.comboBox_Nombre.currentText() != "" and self.lineEdit_Direcion.text() != "" and \
                len(self.comboBox_Nombre.currentText().split(" - ")) < 2:
            clientes = ControlModule.get_Cliente(self.comboBox_Nombre.currentText(), self.lineEdit_Direcion.text())
            if len(clientes) > 0:
                QMessageBox.warning(self, "Error!", "El cliente ingresado ya existe!")
                self.on_click_buscar()
                return
            if self.lineEdit_Direcion.text() != "":
                if self.lineEdit_Telefono.text() != "":
                    if self.cmb_zona_cliente.currentIndex() != -1:
                        ControlModule.set_client((self.comboBox_Nombre.currentText(), self.lineEdit_Direcion.text(),
                                                  self.cmb_zona_cliente.currentIndex() + 1,
                                                  int(self.lineEdit_Telefono.text()),))
        else:
            QMessageBox.warning(self, "Error!", "Formato para el cliente inclumplido. "
                                                "Ingrese un nombre y una dirección válida.")

    def on_click_pagar(self):
        def item_childs_to_dict(item):
            result = []
            for j in range(0, item.childCount()):
                sub_item = None
                data = item.child(j).text(1).split(": ")
                if len(data) == 1:
                    tipo = "Producto"
                    data = [item.child(j).text(1)]
                elif len(data) == 2:
                    tipo = data[0]
                    data = [item.child(j).text(1), item.child(j).text(2), ""]
                sub_item = {
                    'tipo': tipo,
                    'datos': data
                }
                if sub_item:
                    result.append(sub_item)
            return result

        if self.treeView_Venta.topLevelItemCount() > 0:
            if self.comboBox_Nombre.currentText() != "" \
                    and self.lineEdit_Direcion.text() != "" \
                    and self.lineEdit_Telefono.text() != "" \
                    and ControlModule.get_Cliente(self.comboBox_Nombre.currentText(), self.lineEdit_Direcion.text()):
                inofrmaion_cliente = {
                    "nombre": self.comboBox_Nombre.currentText(),
                    "direccion": self.lineEdit_Direcion.text(),
                    "telefono": self.lineEdit_Telefono.text(),
                }
                if self.is_despacho or self.is_pedidos_ya:
                    nombre_zona = self.cmb_zona_cliente.currentText()
                    precio = self.treeView_Venta.topLevelItem(self.treeView_Venta.topLevelItemCount()-1).text(1)
                else:
                    nombre_zona = None
                    precio = None
                data_despacho = {
                    'despacho': self.is_despacho,
                    'pedidos_ya': self.is_pedidos_ya,
                    'zona': nombre_zona,
                    'precio': precio
                }
                componentes_boleta = {}
                for i in range(0, self.treeView_Venta.topLevelItemCount()):
                    item = self.treeView_Venta.topLevelItem(i)
                    if not item.text(0) in componentes_boleta:
                        componentes_boleta[item.text(0)] = {
                            'precio': item.text(1),
                            'tamanio': item.text(3),
                            'sub_items': [],
                            'otros': [],
                            'cantidad': 1
                        }
                        componentes_boleta[item.text(0)]['sub_items'] += item_childs_to_dict(item)
                    else:
                        temp = {
                            'precio': item.text(1),
                            'tamanio': item.text(3),
                            'sub_items': [],
                            'otros': [],
                            'cantidad': componentes_boleta[item.text(0)]['cantidad']
                        }
                        if item.childCount() == len(componentes_boleta[item.text(0)]['sub_items']):
                            temp['sub_items'] += item_childs_to_dict(item)
                            if temp['sub_items'] == componentes_boleta[item.text(0)]['sub_items']:
                                componentes_boleta[item.text(0)]['cantidad'] += 1
                            else:
                                is_inside = False
                                for ch in componentes_boleta[item.text(0)]['otros']:
                                    if temp['sub_items'] == ch['sub_items']:
                                        is_inside = True
                                        ch['cantidad'] += 1
                                        break
                                if not is_inside:
                                    temp['cantidad'] = 1
                                    componentes_boleta[item.text(0)]['otros'].append(temp)
                        else:
                            temp['cantidad'] = 1
                            temp['sub_items'] += item_childs_to_dict(item)
                            componentes_boleta[item.text(0)]['otros'].append(temp)

                    # for j in range(0, item.childCount()):
                    #     sub_item = None
                    #     data = item.child(j).text(1).split(": ")
                    #     if len(data) == 1:
                    #         tipo = "Producto"
                    #         data = [item.child(j).text(1)]
                    #     elif len(data) == 2:
                    #         tipo = data[0]
                    #         data = [item.child(j).text(1), item.child(j).text(2), ""]
                    #     sub_item = {
                    #         'tipo': tipo,
                    #         'datos': data
                    #     }
                    #     if sub_item:
                    #         componentes_boleta[item.text(0)]['sub_items'].append(sub_item)
                dialog = QDialog()
                dialog.ui = Pagar_Dialog()
                dialog.ui.setupUi(dialog, self.user_name, inofrmaion_cliente, data_despacho,
                                  self.id_session, componentes_boleta)
                rec = dialog.exec()
                if rec == 1:
                    self.treeView_Venta.clear()
                    self.comboBox_Nombre.clear()
                    self.lineEdit_Direcion.clear()
                    self.lineEdit_Direcion.clear()
                    self.cmb_zona_cliente.setCurrentIndex(0)
            else:
                QMessageBox.warning(self, "Error!", "Debe ingresar un cliente para procesar el pago."
                                                    "Ingrese cliente.")

    def load_buttons(self):
        """
        """
        self.listPizzas.clear()
        self.listEmpanadas.clear()
        self.listAgregados.clear()
        self.listBebidas.clear()
        self.listPromociones.clear()
        productos = ControlModule.get_Productos()
        promociones = ControlModule.get_Promociones()
        if productos:
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
                    ######################################################################
                elif categoria == 'Despacho':   # Cargar los despachos a la lista de zonas
                    self.cmb_zona_cliente.addItem(producto['Nombre_producto'])
                    ######################################################################
        if promociones:
            for promocion, i in zip(promociones, range(len(promociones))):
                # if "ñ" in promocion['Nombre_promocion']
                self.listPromociones.addItem(promocion['Nombre_promocion'])
            self.promociones = promociones

    def load_tree(self):
        self.treeView_Venta.setColumnCount(3)
        self.treeView_Venta.setHeaderLabels(["Producto", "Detalle", "Cobros extra"])
        self.treeView_Venta.addActions([self.accion_editar, self.accion_ingrediente, self.accion_comentario])


    def on_click_action_agregar_productos_CSV(self):
        files = self.buscar_archivo()
        if files:
            new_products = {}
            data = genfromtxt(files[0], dtype=str, delimiter=",", encoding="utf-8")
            headers = data[0][1:].split(";")[:6]
            for line in data[1:]:
                line = line
                product = line.split(";")[:6]
                new_products[headers[0]] = product[0]
                if product[1] == '':
                    self.load_buttons()
                    return
                new_products[headers[1]] = int(product[1])
                if product[2]:
                    new_products[headers[2]] = int(product[2])
                else:
                    new_products[headers[2]] = None
                if product[3]:
                    new_products[headers[3]] = int(product[3])
                else:
                    new_products[headers[3]] = None
                new_products[headers[4]] = product[4]
                if product[5]:
                    new_products[headers[5]] = product[5]
                else:
                    new_products[headers[5]] = None
                ControlModule.insert_product(new_products)
        self.load_buttons()

    def on_click_action_agregar_promociones_CSV(self):
        files = self.buscar_archivo(" Lista de productos")
        if files:
            new_promo = {}
            data = genfromtxt(files[0], dtype=str, delimiter=",", encoding="ISO-8859-1")
            headers = data[0].split(";")[:4]
            for line in data[1:]:
                product = line.split(";")[:4]
                new_promo[headers[0]] = product[0]
                if product[1] == '':
                    break
                new_promo[headers[1]] = int(product[1])
                new_promo[headers[2]] = int(product[2])
                new_promo[headers[3]] = int(product[3])
                ControlModule.insert_promo(new_promo)
            second_files = self.buscar_archivo(" Lista de componentes de productos")
            if second_files:
                new_component = {}
                data = genfromtxt(second_files[0], dtype=str, delimiter=",", encoding="ISO-8859-1")
                headers = data[0].split(";")[:6]
                for line in data[1:]:
                    product = line.split(";")[:6]
                    new_component[headers[0]] = product[0]
                    if product[1]:
                        new_component[headers[1]] = product[1]
                    else:
                        new_component[headers[1]] = None
                    if product[2]:
                        new_component[headers[2]] = product[2]
                    else:
                        new_component[headers[2]] = None
                    if product[3] == '':
                        self.load_buttons()
                        return
                    new_component[headers[3]] = int(product[3])
                    ControlModule.insert_Componente_promo(new_component)
        self.load_buttons()

    def on_click_action_editar(self):
        current_index = self.treeView_Venta.currentIndex()
        if current_index.row() >= 0:
            current_item = self.treeView_Venta.currentItem()
            if current_item.text(0) == "":
                QMessageBox.about(self, "Error de tipo", "No se puede editar una promoción ni un comentario añadido.")
                return
            nombre_producto = self.treeView_Venta.currentItem().text(0)
            precio = self.treeView_Venta.currentItem().text(1)
            dialog = QDialog()
            dialog.ui = Editar_producto_boleta_Dialog(name=nombre_producto, price=precio)
            dialog.ui.setupUi(dialog, name=nombre_producto, price=precio)
            response = dialog.exec()
            nombre_producto = dialog.ui.lineNombre_producto.text()
            precio = dialog.ui.linePrecio.text()
            if response == dialog.Accepted:
                self.treeView_Venta.currentItem().setText(0, nombre_producto)
                self.treeView_Venta.currentItem().setText(1, precio)
                self.on_change_tree()

    def on_click_action_ingrediente(self):
        item = self.treeView_Venta.currentItem()
        if item:
            nombre = item.text(1).split(": ")
            tamanio_precio = item.text(3)
            if tamanio_precio == '' and item.parent() != self.treeView_Venta:
                tamanio_precio = item.parent().text(3)
            if tamanio_precio == '1':
                tamanio_precio = "Precio_unitario"
            elif tamanio_precio == '2':
                tamanio_precio = "Precio_mediana"
            elif tamanio_precio == '3':
                tamanio_precio = "Precio_familiar"
            elif tamanio_precio == "":
                tamanio_precio = "Precio_unitario"
            dialog = QDialog()
            dialog.ui = Añadir_ingrediente_Dialog()
            dialog.ui.setupUi(dialog, tamanio_precio)
            response = dialog.exec()
            nombre_ingrediente = dialog.ui.cmb_nombre.currentText()
            precio = dialog.ui.lineEdit_precio.text()
            if response == dialog.Accepted:
                if nombre[0] not in ["Agregado", "Comentario"]:
                    new_item = QtWidgets.QTreeWidgetItem(item)
                    new_item.setText(1, "Agregado: " + nombre_ingrediente)
                    new_item.setText(2, precio)
                    item.addChild(new_item)
                else:
                    new_item = QtWidgets.QTreeWidgetItem(item.parent())
                    new_item.setText(1, "Agregado: " + nombre_ingrediente)
                    new_item.setText(2, precio)
                    item.parent().addChild(new_item)
                self.on_change_tree()

    def on_click_action_comentario(self):
        item = self.treeView_Venta.currentItem()
        if item:
            nombre = item.text(1).split(": ")
            dialog = QDialog()
            dialog.ui = Añadir_comentario_Dialog()
            dialog.ui.setupUi(dialog)
            response = dialog.exec()
            if response == dialog.Accepted:
                comentario = dialog.ui.lineEdit_comentario.text()
                if nombre[0] not in ["Agregado", "Comentario"]:
                    new_item = QtWidgets.QTreeWidgetItem(item)
                    new_item.setText(1, "Comentario: " + comentario)
                    item.addChild(new_item)
                else:
                    new_item = QtWidgets.QTreeWidgetItem(item.parent())
                    new_item.setText(1, "Comentario: " + comentario)
                    item.parent().addChild(new_item)
                self.treeView_Venta.expandAll()

    def on_click_action_boletin_fechas(self):
        dialog = QDialog()
        dialog.ui = Exportar_Boletin_Fechas_Dialog()
        dialog.ui.setupUi(dialog)
        response = dialog.exec()


class CustomCombo(QtWidgets.QComboBox):
    enter_pressed = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.text() == '\r':
            self.enter_pressed.emit()
        else:
            QtWidgets.QComboBox.keyPressEvent(self, event)
            # if the key is not return, handle normally


class Inicio_session_Dialog(QMainWindow, Ui_inicio_session):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi(self)


class Editar_producto_boleta_Dialog(QMainWindow, Ui_edicion_producto_boleta):

    def __init__(self, name=None, price=None, parent=None):
        super().__init__(parent)
        self.setupUi(self, name, price)


class Añadir_comentario_Dialog(QMainWindow, Ui_añadir_comentario):

    def __init__(self):
        super().__init__()


class Añadir_ingrediente_Dialog(QMainWindow, Ui_añadir_ingrediente):

    def __init__(self):
        super().__init__()


class Buscador_archvos(QMainWindow, Ui_file_browser_Dialog):

    def __init__(self):
        super().__init__()


class Select_promo_component(QMainWindow, Ui_sub_cathegory_promo_select):

    def __init__(self):
        super().__init__()


class Pagar_Dialog(QMainWindow, Ui_Pagar_Dialog):

    def __init__(self):
        super().__init__()


class Crear_Usuario_Dialog(QMainWindow, Ui_Aniadir_Usuario_Dialog):

    def __init__(self):
        super().__init__()


class Modificar_Usuario_Dialog(QMainWindow, Ui_Modificar_Usuario_Dialog):

    def __init__(self):
        super().__init__()


class Eliminar_Usuario_Dialog(QMainWindow, Ui_Eliminar_Usuario_Dialog):

    def __init__(self):
        super().__init__()


class Aniadir_Retiro_Dialog(QMainWindow, Ui_Aniadir_Retiro_Dialog):

    def __init__(self):
        super().__init__()


class Exportar_Boletin_Fechas_Dialog(QMainWindow, UI_Export_Boletin_Fechas_Dialog):

    def __init__(self):
        super().__init__()
