from database import conectar

# Función para eliminar un cliente
def eliminar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    conn.commit()
    conn.close()

# Función para eliminar un empleado
def eliminar_empleado(id_empleado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM empleados WHERE id = ?', (id_empleado,))
    conn.commit()
    conn.close()

# Puedes agregar funciones adicionales para otros CRUDs según sea necesario.
