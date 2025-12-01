import mysql.connector
from mysql.connector import Error

class ConexionBD:
    _connection = None

    @classmethod
    def get_conexion(cls):
        if cls._connection is None or not cls._connection.is_connected():
            try:
                # Ajusta tus credenciales si es necesario
                cls._connection = mysql.connector.connect(
                    host='localhost',
                    database='bd_coches',
                    user='root',
                    password='' 
                )
            except Error as e:
                print(f"Error al conectar a la BD: {e}")
                cls._connection = None
        return cls._connection

    @classmethod
    def cerrar_conexion(cls):
        if cls._connection and cls._connection.is_connected():
            cls._connection.close()