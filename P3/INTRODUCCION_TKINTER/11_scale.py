from tkinter import *
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Scale")

def mostrarValor(lol):
    print(lol)
    lbl.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

valor = IntVar()
scale = Scale(ventana,orient="horizontal",variable=valor,from_=20,to=200,sliderlength=50,length=300,command=mostrarValor)
scale.pack()

btn = Button(ventana,text="Mostrar valor",command=mostrarValor)
btn.pack()

lbl = Label(ventana,text="")
lbl.pack()

ventana.mainloop()