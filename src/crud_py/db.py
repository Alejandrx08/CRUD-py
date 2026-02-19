import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "app.db"
SCHEMA_PATH = BASE_DIR / "schema" / "schema.sql"


def abrir_conexion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    sql = SCHEMA_PATH.read_text(encoding="utf-8")
    with abrir_conexion() as conn:
        conn.executescript(sql)
