"""
4 DICIEMBRE
    1) Controlador

        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()

Productos Entregables:
    **Interacción con la funcionalidad (controlador) de las
    interfaces anteriores.
    **Nombre del commit: "commit_04_12_25"
"""
"""
5 DICIEMBRE
    1) Controlador

        1.1 insertar_camiones()
        1.2 consultar_camiones()
        1.3 cambiar_camiones()
        1.4 borrar_camiones()

Productos Entregables:
    **Interacción con la funcionalidad (controlador) de las
    interfaces anteriores.
    **Nombre del commit: "commit_05_12_25"
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
