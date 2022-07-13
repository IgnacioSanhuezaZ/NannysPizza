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
    Keys: Nombre_producto, Precio, Categoria
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
