from tkinter import *
from tkinter import ttk, messagebox


class Vista:
    def __init__(self,ventana:Tk):
        ventana.title("Sistema de Gestión de autos")
        ventana.geometry("1024x768")
        ventana.resizable(0,0)
        self.menu_principal(ventana)

    @staticmethod
    def menu_principal(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=".::Menú principal::.").pack()
        Button(ventana,text="Autos",width=15,command=lambda:Vista.menu_acciones(ventana,"Autos")).pack(pady=15)
        Button(ventana,text="Camionetas",width=15,command=lambda:Vista.menu_acciones(ventana,"Camionetas")).pack(pady=15)
        Button(ventana,text="Camiones",width=15,command=lambda:Vista.menu_acciones(ventana,"Camiones")).pack(pady=15)
        Button(ventana,text="Salir",width=15,command=lambda:ventana.destroy()).pack(pady=15)

    @staticmethod
    def limpiar_ventana(ventana):
        for widget in ventana.winfo_children():
            widget.pack_forget()

    @staticmethod
    def menu_acciones(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Menú principal {tipo}::.").pack()
        Button(ventana,text="1.-Insertar",width=15,command=lambda:Vista.insertar(ventana,tipo)).pack(pady=15)
        Button(ventana,text="2.-Consultar",width=15,command=lambda:Vista.consultar(ventana,tipo)).pack(pady=15)
        Button(ventana,text="3.-Actualizar",width=15,command=lambda:Vista.actualizar(ventana,tipo)).pack(pady=15)
        Button(ventana,text="4.-Eliminar",width=15,command=lambda:Vista.eliminar(ventana,tipo)).pack(pady=15)
        Button(ventana,text="5.-Regresar",width=15,command=lambda:Vista.menu_principal(ventana)).pack(pady=15)


    @staticmethod
    def insertar(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Insertar {tipo}::.").pack()

        Label(ventana,text="Marca").pack(pady=15)
        marca = StringVar()
        txt_marca= Entry(ventana,textvariable=marca)
        txt_marca.pack()
        txt_marca.focus()

        Label(ventana,text="Color").pack(pady=15)
        Color = StringVar()
        txt_Color= Entry(ventana,textvariable=Color)
        txt_Color.pack()
        
        Label(ventana,text="Modelo").pack(pady=15)
        Modelo = StringVar()
        txt_Modelo= Entry(ventana,textvariable=Modelo)
        txt_Modelo.pack()

        Label(ventana,text="Velocidad").pack(pady=15)
        Velocidad = StringVar()
        txt_Velocidad= Entry(ventana,textvariable=Velocidad)
        txt_Velocidad.pack()

        Label(ventana,text="Caballaje").pack(pady=15)
        Caballaje = StringVar()
        txt_Caballaje= Entry(ventana,textvariable=Caballaje)
        txt_Caballaje.pack()

        Label(ventana,text="Plazas").pack(pady=15)
        Plazas = StringVar()
        txt_Plazas= Entry(ventana,textvariable=Plazas)
        txt_Plazas.pack()



        Button(ventana,text="Guardar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def consultar(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Consultar {tipo}::.").pack()

        frame_tabla = Frame(ventana)
        frame_tabla.pack(fill="both")

        tabla = ttk.Treeview(frame_tabla, columns=("ID", "Color", "Marca", "Modelo","Velocidad","Caballaje","Plazas"), show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Título", text="Título")
        tabla.heading("Director", text="Director")
        tabla.heading("Año", text="Año")
        tabla.pack(fill="both", expand=True)

        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def actualizar(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Actualizar {tipo}::.").pack()

        Label(ventana,text="Marca").pack(pady=15)
        marca = StringVar()
        txt_marca= Entry(ventana,textvariable=marca)
        txt_marca.pack()
        txt_marca.focus()

        Label(ventana,text="Color").pack(pady=15)
        Color = StringVar()
        txt_Color= Entry(ventana,textvariable=Color)
        txt_Color.pack()
        
        Label(ventana,text="Modelo").pack(pady=15)
        Modelo = StringVar()
        txt_Modelo= Entry(ventana,textvariable=Modelo)
        txt_Modelo.pack()

        Label(ventana,text="Velocidad").pack(pady=15)
        Velocidad = StringVar()
        txt_Velocidad= Entry(ventana,textvariable=Velocidad)
        txt_Velocidad.pack()

        Label(ventana,text="Caballaje").pack(pady=15)
        Caballaje = StringVar()
        txt_Caballaje= Entry(ventana,textvariable=Caballaje)
        txt_Caballaje.pack()

        Label(ventana,text="Plazas").pack(pady=15)
        Plazas = StringVar()
        txt_Plazas= Entry(ventana,textvariable=Plazas)
        txt_Plazas.pack()



        Button(ventana,text="Actualizar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def eliminar(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Eliminar {tipo}::.").pack()
        Label(ventana,text="ID del registro a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Eliminar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
