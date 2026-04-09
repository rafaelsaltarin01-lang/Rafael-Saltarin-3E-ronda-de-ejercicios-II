class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []  

    
    def consultar_nombre(self):
        return self.__nombre

    def consultar_edad(self):
        return self.__edad

    
    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("Error: La nota debe estar entre 0 y 100.")

    
    def calcular_promedio(self):
        if not self.__notas:
            return 0  
        return sum(self.__notas) / len(self.__notas)