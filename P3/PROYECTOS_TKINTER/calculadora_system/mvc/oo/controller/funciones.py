from tkinter import messagebox
from model import operaciones
class Funciones:
    @staticmethod
    def operacion(opc,n1,n2,signo):
        match opc:
            case "Suma":
                signo = "+"
                result = n1+n2
                resultado = f"{n1} {signo} {n2} = {result} "
            case "Resta":
                result = n1-n2
                resultado = f"{n1} {signo} {n2} = {result} "
            case "Multiplicación":
                result = n1*n2
                resultado = f"{n1} {signo} {n2} = {result} "
            case "División":
                if n2 ==0:
                    resultado="No es posible dividir entre 0"
                else:
                    result = n1/n2
                    resultado = f"{n1} / {n2} = {result}"
        resp = messagebox.askquestion(title=opc,message=f"{resultado}\n¿Deseas guardar en la base de datos?",icon="info")
        if resp=="yes":
            operaciones.Operaciones.insertar(n1,n2,signo,result)
    
    @staticmethod
    def eliminar(id):
        operaciones.Operaciones.eliminar(id)

    @staticmethod
    def mensaje_sql(accion):
        if accion:
            messagebox.showinfo("Exito","La acción se realizó con exito")
        else:
            messagebox.showinfo("Error","No fue posible realizar la acción ")
        