from db import abrir_conexion
from db import init_db
from users import crear_usuarios
from users import listar_usuarios
from users import buscar_correo
from users import eliminar_id
from users import actualizar_usuario
from app import login
from security import verify_password

conx = abrir_conexion()
print(conx)

init_db()

###

#crear_usuarios("Alejandro", "Ibarra", "AleIb@mail.com", "2008", "admin", "dev")
#print("Usuario insertado")

###

#usuarios = listar_usuarios()

#for u in usuarios:
    #print(dict(u))

###

#fila = buscar_correo("harry@mail.com")

#if fila:
#    print(dict(fila))
#else:
#    print("No encontrado")

###

#filas = eliminar_id(1)

#if filas == 0:
#   print("No existía ese usuario")
#else:
#    print("Usuario eliminado")

###

#from users import buscar_correo
#print(buscar_correo("harry@mail.com"))

###

#verify_password("1234", fila["password"])

###

init_db()

try:
    crear_usuarios("Alejandro", "Ibarra", "AleIb@mail.com", "2008", "admin", "dev")
    crear_usuarios("Maria", "Lopez", "maria@mail.com", "pass456", "user", "alumno")
    crear_usuarios("Carlos", "Gomez", "carlos@mail.com", "carlos789", "user", "alumno")
    crear_usuarios("Ana", "Martinez", "ana@mail.com", "ana321", "user", "alumno")
    crear_usuarios("Luis", "Hernandez", "luis@mail.com", "luis654", "user", "alumno")
    crear_usuarios("Sofia", "Ramirez", "sofia@mail.com", "sofia987", "user", "alumno")
    crear_usuarios("Diego", "Torres", "diego@mail.com", "diego111", "user", "alumno")
    crear_usuarios("Valeria", "Flores", "valeria@mail.com", "vale222", "user", "alumno")
    crear_usuarios("Andres", "Castro", "andres@mail.com", "andres333", "user", "alumno")

    print("✔ 10 usuarios creados correctamente")

except Exception as e:
    print("Error creando usuarios:", e)