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
    db = sqlite3.connect('nannys_pizza.sqlite', sqlite3.PARSE_DECLTYPES)
    db.row_factory = dict_factory
    print("Conexión con la base de datos establecida")
    return db


def close_db(db):
    """Cierra la conexión a la base de datos"""
    if db is not None:
        db.close()
        print("Conexión con base de datos cerrada")


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
        print("Failed to get data into sqlite table", error)
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
        print("Failed to get data into sqlite table", error)
        records = []
    return records


def selectBoletas(args, cursor, values=None):
    """
    Keys: Id_entrada, Id_boleta, Nombre_producto, Cantidad
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
        print("Failed to get data into sqlite table", error)
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
        print("Failed to get data into sqlite table", error)
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
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data into sqlite table", error)
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
        print("Failed to get data into sqlite table", error)
        records = []
    return records


def selectVentas(args, cursor, values=None):
    """
    Keys: Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesion
    :param args:
    :param cursor:
    :param values:
    :return:
    """
    try:
        sqlite_select_query = """SELECT * from Ventas """
        if args != "":
            sqlite_select_query += args
            records = list(cursor.execute(sqlite_select_query, tuple(values)))
        else:
            records = list(cursor.execute(sqlite_select_query))
    except sqlite3.Error as error:
        print("Failed to get data into sqlite table", error)
        records = []
    return records


"""---------------------------------------------------------------------------------
                                Obtención de datos
   ---------------------------------------------------------------------------------"""


def GetUser(user):
    cursor = get_db()
    record = selectUser("WHERE Nombre_usuario = ?;", cursor, (user,))
    cursor.close()
    return record


def GetClient(client):
    """Keys: Nombre_cliente, Direccion, Sector, Telefono"""
    cursor = get_db()
    record = selectClient("WHERE Nombre_cliente = ? AND Direccion = ?;", cursor, (client,))
    cursor.close()
    return record


def GetBoletas(boleta_key):
    """Keys: Id_entrada, Id_boleta, Nombre_producto, Cantidad"""
    cursor = get_db()
    record = selectBoletas("WHERE Id_entrada = ?;", cursor, (boleta_key,))
    cursor.close()
    return record


def GetProduct(product_key):
    """Keys: Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar"""
    cursor = get_db()
    record = selectProducto("WHERE Nombre_producto = ?;", cursor, (product_key,))
    cursor.close()
    return record


def GetSesion(sesion_key):
    """Keys: Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    cursor = get_db()
    record = selectSesion("WHERE Id_sesion = ?;", cursor, (sesion_key,))
    cursor.close()
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
    """Keys: Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesion"""
    cursor = get_db()
    record = selectVentas("WHERE Id_turno = ? AND Id_sesion = ?;", cursor, (venta_key,))
    cursor.close()
    return record


def GetVentaPerClient(venta_key):
    """Keys: Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesion"""
    cursor = get_db()
    record = selectVentas("WHERE Direccion_cliente = ?;", cursor, (venta_key,))   # type: dict
    cursor.close()
    """
    if 'Id_boleta' in record:
        id_boleta = record['Id_boleta']
        boleta = GetBoletas(id_boleta)   # type: dict
        del boleta['Id_entrada']
        del boleta['Id_boleta']
        del record['Id_boleta']
        record['Boleta'] = boleta
    """
    return record



def GetLastNVentas(venta_key, n):
    """Keys: Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesion"""
    cursor = get_db()
    record = selectVentas("ORDER BY Id_venta DESC;", cursor, (venta_key,))   # type: dict
    if len(record) > n:
        record = record[:n]
    for rec in record:
        if 'Id_boleta' in rec:
            id_boleta = rec['Id_boleta']
            boleta = GetBoletas(id_boleta)   # type: dict
            del boleta['Id_entrada']
            del boleta['Id_boleta']
            del rec['Id_boleta']
            rec['Boleta'] = boleta
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
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertBoleta(values, cursor):
    """Keys: Id_entrada, Id_boleta (fk_Boletas), Nombre_producto (fk_Productos), Cantidad"""
    query = """INSERT INTO Boletas (Id_entrada, Id_boleta, Nombre_producto, Cantidad) VALUES (?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
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
    """Keys: Id_sesion, Nombre_usuario (fk_Usuarios), Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja"""
    query = """INSERT INTO Sesiones (Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja)\
    VALUES (?, ?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertTurnos_caja(values, cursor):
    """Keys: Id_turno, Id_sesion (fk_Sesiones), Nombre_usuario (fk_Usuarios)"""
    query = """INSERT INTO Turnos_caja (Id_turno, Id_sesion, Nombre_usuario) VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)


def insertVenta(values, cursor):
    """Keys: Id_venta, Nombre_usuario (fk_Usuarios), Id_boleta (fk_Boletas), Nombre_cliente (fk_Clientes),
        Direccion_cliente (fk_Clientes), Id_sesion (fk_Sesiones)"""
    query = """INSERT INTO Ventas (Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesion)\
     VALUES (?, ?, ?, ?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
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
                SET Nombre_usuario = ? ,
                    Contrasena = ?,
                    Administra = ?
                WHERE Nombre_usuario = ?;"""
    try:
        if len(values) != 4:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Usuarios successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)


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
    Keys: Id_entrada, Id_boleta (fk_Boletas), Nombre_producto (fk_Productos), Cantidad

    :param cursor: sqlite3 database cursor
    :param values: tuple(Id_entrada, Id_boleta, Nombre_producto, Cantidad, Id_entrada)
    :return: None
    """
    query = """UPDATE Boletas 
                SET Id_entrada = ? ,
                    Id_boleta = ?,
                    Nombre_producto = ?,
                    Cantidad = ?
                WHERE Id_entrada = ?;"""
    try:
        if len(values) != 5:
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
    :param values: tuple(Nombre_producto, Precio_unitario, Categoria, Sub_categoria, Precio_mediana, Precio_familiar,
                         Nombre_producto)
    :return: None
    """
    query = """UPDATE Producto 
                SET Nombre_producto = ? ,
                    Precio_unitario = ?,
                    Categoria = ?,
                    Sub_categoria = ?,
                    Precio_mediana = ?,
                    Precio_familiar = ?
                WHERE Nombre_producto = ?;"""
    try:
        if len(values) != 7:
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
    :param values: tuple(Id_sesion, Nombre_usuario, Cerrado, Fecha_apertura, Fecha_cierre, Apertura_caja, Id_sesion)
    :return: None
    """
    query = """UPDATE Sesiones 
                SET Id_sesion = ? ,
                    Nombre_usuario = ?,
                    Cerrado = ?
                    Fecha_apertura = ?,
                    Fecha_cierre = ?,
                    Apertura_caja = ?,
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


def updateTurnos_caja(cursor, values):
    """
    Keys: Id_turno, Id_sesion (fk_Sesiones), Nombre_usuario (fk_Usuarios)

    :param cursor: sqlite3 database cursor
    :param values: tuple(Id_turno, Id_sesion, Nombre_usuario, Id_turno)
    :return: None
    """
    query = """UPDATE Turnos_caja 
                SET Id_turno = ? ,
                    Id_sesion = ?,
                    Nombre_usuario = ?
                WHERE Id_turno = ?;"""
    try:
        if len(values) != 4:
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
    Keys: Id_venta, Nombre_usuario (fk_Usuarios), Id_boleta (fk_Boletas), Nombre_cliente (fk_Clientes),
        Direccion_cliente (fk_Clientes), Id_sesion (fk_Sesiones)

    :param cursor: sqlite3 database cursor
    :param values: tuple(Id_venta, Nombre_usuario, Id_boleta, Nombre_cliente, Direccion_cliente, Id_sesio, Id_venta)
    :return: None
    """
    selectVentas()
    query = """UPDATE Ventas 
                SET Id_venta = ? ,
                    Nombre_usuario = ?,
                    Id_boleta = ?,
                    Nombre_cliente = ?,
                    Direccion_cliente = ?,
                    Id_sesio = ?
                WHERE Id_venta = ?;"""
    try:
        if len(values) != 7:
            print("Wrong amount of parameters!")
            raise sqlite3.Error
        else:
            cursor.execute(query, tuple(values))
            cursor.commit()
            print("Table Ventas successfully updated")
    except sqlite3.Error as error:
        print("Failed to update data from table", error)
