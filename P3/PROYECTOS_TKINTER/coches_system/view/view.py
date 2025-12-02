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
        match tipo:
            case "Autos":
                Vista.insertar_autos(ventana,tipo)
            case "Camionetas":
                Vista.insertar_camionetas(ventana,tipo)
            case "Camiones":
                Vista.insertar_camiones(ventana,tipo)

    @staticmethod
    def actualizar(ventana,tipo):
        match tipo:
            case "Autos":
                Vista.actualizar_autos(ventana,tipo)
            case "Camionetas":
                Vista.actualizar_camionetas(ventana,tipo)
            case "Camiones":
                Vista.actualizar_camiones(ventana,tipo)


    @staticmethod
    def consultar(ventana,tipo):
        match tipo:
            case "Autos":
                Vista.consultar_autos(ventana,tipo)
            case "Camionetas":
                Vista.consultar_camionetas(ventana,tipo)
            case "Camiones":
                Vista.consultar_camiones(ventana,tipo)

    @staticmethod
    def eliminar(ventana,tipo):
        match tipo:
            case "Autos":
                Vista.eliminar_autos(ventana,tipo)
            case "Camionetas":
                Vista.eliminar_camionetas(ventana,tipo)
            case "Camiones":
                Vista.eliminar_camiones(ventana,tipo)

        
        
    @staticmethod
    def insertar_autos(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Insertar Autos::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)
        Button(ventana,text="Guardar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def insertar_camionetas(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Insertar Camionetas::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)

        Label(frame_entry,text="Tracción").grid(row=2,column=1)
        Traccion = StringVar()
        txt_Traccion= Entry(frame_entry,textvariable=Traccion)
        txt_Traccion.grid(row=2,column=2)

        Label(frame_entry,text="Cerrada").grid(row=2,column=3)
        Cerrada = StringVar()
        txt_Cerrada= Entry(frame_entry,textvariable=Cerrada)
        txt_Cerrada.grid(row=2,column=4)
        Button(ventana,text="Guardar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def insertar_camiones(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Insertar Camionetas::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)

        Label(frame_entry,text="Eje").grid(row=2,column=1)
        Eje = StringVar()
        txt_Eje= Entry(frame_entry,textvariable=Eje)
        txt_Eje.grid(row=2,column=2)

        Label(frame_entry,text="Capacidad").grid(row=2,column=3)
        Capacidad = StringVar()
        txt_Capacidad= Entry(frame_entry,textvariable=Capacidad)
        txt_Capacidad.grid(row=2,column=4)
        Button(ventana,text="Guardar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def actualizar_autos(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Actualizar Autos::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)
        Button(ventana,text="Actualizar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def actualizar_camionetas(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Actualizar Camionetas::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)

        Label(frame_entry,text="Tracción").grid(row=2,column=1)
        Traccion = StringVar()
        txt_Traccion= Entry(frame_entry,textvariable=Traccion)
        txt_Traccion.grid(row=2,column=2)

        Label(frame_entry,text="Cerrada").grid(row=2,column=3)
        Cerrada = StringVar()
        txt_Cerrada= Entry(frame_entry,textvariable=Cerrada)
        txt_Cerrada.grid(row=2,column=4)
        Button(ventana,text="Actualizar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def actualizar_camiones(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Actualizar Camionetas::.").pack()

        frame_entry = Frame(ventana)
        frame_entry.pack()

        Label(frame_entry,text="Marca").grid(row=0,column=1)
        marca = StringVar()
        txt_marca= Entry(frame_entry,textvariable=marca)
        txt_marca.grid(row=0,column=2)
        txt_marca.focus()

        Label(frame_entry,text="Color").grid(row=0,column=3)
        Color = StringVar()
        txt_Color= Entry(frame_entry,textvariable=Color)
        txt_Color.grid(row=0,column=4)
        
        Label(frame_entry,text="Modelo").grid(row=0,column=5)
        Modelo = StringVar()
        txt_Modelo= Entry(frame_entry,textvariable=Modelo)
        txt_Modelo.grid(row=0,column=6)

        Label(frame_entry,text="Velocidad").grid(row=1,column=1)
        Velocidad = StringVar()
        txt_Velocidad= Entry(frame_entry,textvariable=Velocidad)
        txt_Velocidad.grid(row=1,column=2)

        Label(frame_entry,text="Caballaje").grid(row=1,column=3)
        Caballaje = StringVar()
        txt_Caballaje= Entry(frame_entry,textvariable=Caballaje)
        txt_Caballaje.grid(row=1,column=4)

        Label(frame_entry,text="Plazas").grid(row=1,column=5)
        Plazas = StringVar()
        txt_Plazas= Entry(frame_entry,textvariable=Plazas)
        txt_Plazas.grid(row=1,column=6)

        Label(frame_entry,text="Eje").grid(row=2,column=1)
        Eje = StringVar()
        txt_Eje= Entry(frame_entry,textvariable=Eje)
        txt_Eje.grid(row=2,column=2)

        Label(frame_entry,text="Capacidad").grid(row=2,column=3)
        Capacidad = StringVar()
        txt_Capacidad= Entry(frame_entry,textvariable=Capacidad)
        txt_Capacidad.grid(row=2,column=4)
        Button(ventana,text="Actualizar",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)



    @staticmethod
    def consultar_autos(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Consultar {tipo}::.").pack()

        frame_tabla = Frame(ventana)
        frame_tabla.pack(fill="both")
        columns = ("ID", "Color", "Marca", "Modelo", "Velocidad", "Caballaje", "Plazas")
        widths = [50, 100, 120, 100, 80, 100, 70]  # anchos por columna
        tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        for col, w in zip(columns, widths):
            tabla.heading(col, text=col)
            tabla.column(col, width=w, anchor="center")
        tabla.pack(fill="both", expand=True)
        
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def consultar_camionetas(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Consultar {tipo}::.").pack()

        frame_tabla = Frame(ventana)
        frame_tabla.pack(fill="both")
        columns = ("ID", "Color", "Marca", "Modelo", "Velocidad", "Caballaje", "Plazas","Tracción","Cerrada")
        widths = [50, 100, 120, 100, 80, 100, 70,70,70]  # anchos por columna
        tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        for col, w in zip(columns, widths):
            tabla.heading(col, text=col)
            tabla.column(col, width=w, anchor="center")
        tabla.pack(fill="both", expand=True)
        
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def consultar_camiones(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Consultar {tipo}::.").pack()

        frame_tabla = Frame(ventana)
        frame_tabla.pack(fill="both")
        columns = ("ID", "Color", "Marca", "Modelo", "Velocidad", "Caballaje", "Plazas","Eje","Capacidad")
        widths = [50, 100, 120, 100, 80, 100, 70,70,70]  # anchos por columna
        tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        for col, w in zip(columns, widths):
            tabla.heading(col, text=col)
            tabla.column(col, width=w, anchor="center")
        tabla.pack(fill="both", expand=True)
        
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)


    @staticmethod
    def eliminar_autos(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Eliminar {tipo}::.").pack()
        Label(ventana,text="ID del registro a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def eliminar_camionetas(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Eliminar {tipo}::.").pack()
        Label(ventana,text="ID del registro a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)

    @staticmethod
    def eliminar_camiones(ventana,tipo):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Eliminar {tipo}::.").pack()
        Label(ventana,text="ID del registro a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_acciones(ventana,tipo)).pack(pady=15)
