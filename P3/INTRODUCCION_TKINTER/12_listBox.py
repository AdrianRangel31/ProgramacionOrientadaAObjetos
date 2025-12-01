from tkinter import *
ventana = Tk()
ventana.geometry("500x500")
ventana.title("ListBox")

def mostrarSeleccion():
    lbl.config(text=f"Selección del usuario: {lista.get(lista.curselection())}")

valor = StringVar()
opciones = ["Azul","Rojo","Verde","Amarillo"]
lista = Listbox(ventana,width=30,height=10,selectmode="multiple",listvariable=valor,
                highlightbackground="black",
                highlightcolor="black")
lista.pack()

for opcion in opciones:
    lista.insert(END,opcion)



btn = Button(ventana,text="Mostrar selección del usuario",command=mostrarSeleccion)
btn.pack()

lbl = Label(ventana,text="")
lbl.pack()

ventana.mainloop()