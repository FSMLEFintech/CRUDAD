from database import conectar

def listar_cursos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cursos')
    cursos = cursor.fetchall()
    conn.close()
    return cursos
