class calculadora:
    def __init__(self,numero1,numero2):
        self.__n1 = numero1
        self.__n2 = numero2

    def sumar(self):
        return self.__n1 + self.__n2

    def restar(self):
        return self.__n1 - self.__n2

    def multiplicar(self):
        return self.__n1 * self.__n2

    def dividir(self):
        return self.__n1 / self.__n2

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
operacion = calculadora(n1,n2)
print(operacion.sumar())
print(operacion.restar())
print(operacion.multiplicar())
print(operacion.dividir())

