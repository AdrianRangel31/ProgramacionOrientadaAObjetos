from tkinter import messagebox
def operacion(opc,n1,n2):
    match opc:
        case "Suma":
            resultado = f"{n1} + {n2} = {n1+n2}"
        case "Resta":
            resultado = f"{n1} - {n2} = {n1-n2}"
        case "Multiplicación":
            resultado = f"{n1} x {n2} = {n1*n2}"
        case "División":
            if n2 ==0:
                resultado="No es posible dividir entre 0"
            else:
                resultado = f"{n1} / {n2} = {n1/n2}"
    messagebox.showinfo(title=opc,message=resultado,icon="info")
