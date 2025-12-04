"""
3 DICIEMBRE
    1) Controlador
        1.1 menu_principal()
        1.2 menu_acciones()
        1.3 insertar_autos()
        1.4 consultar_autos()
        1.5 cambiar_autos()
        1.6 borrar_autos()

Productos Entregables:
    **Interacción con la funcionalidad (controlador) de las
    interfaces anteriores.
    **Nombre del commit: "commit_03_12_25"
"""
from tkinter import *
from view import view

class App:
    def __init__(self,ventana):
        vista = view.Vista(ventana)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()   
