from tkinter import *
ventana = Tk()
ventana.geometry("500x500")
ventana.title("RadioButtons")

def mostrarSeleccion():
    lbl.config(text=f"Opción seleccionada: {opcion.get()}")

opcion = StringVar()
radbtn1 = Radiobutton(ventana,text="Opción 1",value="Opción 1",variable=opcion)
radbtn2 = Radiobutton(ventana,text="Opción 2",value="Opción 2",variable=opcion)
radbtn3 = Radiobutton(ventana,text="Opción 3",value="Opción 3",variable=opcion)

radbtn1.pack()
radbtn2.pack()
radbtn3.pack()


btn = Button(ventana,text="Mostrar seleccion",command=mostrarSeleccion)
btn.pack()

lbl = Label(ventana,text="")
lbl.pack()

ventana.mainloop()