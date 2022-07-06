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


"""------------------------------------------------------------------------------
                                Sección de utilidades
   ------------------------------------------------------------------------------"""



