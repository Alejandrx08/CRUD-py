import sqlite3
from pathlib import Path

ruta = Path(__file__)

carpeta = ruta.parent

ruta_db = carpeta / "app.db"

ruta_schema = carpeta/"schema.sql"

def abrir_conexion():
    conn = sqlite3.connect(ruta_db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    sql = ruta_schema.read_text(encoding="utf-8")

    with abrir_conexion() as conn:
        conn.executescript(sql)
        conn.commit()

        print("db inicializada")