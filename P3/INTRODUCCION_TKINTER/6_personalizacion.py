from tkinter import *

def hazClick():
    lbl_titulo.config(
    text="POO con python",
    bg="green",
    font=("Arial",20,"bold"),
    fg="red",
    height=4,
    border=2,
    relief=GROOVE
    )
def regresarClick():
    lbl_titulo.config(
    text="Bienvenidos a Tkinter",
    bg="lightblue",
    font=("Helvetica",20,"italic"),
    fg="Blue",
    height=4,
    border=2,
    relief=GROOVE
    )
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Uso de botones")
ventana.config(
    bg="white"
)
lbl_titulo = Label(ventana,text="Bienvenidos a Tkinter")
lbl_titulo.config(
    bg="lightblue",
    font=("Helvetica",20,"italic"),
    fg="Blue",
    height=4,
    border=2,
    relief=GROOVE
    
)
lbl_titulo.pack(fill="x",pady=20)


btn1 = Button(ventana,text="Has click aqui",command=hazClick)
btn1.config(
    font=("Arial",15,"bold"),
    fg="Red",
    activeforeground="Orange",
    width=15
)
btn1.pack(pady=5)

btn2 = Button(ventana,text="Regresa click aqui",command=regresarClick)
btn2.config(
    font=("Arial",15,"bold"),
    fg="black",
    activeforeground="blue",
    width=15
)
btn2.pack(pady=5)




ventana.mainloop()