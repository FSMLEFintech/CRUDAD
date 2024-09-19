from database import conectar

# Función para editar un cliente
def editar_cliente(id_cliente, nuevo_nombre, nueva_direccion, nuevo_telefono, nueva_orden):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clientes
        SET nombre = ?, direccion = ?, telefono = ?, orden = ?
        WHERE id = ?
    ''', (nuevo_nombre, nueva_direccion, nuevo_telefono, nueva_orden, id_cliente))
    conn.commit()
    conn.close()

# Función para editar un empleado
def editar_empleado(id_empleado, nuevo_nombre, nuevo_puesto, nuevo_salario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE empleados
        SET nombre = ?, puesto = ?, salario = ?
        WHERE id = ?
    ''', (nuevo_nombre, nuevo_puesto, nuevo_salario, id_empleado))
    conn.commit()
    conn.close()

# Puedes agregar funciones adicionales para otros CRUDs según sea necesario.
