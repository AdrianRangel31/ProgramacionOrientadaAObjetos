from model import coches,cochesBD
import os
class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n\t\t Oprima tecla para continuar ...")
    #
    def datos_autos(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
        marca=input("Marca: ").upper()
        color=input("Color: ").upper()
        modelo=input("Modelo: ").upper()
        velocidad=int(input("Velocidad: "))
        potencia=int(input("Potencia: "))
        plazas=int(input("No. de plazas: "))
        return marca,color,modelo,velocidad,potencia,plazas

    def imprimir_datos_vehiculo(self,marca,color,modelo,velocidad,potencia,plazas):
        self.borrarPantalla()
        print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

    def respuesta_sql(self,respuesta):
        if respuesta:
            print("\n\t ... Accion realizada correctamente ...")
        else:
            print("... No fue posible realizar la accion correctamente, vuelva a intentarlo ...")
        self.esperarTecla()

    def autos(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Auto")
        coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
        self.borrarPantalla()
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        self.esperarTecla()
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas

    def camionetas(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camioneta")
        traccion=input("Traccion: ").upper()
        cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
        if cerrada=="SI":
            cerrada=True
        else:
            cerrada=False    
        coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada
        
    def camiones(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camiones")
        eje=int(input("No. de ejes: "))
        capacidadCarga=int(input("Capacidad de carga: "))
        coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
        return marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga
    
    def menu_acciones(self,tipo):
        print(f"\n\t\t .:: Menu Principal {tipo}::.\n\t1.-Insertar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar")
        opcion=input("\n\t\t Elige una opcion: ").upper().strip()
        return opcion

    def menu_autos(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Autos")
            if opcion=="1" or opcion=="INSERTAR":
                marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                #Agregar el registro a la BD
                auto=cochesBD.AutosBD(marca,color,modelo,velocidad,caballaje,plazas)
                respuesta=auto.insertar()
                self.respuesta_sql(respuesta)

            elif opcion=="2" or opcion=="CONSULTAR":
                self.borrarPantalla()
                registros=cochesBD.AutosBD.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nAuto # {num_autos} con ID: {fila[0]}\nMarca: {fila[2]}\nColor:{fila[1]}\nModelo: {fila[3]}\nVelocidad {fila[4]}\nPotencia {fila[5]}\nPlazas: {fila[6]}")
                        num_autos+=1
                    
                else:
                    print("\n\t\t ... No existen datos que mostrar, por el momento ...")
                self.esperarTecla()


            elif opcion=="3" or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                id=input("Ingrese el ID actualizar: ").strip()
                marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                resp=cochesBD.AutosBD.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
                self.respuesta_sql(resp)

            elif opcion=="4" or opcion=="ELIMINAR":
                self.borrarPantalla()
                id=input("Ingrese el ID a eliminar: ").strip()
                respuesta=cochesBD.AutosBD.eliminar(id)
                self.respuesta_sql(respuesta)

            elif opcion=="5" or opcion=="Regresar":
                break
            else:
                print("\n\t\t ... Opcion no valida. Intentelo de nuevo ...")
                self.esperarTecla()

    def menu_camionetas(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Camionetas")
            if opcion=="1" or opcion=="INSERTAR":
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                #Acceder a la BD
                respuesta=cochesBD.CamionetasBD.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
                self.respuesta_sql(respuesta)
                

            elif opcion=="2" or opcion=="CONSULTAR":
                self.borrarPantalla()
                registros=cochesBD.CamionetasBD.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"Camioneta # {num_autos} con ID: {fila[0]}\nMarca: {fila[1]}\nColor:{fila[2]}\nModelo: {fila[3]}\nVelocidad {fila[4]}\nPotencia {fila[5]}\nPlazas: {fila[6]}\nTraccion: {fila[7]}\nCerrada: {fila[8]}")
                        num_autos+=1
                    self.esperarTecla()
                else:
                    print("\n\t\t ... No existen datos que mostrar, por el momento ...")
                    self.esperarTecla()

            elif opcion=="3" or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                id=input("Ingrese el ID actualizar: ").strip()
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                respuesta=cochesBD.CamionetasBD.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
                self.respuesta_sql(respuesta)

            elif opcion=="4" or opcion=="ELIMINAR":
                self.borrarPantalla()
                id=input("Ingrese el ID a eliminar: ").strip()
                respuesta=cochesBD.CamionetasBD.eliminar(id)
                self.respuesta_sql(respuesta)

            elif opcion=="5" or opcion=="Regresar":
                break
            else:
                print("\n\t\t ... Opcion no valida. Intentelo de nuevo ...")
                self.esperarTecla()

    def menu_camiones(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Camiones")
            if opcion=="1" or opcion=="INSERTAR":
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad=self.camiones()
                #Acceder a la BD
                respuesta=cochesBD.CamionesBD.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad)
                self.respuesta_sql(respuesta)

            elif opcion=="2" or opcion=="CONSULTAR":
                self.borrarPantalla()
                registros=cochesBD.CamionesBD.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"Camioneta # {num_autos} con ID: {fila[0]}\nMarca: {fila[1]}\nColor:{fila[2]}\nModelo: {fila[3]}\nVelocidad {fila[4]}\nPotencia {fila[5]}\nPlazas: {fila[6]}\neje: {fila[7]}\nCerrada: {fila[8]}")
                        num_autos+=1
                    self.esperarTecla()
                else:
                    print("\n\t\t ... No existen datos que mostrar, por el momento ...")
                    self.esperarTecla()

            elif opcion=="3" or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                id=input("Ingrese el ID actualizar: ").strip()
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad=self.camiones()
                respuesta=cochesBD.CamionesBD.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id)
                self.respuesta_sql(respuesta)

            elif opcion=="4" or opcion=="ELIMINAR":
                self.borrarPantalla()
                id=input("Ingrese el ID a eliminar: ").strip()
                respuesta=cochesBD.CamionesBD.eliminar(id)
                self.respuesta_sql(respuesta)

            elif opcion=="5" or opcion=="Regresar":
                break
            else:
                print("\n\t\t ... Opcion no valida. Intentelo de nuevo ...")
                self.esperarTecla()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_autos()
                    self.esperarTecla()
                case "2":
                    self.menu_camionetas()
                    self.esperarTecla()  
                case "3":
                    self.menu_camiones()
                    self.esperarTecla()
                case "4":
                    self.borrarPantalla()
                    input("\n\t\tSalir del Sistema")
                    opcion=False   
                case _:
                    input("Opcion invalidad ... vuelva a intertarlo ... ")      
if __name__=="__main__":
    app = App()