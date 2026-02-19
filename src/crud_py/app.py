from .users_repo import buscar_correo
from .security import verify_password

def login():
    print("Bienvendo a CRUD")

    correoinput = input("ingrese su correo: ").strip().lower()

    if correoinput == "":
        print("Credenciales incorrectas...")
        return False

    passinput = input("ingrese su contraseña: ")

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

    print("Bienvenido", db_usuario["nombre"])
    return True

def main():
    for i in range(3):
        ok = login()
        if ok:
            return
    else:
        print("intentos excedidos. cerrado el programa...")
        raise SystemExit(1)