from config.settings import *
from db.psql import PostgresConnection


def seed():
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
        cursor.execute(
            """
            CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
            CREATE TABLE IF NOT EXISTS productos (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                url_producto TEXT,
                imagen_src TEXT,
                texto TEXT,
                precio TEXT,
                cantidad TEXT
            )
        """
        )
        print("Tabla creada correctamente")
        connection.connection.commit()
        cursor.close()
    except Exception as e:
        print("Error al crear la tabla:", e)

    finally:
        connection.disconnect()
