from database import conectar

# Función para agregar un cliente (que ya tienes)
def agregar_cliente(nombre, direccion, telefono, orden):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nombre, direccion, telefono, orden)
        VALUES (?, ?, ?, ?)
    ''', (nombre, direccion, telefono, orden))
    conn.commit()
    conn.close()

# Función para agregar un empleado
def agregar_empleado(nombre, puesto, salario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO empleados (nombre, puesto, salario)
        VALUES (?, ?, ?)
    ''', (nombre, puesto, salario))
    conn.commit()
    conn.close()
