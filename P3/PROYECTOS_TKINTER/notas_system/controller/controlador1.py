from tkinter import messagebox
from model import usuario,nota
from view import view1

class Controlador:
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado = usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos} se registró correctamente, con el email: {email}",title="Usuarios")
        else:
            messagebox.showinfo(icon="info",message=f"No fue posible realizar el registro",title="Usuarios")

    @staticmethod
    def inicio_sesion(ventana,email,password):
        registro = usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f"{registro[1]} {registro[2]} iniciaste sesión correctamente.",title="Usuarios")
            view1.Vista.menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showinfo(icon="info",message=f"Email y/o contraseña incorrectos. Vuelva a intentarlo.",title="Usuarios")
 