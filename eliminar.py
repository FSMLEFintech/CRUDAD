from database import conectar

def eliminar_curso(id_curso):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cursos WHERE id = ?', (id_curso,))
    conn.commit()
    conn.close()
