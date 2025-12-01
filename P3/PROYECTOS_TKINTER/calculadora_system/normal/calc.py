"""
Crear una calculadora:
    1.- Dos campos de texto
    2.- 4 botones para las operaciones
    3.- Mostrar el resultado en una alerta
    4.-Programado de forma estructurada
    5.-Considerar el MVC
"""

from tkinter import *
from tkinter import messagebox 

def operacion(opc):
    n1 = valor1.get()
    n2 = valor2.get()
    match opc:
        case "suma":
            resultado = f"{n1} + {n2} = {n1+n2}"
        case "resta":
            resultado = f"{n1} - {n2} = {n1-n2}"
        case "multi":
            resultado = f"{n1} x {n2} = {n1*n2}"
        case "div":
            if n2 ==0:
                resultado="No es posible dividir entre 0"
            else:
                resultado = f"{n1} / {n2} = {n1/n2}"
    messagebox.showinfo(message=resultado,icon="info")

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("400x700")
calculadora.resizable(False,False)
calculadora.config(bg="#ffffff")

Label(calculadora,text="CALCULADORA",font=("Arial",20,"bold")).pack()

frame_valores = Frame(calculadora)
frame_valores.pack(fill="x",padx=100)
lbl_val1 = Label(frame_valores,text="Valor 1",font=("Arial",16))
lbl_val1.grid(row=0,column=0)
valor1 = IntVar()
entry1 = Entry(frame_valores,width=10,textvariable=valor1)
entry1.grid(row=0,column=1)

lbl_val1 = Label(frame_valores,text="Valor 2",font=("Arial",16))
lbl_val1.grid(row=1,column=0)
valor2 = IntVar()
entry2 = Entry(frame_valores,width=10,textvariable=valor2)
entry2.grid(row=1,column=1)

frame_botones = Frame(calculadora)
frame_botones.pack(fill="x",padx=70,pady=20)

btn_suma = Button(frame_botones,text="+",font=("Arial",14),command=lambda:operacion("suma"),width=10)
btn_suma.grid(row=0,column=0,padx=5,pady=5)

btn_resta = Button(frame_botones,text="-",font=("Arial",14),command=lambda:operacion("resta"),width=10)
btn_resta.grid(row=0,column=1,padx=5,pady=5)

btn_multi = Button(frame_botones,text="x",font=("Arial",14),command=lambda:operacion("multi"),width=10)
btn_multi.grid(row=1,column=0,padx=5,pady=5)

btn_div = Button(frame_botones,text="/",font=("Arial",14),command=lambda:operacion("div"),width=10)
btn_div.grid(row=1,column=1,padx=5,pady=5)

""" btn_calcular = Button(calculadora,text="=",font=("Arial",14),command="",width=10)
btn_calcular.pack() """

btn_calcular = Button(calculadora,text="Salir",font=("Arial",14),command=calculadora.destroy,width=10)
btn_calcular.pack(pady=10)

calculadora.mainloop()

