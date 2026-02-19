from users import buscar_correo
from security import verify_password

def login():
    print("Bienvendo a CRUD")

    correoinput = input("ingrese su correo: ").strip()
    input("press any button to continue...")

    if correoinput == "":
        print("Credenciales incorrectas...")
        return False

    passinput = input("ingrese su contraseña: ")
    input("press any button to continue...")
    
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