import sqlite3

def conectar():
    conn = sqlite3.connect('veterinaria.db')
    return conn

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    # Crear tabla de clientes si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            orden TEXT NOT NULL
        )
    ''')

    # Crear tabla de empleados si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puesto TEXT NOT NULL,
            salario REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
