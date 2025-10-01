class alumno:
    def __init__(self,nombre,edad,matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula
    
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property 
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,eda):
        self.__edad = eda

    @property 
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,mat):
        self.__matricula = mat

    def inscribirse(self):
        pass

    def estudiar(self):
        pass

class curso:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property 
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod


    @property 
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self,cred):
        self.__creditos = cred

    def asignar(self):
        pass


class profesor:
    def __init__(self,nombre,experiencia,num_prof):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_prof = num_prof

    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property 
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self,exp):
        self.__experiencia = exp

    @property 
    def num_prof(self):
        return self.__num_prof
    
    @num_prof.setter
    def num_prof(self,num):
        self.__num_prof = num

    def impartir(self):
        pass

    def evaluar(self):
        pass

alumno1 = alumno("Emilio Lopez",19,920913)
alumno2 = alumno("Ana Rodriguez",19,958128)

curso1 = curso("Inglés","ENG1",100)
curso2 = curso("Redes","RED1",120)

profesor1 = profesor("Juan Pablo","10 años",12)
profesor2 = profesor("Maria Jose","1 años",23)

print("Alumno 1\n" 
      f"Nombre: {alumno1.nombre}\n"
      f"Edad: {alumno1.edad}\n"
      f"Matricula: {alumno1.matricula}\n")

print("curso 1\n" 
      f"Nombre: {curso1.nombre}\n"
      f"Codigo: {curso1.codigo}\n"
      f"Creditos: {curso1. creditos}\n")
