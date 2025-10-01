
import os
os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def caballaje(self):
        return self._caballaje

    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje = caballaje

    @property
    def plazas(self):
        return self._plazas

    @plazas.setter
    def plazas(self, plazas):
        self._plazas = plazas
    
    def acelerar(self):
        return "Estas acelerando el coche"

    def frenar(self):
        return "Estas frenando el coche"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidad):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje = eje
        self.__capacidad = capacidad

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando el camión"

    def frenar(self):
        return "Estas frenando el camión"

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self,eje):
        self.__eje = eje

    @property
    def capacidad(self):
        return self.__capacidad
    
    @capacidad.setter
    def capacidad(self,capacidad):
        self.__capacidad = capacidad

    
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando la camioneta"

    def frenar(self):
        return "Estas frenando la camioneta"

    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def traccion(self,traccion):
        self.__traccion = traccion

    @property
    def cerrada(self):
        return self.__cerrada
    
    @cerrada.setter
    def cerrada(self,cerrada):
        self.__cerrada = cerrada

