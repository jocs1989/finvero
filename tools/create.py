from db.psql import PostgresConnection
from config.settings import *
from psycopg2 import extras



def insert_db(datos: tuple):

    if datos:
        connection = PostgresConnection(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT_PC,  # Puerto predeterminado de PostgreSQL
        )

    connection.connect()

    # Crear una tabla en la base de datos
    try:
        cursor = connection.connection.cursor()
        print(datos)
        # Ejecutar la consulta de inserción con los valores proporcionados
        consulta = "INSERT INTO productos (url_producto, imagen_src, texto, precio, cantidad) VALUES %s"
        extras.execute_values(cursor, consulta, datos)
        # Confirmar la transacción
        connection.commit()
        print("Datos insertados correctamente")
        
        cursor.close()
    except Exception as e:
        print("Error insertar valores:", e)

    finally:
        connection.disconnect()
    # Aquí puedes realizar otras operaciones utilizando la semilla
