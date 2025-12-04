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
    def mensaje_sql(condicion,exito,error):
        if condicion:
            messagebox.showinfo("Exito",exito)
        else:
            messagebox.showerror("Error",error)

    @staticmethod
    def buscar_auto(id):
        buscar = AutosBD.buscar(id)
        if buscar:
            return buscar
        else:
            return False
 