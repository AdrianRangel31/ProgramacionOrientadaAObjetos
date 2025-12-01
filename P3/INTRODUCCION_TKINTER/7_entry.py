from tkinter import *

def hazClick():
    lbl_resultado.pack(pady=5,fill="x")
    lbl_resultado.config(
        text=f"Bienvenido {txt_nombre.get()}"
    )
    lbl_resultado.pack()
    
def borrar():
    lbl_resultado.destroy()
    txt_nombre.delete(0,END)
    txt_password.delete(0,END)
    txt_nombre.focus()

def salir():
    ventana.quit()

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
lbl_titulo.pack(fill="x")

marco_principal = Frame(ventana,width=800,height=300)
marco_principal.pack()

lbl_nombre = Label(marco_principal,text="Ingrese el nombre")
lbl_nombre.grid(row=0,column=0,padx=5,pady=5)

resultado = StringVar()
txt_nombre = Entry(marco_principal,textvariable=resultado)
txt_nombre.grid(row=0,column=1,padx=5,pady=5)
txt_nombre.focus()

 
lbl_password = Label(marco_principal,text="Ingrese la contraseña")
lbl_password.grid(row=1,column=0,padx=5,pady=5)

txt_password = Entry(marco_principal,show="*")

txt_password.grid(row=1,column=1,padx=5,pady=5)

marco_botones = Frame(ventana,width=800,height=100)
marco_botones.pack()

btn_entrar = Button(marco_botones,text="Has click aqui",command=hazClick)
btn_entrar.grid(row=0,column=0,padx=5,pady=5)

btn_borrar = Button(marco_botones,text="Borrar",command=borrar)
btn_borrar.grid(row=0,column=1,padx=5,pady=5)

btn_salir = Button(marco_botones,text="Cerrar",command=salir)
btn_salir.grid(row=0,column=2,padx=5,pady=5)

lbl_resultado = Label(ventana,text="")
lbl_resultado.config(
    bg="silver",
    font=("Helvetica",20,"italic"),
    fg="Blue",
    height=4,
    border=2,
    relief=GROOVE
)


ventana.mainloop()