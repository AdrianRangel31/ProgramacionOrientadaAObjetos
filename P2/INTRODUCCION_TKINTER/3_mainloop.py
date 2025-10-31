from tkinter import *
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Mainloop")
marco = Frame(ventana)
marco.config(width=600,
             height=400,
             bg="#3095e3",
             border=10,
             relief=RAISED)
marco.pack(side="bottom",anchor="center")

ventana.mainloop()