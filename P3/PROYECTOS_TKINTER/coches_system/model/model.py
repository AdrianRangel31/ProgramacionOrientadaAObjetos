from ConexionBD import *

class AutosBD:
    @staticmethod
    def insertar(color,marca,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                           (color,marca,modelo,velocidad,caballaje,plazas))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from coches")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def actualizar(color,marca,modelo,velocidad,potencia,plazas,id):
        try:
            cursor.execute(f"update coches set Color = '{color}',Marca = '{marca}',Modelo = '{modelo}',Velocidad = '{velocidad}',Caballaje = '{potencia}',Plazas = '{plazas}' where ID_Coches = {id}")
            conexion.commit()
            return True
        except:
            return False
            
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id_coches = %s",(id,))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(id):
        try:
            cursor.execute(f"Select * from coches where id_coches = {id}")
            return cursor.fetchall()
        except:
            return False

class CamionetasBD:
    @staticmethod
    def insertar(color,marca,modelo,velocidad,potencia,plazas,traccion,cerrada):
        try:
            cursor.execute("insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (color,marca,modelo,velocidad,potencia,plazas,traccion,cerrada))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camionetas")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(color,marca,modelo,velocidad,potencia,plazas,traccion,cerrada,id):
        try:
            cursor.execute(f"update camionetas set Color = '{color}',Marca = '{marca}',Modelo = '{modelo}',Velocidad = '{velocidad}',Caballaje = '{potencia}',Plazas = '{plazas}',Traccion = '{traccion}',Cerrada = '{cerrada}' where ID_Camionetas = {id}")
            conexion.commit()
            return True
        except:
            return False
            
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camionetas where ID_Camionetas = %s",(id,))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(id):
        try:
            cursor.execute(f"Select * from camionetas where id_camionetas = {id}")
            return cursor.fetchall()
        except:
            return False
        
class CamionesBD:
    @staticmethod
    def insertar(color,marca,modelo,velocidad,potencia,plazas,eje,capacidad):
        try:
            cursor.execute("insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (color,marca,modelo,velocidad,potencia,plazas,eje,capacidad))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camiones")
            return cursor.fetchall()
        except:
            return []
            
    @staticmethod
    def actualizar(color,marca,modelo,velocidad,potencia,plazas,eje,capacidad,id):
        try:
            cursor.execute(f"update camiones set Color = '{color}',Marca = '{marca}',Modelo = '{modelo}',Velocidad = '{velocidad}',Caballaje = '{potencia}',Plazas = '{plazas}',Eje = '{eje}',Capacidad = '{capacidad}' where ID_Camiones = {id}")
            conexion.commit()   
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camiones where id_camiones = %s",(id,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def buscar(id):
        try:
            cursor.execute(f"Select * from camiones where id_camiones = {id}")
            return cursor.fetchall()
        except:
            return False
