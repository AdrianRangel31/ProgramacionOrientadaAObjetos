"""     
1er diciembre
    1)Implementación de MVC
    2)
    3)
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()

    Productos Entregables:
        *Estructura del proyecto basado en MVC
        *Interacción con las interfaces
        *Commit: "commit_01_12_25"
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
