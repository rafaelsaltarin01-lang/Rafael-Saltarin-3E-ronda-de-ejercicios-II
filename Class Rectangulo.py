class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("Las dimensiones deben ser mayores a cero.")
        self.__largo = largo
        self.__ancho = ancho

    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Error: Largo y ancho deben ser mayores a cero.")

    
    def calcular_area(self):
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)

    
    def consultar_dimensiones(self):
        return {"largo": self.__largo, "ancho": self.__ancho}