""" from tkinter import *

def cambiar_texto():
    mensajeCambiante.config(text="Texto cambiado")

def restaurar_texto():
    mensajeCambiante.config(text="Texto Original")

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Uso de botones")
frame_principal = Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=100,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)
label_titulo = Label(frame_principal,text="Uso de botones")
label_titulo.config(
    bg="silver",
    width=20
)
label_titulo.pack(pady=40)

mensajeCambiante=Label(ventana,text="Texto Original")
mensajeCambiante.pack()

boton_cambiar = Button(ventana,text="Cambiar texto",command=cambiar_texto)
boton_cambiar.pack()

boton_restaurar = Button(ventana,text="Restaurar texto",command=restaurar_texto)
boton_restaurar.pack(pady=10)

ventana.mainloop()
 """

from tkinter import *

def login():
    framelogin.pack_forget()
    framemain.pack(fill="both")
    label_main.pack(ipadx=10,ipady=10,pady=30)
    boton_logout.pack()

def logout():
    framemain.pack_forget()
    framelogin.pack(fill="both")
    label_login.pack(ipadx=10,ipady=10,pady=30)
    boton_login.pack()


ventana = Tk()
ventana.geometry("800x600")
ventana.title("Uso de botones")
framelogin = Frame(ventana)
framelogin.config(
    bg="#5dc7e7",
    border=2,
    width=800,
    height=600,
    relief=GROOVE
)
framelogin.pack_propagate(False)
framelogin.pack(fill="both")
label_login = Label(framelogin,text="LOGIN")
label_login.config(
    font="Arial, 24",
    bg="#89d9f1",
    width=200
)
label_login.pack(ipadx=10,ipady=10,pady=30)

framemain = Frame(ventana)
framemain.config(
    bg="#5dc7e7",
    border=2,
    width=800,
    height=600,
    relief=GROOVE
)
framemain.pack_propagate(False)
label_main = Label(framemain,text="Menu principal")
label_main.config(
    font="Arial, 24",
    bg="#89d9f1",
    width=200
)

boton_login = Button(framelogin,text="Iniciar sesión",command=login)
boton_login.config(
    font="Arial, 16",
    bg="#05c0f9",
    fg="white"
)
boton_logout = Button(framemain,text="Cerrar sesión",command=logout)
boton_logout.config(
    font="Arial, 16",
    bg="#05c0f9",
    fg="white"
)
boton_login.pack()
ventana.mainloop()