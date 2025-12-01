from tkinter import *
ventana = Tk()
ventana.geometry("500x500")
ventana.title("CheckButton")

def confirmar():
    if opcion.get()==1:
        lbl.config(text="Notificaciones: Activado")
    else:
        lbl.config(text="Notificaciones: Desactivado")



opcion = IntVar()
chbtn = Checkbutton(ventana,
                    text="¿Desea recibir notificaciones?",
                    variable=opcion,
                    onvalue=1,
                    offvalue=0)
chbtn.pack()

btn = Button(ventana,text="Confirmar",command=confirmar)
btn.pack()

lbl = Label(ventana,text="")
lbl.pack()


ventana.mainloop()