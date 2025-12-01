from tkinter import *
from tkinter import messagebox
from controller import funciones
from conexionBD import *
from tkinter import ttk
from model.operaciones import *

class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("400x700")
        ventana.resizable(False,False)
        ventana.config(bg="#ffffff")
        self.valores = None
        self.interfaz_principal(ventana)

    
    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar) 
        archivoMenu = Menu(menuBar , tearoff=0)
        menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: Vista.interfaz_principal(ventana) )
        archivoMenu.add_command(label="Consultar",command=lambda: Vista.interfaz_consultar(ventana) )
        archivoMenu.add_command(label="Cambiar",command=lambda: Vista.interfaz_buscar(ventana) )
        archivoMenu.add_command(label="Borrar",command=lambda: Vista.interfaz_eliminar(ventana) )
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir",command=ventana.quit)

    @staticmethod
    def interfaz_eliminar(ventana):
        Vista.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana,text=".::Borrar una operacion::.", bg="#f7fbff")
        lbl_titulo.pack()
        lbl_id = Label(ventana,text="ID de la Operación:", bg="#f7fbff")
        lbl_id.pack()
        id = IntVar()
        txt_id = Entry(ventana,textvariable=id) 
        txt_id.focus()
        txt_id.pack()
        btn_eliminar = Button(ventana,text="Eliminar", bg="#d9ecf5", command=lambda:Vista.eliminar(txt_id.get()))
        btn_eliminar.pack()
        btn_volver = Button(ventana,text="Volver", bg="#d9ecf5", command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()

    @staticmethod
    def limpiar_ventana(ventana):
        for widget in ventana.winfo_children():
            widget.pack_forget()

    @staticmethod
    def interfaz_consultar(ventana):
        Vista.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana,text=".::Listado de operaciones::.",font=("Arial",16), bg="#f7fbff")
        lbl_titulo.pack(padx=5)
        registros = Operaciones.consultar()
        i=1
        for registro in registros:
            texto = f"Operación {i} ID: {registro[0]} Fecha de creación: {registro[1]},\nOperación: {registro[2]} {registro[4]} {registro[3]} = {registro[5]}"
            Label(ventana,text=texto, bg="#f7fbff").pack(padx=15,pady=2)
            i+=1
        btn_volver = Button(ventana,text="Volver", bg="#d9ecf5", command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()

    @staticmethod
    def interfaz_buscar(ventana):
        Vista.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana,text=".::Buscar una operación::.",font=("Arial",16), bg="#f7fbff")
        lbl_titulo.pack(padx=5)
        id = IntVar()
        Label(ventana,text="ID de la operación: ", bg="#f7fbff").pack()
        txt_id = Entry(ventana,textvariable=id)
        txt_id.pack()
        txt_id.focus()


        btn_buscar = Button(ventana,text="Buscar", bg="#d9ecf5", command=lambda:Vista.buscar(ventana,id.get()))
        btn_buscar.pack()

        btn_volver = Button(ventana,text="Volver", bg="#d9ecf5", command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()

    @staticmethod
    def interfaz_actualizar(ventana,id_op,num1,num2,sign,result):
        Vista.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana,text=".::Cambiar una operación::.",font=("Arial",16), bg="#f7fbff")
        lbl_titulo.pack(padx=5)
        id = IntVar()
        Label(ventana,text="ID de la operación: ", bg="#f7fbff").pack()
        txt_id = Entry(ventana,textvariable=id)
        txt_id.pack()
        txt_id.delete(0,"end")
        txt_id.insert(0,f"{id_op}")
        txt_id.config(state="readonly")


        n1 = IntVar()
        Label(ventana,text="Número 1: ", bg="#f7fbff").pack()
        txt_n1 = Entry(ventana,textvariable=n1)
        txt_n1.pack()
        txt_n1.delete(0,"end")
        txt_n1.insert(0,f"{num1}")
        txt_n1.focus()


        n2 = IntVar()
        Label(ventana,text="Número 2: ", bg="#f7fbff").pack()
        txt_n2 = Entry(ventana,textvariable=n2)
        txt_n2.pack()
        txt_n2.delete(0,"end")
        txt_n2.insert(0,f"{num2}")

        signo = StringVar()
        Label(ventana,text="Nuevo signo: ", bg="#f7fbff").pack()
        txt_signo = Entry(ventana,textvariable=signo)
        txt_signo.pack()
        txt_signo.delete(0,"end")
        txt_signo.insert(0,f"{sign}")

        resultado = IntVar()
        Label(ventana,text="Nuevo resultado: ", bg="#f7fbff").pack()
        txt_resultado = Entry(ventana,textvariable=resultado)
        txt_resultado.pack()
        txt_resultado.delete(0,"end")
        txt_resultado.insert(0,f"{result}")

        btn_guardar = Button(ventana,text="Guardar", bg="#d9ecf5", command=lambda:Vista.actualizar(ventana,n1.get(),n2.get(),signo.get(),resultado.get(),id.get()))
        btn_guardar.pack()

        btn_volver = Button(ventana,text="Volver", bg="#d9ecf5", command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()

    @staticmethod
    def actualizar(ventana,n1,n2,signo,resultado,id):
        actualizar = Operaciones.actualizar(n1,n2,signo,resultado,id)
        funciones.Funciones.mensaje_sql(actualizar)
        Vista.interfaz_principal(ventana)

    @staticmethod
    def eliminar(id):
        eliminar = Operaciones.eliminar(id)
        funciones.Funciones.mensaje_sql(eliminar)

    @staticmethod
    def buscar(ventana,id):
        buscar = Operaciones.buscar(id)
        if buscar:
            registro = buscar[0]
            Vista.interfaz_actualizar(ventana,registro[0],registro[2],registro[3],registro[4],registro[5])
        else:
            messagebox.showerror("Advertencia",f"No se encontró el registro con ID: {id}")

    @staticmethod
    def interfaz_principal(ventana):
        Vista.menuPrincipal(ventana)
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="CALCULADORA",font=("Arial",20,"bold"), bg="#f7fbff").pack()

        frame_valores = Frame(ventana,bg="#e8f4fa")
        frame_valores.pack(fill="x",padx=100)

        lbl_val1 = Label(frame_valores,text="Valor 1",font=("Arial",16),bg="#e8f4fa")
        lbl_val1.grid(row=0,column=0)
        valor1 = IntVar()
        entry1 = Entry(frame_valores,width=10,textvariable=valor1)
        entry1.grid(row=0,column=1)

        lbl_val2 = Label(frame_valores,text="Valor 2",font=("Arial",16),bg="#e8f4fa")
        lbl_val2.grid(row=1,column=0)
        valor2 = IntVar()
        entry2 = Entry(frame_valores,width=10,textvariable=valor2)
        entry2.grid(row=1,column=1)

        frame_botones = Frame(ventana,bg="#e8f4fa")
        frame_botones.pack(fill="x",padx=70,pady=20)

        btn_suma = Button(frame_botones,text="+",font=("Arial",14), bg="#d9ecf5", command=lambda:funciones.Funciones.operacion("Suma",valor1.get(),valor2.get(),"+"),width=10)
        btn_suma.grid(row=0,column=0,padx=5,pady=5)

        btn_resta = Button(frame_botones,text="-",font=("Arial",14), bg="#d9ecf5", command=lambda:funciones.Funciones.operacion("Resta",valor1.get(),valor2.get(),"-"),width=10)
        btn_resta.grid(row=0,column=1,padx=5,pady=5)

        btn_multi = Button(frame_botones,text="x",font=("Arial",14), bg="#d9ecf5", command=lambda:funciones.Funciones.operacion("Multiplicación",valor1.get(),valor2.get(),"*"),width=10)
        btn_multi.grid(row=1,column=0,padx=5,pady=5)

        btn_div = Button(frame_botones,text="/",font=("Arial",14), bg="#d9ecf5", command=lambda:funciones.Funciones.operacion("División",valor1.get(),valor2.get(),"/"),width=10)
        btn_div.grid(row=1,column=1,padx=5,pady=5)

        btn_salir = Button(ventana,text="Salir",font=("Arial",14), bg="#d9ecf5", command=ventana.destroy,width=10)
        btn_salir.pack(pady=10)
