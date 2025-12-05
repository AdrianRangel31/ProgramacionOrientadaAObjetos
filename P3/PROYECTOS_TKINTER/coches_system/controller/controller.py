from tkinter import ttk, messagebox
from model.model import *
class Controlador:
    @staticmethod
    def menu_principal():
        pass

    @staticmethod
    def menu_acciones():
        pass

    @staticmethod
    def insertar_autos(color,marca,modelo,velocidad,caballaje,plazas):
        insertar = AutosBD.insertar(color,marca,modelo,velocidad,caballaje,plazas)
        Controlador.mensaje_sql(insertar,"Se insertó correctamente el registro","No fue posible insertar el registro")

    @staticmethod
    def consultar_autos():
        registros = AutosBD.consultar()
        if len(registros) > 0:
            return registros
        else:
            Controlador.mensaje_sql(True,"No se encontró ningún registro","")

    @staticmethod
    def cambiar_autos(color,marca,modelo,velocidad,caballaje,plazas,id):
        cambiar = AutosBD.actualizar(color,marca,modelo,velocidad,caballaje,plazas,id)
        Controlador.mensaje_sql(cambiar,"Se actualizó correctamente el registro","No fue posible actualizar el registro")

    @staticmethod
    def borrar_autos(id):
        borrar = AutosBD.eliminar(id)
        Controlador.mensaje_sql(borrar,"Se eliminó correctamente el registro","No fue posible eliminar el registro")

    @staticmethod
    def buscar_auto(id):
        buscar = AutosBD.buscar(id)
        if buscar:
            return buscar
        else:
            return False
 
    @staticmethod
    def insertar_camionetas(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        insertar = CamionetasBD.insertar(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controlador.mensaje_sql(insertar,"Se insertó correctamente el registro","No fue posible insertar el registro")

    @staticmethod
    def consultar_camionetas():
        registros = CamionetasBD.consultar()
        if len(registros) > 0:
            return registros
        else:
            Controlador.mensaje_sql(True,"No se encontró ningún registro","")

    @staticmethod
    def cambiar_camionetas(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        cambiar = CamionetasBD.actualizar(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Controlador.mensaje_sql(cambiar,"Se actualizó correctamente el registro","No fue posible actualizar el registro")

    @staticmethod
    def borrar_camionetas(id):
        borrar = CamionetasBD.eliminar(id)
        Controlador.mensaje_sql(borrar,"Se eliminó correctamente el registro","No fue posible eliminar el registro")

    @staticmethod
    def buscar_camionetas(id):
        buscar = CamionetasBD.buscar(id)
        if buscar:
            return buscar
        else:
            return False

    @staticmethod
    def insertar_camiones(color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad):
        insertar = CamionesBD.insertar(color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad)
        Controlador.mensaje_sql(insertar,"Se insertó correctamente el registro","No fue posible insertar el registro")

    @staticmethod
    def consultar_camiones():
        registros = CamionesBD.consultar()
        if len(registros) > 0:
            return registros
        else:
            Controlador.mensaje_sql(True,"No se encontró ningún registro","")

    @staticmethod
    def cambiar_camiones(color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad,id):
        cambiar = CamionesBD.actualizar(color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad,id)
        Controlador.mensaje_sql(cambiar,"Se actualizó correctamente el registro","No fue posible actualizar el registro")

    @staticmethod
    def borrar_camiones(id):
        borrar = CamionesBD.eliminar(id)
        Controlador.mensaje_sql(borrar,"Se eliminó correctamente el registro","No fue posible eliminar el registro")

    @staticmethod
    def buscar_camiones(id):
        buscar = CamionesBD.buscar(id)
        if buscar:
            return buscar
        else:
            return False
  
    @staticmethod
    def mensaje_sql(condicion,exito,error):
        if condicion:
            messagebox.showinfo("Exito",exito)
        else:
            messagebox.showerror("Error",error)

            