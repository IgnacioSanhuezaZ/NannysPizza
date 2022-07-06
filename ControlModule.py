from . import DatabaseModule as db


"""---------------------------------------------------------------------------------
                        Sección de control de acceso y gestión
   ---------------------------------------------------------------------------------"""

def control_acceso(credenciales, p_opcion):
    cursor = db.get_db()
    usu_tipo_usuario = db.selectUser("WHERE Usuarios_pk = ? AND Contrasena = ?;", cursor, tuple(credenciales))
    if usu_tipo_usuario == []:
        print("Usuario o contraseña incorrecta")
        cursor.close()
        return ["Invalid user or password provided", 'error']
    cursor.close()
    return usu_tipo_usuario