"""
Crear los métodos getters y setters, estos metodos son importantes y necesarios en todas las clases 
para que el programador interactue con los valores de los atributos a traves de estos metodos...digamos 
que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set)
a un atributo en particular de la clase a traves de un objeto.
En teoria se deberia crear un metodo getter y setter por cada atributo que contenga la clase
Los metodos get siempre regresan un valor es decir el valor de la propiedad a traves del return
Por otro lado el metodo set siempre recibe parametros para cambbiar  modificar el valor del atributo
o propiedad en cuestion.

"""
import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
  marca=""
  color=""
  modelo=""
  velocidad=0
  caballaje=0
  plazas=0

    #Metodos o acciones o funciones que hace el objeto 

  def getMarca(self):
    return self.marca
  
  def setMarca(self,marca):
    self.marca = marca

  def getColor(self):
    return self.color
  
  def setColor(self,color):
    self.color = color


  def getModelo(self):
    return self.modelo
  
  def setModelo(self,modelo):
    self.modelo = modelo


  def getVelocidad(self):
    return self.velocidad
  
  def setVelocidad(self,velocidad):
    self.velocidad = velocidad


  def getCaballaje(self):
    return self.caballaje
  
  def setCaballaje(self,caballaje):
    self.caballaje = caballaje

  def getPlazas(self):
    return self.plazas
  
  def setPlazas(self,plazas):
    self.plazas = plazas

  @property
  def marca2(self):
    return self.marca2
  
  @marca2.setter
  def marca2(self,marca2):
    self.marca2=marca2



  def acelerar(self):
    pass

  def frenar(self):
    pass  

coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Blanco")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3 = Coches()
coche3.marca2("honda")
print(coche3.marca2)