from database import conectar

def agregar_curso(codigo, nombre, creditos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cursos (codigo, nombre, creditos)
        VALUES (?, ?, ?)
    ''', (codigo, nombre, creditos))
    conn.commit()
    conn.close()
