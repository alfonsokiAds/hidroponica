import pymysql
import pyodbc


mysql_config = {# Configuración de la conexión a MySQL
    'host': 'localhost',
    'user': 'root',
    'password': 'happyme',
    'database': 'GranjaHidroponica',
}


sqlserver_config = {# Configuración de la conexión a SQL Server
    'server': 'LAPTOP-GHJ9NM02\\SQLEXPRESS',
    'database': 'GranjaHidroponica',
    'username': 'sa',
    'password': '12345678',
    'driver': 'ODBC Driver 17 for SQL Server'
}

# Conectar a MySQL
def connect_mysql():
    return pymysql.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database'],
    )

# Conectar a SQL Server
def connect_sqlserver():
    conn_str = f"DRIVER={sqlserver_config['driver']};SERVER={sqlserver_config['server']};DATABASE={sqlserver_config['database']};UID={sqlserver_config['username']};PWD={sqlserver_config['password']}"
    return pyodbc.connect(conn_str)

# Migrar datos de una tabla específica con IDENTITY_INSERT
def migrate_table(mysql_table, sqlserver_table, columns, use_identity_insert=False):
    # Conexión a MySQL
    mysql_conn = connect_mysql()
    mysql_cursor = mysql_conn.cursor()

    # Conexión a SQL Server
    sqlserver_conn = connect_sqlserver()
    sqlserver_cursor = sqlserver_conn.cursor()

    # Seleccionar datos desde MySQL
    query = f"SELECT {', '.join(columns)} FROM {mysql_table}"
    mysql_cursor.execute(query)
    rows = mysql_cursor.fetchall()

    # Activar IDENTITY_INSERT si es necesario
    if use_identity_insert:
        sqlserver_cursor.execute(f"SET IDENTITY_INSERT {sqlserver_table} ON")
        sqlserver_conn.commit()

    # Insertar datos en SQL Server
    for row in rows:
        placeholders = ', '.join(['?'] * len(columns))
        sql_insert = f"INSERT INTO {sqlserver_table} ({', '.join(columns)}) VALUES ({placeholders})"
        sqlserver_cursor.execute(sql_insert, row)

    # Desactivar IDENTITY_INSERT si fue activado
    if use_identity_insert:
        sqlserver_cursor.execute(f"SET IDENTITY_INSERT {sqlserver_table} OFF")
        sqlserver_conn.commit()

    # Confirmar y cerrar conexiones
    sqlserver_conn.commit()
    mysql_cursor.close()
    mysql_conn.close()
    sqlserver_cursor.close()
    sqlserver_conn.close()

# Migrar todas las tablas
def migrate_data():
    # Migración de la tabla Cultivo (con IDENTITY_INSERT activado)
    print("Migrando tabla Cultivo")
    migrate_table(
        mysql_table='Cultivo',
        sqlserver_table='Cultivo',
        columns=['id_cultivo', 'tipo_planta', 'fecha_siembra', 'estado_crecimiento', 'rendimiento_esperado'],
        use_identity_insert=True
    )

    # Migración de la tabla Insumo
    print("Migrando tabla Insumo")
    migrate_table(
        mysql_table='Insumo',
        sqlserver_table='Insumo',
        columns=['id_insumo', 'tipo_insumo', 'cantidad_disponible', 'fecha_caducidad'],
        use_identity_insert=True
    )

    # Migración de la tabla Cliente
    print("Migrando tabla Cliente")
    migrate_table(
        mysql_table='Cliente',
        sqlserver_table='Cliente',
        columns=['id_cliente', 'nombre', 'correo', 'telefono'],
        use_identity_insert=True
    )

    # Migración de la tabla Venta
    print("Migrando tabla Venta")
    migrate_table(
        mysql_table='Venta',
        sqlserver_table='Venta',
        columns=['id_venta', 'cliente_id', 'fecha_venta', 'total'],
        use_identity_insert=True
    )

    # Migración de la tabla Detalle_Venta
    print("Migrando tabla Detalle_Venta")
    migrate_table(
        mysql_table='Detalle_Venta',
        sqlserver_table='Detalle_Venta',
        columns=['id_detalle', 'venta_id', 'cultivo_id', 'cantidad', 'subtotal'],
        use_identity_insert=True
    )

    print("Migración completada.")

if __name__ == "__main__":
    migrate_data()