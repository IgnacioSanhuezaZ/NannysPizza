# from escpos.connections import getUSBPrinter
# from escpos.printer import Usb
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QDialog
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


def get_Producto(nombre_producto):
    return db.GetProduct((nombre_producto,))


def get_Producto_by_Cathegory(nombre_categoria):
    print(nombre_categoria)
    return db.GetProductBySubCathegory((nombre_categoria,))


def get_Productos():
    return db.GetAllProducts()


def get_Promociones():
    return db.GetPromociones()


def get_Promocion(nombre_promocion):
    print("in_promo")
    return db.GetPromocion((nombre_promocion,))


def getLastSession():
    return db.GetLastSesion()


def get_Clientes_by_name(nombre_cliente):
    return db.GetClientPerNameOnly((nombre_cliente,))


def get_Cliente(nombre_cliente, direccion):
    return db.GetClient((nombre_cliente, direccion,))


def set_client(data):
    if len(data) == 4:
        cursor = db.get_db()
        db.insertClient(cursor=cursor, values=tuple(data))
    else:
        print("wrong values length", len(data))


def insert_product(product_data: dict):
    data = [None for i in product_data.keys()]
    for key in product_data.keys():
        if key == 'Nombre_producto':
            data[0] = product_data['Nombre_producto']   # type: str
        elif key == 'Precio_unitario':
            data[1] = product_data['Precio_unitario']   # type: str
        elif key == 'Categoria':
            data[2] = product_data['Categoria']   # type: str
        elif key == 'Sub_categoria':
            data[3] = product_data['Sub_categoria']   # type: str
        elif key == 'Precio_mediana':
            data[4] = product_data['Precio_mediana']   # type: str
        elif key == 'Precio_familiar':
            data[5] = product_data['Precio_familiar']   # type: str
    cursor = db.get_db()
    verify = db.GetProduct(tuple((data[0],)))
    if len(verify) == 0:
        db.insertProduct(tuple(data), cursor)
    else:
        print("Producto ya ingresado, actualizando...")
        data.append(data[0])
        data.pop(0)
        db.updateProducto(cursor, tuple(data))
        print("Producto actualizado.")


def insert_promo(promo_data: dict, componentes_data: list):
    """:param promo_data: dict(Nombre_promocion, Is_by_sub_cathegory, precio, Tamano)
        :param componentes_data: list([Tuple(Is_by_sub_cathegory, Cantidad, Nombre_Producto, Sub_categoria)])"""
    data_promo = [None for i in promo_data.keys()]
    data_componentes = [None for i in componentes_data[0].keys()]
    for key in promo_data.keys():
        if key == 'Nombre_promocion':
            data_promo[0] = promo_data['Nombre_promocion']
        elif key == 'Is_by_sub_cathegory':
            data_promo[1] = promo_data['Is_by_sub_cathegory']
        elif key == 'precio':
            data_promo[2] = promo_data['precio']
        elif key == 'Tamano':
            data_promo[3] = promo_data['Tamano']
    for component in componentes_data:
        for key in component.keys():
            if key == 'Is_by_sub_cathegory':
                data_componentes[0] = component['Is_by_sub_cathegory']
            elif key == 'Cantidad':
                data_componentes[1] = component['Cantidad']
            elif key == 'Nombre_Producto':
                data_componentes[2] = component['Nombre_Producto']
            elif key == 'Sub_categoria':
                data_componentes[3] = component['Sub_categoria']
    cursor = db.get_db()
    verify = db.GetPromocion(tuple((data_promo[0],)))
    if len(verify) == 0:
        db.insertPromocion(tuple(data_promo), tuple(data_componentes), cursor)

    else:
        print("Producto ya ingresado, actualizando...")
        data_promo.append(data_promo[0])
        data_promo.pop(0)
        db.updatePromocion(cursor, tuple(data_promo), tuple(data_componentes))
        print("Producto actualizado.")


def set_boleta(data_venta, data_boleta):
    """
    key order venta: (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion,)

    key order boleta: (Nombre_producto, Cantidad, Tamano, Nombre_promocion, Cobro_adicional,)
    :param data_venta:
    :param data_boleta:
    :return:
    """
    if len(data_venta) == 4:
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


def print_in_printer(content: str):
    # p = usbcon(vendor_id=0x0416, product_id=0x5011)
    # p = printer.Usb(idVendor=0x0416, idProduct=0x5011)
    p = Usb(idVendor=0x0416, idProduct=0x5011)
    # p = getUSBPrinter(commandSet='Generic')(idVendor=0x0416, idProduct=0x5011)
    print(p)
    print("A punto de ...", p)
    p.set()
    p.panel_buttons(enable=True)
    p.open()
    p.text("Probando\nLa\Máquina\n.\n.\n.\n")
    p.print_and_feed()
    p.beep()
    p.cut()
    print(p.idProduct)
    # p.write("Probando\nLa\Máquina\n.\n.\n.\n")
    # p.text("Probando\nLa\Máquina\n.\n.\n.\n")
    # p.catch()
    # p.write(content)
    # p.lf()
