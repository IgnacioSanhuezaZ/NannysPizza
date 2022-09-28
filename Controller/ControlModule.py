# from escpos.connections import getUSBPrinter
# from escpos.printer import Usb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# from PyQt5.QtWidgets import QMainWindow, QDialog
from escpos import printer
from escpos.printer import Network
from escpos.printer import Usb, Serial

from Database import DatabaseModule as db
# from escpos.conn import USBConnection as usbcon
# from escpos.connections import getUSBPrinter
import json

# import libusb1

"""---------------------------------------------------------------------------------
                        Sección de control de acceso y gestión
   ---------------------------------------------------------------------------------"""


def control_acceso(credenciales):
    cursor = db.get_db()
    usu_tipo_usuario = db.selectUser("WHERE Nombre_usuario = ? AND Contrasena = ?;", cursor, tuple(credenciales))
    if not usu_tipo_usuario:
        QMessageBox.warning(None, "Error!", "Usuario o contraseña incorrecta")
        cursor.close()
        return ["Invalid user or password provided", 'error']
    cursor.close()
    return usu_tipo_usuario


def verificar_existencia_usuario(credenciales):
    cursor = db.get_db()
    usu_tipo_usuario = db.selectUser("WHERE Nombre_usuario = ? AND Contrasena = ?;", cursor, tuple(credenciales))
    if usu_tipo_usuario:
        QMessageBox.warning(None, "Error!", "Usuario ya existe. Use otro nombre!")
        cursor.close()
        return usu_tipo_usuario
    cursor.close()
    return usu_tipo_usuario


def Ingreso_cuenta(args):
    cursor = db.get_db()
    verify = db.selectUser("WHERE Nombre_usuario = ? AND Contrasena = ?;", cursor, (args[0], args[1],))
    if verify:
        QMessageBox.warning(None, "Error!", "Usuario ya existe, inicie sesión con normalidad.")
        cursor.close()
        return
    else:
        db.Pragma_foreign_key_on(cursor)
        db.insertUser(tuple(args), cursor)
        cursor.close()


def get_User_by_name(nombre):
    return db.GetUser((nombre,))


def Update_User(credenciales):
    cursor = db.get_db()
    db.Pragma_foreign_key_on(cursor)
    return db.updateUser(cursor, tuple(credenciales))


def Erase_User(nombre):
    cursor = db.get_db()
    return db.eraseUser(cursor, (nombre,))


def Get_all_Usernames():
    cursor = db.get_db()
    rec = db.selectUser("", cursor=cursor)
    names = []
    for elem in rec:
        names.append(elem['Nombre_usuario'])
    return names


def get_Producto(nombre_producto):
    return db.GetProduct((nombre_producto,))


def get_Producto_by_Cathegory(nombre_categoria):
    return db.GetProductByCathegory((nombre_categoria,))


def get_Producto_by_Subcathegory(nombre_categoria):
    return db.GetProductBySubCathegory((nombre_categoria,))


def get_Productos():
    return db.GetAllProducts()


def get_Promociones():
    return db.GetPromociones()


def get_Promocion(nombre_promocion):
    return db.GetPromocion((nombre_promocion,))


def getLastSession():
    return db.GetLastSesion()


def get_Clientes_by_name(nombre_cliente):
    return db.GetClientPerNameOnly(("%" + nombre_cliente + "%",))


def get_Cliente(nombre_cliente, direccion):
    return db.GetClient((nombre_cliente, direccion,))


def set_client(data):
    if len(data) == 4:
        cursor = db.get_db()
        db.insertClient(cursor=cursor, values=tuple(data))
    else:
        print("wrong values length", len(data))


def set_session(values: list):
    """Keys: Nombre_usuario (fk_Usuarios), Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre"""
    if len(values) == 5:
        cursor = db.get_db()
        db.insertSesion(tuple(values), cursor)
    else:
        print("wrong values length", len(values))


def update_session(values: list):
    """tuple(Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, Id_sesion)"""
    if len(values) == 7:
        cursor = db.get_db()
        db.updateSesiones(cursor, tuple(values))
    else:
        print("wrong values length", len(values))


def set_turno(values: list):
    if len(values) == 2:
        cursor = db.get_db()
        db.insertTurnos_caja(tuple(values), cursor)
    else:
        print("wrong values length", len(values))


def update_turno(values: list):
    """tuple(Id_sesion, Nombre_usuario, Id_turno)"""
    if len(values) == 3:
        cursor = db.get_db()
        db.updateTurnos_caja(cursor, tuple(values))
    else:
        print("wrong values length", len(values))

def insert_product(product_data: dict):
    data = [None for i in product_data.keys()]
    for key in product_data.keys():
        if key == 'Nombre_producto':
            data[0] = product_data['Nombre_producto']  # type: str
        elif key == 'Precio_unitario':
            data[1] = product_data['Precio_unitario']  # type: str
        elif key == 'Categoria':
            data[2] = product_data['Categoria']  # type: str
        elif key == 'Sub_categoria':
            data[3] = product_data['Sub_categoria']  # type: str
        elif key == 'Precio_mediana':
            data[4] = product_data['Precio_mediana']  # type: str
        elif key == 'Precio_familiar':
            data[5] = product_data['Precio_familiar']  # type: str
    cursor = db.get_db()
    verify = db.GetProduct(tuple((data[0],)))
    if len(verify) == 0:
        db.insertProduct(tuple(data), cursor)
    else:
        data.append(data[0])
        data.pop(0)
        db.updateProducto(cursor, tuple(data))


def insert_promo(promo_data: dict):
    """:param promo_data: dict(Nombre_promocion, Is_by_sub_cathegory, precio, Tamano)
       """
    data_promo = [None for i in promo_data.keys()]
    for key in promo_data.keys():
        if key == 'Nombre_promocion':
            data_promo[0] = promo_data['Nombre_promocion']
        elif key == 'Is_by_sub_cathegory':
            data_promo[1] = promo_data['Is_by_sub_cathegory']
        elif key == 'precio':
            data_promo[2] = promo_data['precio']
        elif key == 'Tamano':
            data_promo[3] = promo_data['Tamano']
    cursor = db.get_db()
    verify = db.GetPromocion(tuple((data_promo[0],)))
    if len(verify) == 0:
        db.insertPromocion(tuple(data_promo), cursor)
    else:
        data_promo.append(verify[0]['Id_promocion'])
        db.updatePromocion(cursor, tuple(data_promo))


def insert_Componente_promo(componentes_data: dict):
    """:param componentes_data: list([Tuple(Is_by_sub_cathegory, Cantidad, Nombre_Producto, Sub_categoria)])"""
    data_componentes = [None for i in componentes_data.keys()]
    for key in componentes_data.keys():
        if key == 'Id_promocion':
            data_componentes[0] = componentes_data['Id_promocion']
        elif key == 'Cantidad':
            data_componentes[1] = componentes_data['Cantidad']
        elif key == 'Nombre_Producto':
            data_componentes[2] = componentes_data['Nombre_Producto']
        elif key == 'Sub_categoria':
            data_componentes[3] = componentes_data['Sub_categoria']
    cursor = db.get_db()
    verify = db.ExistComponentesPromocion(tuple(data_componentes))
    if not verify:
        db.insertComponentePromo(tuple(data_componentes), cursor)
    else:
        data_componentes.append(verify)
        db.updateComponentePromo(tuple(data_componentes), cursor)


def set_boleta(data_venta, data_boleta):
    """
    key order venta: (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Adicional, Efectivo ,)

    key order boleta: (Nombre_producto, Cantidad, Tamano, Nombre_promocion, Cobro_adicional,)
    :param data_venta:
    :param data_boleta:
    :return:
    """
    if len(data_venta) == 5:
        cursor = db.get_db()
        db.insertVenta(cursor=cursor, values=tuple(data_venta))
        last = db.GetLastNVentas(1)
        last_id = None
        if last:
            last_id = last[0]['']
        if last_id:
            for data in data_boleta:
                if len(data) == 5:
                    db.insertBoleta(cursor=cursor, values=tuple([last_id] + data))
        else:
            QMessageBox.warning(None, "Error!", "Hubo un problema al ingresar el pago, venta no registrada.")

    def Get_Ventas_por_Fechas(fecha1, fecha2):
        cursor = db.get_db()
        db.GetLastNVentas()


def Calculate_end_session(id):
    cursor = db.get_db()
    return db.GetVentasPerId(id)


def set_retiro(values: list):
    """Keys: (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Adicional, Efectivo)"""
    cursor = db.get_db()
    if len(values) == 6:
        db.insertVenta(values, cursor)
    else:
        print("wrong values length", len(values))



def print_in_printer(content: str):
    # p = usbcon(vendor_id=0x0416, product_id=0x5011)
    # p = Network("192.168.1.100")
    p = printer.Usb(idVendor=0x1d6b, idProduct=0x0003)
    # p = Usb(idVendor=0x5986, idProduct=0x2113)
    # p = getUSBPrinter(commandSet='Generic')(idVendor=0x0416, idProduct=0x5011)
    p.text("Probando\nLa\Máquina\n.\n.\n.\n")
    p.set()
    p.panel_buttons(enable=True)
    p.open()
    p.print_and_feed()
    p.beep()
    p.cut()
    # p.write("Probando\nLa\Máquina\n.\n.\n.\n")
    # p.text("Probando\nLa\Máquina\n.\n.\n.\n")
    # p.catch()
    # p.write(content)
    # p.lf()
