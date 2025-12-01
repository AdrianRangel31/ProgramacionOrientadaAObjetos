from conexion import ConexionBD

class CochesModel:
    @staticmethod
    def read_all():
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM coches")
            res = cursor.fetchall()
            cursor.close()
            return res
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def create(datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO coches (Color, Marca, Modelo, Velocidad, Caballaje, Plazas) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, datos)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def update(id_item, datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "UPDATE coches SET Color=%s, Marca=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s WHERE ID_Coches=%s"
            datos_con_id = list(datos) + [id_item]
            cursor.execute(query, datos_con_id)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def delete(id_item):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM coches WHERE ID_Coches = %s", (id_item,))
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

class CamionetasModel:
    @staticmethod
    def read_all():
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM camionetas")
            res = cursor.fetchall()
            cursor.close()
            return res
        except Exception:
            return []

    @staticmethod
    def create(datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO camionetas (Marca, Color, Modelo, Velocidad, Caballaje, Plazas, Traccion, Cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, datos)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def update(id_item, datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "UPDATE camionetas SET Marca=%s, Color=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s, Traccion=%s, Cerrada=%s WHERE ID_Camionetas=%s"
            datos_con_id = list(datos) + [id_item]
            cursor.execute(query, datos_con_id)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def delete(id_item):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM camionetas WHERE ID_Camionetas = %s", (id_item,))
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

class CamionesModel:
    @staticmethod
    def read_all():
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM camiones")
            res = cursor.fetchall()
            cursor.close()
            return res
        except Exception:
            return []

    @staticmethod
    def create(datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO camiones (Color, Marca, Modelo, Velocidad, Caballaje, Plazas, Eje, Capacidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, datos)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def update(id_item, datos):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            query = "UPDATE camiones SET Color=%s, Marca=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s, Eje=%s, Capacidad=%s WHERE ID_Camiones=%s"
            datos_con_id = list(datos) + [id_item]
            cursor.execute(query, datos_con_id)
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False

    @staticmethod
    def delete(id_item):
        try:
            conn = ConexionBD.get_conexion()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM camiones WHERE ID_Camiones = %s", (id_item,))
            conn.commit()
            cursor.close()
            return True
        except Exception:
            return False