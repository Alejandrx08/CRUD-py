from .users_repo import buscar_correo
from .security import verify_password
from .users_repo import listar_usuarios
from .users_repo import crear_usuarios
from .users_repo import buscar_id
from .users_repo import actualizar_usuario
from .users_repo import eliminar_id
from .db import init_db


def login():
    print("Bienvendo a CRUD")

    correoinput = input("ingrese su correo: ").strip().lower()

    if correoinput == "":
        print("Credenciales incorrectas...")
        return False

    passinput = input("ingrese su contraseña: ").strip()

    if passinput == "":
        print("Credenciales incorrectas...")
        return False

    db_usuario = buscar_correo(correoinput)

    if db_usuario is None:
        print("Credenciales incorrectas...")
        return False

    if db_usuario["activo"] == 0:
        print("Credenciales incorrectas...")
        return False

    db_pass = verify_password(passinput, db_usuario["password"])

    if db_pass == False:
        print("Credenciales incorrectas...")
        return False
    return db_usuario


def main():
    init_db()
    for i in range(3):
        logged = login()
        if logged:
            menu(logged)
            return
    else:
        print("intentos excedidos. cerrado el programa...")
        raise SystemExit(1)


def menu(usuario):
    while True:
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print("  Bienvenido", usuario["nombre"])
        print("  Que accion desea realizar?  ")
        print("  1.Listar Usuarios           ")
        print("  2.Crear un usuario          ")
        print("  3.Buscar por ID             ")
        print("  4.Editar usuario            ")
        print("  5.Eliminar usuario          ")
        print("  0.Salir                     ")
        accion = input("  : ").strip()
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

        if accion == "1":
            usuarios = listar_usuarios()
            for u in usuarios:
                print(dict(u))

        elif accion == "2":
            if usuario["rango"] == "admin":
                nombre = input("Nombre: ").strip()
                if nombre == "":
                    continue
                if nombre.isdigit():
                    print("La entrada no puede ser numerica.")
                    continue

                apellido = input("Apellido: ").strip()
                if apellido == "":
                    continue
                if apellido.isdigit():
                    print("La entrada no puede ser numerica.")
                    continue

                correo = input("Correo: ").strip()
                if correo == "":
                    continue

                password = input("Contraseña: ").strip()
                if password == "":
                    continue

                print("Rango")
                print("1. Admin, 2.Usuario")
                rangonum = input(": ")
                if rangonum == "1":
                    rango = "admin"
                elif rangonum == "2":
                    rango = "usuario"
                else:
                    print("Caracter invalido.")
                    continue

                print("Tipo")
                print("1.Dev, 2.Alumno")
                tiponum = input(": ")
                if tiponum == "1":
                    tipo = "dev"
                elif tiponum == "2":
                    tipo = "alumno"
                else:
                    print("Caracter invalido.")
                    continue

                count = crear_usuarios(nombre, apellido, correo, password, rango, tipo)
                if count == 1:
                    print("Usuario creado exitosamente.")
                elif count == 0:
                    print("El correo ya esta en uso.")
                    continue
                else:
                    print("Error inesperado al crear usuario.")

            else:
                print("Opcion solo disponible para admin.")

        elif accion == "3":
            user_id = input("Id: ").strip()

            if not user_id.isdigit():
                print("El valor debe ser numérico.")
                continue

            usernum = int(user_id)

            user = buscar_id(usernum)
            if user is None:
                print("Usuario no existente.")
                continue

            print(dict(user))

        elif accion == "4":
            if usuario["rango"] == "admin":

                user_id = input("Id: ").strip()

                if not user_id.isdigit():
                    print("el valor debe ser numerico")
                    continue

                usernum = int(user_id)

                idex = buscar_id(usernum)
                if idex is None:
                    print("Usuario no existente.")
                    continue

                nombre = input("Nombre: ").strip()
                if nombre == "":
                    continue
                if nombre.isdigit():
                    print("La entrada no puede ser numerica.")
                    continue

                apellido = input("Apellido: ").strip()
                if apellido == "":
                    continue
                if apellido.isdigit():
                    print("La entrada no puede ser numerica.")
                    continue

                correo = input("Correo: ").strip()
                if correo == "":
                    continue

                password = input("Contraseña (Enter para no cambiar): ").strip()

                print("Rango")
                print("1. Admin, 2.Usuario")
                rangonum = input(": ")
                if rangonum == "1":
                    rango = "admin"
                elif rangonum == "2":
                    rango = "usuario"
                else:
                    print("Caracter invalido.")
                    continue

                print("Tipo")
                print("1.Dev, 2.Alumno")
                tiponum = input(": ")
                if tiponum == "1":
                    tipo = "dev"
                elif tiponum == "2":
                    tipo = "alumno"
                else:
                    print("Caracter invalido.")
                    continue

                print("Estado")
                print("1.Activo, 2.Inativo")
                estado = input(": ")
                if estado == "1":
                    activo = 1
                elif estado == "2":
                    activo = 0
                else:
                    print("Caracter invalido.")
                    continue

                exc = actualizar_usuario(
                    usernum, nombre, apellido, correo, password, rango, tipo, activo
                )
                if exc == 1:
                    print("Usuario actualizado exitosamente")
                elif exc == -2:
                    print("El correo ya esta en uso")
                else:
                    print("No hubo cambios")

            else:
                print("Opcion solo disponible para admin.")

        elif accion == "5":
            if usuario["rango"] == "admin":
                user_id = input("Id: ").strip()

                if not user_id.isdigit():
                    print("el valor debe ser numerico")
                    continue

                usernum = int(user_id)

                idex = buscar_id(usernum)
                if idex is None:
                    print("Usuario no existente.")
                    continue

                count = eliminar_id(usernum)
                if count > 0:
                    print(count, "Usuario eliminado exitosamente")
                else:
                    print("No se eliminó nada (ya no existía o hubo un error).")

            else:
                print("Opcion solo disponible para admin.")

        elif accion == "0":
            print("gracias por utilizar CRUD-Py...")
            return
