import pyodbc

def crear_conexion():
    sql_server_config = {
        'server': 'LAPTOP-GHJ9NM02\\SQLEXPRESS',
        'database': 'GranjaHidroponica',
        'username': 'sa',
        'password': '12345678'
    }

    conexion = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={sql_server_config['server']};"
        f"DATABASE={sql_server_config['database']};"
        f"UID={sql_server_config['username']};"
        f"PWD={sql_server_config['password']}"
    )

    return conexion

# Funciones para la tabla Cultivo
def consultar_cultivos():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Cultivo")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def insertar_cultivo(tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Cultivo (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado))
    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones para la tabla Insumo
def consultar_insumos():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Insumo")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def insertar_insumo(tipo_insumo, cantidad_disponible, fecha_caducidad):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Insumo (tipo_insumo, cantidad_disponible, fecha_caducidad)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (tipo_insumo, cantidad_disponible, fecha_caducidad))
    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones para la tabla Cliente
def consultar_clientes():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Cliente")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def insertar_cliente(nombre, correo, telefono):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Cliente (nombre, correo, telefono)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (nombre, correo, telefono))
    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones para la tabla Venta
def consultar_ventas():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Venta")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def insertar_venta(cliente_id, fecha_venta, total):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Venta (cliente_id, fecha_venta, total)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (cliente_id, fecha_venta, total))
    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones para la tabla Detalle_Venta
def consultar_detalle_ventas():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Detalle_Venta")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def insertar_detalle_venta(venta_id, cultivo_id, cantidad, subtotal):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Detalle_Venta (venta_id, cultivo_id, cantidad, subtotal)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (venta_id, cultivo_id, cantidad, subtotal))
    conexion.commit()
    cursor.close()
    conexion.close()

# Ejemplo de uso
insertar_cultivo("lechuga ", "2024-10-29", "aumento", 150.00)
print("NUevo Cultivo agregado a la base de datos.")

cultivos = consultar_cultivos()
for cultivo in cultivos:
    print(cultivo)

insertar_cliente("Nicolas Bustos", "Wilson@example.com", "123456789")
print("El cliente se agrego a la base de datos.")

clientes = consultar_clientes()
for cliente in clientes:
    print(cliente)