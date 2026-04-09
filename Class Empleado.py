class Empleado:
    
    __total_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
        Empleado.__total_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        
        return cls.__total_empleados


e1 = Empleado("Ana", 2000)
e2 = Empleado("Luis", 2500)
print(f"Total de empleados: {Empleado.cantidad_empleados()}") 