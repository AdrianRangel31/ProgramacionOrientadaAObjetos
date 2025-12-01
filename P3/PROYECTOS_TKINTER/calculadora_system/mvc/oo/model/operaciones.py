from conexionBD import *

class Operaciones:
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            sql = "insert into operaciones values(null,NOW(),%s,%s,%s,%s)"
            val = (numero1,numero2,signo,resultado)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
    @staticmethod    
    def consultar():
        try:
            sql = "select * from operaciones"
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return False
    @staticmethod    
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute("update operaciones set fecha = NOW(), numero1 = %s, numero2 = %s, signo = %s, resultado = %s where id = %s",(numero1,numero2,signo,resultado,id))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod    
    def eliminar(id):
        try:
            cursor.execute("delete from operaciones where id = %s",(id,))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def buscar(id):
        cursor.execute(f"select * from operaciones where id = {id}")
        registro = cursor.fetchall()
        if registro == []:
            return False
        else:
            return registro
        
