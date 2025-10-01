from Coches import *

""" coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,5)
 """

def autos():
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    coche = Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"Marca:\t{coche.marca}\nColor:\t{coche.color}\nModelo:\t{coche.modelo}"
          f"\nVelocidad:\t{coche.velocidad}\nPotencia:\t{coche.caballaje}\nPlazas:\t{coche._plazas}")

def camionetas():
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    traccion = input("Tracción: ").upper()
    cerrada = True if input("Ingrese SI/NO si es cerrada o no: ").upper().strip() == "SI" else False
    camioneta = Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    print(f"Marca:\t{camioneta.marca}\nColor:\t{camioneta.color}\nModelo:\t{camioneta.modelo}"
          f"\nVelocidad:\t{camioneta.velocidad}\nPotencia:\t{camioneta.caballaje}\nPlazas:\t{camioneta.plazas}"
          f"\nTracción::\t{camioneta.traccion}\nCerrada:\t{camioneta.cerrada}")

def camiones():
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    eje = int(input("Eje: ").upper())
    capacidad = int(input("Capacidad: ").upper())
    camion = Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad)
    print(f"Marca:\t{camion.marca}\nColor:\t{camion.color}\nModelo:\t{camion.modelo}"
          f"\nVelocidad:\t{camion.velocidad}\nPotencia:\t{camion.caballaje}\nPlazas:\t{camion.plazas}"
          f"\nEje::\t{camion.eje}\nCapacidad:\t{camion.capacidad}")

opcion = 0
while opcion != "4":
    os.system("cls")
    opcion = input("\n\t...::Menu principal::..."
                "\n\t1.- Coches"
                "\n\t2.- Camionetas"
                "\n\t3.- Camiones"
                "\n\t4.- Salir"
                "\n\t     Elige una opción:").lower().strip()
    match opcion:
        case "1":
            print("--Coches--")
            autos()
            input("Ingrese tecla para continuar")
        case "2":
            print("--Camionetas--")
            camionetas()
            input("Ingrese tecla para continuar")
        case "3":
            print("--Camiones--")
            camiones()
            input("Ingrese tecla para continuar")
        case "4":
            print("Cerrando...")
        case _:
            input("Opción invalida")







""" 
coche = Coches("BMW","Blanco","2020",220,100,2)
print(coche._color,coche.acelerar())
camion = Camiones("Volvo","Azul","2012",200,100,2,4,2000)
print(camion._color,camion.acelerar())
camioneta = Camionetas("RAM","Gris","2023",180,90,4,2,4)
print(camioneta._color,camioneta.acelerar()) """