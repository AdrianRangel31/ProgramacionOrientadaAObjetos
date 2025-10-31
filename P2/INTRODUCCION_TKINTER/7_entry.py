from tkinter import *

def hazClick():
    lbl_resultado.config(
        text="Bienvenido"
    )
    lbl_resultado.pack()
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Entry")
ventana.config(
    bg="white"
)
lbl_titulo = Label(ventana,text="Acceso al sistema Tkinter")
lbl_titulo.config(
    bg="lightblue",
    font=("Helvetica",20,"italic"),
    fg="Blue",
    height=4,
    border=2,
    relief=GROOVE
    
)
lbl_titulo.pack(fill="x",pady=20)

lbl_nombre = Label(ventana,text="Ingrese el nombre")
lbl_nombre.pack(pady=10)

txt_nombre = Entry(ventana)
txt_nombre.pack(pady=5)

lbl_password = Label(ventana,text="Ingrese la contraseña")
lbl_password.pack(pady=10)

txt_nombre = Entry(ventana,show="*")
txt_nombre.pack(pady=5)



btn_entrar = Button(ventana,text="Has click aqui",command="entrar")

btn_entrar.pack(pady=5)

btn_ = Button(ventana,text="Regresa click aqui",command="borrar")

btn_.pack(pady=5)

lbl_resultado = Label(ventana,text="")
lbl_resultado.pack(pady=5)


ventana.mainloop()