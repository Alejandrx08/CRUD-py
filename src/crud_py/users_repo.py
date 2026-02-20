from .db import abrir_conexion
from .security import hash_password


def crear_usuarios(nombre, apellido, correo, password, rango, tipo):
    hashed = hash_password(password)
    correolow = correo.strip().lower()

    try:
        with abrir_conexion() as conn:
            cur = conn.execute(
                """INSERT INTO usuarios(nombre, apellido, correo, password, rango, tipo)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (nombre, apellido, correolow, hashed, rango, tipo),
            )
            conn.commit()
            return cur.rowcount

    except sqlite3.IntegrityError:
        return 0


def listar_usuarios():
    with abrir_conexion() as conn:
        cursor = conn.execute("SELECT * FROM usuarios")

        usuarios = cursor.fetchall()
        return usuarios


def buscar_correo(correo):
    with abrir_conexion() as conn:
        cursor = conn.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))

        fila = cursor.fetchone()
        return fila


def buscar_id(user_id):
    with abrir_conexion() as conn:
        cursor = conn.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))

        fila = cursor.fetchone()
        return fila


def eliminar_id(user_id):
    with abrir_conexion() as conn:
        cursor = conn.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))

        count = cursor.rowcount
        conn.commit()
        return count


import sqlite3


def actualizar_usuario(
    user_id, nombre, apellido, correo, password, rango, tipo, activo
):
    correolow = correo.strip().lower()

    try:
        with abrir_conexion() as conn:
            if password == "":
                cursor = conn.execute(
                    """UPDATE usuarios
                       SET nombre=?, apellido=?, correo=?, rango=?, tipo=?, activo=?
                       WHERE id=?""",
                    (nombre, apellido, correolow, rango, tipo, activo, user_id),
                )
            else:
                hashed = hash_password(password)
                cursor = conn.execute(
                    """UPDATE usuarios
                       SET nombre=?, apellido=?, correo=?, password=?, rango=?, tipo=?, activo=?
                       WHERE id=?""",
                    (nombre, apellido, correolow, hashed, rango, tipo, activo, user_id),
                )

            conn.commit()
            return cursor.rowcount

    except sqlite3.IntegrityError:
        return -2
