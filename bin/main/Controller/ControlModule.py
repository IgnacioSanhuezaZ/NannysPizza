from PyQt5.QtWidgets import QMessageBox

from Database import DatabaseModule as db

import openpyxl



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


def verificar_existencia_cliente(credenciales):
    """Keys: (Nombre_cliente, Direccion, )"""
    cursor = db.get_db()
    usu_tipo_usuario = db.GetClient(tuple(credenciales))
    if not usu_tipo_usuario:
        QMessageBox.warning(None, "Error!", "Cliente no existe. Ingrese un cliente válido o cree uno nuevo!")
        cursor.close()
        return False
    cursor.close()
    return True


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
    if len(values) == 6:
        cursor = db.get_db()
        db.insertSesion(tuple(values), cursor)
    else:
        print("wrong values length", len(values))


def update_session(values: list):
    """tuple(Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre, Id_sesion)"""
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
    key order venta: (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo ,)

    key order boleta: (Nombre_producto, Cantidad, Tamano, Nombre_promocion,)
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
            last_id = last[0]['Id_venta']
        if not last_id:
            last_id = 0
        for data in data_boleta:
            if len(data) == 4:
                db.insertBoleta(cursor=cursor, values=tuple([last_id] + data))


def Get_Ventas_por_Fechas(fecha1, fecha2):
    sesiones = db.GetSesionPerDates(fecha1, fecha2)
    data = {}
    total_efectivo = 0
    total_final = 0
    for sesion in sesiones:
        id = sesion['Id_sesion']
        fecha = sesion['Fecha_apertura']
        record, retiros, final, efectivo = db.GetVentasPerId((id,))
        data[fecha] = {'ventas': record.copy(),
                       'retiros': retiros.copy(),
                       'total': final,
                       'efectivo': efectivo
                       }
        total_final += final
        total_efectivo += efectivo
    data['total_final'] = total_final
    data['total_efectivo'] = total_efectivo
    data['fecha_inicio'] = fecha1
    data['fecha_final'] = fecha2
    return data


def Calculate_end_session(id):
    cursor = db.get_db()
    return db.GetVentasPerId((id,))


def Write_excel(data, out_path):
    workbook = openpyxl.Workbook()
    workbook.create_sheet()
    worksheet = workbook.active
    worksheet['A1'] = 'Informe de ventas'
    if data['fecha_inicio'] == data['fecha_final']:
        fecha_inicio = str(data['fecha_inicio'])
        fecha_inicio = fecha_inicio[:4] + "-" + fecha_inicio[4:6] + "-" + fecha_inicio[6:8]
        worksheet['B1'] = fecha_inicio
    else:
        fecha_inicio = str(data['fecha_inicio'])
        fecha_inicio = fecha_inicio[:4] + "-" + fecha_inicio[4:6] + "-" + fecha_inicio[6:8]
        fecha_final = str(data['fecha_final'])
        fecha_final = fecha_final[:4] + "-" + fecha_final[4:6] + "-" + fecha_final[6:8]
        worksheet['B1'] = fecha_inicio
        worksheet['C1'] = fecha_final
    worksheet['A3'] = 'Fecha'
    worksheet['B3'] = "Detalle"
    worksheet['C3'] = "Monto"
    i = 4
    for fecha in data:
        if fecha in ['total_final', 'total_efectivo', 'fecha_inicio', 'fecha_final']:
            continue
        date_to_write = str(fecha)
        date_to_write = date_to_write[:4] + "-" + date_to_write[4:6] + "-" + date_to_write[6:8]
        worksheet['A'+str(i)] = date_to_write
        i += 1
        for venta in data[fecha]['ventas']:
            for element in venta['Boleta']:
                nombre = element['Nombre_producto']
                promo = element['Nombre_promocion']
                precio = element['Precio']
                if nombre:
                    worksheet['B'+str(i)] = nombre
                else:
                    worksheet['B'+str(i)] = promo
                worksheet['C' + str(i)] = int(precio)
                i += 1
        for retiro in data[fecha]['retiros']:
            worksheet['B' + str(i)] = "Retiro: " + retiro['Descripcion']
            worksheet['C' + str(i)] = int(retiro['Monto'])
            i += 1
        i += 1
        worksheet['B' + str(i)] = "Total Efectivo en venta del día: "
        worksheet['C' + str(i)] = int(data[fecha]['efectivo'])
        i += 1
        worksheet['B' + str(i)] = "Total en venta del día: "
        worksheet['C' + str(i)] = int(data[fecha]['total'])
        i += 1
    i += 1
    worksheet['B' + str(i)] = "Total efectivo en ventas: "
    worksheet['C' + str(i)] = int(data['total_efectivo'])
    i += 1
    worksheet['B' + str(i)] = "Total en venta: "
    worksheet['C' + str(i)] = int(data['total_final'])
    i += 1
    workbook.save(out_path)
    workbook.close()





def set_retiro(values: list):
    """Keys: Monto, Descripcion, Id_retiro, Id_sesion"""
    cursor = db.get_db()
    if len(values) == 3:
        db.insertRetiro(values, cursor)
    else:
        print("wrong values length", len(values))

