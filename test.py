from db import abrir_conexion
from db import init_db
from users import crear_usuarios
from users import listar_usuarios
from users import buscar_correo
from users import eliminar_id
from users import actualizar_usuario

conx = abrir_conexion()
print(conx)

init_db()


#crear_usuarios("Alejandro", "Ibarra", "AleIb@mail.com", "2008", "admin", "dev")
#print("Usuario insertado")

usuarios = listar_usuarios()

for u in usuarios:
    print(dict(u))

#fila = buscar_correo("harry@mail.com")

#if fila:
    #print(dict(fila))
#else:
    #print("No encontrado")


#filas = eliminar_id(1)

#if filas == 0:
#   print("No existía ese usuario")
#else:
#    print("Usuario eliminado")


#filas = actualizar_usuario(
#    2,
#    "Juan",
#    "Perez",
#    "juan@mail.com",
#    "1234",
#    "user",
#    "dev",
#    1
#)

#print("Filas afectadas:", filas)

