from ConexionBD import *

class AutosBD:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    def insertar(self):
        try:
            cursor.execute("insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                           (self._color,self._marca,self._modelo,self._velocidad,self._caballaje,self._plazas))
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

class CamionetasBD:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas
        self._traccion = traccion
        self._cerrada = cerrada

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
        
class CamionesBD:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas
        self._eje = eje
        self._capacidad = capacidad

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

