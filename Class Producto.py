class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  
        if precio <= 0:
            raise ValueError("El precio inicial debe ser mayor a cero.")
        self.__precio = precio  

    
    def obtener_nombre(self):
        return self.__nombre

    def consultar_precio(self):
        return self.__precio

    
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("Error: El nuevo precio debe ser mayor que cero.")

    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
        else:
            raise ValueError("Error: El porcentaje debe estar entre 0 y 100.")
        