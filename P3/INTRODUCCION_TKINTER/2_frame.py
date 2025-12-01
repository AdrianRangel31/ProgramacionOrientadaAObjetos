from tkinter import *

ventana = Tk()
ventana.title("Uso de Frame")
ventana.geometry("600x400")
ventana.resizable(False,False)
marco = Frame(ventana,bg="blue",width=400,height=200,borderwidth=2,relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady=100)
marco2 = Frame(marco,bg="red",width=200,height=100,borderwidth=12)
marco2.pack(pady=50)
ventana.mainloop()