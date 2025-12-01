from tkinter import *
from controller import controlador1

class Vista:
    def __init__(self,ventana:Tk):
        ventana.title("Gestión de notas")
        ventana.geometry("800x600")
        ventana.resizable(0,0)
        self.menu_principal(ventana)


    @staticmethod
    def menu_principal(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=".::Menú principal::.").pack()
        Button(ventana,text="1.-Registro",width=15,command=lambda:Vista.registro(ventana)).pack(pady=15)
        Button(ventana,text="2.-Login",width=15,command=lambda:Vista.login(ventana)).pack(pady=15)
        Button(ventana,text="3.-Salir",width=15,command=lambda:ventana.destroy()).pack(pady=15)

    @staticmethod
    def registro(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=".::Registro::.").pack(pady=5)
        Label(ventana,text="¿Cuál es tu nombre?").pack(pady=15)
        txt_nombre= Entry(ventana)
        txt_nombre.pack()
        txt_nombre.focus()
        Label(ventana,text="¿Cuales son tus apellidos?").pack(pady=15)
        txt_apellido = Entry(ventana)
        txt_apellido.pack()
        Label(ventana,text="Ingresa tu email").pack(pady=15)
        txt_email = Entry(ventana)
        txt_email.pack()
        Label(ventana,text="Ingresa tu contraseña").pack(pady=15)
        txt_contra = Entry(ventana,show="*")
        txt_contra.pack()
        Button(ventana,text="Registrar",width=15,
               command=lambda:  {
                                controlador1.Controlador.registrar(txt_nombre.get(),txt_apellido.get(),txt_email.get(),txt_contra.get()),
                                Vista.login(ventana)
                                }
                                ).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_principal(ventana)).pack(pady=15)

    @staticmethod
    def login(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=".::Inicio de sesión::.").pack(pady=5)
        Label(ventana,text="Ingresa tu email").pack(pady=15)
        txt_email = Entry(ventana)
        txt_email.pack()
        txt_email.focus()
        Label(ventana,text="Ingresa tu contraseña").pack(pady=15)
        txt_contra = Entry(ventana,show="*")
        txt_contra.pack()
        Button(ventana,text="Entrar",width=15,command=lambda:controlador1.Controlador.inicio_sesion(ventana,txt_email.get(),txt_contra.get())).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_principal(ventana)).pack(pady=15)

    @staticmethod
    def menu_notas(ventana,id,nombre,apellido):
        global id_user,nom_user,ape_user
        id_user = id
        nom_user = nombre
        ape_user = apellido
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f".::Bienvenido {nombre} {apellido}, has iniciado sesión::.").pack()
        Button(ventana,text="1.-Crear",width=15,command=lambda:Vista.crear_nota(ventana)).pack(pady=15)
        Button(ventana,text="2.-Mostrar",width=15,command=lambda:Vista.mostrar_nota(ventana)).pack(pady=15)
        Button(ventana,text="3.-Cambiar",width=15,command=lambda:Vista.cambiar_nota(ventana)).pack(pady=15)
        Button(ventana,text="4.-Eliminar",width=15,command=lambda:Vista.eliminar_nota(ventana)).pack(pady=15)
        Button(ventana,text="5.-Regresar",width=15,command=lambda:Vista.menu_principal(ventana)).pack(pady=15)

    @staticmethod
    def crear_nota(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=".::Crear nota::.").pack()
        Label(ventana,text="Titulo").pack(pady=15)
        txt_titulo= Entry(ventana)
        txt_titulo.pack()
        txt_titulo.focus()
        Label(ventana,text="Descripción").pack(pady=15)
        txt_desc = Entry(ventana)
        txt_desc.pack()
        Button(ventana,text="Guardar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_notas(ventana,id_user,nom_user,ape_user)).pack(pady=15)

    @staticmethod
    def mostrar_nota(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text=f"{nom_user,ape_user}, tus notas son").pack()
        filas = ""
        registros = [("1","100","Nota 1","Descripcion de la nota 1","2025-11-24")]
        i = 1
        for fila in registros:
            filas += filas + f"Nota: {i}\nID {fila[0]} .- Titulo {fila[2]}, Fecha de creación: {fila[4]}\n Descripción: {fila[3]}"
            i+=1
        Label(ventana,text=filas).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_notas(ventana,id_user,nom_user,ape_user)).pack(pady=15)

    @staticmethod
    def cambiar_nota(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="Usuario, vamos a cambiar una nota").pack()
        Label(ventana,text="ID de la nota a cambiar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Label(ventana,text="Nuevo Titulo").pack(pady=15)
        txt_titulo= Entry(ventana)
        txt_titulo.pack()
        Label(ventana,text="Nueva Descripción").pack(pady=15)
        txt_desc = Entry(ventana)
        txt_desc.pack()
        Button(ventana,text="Guardar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_notas(ventana,id_user,nom_user,ape_user)).pack(pady=15)

    @staticmethod
    def eliminar_nota(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="Usuario, vamos a eliminar una nota").pack()
        Label(ventana,text="ID de la nota a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Eliminar",width=15,command=lambda:"").pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:Vista.menu_notas(ventana,id_user,nom_user,ape_user)).pack(pady=15)

    @staticmethod
    def limpiar_ventana(ventana):
        for widget in ventana.winfo_children():
            widget.pack_forget()