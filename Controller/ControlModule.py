from Database import DatabaseModule as db

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
