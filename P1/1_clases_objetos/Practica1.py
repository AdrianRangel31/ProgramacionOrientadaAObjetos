#Estructurado
def calcular_area(base,altura):
    area = base*altura
    return area
area = calcular_area(10,2)
print(f"El area es: {area}")
#POO
class figuras():
    class rectangulo():
        def __init__(self):
            print("Se creó un rectangulo")
            self.base = int(input("Ingrese la base del rectangulo: "))
            self.altura = int(input("Ingrese la altura del rectangulo: "))
            self.area = 0

        def calcular_area(self):
            self.area = self.base * self.altura
            

rectangulo_1 = figuras.rectangulo()
rectangulo_1.calcular_area()
print(f"El area del rectangulo 1 es: {rectangulo_1.area}")
rectangulo_2 = figuras.rectangulo()
rectangulo_2.calcular_area()
print(f"El area del rectangulo 2 es: {rectangulo_2.area}")


