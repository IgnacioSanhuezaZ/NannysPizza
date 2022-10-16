import sqlite3

"""------------------------------------------------------------------------------
                                Sección de utilidades
   ------------------------------------------------------------------------------"""


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db():
    """Obtiene el conector desde la base de datos"""
    db = sqlite3.connect('Database/nannys_pizza.sqlite', sqlite3.PARSE_DECLTYPES)
    db.row_factory = dict_factory
    return db


def close_db(db):
    """Cierra la conexión a la base de datos"""
    if db is not None:
        db.close()


def Pragma_foreign_key_on(cursor):
    query = """PRAGMA foreign_keys = ON;"""
    try:
        cursor.execute(query)
    except sqlite3.Error as error:
        print("Error handling PRAGMA foreign keys")
        print(error)


"""---------------------------------------------------------------------------------
                        Sección de selección de datos
   ---------------------------------------------------------------------------------"""


def selectUser(args, cursor, values=None):
    """
    Keys: Nombre_usuario, Contrasena, Administra

    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Usuarios """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectClient(args, cursor, values=None):
    """
    Keys: Nombre_cliente, Direccion, Sector, Telefono
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Cliente """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectBoletas(args, cursor, values=None):
    """
    Keys: Id_entrada, Id_boleta, Nombre_producto, Cantidad, Tamano, Nombre_promocion
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Boletas """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectProducto(args, cursor, values=None):
    """
    Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Producto """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectSesion(args, cursor, values=None):
    """
    Keys: Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Sesiones """
        if args != "" and values:
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectTurnos_caja(args, cursor, values=None):
    """
    Keys: Id_turno, Id_sesion, Nombre_usuario
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Turnos_caja """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectVentas(args, cursor, values=None):
    """
    Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Ventas """
        if args != "" and values:
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectPromociones(args, cursor, values=None):
    """
        Keys: Id_promocion, Nombre_promocion, Is_by_sub_cathegory, precio, Tamano
        :param args:
        :param cursor:
        :param values:
        :return:
        """
    try:
        sqlite_select_query = """SELECT * from Promociones """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectRetiros(args, cursor, values=None):
    """
        Keys: Monto, Descripcion, Id_retiro, Id_sesion
        :param args:
        :param cursor:
        :param values:
        :return:
        """
    try:
        sqlite_select_query = """SELECT * from Retiros """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


def selectComponentesPromociones(args, cursor, values=None):
    """
        Keys: Id_componente, Id_promocion, Cantidad, Nombre_Producto, Sub_categoria
        :param args:
        :param cursor:
        :param values:
        :return:
        """
    try:
        sqlite_select_query = """SELECT * from Componentes_promociones """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
        records = []
    return records


"""---------------------------------------------------------------------------------
                                Obtención de datos
   ---------------------------------------------------------------------------------"""


def GetUser(user):
    cursor = get_db()
    record = selectUser("WHERE Nombre_usuario = ?;", cursor, tuple(user))
    cursor.close()
    return record


def GetClient(client):
    """Keys: Nombre_cliente, Direccion, Sector, Telefono"""
    cursor = get_db()
    record = selectClient("WHERE Nombre_cliente = ? AND Direccion = ?;", cursor, tuple(client))
    cursor.close()
    return record


def GetClientPerNameOnly(client):
    """Keys: Nombre_cliente, Direccion, Sector, Telefono"""
    cursor = get_db()
    record = selectClient("WHERE Nombre_cliente LIKE ?;", cursor, tuple(client))
    cursor.close()
    return record


def GetBoletas(boleta_key):
    """Keys: Id_entrada, Id_boleta, Nombre_producto, Cantidad, Tamano, Nombre_promocion"""
    cursor = get_db()
    record = selectBoletas("WHERE Id_boleta = ?;", cursor, (boleta_key,))
    cursor.close()
    return record


def GetProduct(product_key):
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    cursor = get_db()
    record = selectProducto("WHERE Nombre_producto = ?;", cursor, tuple(product_key))
    cursor.close()
    return record


def GetProductBySubCathegory(product_key):
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    cursor = get_db()
    record = selectProducto("WHERE Sub_categoria = ?;", cursor, tuple(product_key))
    cursor.close()
    return record


def GetProductByCathegory(product_key):
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    cursor = get_db()
    record = selectProducto("WHERE Categoria = ?;", cursor, tuple(product_key))
    cursor.close()
    return record


def GetAllProducts():
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    cursor = get_db()
    record = selectProducto("", cursor)
    cursor.close()
    return record


def GetSesion(sesion_key):
    """Keys: Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    cursor = get_db()
    record = selectSesion("WHERE Id_sesion = ?;", cursor, (sesion_key,))
    cursor.close()
    return record


def GetSesionPerDates(date_1, date_2):
    """Keys: Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    cursor = get_db()
    record = selectSesion("WHERE Fecha_apertura >= ? and Fecha_apertura <= ?;", cursor, (date_1, date_2,))
    cursor.close()
    return record


def GetLastSesion():
    """Keys: Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    cursor = get_db()
    record = selectSesion("ORDER BY Fecha_apertura ASC;", cursor)
    cursor.close()
    if len(record) > 0:
        return record[-1]
    return record


def GetAllTurns(turn_key):
    """Keys: Id_turno, Id_sesion, Nombre_usuario"""
    cursor = get_db()
    record = selectTurnos_caja("WHERE Id_turno = ?;", cursor, (turn_key,))
    cursor.close()
    return record


def GetOneTurn(turn_key):
    """Keys: Id_turno, Id_sesion, Nombre_usuario"""
    cursor = get_db()
    record = selectTurnos_caja("WHERE Id_turno = ? AND Id_sesion = ?;", cursor, (turn_key,))
    cursor.close()
    return record


def GetVentaPerKey(venta_key):
    """Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo"""
    cursor = get_db()
    record = selectVentas("WHERE Id_turno = ? AND Id_sesion = ?;", cursor, (venta_key,))  # type: dict
    for element in record:
        if 'Id_venta' in element:
            id_boleta = element['Id_venta']
            boleta = GetBoletas(id_boleta)  # type: dict
            for componente in boleta:
                if 'Tamano' in componente:
                    tamano = componente['Tamano']
                else:
                    tamano = 1
                nombre_producto = componente['Nombre_producto']
                verify = nombre_producto.split(" - ")
                if len(verify) > 1:
                    nombre_producto = verify[0]
                producto = GetProduct((nombre_producto,))[0]
                if tamano == 1:
                    precio = producto['Precio_unitario']
                else:
                    precio = producto[tamano]
                componente['Precio'] = precio
            element['Boleta'] = boleta
    cursor.close()
    return record


def GetVentaPerClient(venta_key):
    """Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Adicional, Efectivo"""
    cursor = get_db()
    record = selectVentas("WHERE Nombre_cliente = ? AND Direccion_cliente = ?;", cursor, tuple(venta_key))  # type: dict
    for element in record:
        if 'Id_venta' in element:
            id_boleta = element['Id_venta']
            boleta = GetBoletas(id_boleta)  # type: dict
            for componente in boleta:
                if 'Tamano' in componente:
                    tamano = componente['Tamano']
                else:
                    tamano = 1
                nombre_producto = componente['Nombre_producto']
                verify = nombre_producto.split(" - ")
                if len(verify) > 1:
                    nombre_producto = verify[0]
                producto = GetProduct((nombre_producto,))[0]
                if tamano == 1:
                    precio = producto['Precio_unitario']
                else:
                    precio = producto[tamano]
                componente['Precio'] = precio
            element['Boleta'] = boleta
    cursor.close()
    return record


def GetLastNVentas(n):
    """Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo"""
    cursor = get_db()
    record = selectVentas("ORDER BY Id_venta DESC;", cursor)[-1:-(n + 1): -1]  # type: dict
    for element in record:
        if 'Id_venta' in element:
            id_boleta = element['Id_venta']
            boleta = GetBoletas(id_boleta)  # type: dict
            for componente in boleta:
                if 'Tamano' in componente:
                    tamano = componente['Tamano']
                else:
                    tamano = 1
                nombre_producto = componente['Nombre_producto']
                nombre_promo = componente['Nombre_promocion']
                verify = nombre_producto.split(" - ")
                if len(verify) > 1:
                    nombre_producto = verify[0]
                if nombre_producto:
                    producto = GetProduct((nombre_producto,))[0]
                else:
                    producto = GetPromocion((nombre_promo,))
                if tamano == 1 and nombre_producto:
                    precio = producto['Precio_unitario']
                elif nombre_producto:
                    precio = producto[tamano]
                else:
                    precio = producto['precio']
                componente['Precio'] = precio
            element['Boleta'] = boleta
    cursor.close()
    return record


def GetVentasPerDates(date_1, date_2):
    """Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo"""
    cursor = get_db()
    sesiones = selectSesion("WHERE Fecha_apertura <= ? and Fecha_apertura >= ?", cursor, (date_1, date_2,))
    if sesiones:
        session_ids = []
        for s in sesiones:
            session_ids.append(s['Id_sesion'])
        print(isinstance(int, (session_ids[0],)))
        session_ids.sort()
        values = (session_ids[0], session_ids[-1],)
        record = selectVentas("WHERE Id_sesion <= ? and Id_sesion >= ? ORDER BY Id_sesion DESC;", cursor, values)
        for element in record:
            total = 0
            if 'Id_venta' in element:
                id_boleta = element['Id_venta']
                boleta = GetBoletas(id_boleta)  # type: list
                for componente in boleta:
                    if 'Tamano' in componente:
                        tamano = componente['Tamano']
                    else:
                        tamano = 1
                    nombre_producto = componente['Nombre_producto']
                    nombre_promo = componente['Nombre_promocion']
                    verify = nombre_producto.split(" - ")
                    if len(verify) > 1:
                        nombre_producto = verify[0]
                    if nombre_producto:
                        producto = GetProduct((nombre_producto,))[0]
                    else:
                        producto = GetPromocion((nombre_promo,))
                    if tamano == 1 and nombre_producto:
                        precio = producto['Precio_unitario']
                    elif nombre_producto:
                        precio = producto[tamano]
                    else:
                        precio = producto['precio']
                    componente['Precio'] = precio
                    total += precio
                element['Boleta'] = boleta
                element['Precio_final'] = total
        cursor.close()
        return record
    return []


def GetVentasPerId(id):
    """Keys: Id_venta, Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo"""
    cursor = get_db()
    record = selectVentas("WHERE Id_sesion = ?", cursor, tuple(id))
    total_final = 0
    total_efectivo = 0
    for element in record:
        total = 0
        if 'Id_venta' in element:
            id_boleta = element['Id_venta']
            boleta = GetBoletas(id_boleta)  # type: list
            for componente in boleta:
                if 'Tamano' in componente:
                    tamano = componente['Tamano']
                else:
                    tamano = 1
                nombre_producto = componente['Nombre_producto']
                nombre_promo = componente['Nombre_promocion']
                verify = nombre_producto.split(" - ")
                if len(verify) > 1:
                    nombre_producto = verify[0]
                if nombre_producto:
                    producto = GetProduct((nombre_producto,))[0]
                else:
                    producto = GetPromocion((nombre_promo,))
                if tamano == 1 and nombre_producto:
                    precio = producto['Precio_unitario']
                elif nombre_producto:
                    precio = producto[tamano]
                else:
                    precio = producto['precio']
                componente['Precio'] = precio
                total += precio
            element['Boleta'] = boleta
            element['Precio_final'] = total
            if element['Efectivo'] == 1:
                total_efectivo += total
    retiros = GetRetiros_por_sesion(id)
    for ret in retiros:
        total_efectivo -= ret['Monto']
        total_final -= ret['Monto']
    cursor.close()
    return record, retiros, total_final, total_efectivo


def GetLastNPromociones(n):
    """Keys: Id_promocion, Nombre_promocion, Is_by_sub_cathegory, precio, Tamano"""
    cursor = get_db()
    record = selectPromociones("ORDER BY Id_promocion DESC;", cursor)[-1:-(n + 1): -1]  # type: list
    for element in record:
        if 'Id_promocion' in element:
            id_promocion = element['Id_promocion']
            componentes = selectComponentesPromociones("WHERE Id_promocion = ?", cursor, (id_promocion,))  # type: list
            for componente in componentes:
                is_by_sub_cathegory = componente['Sub_categoria']
                if is_by_sub_cathegory is None or is_by_sub_cathegory == "":
                    nombre_producto = componente['Nombre_producto']
                    verify = nombre_producto.split(" - ")
                    if len(verify) > 1:
                        nombre_producto = verify[0]
                    producto = GetProduct((nombre_producto,))[0]
                    componente['Producto'] = producto
            element['Componentes'] = componentes
    cursor.close()
    return record


def GetPromociones():
    """Keys: Id_promocion, Nombre_promocion, Is_by_sub_cathegory, precio, Tamano"""
    cursor = get_db()
    record = selectPromociones("", cursor)  # type: dict
    for element in record:
        if 'Id_promocion' in element:
            id_promocion = element['Id_promocion']
            componentes = selectComponentesPromociones("WHERE Id_promocion = ?", cursor, (id_promocion,))  # type: list
            for componente in componentes:
                is_by_sub_cathegory = componente['Sub_categoria']
                if is_by_sub_cathegory is None or is_by_sub_cathegory == "":
                    nombre_producto = componente['Nombre_producto']
                    verify = nombre_producto.split(" - ")
                    if len(verify) > 1:
                        nombre_producto = verify[0]
                    producto = GetProduct((nombre_producto,))[0]
                    componente['Producto'] = producto
            element['Componentes'] = componentes
    cursor.close()
    return record


def GetPromocion(nombre_promocion):
    """Keys: Id_promocion, Nombre_promocion, Is_by_sub_cathegory, precio, Tamano"""
    cursor = get_db()
    record = selectPromociones("WHERE Nombre_promocion = ?;", cursor, nombre_promocion)  # type: list
    for element in record:
        if 'Id_promocion' in element:
            id_promocion = element['Nombre_promocion']
            componentes = selectComponentesPromociones("WHERE Id_promocion = ?", cursor,
                                                       tuple((id_promocion,)))  # type: list
            for componente in componentes:
                is_by_sub_cathegory = componente['Sub_categoria']
                if is_by_sub_cathegory is None or is_by_sub_cathegory == "":
                    nombre_producto = componente['Nombre_Producto']
                    verify = nombre_producto.split(" - ")
                    if len(verify) > 1:
                        nombre_producto = verify[0]
                    producto = GetProduct((nombre_producto,))[0]
                    componente['Producto'] = producto
            element['Componentes'] = componentes
    cursor.close()
    return record[:1]


def GetComponentesPromocion(Id_promocion):
    """Keys: Id_componente, Id_promocion, Cantidad, Nombre_Producto, Sub_categoria"""
    cursor = get_db()
    record = selectPromociones("WHERE Id_promocion = ?;", cursor, Id_promocion)  # type: list
    for element in record:
        if 'Id_promocion' in element:
            id_promocion = element['Id_promocion']
            componentes = selectComponentesPromociones("WHERE Id_promocion = ?", cursor,
                                                       tuple((id_promocion,)))  # type: list
            for componente in componentes:
                is_by_sub_cathegory = componente['Sub_categoria']
                if is_by_sub_cathegory is None or is_by_sub_cathegory == "":
                    nombre_producto = componente['Nombre_producto']
                    verify = nombre_producto.split(" - ")
                    if len(verify) > 1:
                        nombre_producto = verify[0]
                    producto = GetProduct((nombre_producto,))[0]
                    componente['Producto'] = producto
            element['Componentes'] = componentes
    cursor.close()
    return record[:1]


def ExistComponentesPromocion(values_componente):
    """Keys: Id_promocion, Cantidad, Nombre_Producto, Sub_categoria
    :return str('Id_componente')"""
    cursor = get_db()
    record = selectComponentesPromociones("WHERE Id_promocion = ? AND Cantidad = ? AND Nombre_Producto = ?\
     and Sub_categoria = ?;", cursor, tuple(values_componente))  # type: list
    if record:
        return record[0]['Id_componente']
    return None


def GetRetiros_por_sesion(sesion_key):
    """Keys: Monto, Descripcion, Id_retiro, Id_sesion"""
    cursor = get_db()
    if type(sesion_key) == tuple or type(sesion_key) == list:
        record = selectRetiros("WHERE Id_sesion = ?;", cursor, tuple(sesion_key))
    else:
        record = selectRetiros("WHERE Id_sesion = ?;", cursor, (sesion_key,))
    cursor.close()
    return record


"""---------------------------------------------------------------------------------
                                Inserción de datos
   ---------------------------------------------------------------------------------"""


def insertUser(values, cursor):
    query = """INSERT INTO Usuarios (Nombre_usuario, Contrasena, Administra) VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertClient(values, cursor):
    """Keys: Nombre_cliente, Direccion, Sector, Telefono"""
    query = """INSERT INTO Cliente (Nombre_cliente, Direccion, Sector, Telefono) VALUES (?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table Cliente")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertBoleta(values, cursor):
    """Keys: Id_entrada, Id_boleta (fk_Boletas), Nombre_producto (fk_Productos), Cantidad, Tamano, Nombre_promocion"""
    query = """INSERT INTO Boletas (Id_boleta, Nombre_producto, Cantidad, Tamano, Nombre_promocion)\
     VALUES (?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table Boletas")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertProduct(values, cursor):
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    query = """INSERT INTO Producto (Nombre_producto, Precio_unitario, Categoria, Sub_categoria,\
 Precio_mediana, Precio_familiar) VALUES (?, ?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertSesion(values, cursor):
    """Keys: Nombre_usuario (fk_Usuarios), Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    query = """INSERT INTO Sesiones (Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre)\
    VALUES (?, ?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table Sesiones")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertTurnos_caja(values, cursor):
    """Keys: Id_sesion (fk_Sesiones), Nombre_usuario (fk_Usuarios)"""
    query = """INSERT INTO Turnos_caja (Id_sesion, Nombre_usuario) VALUES (?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertVenta(values, cursor):
    """Keys: Nombre_usuario (fk_Usuarios), Nombre_cliente (fk_Clientes),
        Direccion_cliente (fk_Clientes), Id_sesion (fk_Sesiones), Efectivo"""
    query = """INSERT INTO Ventas (Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesion, Efectivo)\
     VALUES (?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table Ventas")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertPromocion(values_promocion, values_componentes, cursor=get_db()):
    """Keys_promocion: Nombre_promocion, Is_by_sub_cathegory, precio, Tamano

       Keys_componentes: Is_by_sub_cathegory, Cantidad, Nombre_Producto, Sub_categoria"""
    query = """INSERT INTO Promociones (Nombre_promocion, Is_by_sub_cathegory, precio, Tamano)\
         VALUES (?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values_promocion))
        cursor.commit()
        print("Data inserted successfully into table Promociones")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)
        return


def insertComponentePromo(values_componentes, cursor=get_db()):
    query = """INSERT INTO Componentes_promociones (Id_promocion, Cantidad, Nombre_Producto, Sub_categoria)\
     VALUES (?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values_componentes))
        cursor.commit()
        print("Data inserted successfully into table Componentes_promociones")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertRetiro(values, cursor=get_db()):
    """Keys: Monto, Descripcion, Id_retiro, Id_sesion"""
    query = """INSERT INTO Retiros (Monto, Descripcion, Id_sesion)\
     VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table Retiros")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


"""---------------------------------------------------------------------------------
                              Modificación de datos
   ---------------------------------------------------------------------------------"""


def updateUser(cursor, values):
    """
    Keys: Nombre_usuario, Contrasena, Administra

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_usuario, Contrasena, Administra, Nombre_usuario)
    :return: None
    """
    query = """UPDATE Usuarios 
                SET Contrasena = ?,
                    Administra = ?
                WHERE Nombre_usuario = ?;"""
    try:
        if len(values) != 3:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Usuarios successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)
        return error


def eraseUser(cursor, values):
    """
    Keys: Nombre_usuario, Contrasena, Administra

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_usuario, Contrasena, Administra, Nombre_usuario)
    :return: None
    """
    query = """DELETE FROM Usuarios 
                WHERE Nombre_usuario = ?;"""
    try:
        if len(values) != 1:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Usuarios successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table Usuarios", error)


def updateCliente(cursor, values):
    """
    Keys: Nombre_cliente, Direccion, Sector, Telefono

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_cliente, Direccion, Sector, Telefono, Nombre_cliente, Direccion)
    :return: None
    """
    query = """UPDATE Cliente 
                SET Nombre_cliente = ? ,
                    Direccion = ?,
                    Sector = ?,
                    Telefono = ?
                WHERE Nombre_cliente = ? AND Direccion = ?;"""
    try:
        if len(values) != 6:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Cliente successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateBoleta(cursor, values):
    """
    Keys: Id_entrada, Id_boleta (fk_Boletas), Nombre_producto (fk_Productos), Cantidad, Tamano, Nombre_promocion, Cobro_adicional

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_producto, Cantidad, Tamano, Nombre_promocion, Id_entrada)
    :return: None
    """
    query = """UPDATE Boletas 
                SET Nombre_producto = ?,
                    Cantidad = ?,
                    Tamano = ?,
                    Nombre_promocion = ?
                WHERE Id_entrada = ?;"""
    try:
        if len(values) != 6:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Boletas successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateProducto(cursor, values):
    """
    Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar

    :param cursor: sqlite3 database cursor
    :param values: tuple(Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar, Nombre_producto)
    :return: None
    """
    query = """UPDATE Producto 
                SET Precio_unitario = ?,
                    Categoria = ?,
                    Sub_categoria = ?,
                    Precio_mediana = ?,
                    Precio_familiar = ?
                WHERE Nombre_producto = ?;"""
    try:
        if len(values) != 6:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Producto successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateSesiones(cursor, values):
    """
    Keys: Id_sesion, Nombre_usuario (fk_Usuarios), Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, monto_cierre, Id_sesion)
    :return: None
    """
    query = """UPDATE Sesiones 
                SET Nombre_usuario = ?,
                    Cerrado = ?,
                    Fecha_apertura = ?,
                    Fecha_cierre = ?,
                    Apertura_caja = ?,
                    monto_cierre = ?
                WHERE Id_sesion = ?;"""
    try:
        if len(values) != 7:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Sesiones successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updatePromocion(cursor, values_promo):
    """
        Keys: Id_promocion, Nombre_promocion, Is_by_sub_cathegory, precio, Tamano

        :param cursor: sqlite3 database cursor
        :param values_promo: tuple(Nombre_promocion, Is_by_sub_cathegory, precio, Tamano, Id_promocion)
        :return: None
        """
    query = """UPDATE Promociones 
                    SET Nombre_promocion = ?,
                        Is_by_sub_cathegory = ?,
                        precio = ?,
                        Tamano = ?
                    WHERE Id_promocion = ?;"""
    try:
        if len(values_promo) != 5:
            print("Wrong amount of parameters!", len(values_promo), values_promo)
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values_promo))
            cursor.commit()
            print("Table Producto successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateComponentePromo(values_componentes, cursor=get_db()):
    """
    keys: Id_promocion, Is_by_sub_cathegory, Cantidad, Nombre_Producto, Sub_categoria, Id_componente
    :param values_componentes: Tuple(Id_promocion, Is_by_sub_cathegory, Cantidad, Nombre_Producto, Sub_categoria, Id_componente)
    :param cursor: sqlite3 database cursor
    :return:
    """
    query = """UPDATE Componentes_promociones 
                        SET Id_promocion = ?,
                            Is_by_sub_cathegory = ?,
                            Cantidad = ?,
                            Nombre_Producto = ?,
                            Sub_categoria = ?
                        WHERE Id_componente = ?;"""
    for componente in values_componentes:
        try:
            if len(componente) != 6:
                print("Wrong amount of parameters!")
                raise sqlite3.Error
            else:
                cursor.execute(query, tuple(componente))
                cursor.commit()
                print("Table Componentes_promociones successfully updated")
        except sqlite3.Error as error:
            print("Failed to update data from table", error)


def updateTurnos_caja(cursor, values):
    """
    Keys: Id_turno, Id_sesion (fk_Sesiones), Nombre_usuario (fk_Usuarios)

    :param cursor: sqlite3 database cursor
    :param values: tuple(Id_sesion, Nombre_usuario, Id_turno)
    :return: None
    """
    query = """UPDATE Turnos_caja 
                SET Id_sesion = ?,
                    Nombre_usuario = ?
                WHERE Id_turno = ?;"""
    try:
        if len(values) != 3:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Turnos_caja successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateVentas(cursor, values):
    """
    Keys: Id_venta, Nombre_usuario (fk_Usuarios), Nombre_cliente (fk_Clientes),
        Direccion_cliente (fk_Clientes), Id_sesion (fk_Sesiones), Efectivo

    :param cursor: sqlite3 database cursor
    :param values: tuple(Nombre_usuario, Nombre_cliente, Direccion_cliente, Id_sesio, Efectivo, Id_venta)
    :return: None
    """
    query = """UPDATE Ventas 
                SET Nombre_usuario = ?,
                    Nombre_cliente = ?,
                    Direccion_cliente = ?,
                    Id_sesio = ?,
                    Efectivo = ?
                WHERE Id_venta = ?;"""
    try:
        if len(values) != 5:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Ventas successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


def updateRetiro(cursor, values):
    """
    Keys: Monto, Descripcion, Id_retiro, Id_sesion

    :param cursor: sqlite3 database cursor
    :param values: tuple(Monto, Descripcion, Id_sesion, Id_retiro)
    :return: None
    """
    query = """UPDATE Ventas 
                SET Monto = ?,
                    Descripcion = ?,
                    Id_sesion = ?
                WHERE Id_retiro = ?;"""
    try:
        if len(values) != 4:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Ventas successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)
