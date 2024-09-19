from database import conectar

# Listar clientes
def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

# Listar empleados
def listar_empleados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()
    conn.close()
    return empleados

# Listar insumos
def listar_insumos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM insumos')
    insumos = cursor.fetchall()
    conn.close()
    return insumos
