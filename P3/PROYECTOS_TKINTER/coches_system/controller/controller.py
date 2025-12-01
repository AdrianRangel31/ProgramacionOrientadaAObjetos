import tkinter as tk
from tkinter import messagebox
from view.view import MenuView, CochesView, CamionetasView, CamionesView
from model.model import CochesModel, CamionetasModel, CamionesModel

class MainController:
    def __init__(self, root):
        self.root = root
        # Contenedor principal
        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # Diccionarios para navegación
        self.views = {}
        self.controllers = {}
        
        self.setup()
        self.show_view("menu")

    def setup(self):
        # 1. Crear Vistas y asignar Controladores específicos
        
        # Menu
        self.views["menu"] = MenuView(self.container, self)

        # Coches
        c_coches = CrudController(CochesModel, self)
        self.controllers["coches"] = c_coches
        self.views["coches"] = CochesView(self.container, c_coches)
        c_coches.view = self.views["coches"] # Enlace bidireccional

        # Camionetas
        c_camionetas = CrudController(CamionetasModel, self)
        self.controllers["camionetas"] = c_camionetas
        self.views["camionetas"] = CamionetasView(self.container, c_camionetas)
        c_camionetas.view = self.views["camionetas"]

        # Camiones
        c_camiones = CrudController(CamionesModel, self)
        self.controllers["camiones"] = c_camiones
        self.views["camiones"] = CamionesView(self.container, c_camiones)
        c_camiones.view = self.views["camiones"]

        # 2. Posicionar todas las vistas en el mismo lugar (grid stack)
        for v in self.views.values():
            v.grid(row=0, column=0, sticky="nsew")
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def show_view(self, name):
        f = self.views.get(name)
        if f:
            f.tkraise()
            # Si tiene controlador de datos, refrescar tabla
            if name in self.controllers:
                self.controllers[name].refresh_data()

    def go_back(self):
        self.show_view("menu")

    def salir(self):
        self.root.quit()

class CrudController:
    def __init__(self, model_class, main_controller):
        self.model = model_class
        self.main = main_controller
        self.view = None # Se asigna después

    def go_back(self):
        self.main.go_back()

    def refresh_data(self):
        data = self.model.read_all()
        if self.view:
            self.view.update_treeView(data)

    def agregar(self, data):
        if data and self.model.create(data):
            messagebox.showinfo("Éxito", "Registro agregado correctamente")
            self.refresh_data()
        else:
            messagebox.showerror("Error", "No se pudo agregar el registro")

    def modificar(self, item_id, data):
        if not item_id:
            messagebox.showwarning("Atención", "Selecciona un registro")
            return
        if data and self.model.update(item_id, data):
            messagebox.showinfo("Éxito", "Registro modificado correctamente")
            self.refresh_data()
        else:
            messagebox.showerror("Error", "No se pudo modificar")

    def eliminar(self, item_id):
        if not item_id:
            messagebox.showwarning("Atención", "Selecciona un registro")
            return
        if messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar?"):
            if self.model.delete(item_id):
                messagebox.showinfo("Éxito", "Registro eliminado")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")