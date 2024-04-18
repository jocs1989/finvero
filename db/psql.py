from config.settings import *
import psycopg2

class SingletonMeta(type):
    """
    La clase Singleton puede ser implementada de diferentes maneras en Python.
    Algunos métodos posibles incluyen: clase base, decorador, metaclase.
    Usaremos la metaclase porque es la más adecuada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Los posibles cambios en el valor del argumento `__init__` no afectan
        a la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class PostgresConnection(metaclass=SingletonMeta):
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            if not self.connection or self.connection.closed != 0:
                self.connection = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port
                )
                print("Conexión exitosa a la base de datos PostgreSQL")
            else:
                print("Ya existe una conexión abierta a la base de datos")
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
        else:
            print("No hay conexión abierta")


    
