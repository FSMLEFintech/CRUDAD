import sqlite3

def conectar():
    conn = sqlite3.connect('cursos.db')
    return conn

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            nombre TEXT NOT NULL,
            creditos INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
