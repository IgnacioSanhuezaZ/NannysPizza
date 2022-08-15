from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
from Database import DatabaseModule as db
from escpos import *
import json

"""---------------------------------------------------------------------------------
                        Sección de control de acceso y gestión
   ---------------------------------------------------------------------------------"""


def control_acceso(credenciales):
    cursor = db.get_db()
    usu_tipo_usuario = db.selectUser("WHERE Nombre_usuario = ? AND Contrasena = ?;", cursor, tuple(credenciales))
    if not usu_tipo_usuario:
        print("Usuario o contraseña incorrecta")
        cursor.close()
        return ["Invalid user or password provided", 'error']
    cursor.close()
    return usu_tipo_usuario


def Ingreso_cuenta(args):
    cursor = db.get_db()
    db.Pragma_foreign_key_on(cursor)
    verify = db.selectUser("WHERE usu_mail = ?;", cursor, (args[0],))
    if verify is None:
        print("User already exist, Log in.")
        cursor.close()
        return ["User already exist, please Log In.", 'error']
    else:
        db.insertUser(args, cursor)
        cursor.close()


def Iniciar_botones_prod(tab_parents: dict):
    def on_click(name: str):
        pass

    cursor = db.get_db()
    data = db.selectProducto("", cursor)
    to_load = open(r"C:\Users\ignac\PycharmProjects\NannysPizza\Controller\scheme.json")
    scheme = json.load(to_load)  # type: dict
    for key in scheme:
        scheme[key] = []
    for e in data:
        if e['Categoria'] not in scheme:
            scheme[e['Categoria']] = []
            with open(r"C:\Users\ignac\PycharmProjects\NannysPizza\Controller\scheme.json", "w") as write_file:
                json.dump(scheme, write_file)
        scheme[e['Categoria']].append(e)
        tab = tab_parents[e['Categoria']]  # type: QtWidgets.QGridLayout
        button = QtWidgets.QPushButton(tab)
        button.setText(e["Nombre_producto"])
        button.clicked.connect(lambda: on_click(e["Nombre_producto"]))
        tab.addWidget(button)

    return scheme


def get_Productos():
    return db.GetAllProducts()
