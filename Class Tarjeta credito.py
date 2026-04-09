class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = str(numero)

    @staticmethod
    def validar_tarjeta(numero):
        
        n = str(numero).replace(" ", "")
        
        digitos = [int(d) for d in n]
        
        for i in range(len(digitos) - 2, -1, -2):
            multiplicado = digitos[i] * 2
            if multiplicado > 9:
                multiplicado -= 9
            digitos[i] = multiplicado
        
       
        return sum(digitos) % 10 == 0


es_valida = TarjetaCredito.validar_tarjeta("4539148803436467")
print(f"¿Tarjeta válida?: {es_valida}")