class Libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__total_paginas = total_paginas
        self.__pagina_actual = 1  

    
    def avanzar_paginas(self, paginas):
        nueva_pagina = self.__pagina_actual + paginas
        if nueva_pagina <= self.__total_paginas:
            self.__pagina_actual = nueva_pagina
        else:
            raise ValueError(f"Error: No puedes avanzar a la pág {nueva_pagina}. El libro solo tiene {self.__total_paginas} páginas.")

    
    def retroceder_paginas(self, paginas):
        nueva_pagina = self.__pagina_actual - paginas
        if nueva_pagina >= 1:
            self.__pagina_actual = nueva_pagina
        else:
            raise ValueError("Error: No puedes retroceder más allá de la página 1.")

    
    def consultar_pagina_actual(self):
        return self.__pagina_actual

    def obtener_informacion_completa(self):
        return {
            "Título": self.__titulo,
            "Autor": self.__autor,
            "Total Páginas": self.__total_paginas,
            "Página Actual": self.__pagina_actual
        }