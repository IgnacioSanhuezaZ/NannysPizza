# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Main_loged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi

from inicio_session import Ui_inicio_session


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print("Main set up")
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
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(610, 80, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 260, 761, 461))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setAutoFillBackground(False)
        self.tab_3.setObjectName("tab_3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/pizza_PNG7143.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/chicken_quesadilla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_6, icon1, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/bbq-ribs-clipart-17336204-an-image-of-barbecue-spare-ribs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/3-bebidas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_7, icon3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\UI\\../Resources/estrella.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon4, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 740, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 740, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 740, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 1200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\UI\\../Resources/fondo_SDM.jpg"))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 30, 391, 691))
        self.groupBox_2.setObjectName("groupBox_2")
        self.treeView = QtWidgets.QTreeView(self.groupBox_2)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 371, 661))
        self.treeView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView.setObjectName("treeView")
        self.label.raise_()
        self.groupBox.raise_()
        self.tabWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdministrar_Sesi_n = QtWidgets.QMenu(self.menubar)
        self.menuAdministrar_Sesi_n.setObjectName("menuAdministrar_Sesi_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIniciar_Sesi_n = QtWidgets.QAction(MainWindow)
        self.actionIniciar_Sesi_n.setObjectName("actionIniciar_Sesi_n")
        self.actionCerrar_caja = QtWidgets.QAction(MainWindow)
        self.actionCerrar_caja.setObjectName("actionCerrar_caja")
        self.actionCerrar_sesi_n = QtWidgets.QAction(MainWindow)
        self.actionCerrar_sesi_n.setObjectName("actionCerrar_sesi_n")
        self.menuAdministrar_Sesi_n.addAction(self.actionIniciar_Sesi_n)
        self.menuAdministrar_Sesi_n.addAction(self.actionCerrar_caja)
        self.menuAdministrar_Sesi_n.addAction(self.actionCerrar_sesi_n)
        self.menubar.addAction(self.menuAdministrar_Sesi_n.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        # self.block_unblock_all(operation=False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nanny\'s Pizza"))
        self.groupBox.setTitle(_translate("MainWindow", "Cliente"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_3.setText(_translate("MainWindow", "Dirección:"))
        self.label_4.setText(_translate("MainWindow", "Teléfono"))
        self.radioButton.setText(_translate("MainWindow", "Despacho"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pizzas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Empanadas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Agregados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Bebidas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Promociones"))
        self.pushButton.setText(_translate("MainWindow", "Editar"))
        self.pushButton_2.setText(_translate("MainWindow", "Pagar"))
        self.pushButton_3.setText(_translate("MainWindow", "Despacho"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Venta"))
        self.menuAdministrar_Sesi_n.setTitle(_translate("MainWindow", "Administrar Sesión"))
        self.actionIniciar_Sesi_n.setText(_translate("MainWindow", "Iniciar esión"))
        self.actionCerrar_caja.setText(_translate("MainWindow", "Cerrar caja"))
        self.actionCerrar_sesi_n.setText(_translate("MainWindow", "Cerrar sesión"))

    def block_unblock_all(self, operation: bool = False):
        self.centralwidget.setEnabled(operation)
        self.groupBox.setEnabled(operation)
        self.verticalLayoutWidget.setEnabled(operation)
        self.verticalLayout_2.setEnabled(operation)
        self.horizontalLayout.setEnabled(operation)
        self.label_2.setEnabled(operation)
        self.lineEdit.setEnabled(operation)
        self.horizontalLayout_3.setEnabled(operation)
        self.label_3.setEnabled(operation)
        self.lineEdit_2.setEnabled(operation)
        self.horizontalLayout_4.setEnabled(operation)
        self.label_4.setEnabled(operation)
        self.lineEdit_3.setEnabled(operation)
        self.radioButton.setEnabled(operation)
        self.tabWidget.setEnabled(operation)
        self.tab_3.setEnabled(operation)
        self.tab_6.setEnabled(operation)
        self.tab_4.setEnabled(operation)
        self.tab_7.setEnabled(operation)
        self.tab_5.setEnabled(operation)
        self.pushButton.setEnabled(operation)
        self.pushButton_2.setEnabled(operation)
        self.pushButton_3.setEnabled(operation)
        self.label.setEnabled(operation)
        self.groupBox_2.setEnabled(operation)
        self.treeView.setEnabled(operation)
        self.menubar.setEnabled(operation)
        self.menuAdministrar_Sesi_n.setEnabled(operation)
        self.statusbar.setEnabled(operation)
        self.actionIniciar_Sesi_n.setEnabled(operation)
        self.actionCerrar_caja.setEnabled(operation)
        self.actionCerrar_sesi_n.setEnabled(operation)

    def login(self):
        close = QtWidgets.QMessageBox.question(self,
                                               "INICIO DE SESIÓN",
                                               "Complete sus datos para iniciar sesión: ",
                                               Window.Yes | Window.No)
        acces_token = self.acces_token
        if close == Window.Yes:
            acces_token = close.access_token
            self.close()

        else:
            pass


class FindReplaceDialog(QtWidgets.QMessageBox):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("UI/Main_loged.ui", self)


class Window(QtWidgets.QMessageBox, Ui_inicio_session):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.boton_ingreso.clicked.connect(self.processEvent)

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    @pyqtSlot()
    def closeEvent(self):
        close = QtWidgets.QMessageBox.question(self,
                                               "SALIR",
                                               "¿Está segura de querer salir?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        acces_token = self.acces_token
        if close == QtWidgets.QMessageBox.Yes:
            acces_token = self.acces_token
            self.close()

        else:
            pass

    @pyqtSlot()
    def processEvent(self):
        acces_token = self.acces_token
        print("acces_token =", acces_token)

        if acces_token:
            self.close()
