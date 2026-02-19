from .db import init_db
from .users_repo import crear_usuarios
from .db import abrir_conexion

conx = abrir_conexion()
print(conx)

init_db()

###

# crear_usuarios("Alejandro", "Ibarra", "AleIb@mail.com", "2008", "admin", "dev")
# print("Usuario insertado")

###

# usuarios = listar_usuarios()

# for u in usuarios:
# print(dict(u))

###

# fila = buscar_correo("harry@mail.com")

# if fila:
#    print(dict(fila))
# else:
#    print("No encontrado")

###

# filas = eliminar_id(1)

# if filas == 0:
#   print("No existía ese usuario")
# else:
#    print("Usuario eliminado")

###

# from users import buscar_correo
# print(buscar_correo("harry@mail.com"))

###

# verify_password("1234", fila["password"])

###
