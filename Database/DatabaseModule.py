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


def GetUser(user):
    cursor = get_db()
    record = selectUser("WHERE Nombre_usuario = ?;", cursor, (user,))
    cursor.close()
    return record


def insertUser(values, cursor):
    query = """INSERT INTO Usuarios (Nombre_usuario, Contrasena, Administra) VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, tuple(values))
        cursor.commit()
        print("Data inserted successfully into table User")
    except sqlite3.Error as error:
        print("Failed to insert data into table", error)
