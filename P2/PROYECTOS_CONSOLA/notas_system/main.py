import funciones
from usuarios.usuario import Usuario
from notas.nota import Nota
import getpass

class App:
    def __init__(self):
        self.main()
    def main(self):
        opcion=True
        while opcion:
            funciones.borrarPantalla()
            opcion=funciones.menu_usuarios()

            if opcion=="1" or opcion=="REGISTRO":
                funciones.borrarPantalla()
                print("\n \t ..:: Registro en el Sistema ::..")
                nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
                apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
                email=input("\t Ingresa tu email: ").lower().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
                resultado = Usuario.registrar(nombre,apellidos,email,password)
                if resultado:
                    print(f"\n\t{nombre} {apellidos} se registró correctamente, con el email: {email}")
                else:
                    print("\n\t..::No fue posible insertar el registro, por favor intentelo de nuevo::..")
                funciones.esperarTecla()
                
            elif opcion=="2" or opcion=="LOGIN": 
                funciones.borrarPantalla()
                print("\n \t ..:: Inicio de Sesión ::.. ")     
                email=input("\t Ingresa tu E-mail: ").lower().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
                registro = Usuario.iniciar_sesion(email,password)
                if registro:
                    self.menu_notas(registro[0],registro[1],registro[2])
                else:
                    print(f"\n\tEmail y/o contraseña incorrectas, vuelva a intentarlo...")
                funciones.esperarTecla()
                
            elif opcion=="3" or opcion=="SALIR": 
                print("Termino la Ejecución del Sistema")
                opcion=False
                funciones.esperarTecla()  
            else:
                print("Opcion no valida")
                opcion=True
                funciones.esperarTecla() 

    def menu_notas(self,usuario_id,nombre,apellidos):
        while True:
            funciones.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
            opcion=funciones.menu_notas()

            if opcion == '1' or opcion=="CREAR":
                funciones.borrarPantalla()
                print(f"\n \t .:: Crear Nota ::. ")
                titulo=input("\tTitulo: ")
                descripcion=input("\tDescripción: ")
                respuesta = Nota.crear(usuario_id,titulo,descripcion)
                if respuesta:
                    print(f"Se creo la nota: {titulo} exitosamente")
                else:
                    print(f"No fue posible crear la nota en este momento vuelve a intentar")
                funciones.esperarTecla()    
            elif opcion == '2' or opcion=="MOSTRAR":
                funciones.borrarPantalla()
                lista_notas = Nota.mostrar(usuario_id)
                if len(lista_notas)>0:
                    print("\n \U0001F50D  .:: Mostrar notas ::. \n")  # 🔍
                    print(f"{'|'}{'ID':<10} {'|'}{'Titulo':<20} {'|'}{'Descripcion':<20}{'|'}{'Fecha':<15}")
                    print(f"{'-'*120}")
                    for fila in lista_notas:
                        print(f"{'|'}{fila[0]:<10}{'|'} {fila[2]:<20}{'|'} {fila[3]:<20}{'|'} {str(fila[4]):<15}{'|'} ")
                    
                else:
                    print("No existen notas para mostrar")
                funciones.esperarTecla()
            elif opcion == '3' or opcion=="CAMBIAR":
                funciones.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")

                lista_notas = Nota.mostrar(usuario_id)
                if len(lista_notas)>0:
                    print("\n \U0001F50D  .:: Mostrar notas ::. \n")  # 🔍
                    print(f"{'|'}{'ID':<10} {'|'}{'Titulo':<20} {'|'}{'Descripcion':<20}{'|'}{'Fecha':<15}")
                    print(f"{'-'*120}")
                    for fila in lista_notas:
                        print(f"{'|'}{fila[0]:<10}{'|'} {fila[2]:<20}{'|'} {fila[3]:<20}{'|'} {str(fila[4]):<15}{'|'} ")
                    id = input("\n\t \t ID de la nota a actualizar: ")
                    if Nota.buscar(id,usuario_id):
                        titulo = input("\t Nuevo título: ")
                        descripcion = input("\t Nueva descripción: ")
                        respuesta = Nota.cambiar(id,titulo,descripcion)
                        if respuesta:
                            print(f"Se actualizo la nota: {titulo} exitosamente")
                        else:
                            print("No fue posible actualizar la nota en este momento vuelve a intentar")
                    else:
                        print("No se encontró la nota")
                else:
                    print("No existen notas para mostrar")
                funciones.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                funciones.borrarPantalla()
                lista_notas = Nota.mostrar(usuario_id)
                if len(lista_notas)>0:
                    print("\n \U0001F50D  .:: Mostrar notas ::. \n")  # 🔍
                    print(f"{'|'}{'ID':<10} {'|'}{'Titulo':<20} {'|'}{'Descripcion':<20}{'|'}{'Fecha':<15}")
                    print(f"{'-'*120}")
                    for fila in lista_notas:
                        print(f"{'|'}{fila[0]:<10}{'|'} {fila[2]:<20}{'|'} {fila[3]:<20}{'|'} {str(fila[4]):<15}{'|'} ")
                    id = input("\n\t \t ID de la nota a eliminar: ")
                    if Nota.buscar(id,usuario_id):
                        rsp = input(f"Desea borrar la nota con ID = {id}?: ").upper().strip()
                        if rsp == "SI":
                            respuesta = Nota.borrar(id)
                            if respuesta:
                                print(f"Se eliminó la nota con ID = {id} exitosamente")
                            else:
                                print("No fue posible eliminar la nota en este momento vuelve a intentar")
                        else:
                            print("No se realizó ningun cambio")
                    else:
                        print("No se encontró la nota")             
                else:
                    print("No existen notas para mostrar")
                    

                funciones.esperarTecla()      
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                funciones.esperarTecla()

if __name__ == "__main__":
    app = App()   
