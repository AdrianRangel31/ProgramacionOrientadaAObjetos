import tkinter as tk
from controller.controller import MainController
from view.view import aplicar_estilos

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gestión de Vehículos ")
    root.geometry("950x700")
    root.configure(bg="#f0f0f0")
    
    aplicar_estilos()
    
    app = MainController(root)
    root.mainloop()