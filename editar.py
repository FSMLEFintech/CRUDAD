from database import conectar

def editar_curso(id_curso, nuevo_codigo, nuevo_nombre, nuevos_creditos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE cursos
        SET codigo = ?, nombre = ?, creditos = ?
        WHERE id = ?
    ''', (nuevo_codigo, nuevo_nombre, nuevos_creditos, id_curso))
    conn.commit()
    conn.close()
