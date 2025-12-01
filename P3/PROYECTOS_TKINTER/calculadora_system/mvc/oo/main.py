"""
Crear una calculadora:
    1.- Dos campos de texto
    2.- 4 botones para las operaciones
    3.- Mostrar el resultado en una alerta
    4.-Programado de forma OO
    5.-Considerar el MVC
"""

from view import interface
from tkinter import *

class App:
    def __init__(self,ventana):
        view = interface.Vista(ventana)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()

