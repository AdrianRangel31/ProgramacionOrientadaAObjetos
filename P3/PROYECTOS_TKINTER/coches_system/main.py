"""
2 DICIEMBRE
    1) INTERFACES
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()

        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()

    ENTREGABLES
        Interaccion con todas las interfaces
        Nombre del Commit: "commit_02_12_25"
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
