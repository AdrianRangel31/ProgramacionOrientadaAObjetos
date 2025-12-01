from conexionBD import *


class Nota:
    @staticmethod
    def crear(usuario_id,titulo,descripcion):
        try:
            sql = "insert into notas (usuario_id,titulo,descripcion,fecha) values(%s,%s,%s,NOW())"
            val = (usuario_id,titulo,descripcion)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
    @staticmethod    
    def mostrar(usuario_id):
        try:
            sql = "select * from notas where usuario_id = %s"
            val = (usuario_id,)
            cursor.execute(sql,val)
            return cursor.fetchall()
        except:
            return False
    @staticmethod    
    def cambiar(id,titulo,descripcion):
        try:
            cursor.execute("update notas set titulo = %s, descripcion = %s where id = %s",(titulo,descripcion,id))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod    
    def borrar(id):
        try:
            cursor.execute("delete from notas where id = %s",(id,))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(id,usuario_id):
        cursor.execute(f"select * from notas where id = {id} and usuario_id = {usuario_id}")
        registro = cursor.fetchall()
        if registro == []:
            return False
        else:
            return True