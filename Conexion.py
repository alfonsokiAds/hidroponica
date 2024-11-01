import pymysql

# Configuración de conexión a la base de datos
def crear_conexion():
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'happyme',
        'database': 'GranjaHidroponica'
    }
    mysql_conn = pymysql.connect(**mysql_config)
    return mysql_conn

# Funciones CRUD para la tabla Cultivo
def insertar_cultivo(tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO Cultivo (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cultivo registrado con éxito.")

def leer_cultivos():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Cultivo")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "UPDATE Cultivo SET tipo_planta = %s, fecha_siembra = %s, estado_crecimiento = %s, rendimiento_esperado = %s WHERE id_cultivo = %s"
    cursor.execute(query, (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado, id_cultivo))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cultivo actualizado exitosamente.")

def eliminar_cultivo(id_cultivo):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "DELETE FROM Cultivo WHERE id_cultivo = %s"
    cursor.execute(query, (id_cultivo,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("el Cultivo a cido eliminado con éxito.")

# Funciones CRUD para la tabla Insumo
def insertar_insumo(tipo_insumo, cantidad_disponible, fecha_caducidad):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO Insumo (tipo_insumo, cantidad_disponible, fecha_caducidad) VALUES (%s, %s, %s)"
    cursor.execute(query, (tipo_insumo, cantidad_disponible, fecha_caducidad))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Insumo agregado con éxito.")

def leer_insumos():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Insumo")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "UPDATE Insumo SET tipo_insumo = %s, cantidad_disponible = %s, fecha_caducidad = %s WHERE id_insumo = %s"
    cursor.execute(query, (tipo_insumo, cantidad_disponible, fecha_caducidad, id_insumo))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Insumo actualizado.")

def eliminar_insumo(id_insumo):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "DELETE FROM Insumo WHERE id_insumo = %s"
    cursor.execute(query, (id_insumo,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("El insumo a cido eliminado con exito.")

# Funciones CRUD para la tabla Cliente
def insertar_cliente(nombre, correo, telefono):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO Cliente (nombre, correo, telefono) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, correo, telefono))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente insertado exitosamente.")

def leer_clientes():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Cliente")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_cliente(id_cliente, nombre, correo, telefono):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "UPDATE Cliente SET nombre = %s, correo = %s, telefono = %s WHERE id_cliente = %s"
    cursor.execute(query, (nombre, correo, telefono, id_cliente))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente actualizado con éxito.")

def eliminar_cliente(id_cliente):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "DELETE FROM Cliente WHERE id_cliente = %s"
    cursor.execute(query, (id_cliente,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente eliminado exitosamente.")

# Funciones CRUD para la tabla Venta
def insertar_venta(cliente_id, fecha_venta, total):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO Venta (cliente_id, fecha_venta, total) VALUES (%s, %s, %s)"
    cursor.execute(query, (cliente_id, fecha_venta, total))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Venta insertada .")

def leer_ventas():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Venta")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_venta(id_venta, cliente_id, fecha_venta, total):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "UPDATE Venta SET cliente_id = %s, fecha_venta = %s, total = %s WHERE id_venta = %s"
    cursor.execute(query, (cliente_id, fecha_venta, total, id_venta))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Se actualizado la venta.")

def eliminar_venta(id_venta):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "DELETE FROM Venta WHERE id_venta = %s"
    cursor.execute(query, (id_venta,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Se a eliminado la venta.")

# Funciones CRUD para la tabla Detalle_Venta
def insertar_detalle_venta(venta_id, cultivo_id, cantidad, subtotal):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "INSERT INTO Detalle_Venta (venta_id, cultivo_id, cantidad, subtotal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (venta_id, cultivo_id, cantidad, subtotal))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Detalle de venta insertado.")

def leer_detalles_venta():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Detalle_Venta")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "UPDATE Detalle_Venta SET venta_id = %s, cultivo_id = %s, cantidad = %s, subtotal = %s WHERE id_detalle = %s"
    cursor.execute(query, (venta_id, cultivo_id, cantidad, subtotal, id_detalle))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Detalle de venta actualizado.")

def eliminar_detalle_venta(id_detalle):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "DELETE FROM Detalle_Venta WHERE id_detalle = %s"
    cursor.execute(query, (id_detalle,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Detalle de venta eliminado.")

# Ejemplo del menú interactivo para cada tabla
while True:
    print("\nSelecciona la tabla para realizar la operación CRUD:")
    print("1. Cultivo")
    print("2. Insumo")
    print("3. Cliente")
    print("4. Venta")
    print("5. Detalle_Venta")
    print("6. Salir")
    
    tabla = int(input("Indique la tabla: "))

    if tabla == 1:
        # Menú de operaciones para Cultivo
        print("\nOpciones para la tabla Cultivo:")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        operacion = int(input("Elige una operación: "))

        if operacion == 1:
            tipo_planta = input("Tipo de planta: ")
            fecha_siembra = input("Fecha de siembra (AAAA-MM-DD): ")
            estado_crecimiento = input("Estado de crecimiento: ")
            rendimiento_esperado = float(input("Rendimiento esperado: "))
            insertar_cultivo(tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)

        elif operacion == 2:
            cultivos = leer_cultivos()
            for cultivo in cultivos:
                print(cultivo)

        elif operacion == 3:
            id_cultivo = int(input("ID del cultivo a actualizar: "))
            tipo_planta = input("Nuevo tipo de planta: ")
            fecha_siembra = input("Nueva fecha de siembra (AAAA-MM-DD): ")
            estado_crecimiento = input("Nuevo estado de crecimiento: ")
            rendimiento_esperado = float(input("Nuevo rendimiento esperado: "))
            actualizar_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)

        elif operacion == 4:
            id_cultivo = int(input("ID del cultivo a eliminar: "))
            eliminar_cultivo(id_cultivo)

    elif tabla == 2:
        # Menú de operaciones para Insumo
        print("\nOpciones para la tabla Insumo:")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        operacion = int(input("Elige una operación: "))

        if operacion == 1:
            tipo_insumo = input("Tipo de insumo: ")
            cantidad_disponible = float(input("Cantidad disponible: "))
            fecha_caducidad = input("Fecha de caducidad (AAAA-MM-DD): ")
            insertar_insumo(tipo_insumo, cantidad_disponible, fecha_caducidad)

        elif operacion == 2:
            insumos = leer_insumos()
            for insumo in insumos:
                print(insumo)

        elif operacion == 3:
            id_insumo = int(input("ID del insumo a actualizar: "))
            tipo_insumo = input("Nuevo tipo de insumo: ")
            cantidad_disponible = float(input("Nueva cantidad disponible: "))
            fecha_caducidad = input("Nueva fecha de caducidad (AAAA-MM-DD): ")
            actualizar_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad)

        elif operacion == 4:
            id_insumo = int(input("ID del insumo a eliminar: "))
            eliminar_insumo(id_insumo)

    elif tabla == 3:
        # Menú de operaciones para Cliente
        print("\nOpciones para la tabla Cliente:")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        operacion = int(input("Elige una operación: "))

        if operacion == 1:
            nombre = input("Nombre del cliente: ")
            correo = input("Correo del cliente: ")
            telefono = input("Teléfono del cliente: ")
            insertar_cliente(nombre, correo, telefono)

        elif operacion == 2:
            clientes = leer_clientes()
            for cliente in clientes:
                print(cliente)

        elif operacion == 3:
            id_cliente = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre: ")
            correo = input("Nuevo correo: ")
            telefono = input("Nuevo teléfono: ")
            actualizar_cliente(id_cliente, nombre, correo, telefono)

        elif operacion == 4:
            id_cliente = int(input("ID del cliente a eliminar: "))
            eliminar_cliente(id_cliente)

    elif tabla == 4:
        # Menú de operaciones para Venta
        print("\nOpciones para la tabla Venta:")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        operacion = int(input("Elige una operación: "))

        if operacion == 1:
            cliente_id = int(input("ID del cliente: "))
            fecha_venta = input("Fecha de la venta (AAAA-MM-DD HH:MM:SS): ")
            total = float(input("Total de la venta: "))
            insertar_venta(cliente_id, fecha_venta, total)

        elif operacion == 2:
            ventas = leer_ventas()
            for venta in ventas:
                print(venta)

        elif operacion == 3:
            id_venta = int(input("ID de la venta a actualizar: "))
            cliente_id = int(input("Nuevo ID del cliente: "))
            fecha_venta = input("Nueva fecha de la venta (AAAA-MM-DD HH:MM:SS): ")
            total = float(input("Nuevo total de la venta: "))
            actualizar_venta(id_venta, cliente_id, fecha_venta, total)

        elif operacion == 4:
            id_venta = int(input("ID de la venta a eliminar: "))
            eliminar_venta(id_venta)

    elif tabla == 5:
        # Menú de operaciones para Detalle_Venta
        print("\nOpciones para la tabla Detalle_Venta:")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        operacion = int(input("Elige una operación: "))

        if operacion == 1:
            venta_id = int(input("ID de la venta: "))
            cultivo_id = int(input("ID del cultivo: "))
            cantidad = float(input("Cantidad: "))
            subtotal = float(input("Subtotal: "))
            insertar_detalle_venta(venta_id, cultivo_id, cantidad, subtotal)

        elif operacion == 2:
            detalles_venta = leer_detalles_venta()
            for detalle in detalles_venta:
                print(detalle)

        elif operacion == 3:
            id_detalle = int(input("ID del detalle a actualizar: "))
            venta_id = int(input("Nuevo ID de la venta: "))
            cultivo_id = int(input("Nuevo ID del cultivo: "))
            cantidad = float(input("Nueva cantidad: "))
            subtotal = float(input("Nuevo subtotal: "))
            actualizar_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal)

        elif operacion == 4:
            id_detalle = int(input("ID del detalle a eliminar: "))
            eliminar_detalle_venta(id_detalle)

    elif tabla == 6:
        print("Saliendo.")
        break

    else:
        print("Opción incorrecta intetalo de nuevo.")